from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'companies.views.index'),
    url(r'^companies/', include('companies.urls')),
    url(r'^admin/', include(admin.site.urls)),
)