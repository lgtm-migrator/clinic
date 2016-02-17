from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from .models import Store, WorkingDay, HolidayWorking, Region, NearestStation, Sortkey

class WorkingDayInline(admin.TabularInline):
	model = WorkingDay
	extra = 8
class HolidayWorkingInline(admin.TabularInline):
	model = HolidayWorking
	extra = 30

class StoreAmin(admin.ModelAdmin):
	readonly_fields=('id',)

	list_display = ( 'name', 'image', 'comment', 'phone', 'mail', 'access')
	list_filter = ('id', 'name', 'phone')
	fieldsets = [
		(None, { 'fields': [ 'name', 'image', 'comment', 'phone', 'mail', 'access'], 'classes': ('wide', ) }),
	]
	inlines = [ WorkingDayInline, HolidayWorkingInline, ]

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


admin.site.register(Region)
admin.site.register(NearestStation)
admin.site.register(Sortkey)
