from django.utils.functional import curry
from django import forms
from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.forms.widgets import HiddenInput
from django.forms.models import BaseModelFormSet
from django.db import models
from django.contrib.auth.models import Group
from bootstrap3_datetime.widgets import DateTimePicker

from .models import *

class WorkingDayInlineAdminForm(forms.ModelForm):
	class Meta:
		model = WorkingDay
		exclude = []

	type = HiddenInput()

	def __init__(self, *args, **kwargs):
		super(WorkingDayInlineAdminForm, self).__init__(*args, **kwargs)

class WorkingDayInlineFormSet(BaseModelFormSet):
	form = WorkingDayInlineAdminForm
	model = WorkingDay
	def __init__(self, *args, **kwargs):
		kwargs['initial'] = [
		    {'type': 'Mo'}, {'type': 'Tu'}, {'type': 'We'}
		]
		super(WorkingDayInlineFormSet, self).__init__(*args, **kwargs)

class WorkingDayInline(admin.TabularInline):
	model = WorkingDay
	form = WorkingDayInlineAdminForm

	def get_extra(self, request, obj=None, **kwargs):
		extra = 8
		if obj:
			return 0
		return extra
	def get_formset(self, request, obj=None, **kwargs):
		formset = super(WorkingDayInline, self).get_formset(request, obj, **kwargs)

		if not obj:
			initial = [ { 'type': d[0:2] for d in x } for x in WORKING_DAY ]
			if request.method != "GET":
				initial = []
			formset.__init__ = curry(formset.__init__, initial=initial)

		return formset

class HolidayWorkingInlineForm(forms.ModelForm):
	model = HolidayWorking
	date = forms.DateTimeField(
		required=False,
		widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}))

class HolidayWorkingInline(admin.TabularInline):
	model = HolidayWorking
	form = HolidayWorkingInlineForm
	extra = 30

class StoreAmin(admin.ModelAdmin):
	readonly_fields=('id', )

	# list_display = ('store_id', 'name', 'phone', 'mail', 'access')
	list_filter = ('store_id', 'name', 'phone')
	fieldsets = [
		(None, { 'fields': [ 'display', 'store_id', 'name', 'image', 'comment', 'region', 'nearest_station', 'phone', 'mail', 'access'], 'classes': ('wide', ) }),
	]
	inlines = [ WorkingDayInline, HolidayWorkingInline, ]
	prepopulated_fields = { 'name': ['name'] }

	readonly_fields = ('image_show', )
	def image_show(self, instance):
		return '<img src="/%s" />' % instance.image
	image_show.allow_tags = True
	image_show.short_description = 'Image'

	class Media:
		js = (
			'javascripts/store_admin.js',
		)

class HolidayAdmin(admin.ModelAdmin):
	pass

admin.site.register(Store, StoreAmin)
admin.site.register(Holiday, HolidayAdmin)

###################################33

class RegionAmin(admin.ModelAdmin):
	list_display = ('code', 'name')

class NearestStationAmin(admin.ModelAdmin):
	list_display = ('code', 'name')

admin.site.register(Region, RegionAmin)
admin.site.register(NearestStation, NearestStationAmin)
admin.site.register(Sortkey)

admin.site.unregister(Group)
