from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from JRequest.views import submit_code

import problems.urls
import users.urls
import myadmin.urls
#import contest.urls
#from problems import urls 
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
    url(r'^image/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMAGE_PATH}),

    url(r'^$', show_index),
    url(r'^problem/', include( problems.urls )),
    url(r'^submit/(\d+)/$', submit_code),
    url(r'^user/', include( users.urls )),

#Not define just have something show    
    #url(r'^contests/', include(contest.urls)),
    url(r'^ranklist/$', show_ranklist),
    url(r'^status/$', show_status),
    url(r'^status/(\d+)$', show_status),
    
    url(r'^faq/$', show_faq),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^myadmin/',include(myadmin.urls))
    
)
