from django.conf.urls import patterns, include, url
from problems.views import show_problem_list 

urlpatterns = patterns('', 
    url(r'^$',show_problem_list),
    url(r'^(\d+)$', show_problem_list),
)