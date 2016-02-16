from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from models import Store, WorkingDay, HolidayWorking

class StoreAmin(admin.ModelAdmin):
	list_display = ( 'name', 'image', 'comment', 'phone', 'mail', 'access')
	list_filter = ('id', 'name', 'phone')
	fieldsets = [
		(None, { 'fields': [ 'id', 'name', 'image', 'comment', 'phone', 'mail', 'access'], 'classes': ('wide', ) }),
		('More', { 'fields': [ 'created' ], 'classes': ['collapse'] })
	]

	readonly_fields = ('image_show', )
	def image_show(self, instance):
		return '<img src="/%s" />' % instance.image
	image_show.allow_tags = True
	image_show.short_description = 'Image'

	def get_urls(self):
		urls = super(StoreAmin, self).get_urls()
		my_urls = [
			url(r'^store_view/$', self.store_list_view),
		]
		return my_urls + urls

	def store_list_view(self, request):
		context = dict(
			self.admin_site.each_context(request),
		)
		return TemplateResponse(request, "admin/store_view_plate.html", context)

class WorkingDayAdmin(admin.ModelAdmin):
	pass

class HolidayWorkingAdmin(admin.ModelAdmin):
	pass

admin.site.register(Store, StoreAmin)
admin.site.register(WorkingDay, WorkingDayAdmin)
admin.site.register(HolidayWorking, HolidayWorkingAdmin)