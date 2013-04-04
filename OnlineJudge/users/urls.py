from django.conf.urls import patterns, include, url
from users.views import *
urlpatterns = patterns('', 
    #url(r'^$',login),
    url(r'^login/$',login_view),
    url(r'^reg/$',reg),
    url(r'^logout/$',logout_view),
    url(r'^changepass/$',change_password),
    url(r'^findpass/$',find_password),
    
)