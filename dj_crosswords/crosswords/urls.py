from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'base.views.home'),
    url(r'^api/', include('base.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
    # Examples:
    # url(r'^$', 'crosswords.views.home', name='home'),
    # url(r'^crosswords/', include('crosswords.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
