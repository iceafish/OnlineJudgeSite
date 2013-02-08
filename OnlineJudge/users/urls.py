from django.conf.urls import patterns, include, url
from users.views import *
urlpatterns = patterns('', 
    #url(r'^$',login),
    url(r'^login/$',login),
    url(r'^reg/$',reg),
    
)