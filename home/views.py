# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from user_agents import parse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage

from .models import Store, Schedule, Region, Holiday, \
	NearestStation, Sortkey, HolidayWorking, WorkingDay

from django.contrib.auth.models import User

from django_select2.forms import Select2Widget
from datetime import datetime, timedelta

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from .forms import ScheForm

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
		paginate_by = 2
		adjacent_pages = 2
		adjacent_pages_mobile = 1

		context = super(IndexView, self).get_context_data(**kwargs)
		context['filter'] = StoreFilter(self.request.GET, queryset=self.model.objects.filter(display=True))

		if "region" in self.request.GET:
			context["url_filter"] = "&region=" + self.request.GET["region"] + \
										"&nearest_station=" + self.request.GET["nearest_station"]
		# context['url_filter'] = region
		# context['filter'] = StoreFilter(self.request.GET, queryset=self.model.objects.filter(display=True))
		paginator = Paginator(context['filter'], paginate_by)
		page = self.request.GET.get('page')
		try:
			paging = paginator.page(page)
		except PageNotAnInteger:
			paging = paginator.page(1)
			page = 1
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			paging = paginator.page(paginator.num_pages)
			page = paginator.num_pages

		context['paging'] = paging


		# format paging
		current_page = int(page)
		num_pages = paginator.num_pages
		
		# for webrowser
		startPage = max(current_page - adjacent_pages, 1)
		if startPage <= 3:
			startPage = 1
		
		endPage = current_page + adjacent_pages + 1
		if endPage >= num_pages - 1:
			endPage = num_pages + 1
		
		showing_pages= [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]

		# for mobile
		startPage = max(current_page - adjacent_pages_mobile, 1)
		if startPage <= 3:
			startPage = 1
		
		endPage = current_page + adjacent_pages_mobile + 1
		if endPage >= num_pages - 1:
			endPage = num_pages + 1
		
		showing_pages_mobi = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]

		context["showing_pages"] = showing_pages
		context["show_first"] = 1 not in showing_pages
		context["show_last"] = num_pages not in showing_pages
		context["last_page"] = num_pages
		context["show_first_mobi"] = 1 not in showing_pages_mobi
		context["show_last_mobi"] = num_pages not in showing_pages_mobi
		context["showing_pages_mobi"] = showing_pages_mobi

		context['is_admin_store'] = False
		if self.request.resolver_match.url_name == 'admin_store':
			if self.request.user.is_staff:
				context['is_admin_store'] = True

		return context

class DetailView(generic.DetailView):
	model = Store
	template_name = 'home/detail.html'
	def get(self, request, *args, **kwargs):
		try:
			self.object = self.get_object()
		except Http404:
			return redirect('/')
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)

		if 'error' in self.request.session.keys():
			context["error"] = self.request.session['error']
			del self.request.session['error']

		current_store = context["store"]

		day_query = datetime.now().date()
		if self.request.method == 'GET' and 'start_day' in self.request.GET:
			day_query = datetime.strptime(self.request.GET["start_day"], '%d/%m/%Y').date()

			# back from booking
			start_week = day_query - timedelta(days=day_query.weekday())
			current_date = datetime.now().date()
			current_start_week = current_date - timedelta(days=current_date.weekday())
			if ((start_week - current_start_week).days / 7 ) % 2 != 0:
				day_query = day_query - timedelta(days=7)


		context["start_day"] = day_query - timedelta(days=day_query.weekday())
		context["end_day"] = context["start_day"] + timedelta(days=13)

		working_days = WorkingDay.objects.filter(store_id=current_store.id).order_by('id')
		working_holidays = HolidayWorking.objects.filter(store_id=current_store.id).filter(date__gte=context["start_day"],
                                date__lte=context["end_day"])
		booked_days = Schedule.objects.filter(store_id=current_store.id).filter(date__gte=context["start_day"],
                                date__lte=context["end_day"])
		if 'back_url' in self.request.GET:
			context["back_url"] = self.request.GET["back_url"]
		else:
			context["back_url"] = "/"
		context["prev_2_weeks"] = context["start_day"] - timedelta(days=14)
		context["next_2_weeks"] = context["end_day"] + timedelta(days=1)
		context["days_range"]   = [context["start_day"] + timedelta(days=x) for x in range(0, 14)]
		context["time_range"]   = current_store.store_time_range(working_days, working_holidays)
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
    ('4', 'Schedule existed'),
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
	# get subject, body mail template
	patient_mail = get_template('home/mailtemplate/patientemail.txt')
	clinic_mail = get_template('home/mailtemplate/clinicemail.txt')
	patient_subj = get_template('home/mailtemplate/patientsubj.txt')
	clinic_subj = get_template('home/mailtemplate/clinicsubj.txt')

	# define context
	hour = '{0:02d}:00'.format(sche.hour) + '-{0:02d}:00'.format(sche.hour + 1)
	patientmaild = Context({ 'date': _(sche.date.strftime('%Y年%m月%d日（')) + _(sche.date.strftime('%a')) + "）",
							'hour':hour, 'name':sche.name, 'cutomerphone':sche.phone,
							'email':sche.email, 'clinicphone':sche.store.phone})

	clinicmaild = Context({ 'date': _(sche.date.strftime('%Y年%m月%d日（')) + _(sche.date.strftime('%a')) + "）",
						'hour':hour, 'name':sche.name, 'phone':sche.phone,
						'email':sche.email, 'ipadress':ipadress, 'device':device})

	patientsubj = Context({'storename': sche.store.name})

	# get email host user
	from_email = settings.EMAIL_HOST_USER

	# generate mail subject
	subject_patient = patient_subj.render(patientsubj)
	subject_clinic = clinic_subj.render(clinicmaild)

	# generate mail body
	message_patient = patient_mail.render(patientmaild)
	message_clinic = clinic_mail.render(clinicmaild)

	# get recieved mail
	to_patient = [sche.email]

	to_clinic = [sche.store.mail]
	# get superuser email
	super_user = User.objects.all()
	for user in super_user:
		to_clinic.append(user.email)

	clinic_email = EmailMessage(subject_clinic, message_clinic, from_email, bcc=to_clinic)

	try:
		send_mail(subject_patient, message_patient, from_email, to_patient)
		clinic_email.send()
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

def ScheView(request, store, date, hour):
	template_name = 'home/booking.html'

	check_url = CheckDataSchedule(store, date, hour)
	if check_url == BOOKING_ERROR[1] or check_url == BOOKING_ERROR[2] or check_url == BOOKING_ERROR[3]:
		return HttpResponseRedirect('/')

	store_object = Store.objects.filter(pk=store)[0]
	booking_date = datetime.strptime(date, "%Y%m%d").date()
	booking_hour = int(hour)
	error = ""
	success = ""

	if 'back_home_url' in request.GET:
		back_home_url = request.GET["back_home_url"]
	else:
		back_home_url = "/"


	if request.method == "POST":
		form = ScheForm(request.POST)
		if form.is_valid():
			schedule = form.save(commit=False)
			schedule.store = store_object
			schedule.date = booking_date
			schedule.hour = booking_hour

			sche = Schedule.objects.filter(store=store_object, date=booking_date, hour=booking_hour)

			if sche:
				request.session['error'] = _("This time is registed by another patient. Please choose another time!")
				url_back = '/store/' + str(store_object.id) + \
							"/?back_home_url=" + back_home_url + \
							"&?start_day=" + booking_date.strftime("%d/%m/%Y")
				return redirect(url_back)
			else:
				schedule.save()
				ip = get_client_ip(request)
				user_agent = parse(request.META['HTTP_USER_AGENT'])
				SendEmail(schedule, ip, user_agent.device.family + " " + user_agent.os.family + " " + user_agent.os.version_string)
				success = _("The registration process was successful, Please check email for more information!")

	else:
		form = ScheForm()


	return render(request, template_name, {'form': form, 'store':store_object,
											'date':booking_date, 'hour':booking_hour,
											'error':error, 'success':success, "back_home_url": back_home_url})

def TimeslotCheck(request, store, date, hour):
	check_url = CheckDataSchedule(store, date, hour)
	return JsonResponse({"status":check_url})
