from django.conf.urls import patterns, include, url
from myadmin.views import *
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^$', show_manage ),
    url(r'^index/$',show_index),
    url(r'^login/$',login),
)