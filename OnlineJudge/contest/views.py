# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contest.models import Contest,Problem
from judger.forms import SubmitForm

def show_contest(request):
    contests = Contest.objects.all()
    
    render_to_response("./contest/index.html",locals())
def show_contest_problem(request,contest_id):
    #to show problems in contest
    contest = Contest.objects.get( id = contest_id )
    problems = Problem.objects.filter( contest_id = contest_id )
    render_to_response("./contest/show_contest.html",locals())
    