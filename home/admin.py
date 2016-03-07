# -*- coding: utf-8 -*-
from django.utils.functional import curry
from django import forms
from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.forms.widgets import HiddenInput
from django.forms.models import BaseModelFormSet, BaseInlineFormSet
from django.db import models
from django.contrib.auth.models import Group
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation import ugettext as _
from django.utils import translation
from django.core.exceptions import ValidationError

from clinic import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER

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
	verbose_name_plural = _('Working days')

	def get_extra(self, request, obj=None, **kwargs):
		extra = 8
		if obj:
			return 0
		return extra
	def get_formset(self, request, obj=None, **kwargs):
		formset = super(WorkingDayInline, self).get_formset(request, obj, **kwargs)

		if not obj:
			initial = [ { 'type': x[:1][0] } for x in WORKING_DAY ]
			if request.method != "GET":
				initial = []
			formset.__init__ = curry(formset.__init__, initial=initial)

		return formset

class CustomDateTimePicker(DateTimePicker):
	class Media:
		class JsFiles(object):
			def __iter__(self):
				yield 'bootstrap3_datetime/js/moment.min.js'
				yield 'bootstrap3_datetime/js/bootstrap-datetimepicker-reset.min.js'
				yield 'bootstrap3_datetime/js/bootstrap-datetimepicker-custom.min.js'
				lang = translation.get_language()
				if lang:
					lang = lang.lower()
					if lang.startswith('zh') and lang not in ('zh-cn', 'zh-tw',):
						if lang == 'zh-hk':
							lang = 'zh-tw'
						else:
							lang = 'zh-cn'
					elif len(lang) > 2 and lang not in ('ar-ma', 'en-au', 'en-ca', 'en-gb', 
														'fa-ir', 'fr-ca', 'ms-my', 'pt-br', 
														'rs-latin', 'tzm-la', ):
						lang = lang[:2]
					if lang != 'en':
						yield 'bootstrap3_datetime/js/locales/bootstrap-datetimepicker.%s.js' % (lang)

		js = JsFiles()
		css = {'all': ('bootstrap3_datetime/css/bootstrap-datetimepicker.min.css',), }

	js_template = '''
		<script>
			$(function() {
				$("#%(picker_id)s").datetimepicker(%(options)s);
			});
		</script>'''

class HolidayWorkingInlineForm(forms.ModelForm):
	model = HolidayWorking
	date = forms.DateTimeField(
		required=False,
		label=_("Holiday working days"),
		widget=CustomDateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))

class HolidayWorkingInlineFormSet(BaseInlineFormSet):
	def clean(self):
		super(HolidayWorkingInlineFormSet, self).clean()
		# TODO: fix exeption when date is null, but time fields.

class HolidayWorkingInline(admin.TabularInline):
	model = HolidayWorking
	form = HolidayWorkingInlineForm
	formset = HolidayWorkingInlineFormSet
	extra = 30
	verbose_name_plural = _('Holiday working days')


def generate_store_id():
	try:
		return "%05d" % (Store.objects.last().id + 1, )
	except:
		return '00001'

class DisplaySelect(forms.widgets.NullBooleanSelect):
	def __init__(self, attrs=None):
		choices = (('2', _('Show')),
			('3', _('Not show')))
		super(forms.widgets.NullBooleanSelect, self).__init__(attrs, choices)

class StoreAdminForm(forms.ModelForm):
	store_id = forms.CharField(
		label=_('Store ID'), 
		widget=forms.widgets.TextInput(attrs={ 'required': 'required' }), 
		)

	class Meta:
		model = Store
		exclude = ['created', ]
	def __init__(self, *args, **kwargs):
		super(StoreAdminForm, self).__init__(*args, **kwargs)
		self.fields["store_id"].initial = generate_store_id()

		self.fields["name"].widget = forms.widgets.TextInput(attrs={ 'autocomplete': 'off'})
		self.fields["name"].error_messages = { 'required': '店舗名を入力してください。' }

		self.fields["mail"].widget = forms.widgets.EmailInput(attrs={ 'autocomplete': 'off'})
		self.fields["mail"].error_messages = { 'required': 'メールアドレスを入力してください。', 'invalid':"メールアドレスの形式が正しくありません。"}
		
		self.fields["phone"].widget = forms.widgets.TextInput(attrs={ 'autocomplete': 'off'})
		self.fields["phone"].error_messages = { 'required': '電話番号を入力してください。' }
		
		self.fields["access"].widget = forms.widgets.TextInput(attrs={ 'autocomplete': 'off'})
		self.fields["comment"].widget = forms.widgets.Textarea(attrs={'rows':4, 'cols':40})
		self.fields["display"].widget = DisplaySelect()

		self.fields["region"].label = _("Region")
		self.fields["nearest_station"].label = _("Nearest station")
		# self.fields["store_id"].widget = forms.widgets.TextInput()
		for field in iter(self.fields):
			if not isinstance(self.fields[field].widget, forms.widgets.CheckboxInput):
				self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})

class StoreAmin(admin.ModelAdmin):
	readonly_fields=('id', )
	form = StoreAdminForm

	# list_display = ('store_id', 'name', 'phone', 'mail', 'access')
	list_filter = ('store_id', 'name', 'phone')
	fieldsets = [
		(None, { 'fields': [ 'display', 'store_id', 'name', 'image', 'comment', 'region', 'nearest_station', 'phone', 'mail', 'access'], 'classes': ('wide', ) }),
	]
	inlines = [ WorkingDayInline, HolidayWorkingInline, ]
	prepopulated_fields = { 'name': ['name'] }

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

class SortKeyAmin(admin.ModelAdmin):
	change_list_template = 'admin/sortkey_change_list.html'

admin.site.register(Region, RegionAmin)
admin.site.register(NearestStation, NearestStationAmin)
admin.site.register(Sortkey, SortKeyAmin)

admin.site.unregister(Group)
