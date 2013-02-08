from django.conf.urls import patterns, include, url
from problems.views import show_problem_list,show_problem

urlpatterns = patterns('', 
    url(r'^$',show_problem_list),
    url(r'^(\d+)$', show_problem),
    
    
    #url(r'^problemlist/(\d+)/$',show_problem_list),
    #url(r'^problem/(\d+)/$',show_problem),
    
    
)