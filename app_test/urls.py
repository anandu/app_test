from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from views import hello

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app_test.views.hello', name='hello'),
    url(r'^app_test/', hello),
    # url(r'^app_test/', include('app_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
