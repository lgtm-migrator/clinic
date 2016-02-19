from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from user_agents import parse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Store, Schedule, Region, Holiday, \
	NearestStation, Sortkey, HolidayWorking, WorkingDay

from django.contrib.auth.models import User

from django_select2.forms import Select2Widget
from datetime import datetime, timedelta

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

import sys
import django_filters
import calendar

class StoreFilter(django_filters.FilterSet):
	# See: https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
	region = django_filters.ModelChoiceFilter(
		queryset=Region.objects.all(),
		widget=Select2Widget,
		# lookup_type='icontains',
	)
	nearest_station = django_filters.ModelChoiceFilter(
		queryset=NearestStation.objects.all(),
		widget=Select2Widget,
		# lookup_type='icontains'
	)
	class Meta:
		fields = ['region', 'nearest_station',]

	def get_order_by(self, order_value):
		sort_key = Sortkey.objects.filter(sorttype='001')[0]
		if sort_key:
			return [sort_key.key1, sort_key.key2]
			# return []
		else:
			return super(StoreFilter, self).get_order_by(order_value)

	def clinic_filter(self, queryset, value):
		pass

class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'stores'
	model = Store

	def get_context_data(self, **kwargs):
		paginate_by = 20

		context = super(IndexView, self).get_context_data(**kwargs)
		context['filter'] = StoreFilter(self.request.GET, queryset=self.model.objects.filter(display=True))

		# context['filter'] = StoreFilter(self.request.GET, queryset=self.model.objects.filter(display=True))
		paginator = Paginator(context['filter'].queryset, paginate_by)
		page = self.request.GET.get('page')
		try:
			paging = paginator.page(page)
		except PageNotAnInteger:
			paging = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			paging = paginator.page(paginator.num_pages)
		
		context['paging'] = paging

		return context

class DetailView(generic.DetailView):
	model = Store
	template_name = 'home/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)

		current_store = context["store"]

		if self.request.method == 'GET' and 'start_day' in self.request.GET:
			day_query = datetime.strptime(self.request.GET["start_day"], '%d/%m/%Y').date()
		else:
			day_query = datetime.now().date()

		context["start_day"] = day_query - timedelta(days=day_query.weekday())
		context["end_day"] = context["start_day"] + timedelta(days=13)

		working_days = WorkingDay.objects.filter(store_id=current_store.id).order_by('id')
		working_holidays = HolidayWorking.objects.filter(store_id=current_store.id).filter(date__gte=context["start_day"],
                                date__lte=context["end_day"])
		booked_days = Schedule.objects.filter(store_id=current_store.id).filter(date__gte=context["start_day"],
                                date__lte=context["end_day"])


		context["prev_2_weeks"] = context["start_day"] - timedelta(days=13)
		context["next_2_weeks"] = context["end_day"] + timedelta(days=1)
		context["days_range"]   = [context["start_day"] + timedelta(days=x) for x in range(0, 14)]
		context["time_range"]   = current_store.store_time_range(working_days)
		context["schedule"]     = current_store.generate_booking_matrix(working_days,
									booked_days, working_holidays,
									context["days_range"],
									context["time_range"], Holiday.objects.all())
		return context

BOOKING_ERROR = (
	('0', 'No Error'),
	('1', 'No Store'),
    ('2', 'Invalid Date'),
    ('3', 'Invalid Hour'),
    ('4', 'Schedule exited'),
)

def CheckDataSchedule(store_id, date, hour):
	store = Store.objects.filter(pk=store_id)
	if not store:
		return BOOKING_ERROR[1]

	if int(hour) <= 6 or int(hour) >= 22:
		return BOOKING_ERROR[3]

	try:
		date = datetime.strptime(date, "%Y%m%d").date()
		schedule = Schedule.objects.filter(store=store, date=date, hour=hour)
		if schedule:
			return BOOKING_ERROR[4]
	except ValueError as e:
		return BOOKING_ERROR[2]

	return BOOKING_ERROR[0]

def SendEmail(sche, ipadress, device):
	patient_mail = get_template('home/mailtemplate/patientemail.txt')
	clinic_mail = get_template('home/mailtemplate/clinicemail.txt')
	patient_subj = get_template('home/mailtemplate/patientsubj.txt')
	clinic_subj = get_template('home/mailtemplate/clinicsubj.txt')
	
	hour = '{0:02d}:00'.format(sche.hour) + '-{0:02d}:00'.format(sche.hour + 1)
	patientmaild = Context({ 'date': _(sche.date.strftime('%Y年%m月%d日')) + _(sche.date.strftime('(%a)')), 
							'hour':hour, 'name':sche.name, 'cutomerphone':sche.phone, 
							'email':sche.email, 'clinicphone':sche.store.phone})

	clinicmaild = Context({ 'date': _(sche.date.strftime('%Y年%m月%d日')) + _(sche.date.strftime('(%a)')), 
						'hour':hour, 'name':sche.name, 'phone':sche.phone, 
						'email':sche.email, 'ipadress':ipadress, 'device':device})

	from_email = settings.EMAIL_HOST_USER
	
	subject_patient = patient_subj.render(patientmaild)
	subject_clinic = clinic_subj.render(clinicmaild)
	
	message_patient = patient_mail.render(patientmaild)
	message_clinic = clinic_mail.render(clinicmaild)
	
	to_patient = [sche.email]
	to_clinic = [sche.store.mail]

	try:
		send_mail(subject_patient, message_patient, from_email, to_patient)
		send_mail(subject_clinic, message_clinic, from_email, to_clinic)
	except BadHeaderError:
		return False
	return True

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class CreateView(generic.CreateView):
	model = Schedule
	fields = ['store', 'date', 'hour', 'name', 'phone', 'email', 'symptom']
	template_name = 'home/booking.html'

	def get(self, request, **kwargs):
		if request.method == "GET":
			store = int(kwargs['store'])
			hour = int(kwargs['hour'])
			date = kwargs['date']
			check_url = CheckDataSchedule(store, date, hour)
			if check_url == BOOKING_ERROR[1] or check_url == BOOKING_ERROR[2] or check_url == BOOKING_ERROR[3]:
				return HttpResponseRedirect('/')
			else:
				return super(CreateView, self).get(request, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(CreateView, self).get_context_data(**kwargs)
		if self.request.method == "GET":
			context['store'] = self.kwargs['store']
			context['hour'] = int(self.kwargs['hour'])
			context['date'] = self.kwargs['date']
			context['date'] = datetime.strptime(self.kwargs['date'], "%Y%m%d").date()
		else:
			context['store'] = self.request.POST['store']
			context['date'] = datetime.strptime(self.request.POST['date'], "%Y%m%d").date()
			context['hour'] = int(self.request.POST['hour'])
			context['name'] = self.request.POST['name']
			context['phone'] = self.request.POST['phone']
			context['email'] = self.request.POST['email']
			context['symptom'] = self.request.POST['symptom']

			store=Store.objects.filter(pk=context['store'])[0]

			schedule = Schedule.objects.filter(store=store, date=context['date'], hour=context['hour'])
			if schedule:
				context['error'] = "This time is registed by another patient. Please choose another time!"
			else:
				schedule = Schedule(store=store, date=context['date'], hour=context['hour'],
									name=context['name'], phone=context['phone'],
									email=context['email'], symptom=context['symptom'])
				schedule.save()

				ip = get_client_ip(self.request)

				user_agent = parse(self.request.META['HTTP_USER_AGENT'])

				SendEmail(schedule, ip, user_agent.device.family + " " + user_agent.os.family + " " + user_agent.os.version_string)
				context['success'] = "The registration process was successful, Please check email for more information!"
				# schedule.delete()
		return context
