from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^board/$', 'base.api.board'),
    url(r'^history/$', 'base.api.history')


)