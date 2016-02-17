from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Store, Schedule, Region, \
	NearestStation, Sortkey

import django_filters
from django_select2.forms import Select2Widget

class StoreFilter(django_filters.FilterSet):
	# See: https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
	name = django_filters.ModelChoiceFilter(
		queryset=Region.objects.all(),
		widget=Select2Widget,
		lookup_type='icontains'
	)
	phone = django_filters.ModelChoiceFilter(
		queryset=NearestStation.objects.all(),
		widget=Select2Widget,
		lookup_type='icontains'
	)
	class Meta:
		model = Store
		fields = ['name', 'phone',]
		# order_by = ( [ 'name', 'phone' ], ['access', 'comment'])

class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'stores'
	paginate_by = 20
	model = Store

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['filter'] = StoreFilter(self.request.GET, queryset=self.model.objects.all())
		return context

class DetailView(generic.DetailView):
	model = Store
	template_name = 'home/detail.html'

class CreateView(generic.CreateView):
	model = Schedule
	fields = ['store', 'date', 'hour', 'name', 'phone', 'email', 'symptom']
	template_name = 'home/booking.html'



