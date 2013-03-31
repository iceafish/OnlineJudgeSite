# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contest.models import Contest,Problem

def show_contest(request):
    contests = Contest.objects.all()
    return render_to_response("./contest/index.html",locals())
def show_contest_problem(request,contest_id):
    #to show problems in contest
    
    contest = Contest.objects.get(id = contest_id)
    problem = contest.problemset.all()
    
    
    
    return render_to_response("./contest/show_contest.html",locals())
def show_problem(request,contest_id,problem_id):
    problem = Contest.objects.get(id = contest_id).problemset.get(id = problem_id)
    
    return render_to_response("./contest/show_problem.html",locals())
