from django.utils.functional import curry
from django import forms
from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.forms.models import BaseModelFormSet
from .models import Store, WorkingDay, HolidayWorking, Region, NearestStation, Sortkey

class WorkingDayInlineAdminForm(forms.ModelForm):
	
	class Meta:
		model = WorkingDay
		exclude = []

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
	extra = 8
	form = WorkingDayInlineAdminForm
	# formset = WorkingDayInlineFormSet
	
class HolidayWorkingInline(admin.TabularInline):
	model = HolidayWorking
	extra = 30

class StoreAmin(admin.ModelAdmin):
	readonly_fields=('id',)

	list_display = ( 'name', 'phone', 'mail', 'access')
	list_filter = ('id', 'name', 'phone')
	fieldsets = [
		(None, { 'fields': [ 'name', 'image', 'comment', 'phone', 'mail', 'access'], 'classes': ('wide', ) }),
	]
	inlines = [ WorkingDayInline, HolidayWorkingInline, ]
	prepopulated_fields = { 'name': ['name'] }

	readonly_fields = ('image_show', )
	def image_show(self, instance):
		return '<img src="/%s" />' % instance.image
	image_show.allow_tags = True
	image_show.short_description = 'Image'

class WorkingDayAdmin(admin.ModelAdmin):
	pass

class HolidayWorkingAdmin(admin.ModelAdmin):
	pass

admin.site.register(Store, StoreAmin)
admin.site.register(WorkingDay, WorkingDayAdmin)
admin.site.register(HolidayWorking, HolidayWorkingAdmin)

###################################33

class RegionAmin(admin.ModelAdmin):
	list_display = ('code', 'name')

class NearestStationAmin(admin.ModelAdmin):
	list_display = ('code', 'name')

admin.site.register(Region, RegionAmin)
admin.site.register(NearestStation, NearestStationAmin)
admin.site.register(Sortkey)
