# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contest.models import Contest,Problem,Contest2Problem


def show_contest(request):
    contests = Contest.objects.all()
    return render_to_response("./contest/index.html",locals())
def show_contest_problem(request,contest_id):
    #to show problems in contest
    
    contest = Contest.objects.get(id = contest_id)
    
    c2p = Contest2Problem.objects.filter(contest = contest).order_by('problemID')
    
    return render_to_response("./contest/show_contest.html",locals())
def show_problem(request,contest_id,problem_id):
    contest = Contest.objects.get(id = contest_id)
    
    c2p = Contest2Problem.objects.get(contest = contest,problemID = problem_id)
    
    
    problem = Problem.objects.get(id = c2p.problem.id)
    
    
    return render_to_response("./contest/show_problem.html",locals())
