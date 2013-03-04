from django.conf.urls import patterns, include, url
from myadmin.views import *
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^$', show_manage ),
    url(r'^logout/$',logout),
    url(r'^index/$',show_index),
    url(r'^login/$',login),
    url(r'^reg/$',reg),
    url(r'^user/add/$',add_user),
    url(r'^user/$',show_user),
    url(r'^user/(\d+)/$',alter_user),
    
    
    url(r'^superuser/add/$',add_super_user),
    url(r'^superuser/$',show_super_user),
    url(r'^superuser/(\d+)/$',alter_super_user),
    
  #  url(r'^problem/add/$',add_problem),
  #  url(r'^problem/$',show_problem),
  #  url(r'^problem/(\d+)/$',alter_problem),
    
)
