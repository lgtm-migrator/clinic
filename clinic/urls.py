from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^store/?$', views.IndexView.as_view(), name='home'),
    url(r'^store/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^booking/$', views.CreateView.as_view(), name='booking'),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)