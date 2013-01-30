from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'companies.views.index'),
    url(r'^companies/', include('companies.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^login/', 'companies.views.login_view'),
    url(r'^logout/', 'companies.views.logout_view'),
    url(r'^signup/', 'companies.views.signup_view'),
)