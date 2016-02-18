from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse

from .models import Store, Schedule, Region, Holiday, \
	NearestStation, Sortkey, HolidayWorking, WorkingDay
from django_select2.forms import Select2Widget
from datetime import datetime, timedelta

import sys
import django_filters
import calendar




class StoreFilter(django_filters.FilterSet):
	# See: https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
	region = django_filters.ModelChoiceFilter(
		queryset=Region.objects.all(),
		widget=Select2Widget,
		lookup_type='icontains'
	)
	nearest_station = django_filters.ModelChoiceFilter(
		queryset=NearestStation.objects.all(),
		widget=Select2Widget,
		lookup_type='icontains'
	)
	class Meta:
		model = Store
		fields = ['region', 'nearest_station',]

	def get_order_by(self, order_value):
		sort_key = Sortkey.objects.filter(sorttype='001')[0]
		if sort_key:
			return [sort_key.key1, sort_key.key2]
			# return []
		else:
			return super(StoreFilter, self).get_order_by(order_value)

class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'stores'
	paginate_by = 20
	model = Store

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['filter'] = StoreFilter(self.request.GET)
		return context

class DetailView(generic.DetailView):
	model = Store
	template_name = 'home/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		current_store = context["store"]

		if self.request.method == 'GET' and 'start_day' in self.request.GET:
			day_query = datetime.strptime(self.request.GET["start_day"], '%d/%m/%Y')
		else:
			day_query = datetime.now().date()

		context["working_day"] = WorkingDay.objects.filter(store_id=current_store.id).order_by('id')
		context["working_holiday"] = HolidayWorking.objects.filter(store_id=current_store.id)
		context["schedule"] = Schedule.objects.filter(store_id=current_store.id)
		context["start_day"] = day_query - timedelta(days=day_query.weekday())
		context["end_day"] = context["start_day"] + timedelta(days=13)
		context["days_range"] = [context["start_day"] + timedelta(days=x) for x in range(0, 14)]
		context["time_range"] = self.store_time_range(context["working_day"])
		context["schedule"] = self.generate_booking_matrix(context["working_day"],
								context["schedule"], context["working_holiday"],
								context["days_range"],
								context["time_range"], Holiday.objects.all())
		return context

	def store_time_range(self, working_day):
		open_hr = 21
		close_hr = 8
		time_range = range(close_hr, open_hr+1)
		for day in working_day:
			for i in time_range:
				if getattr(day, "hour_"+str(i)) == 1:
					if i < open_hr:
						open_hr = i
					if i > close_hr:
						close_hr = i
		return range(open_hr,close_hr+1)

	def generate_booking_matrix(self, working_day, schedule_list, working_holiday,
								days_range, time_range, holiday_default_list):
		# declare a hash table mat which keys are hours, values are working days and its status
		mat = {
			"8": {}, "9": {}, "10": {}, "11": {}, "12": {},
			"13": {}, "14": {}, "15": {}, "16": {}, "17": {},
			"18": {}, "19": {}, "20": {}, "21": {}, "holiday": {}
		}
		today = datetime.now().date()
		holiday_default = None

		# populate all booked slot from schedule table into hash table mat, if
		# a time slot is booked with hour=h, day=d, then hash table with key = h,
		# value = d will accept a child object with attributes book = 1
		for booked_day in schedule_list:
			mat[str(booked_day.hour)][booked_day.date.strftime("%d/%m/%Y")] = {"book": 1}

		# populate all avalable slot in working day to hash table, each available slot with
		# hour=h, weekday=wd, we will find current dates maps with weekday and set
		# child object new attributes available = 1
		for index,day in enumerate(working_day):
			if holiday_default == None and day.type == "No":
				holiday_default = day
			for i in time_range:
				day_str = days_range[index].strftime("%d/%m/%Y")

				if (day.is_dayoff(time_range) == True):
					mat[str(i)][day_str] = {"dayoff": 1}
				if getattr(day, "hour_"+str(i)) == 1:
					if not day_str in mat[str(i)]:
						mat[str(i)][day_str] = {}
					if days_range[index] > today:
						mat[str(i)][day_str]["available"] = 1
					if index < 7:
						next_day_str = days_range[index+7].strftime("%d/%m/%Y")
						if not next_day_str in mat[str(i)]:
							mat[str(i)][next_day_str] = {}
						if days_range[index+7] > today:
							mat[str(i)][next_day_str]["available"] = 1

		# populate available slot in holiday default list
		for day in holiday_default_list:
			day_str = day.date.strftime("%d/%m/%Y")
			mat["holiday"][day_str] = 1
			for i in time_range:
				if day_str in mat[str(i)]:
					mat[str(i)][day_str]["holiday"] = 1
					if getattr(holiday_default, "hour_"+str(i)) == 1 and day.date>today and mat[str(i)][day_str].get("dayoff") != 1:
						mat[str(i)][day_str]["holiday_available"] = 1

		# populate available slot in holiday working to hash table
		for day in working_holiday:
			mat["holiday"][day.date.strftime("%d/%m/%Y")] = 1
			for i in time_range:
				if day.is_dayoff(time_range) == False and not day.date.strftime("%d/%m/%Y") in mat[str(i)]:
					mat[str(i)][day.date.strftime("%d/%m/%Y")] = {}
				if day.date.strftime("%d/%m/%Y") in mat[str(i)]:
					mat[str(i)][day.date.strftime("%d/%m/%Y")]["holiday"] = 1
					if getattr(day, "hour_"+str(i)) == 1 and day.date>today:
						mat[str(i)][day.date.strftime("%d/%m/%Y")]["holiday_available"] = 1

		return mat



class CreateView(generic.CreateView):
	model = Schedule
	fields = ['store', 'date', 'hour', 'name', 'phone', 'email', 'symptom']
	template_name = 'home/booking.html'
