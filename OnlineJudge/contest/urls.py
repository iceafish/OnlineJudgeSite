from django.conf.urls import patterns, include, url
from contest.views import show_contest,show_contest_problem,show_problem


urlpatterns = patterns('', 
    url(r'^$', show_contest ),
    url(r'^(\d+)/$',show_contest_problem),
    url(r'^(\d+)/(\d+)/$',show_problem),
    
    
)