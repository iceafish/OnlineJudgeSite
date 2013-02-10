from django.conf.urls import patterns, include, url
from myAdmin import views
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^$', views.show_manage ),
    
)