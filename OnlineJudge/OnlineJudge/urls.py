from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from problems import urls
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
    url(r'^image/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMAGE_PATH}),
    url(r'^$', show_index),

    url(r'^problem/', include( urls )),
    url(r'^faq/$', show_faq),
    #url(r'^submit/(\d+)$', submit_code),
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^problemlist/(\d+)/$',show_problem_list),
    #url(r'^problem/(\d+)/$',show_problem),
    
)
