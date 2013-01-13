from django.conf.urls import patterns, include, url

urlpatterns = patterns('companies.views',
    url(r'^$', 'index'),
    url(r'^(?P<company_id>\d+)/$', 'detail'),
)