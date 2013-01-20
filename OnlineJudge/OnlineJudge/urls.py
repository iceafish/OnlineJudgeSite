from django.conf.urls import patterns, include, url
from views import show_index,show_faq
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', show_index),

    #url(r'^problem/', include( urls )),
    url(r'^faq/$', show_faq),
    #url(r'^admin/', include(admin.site.urls)),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)