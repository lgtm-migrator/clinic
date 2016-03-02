from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^store/?$', views.IndexView.as_view(), name='home'),
    url(r'^admin/store/?$', views.IndexView.as_view(), name='admin_store'),
    url(r'^admin/home/store/?$', views.IndexView.as_view(), name='admin_store'),
    url(r'^store/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='store-schedule'),
    url(r'^booking/(?P<store>[0-9]+)/(?P<date>[0-9]{8})/(?P<hour>[0-9]{1,2})/$', views.ScheView, name='booking'),
    url(r'^timeslot_checking/(?P<store>[0-9]+)/(?P<date>[0-9]{8})/(?P<hour>[0-9]{1,2})/$', views.TimeslotCheck, name='timeslot-checking'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'})
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
