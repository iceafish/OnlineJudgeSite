from django.http import HttpResponse
from django.shortcuts import render_to_response
from problems import models
from judger.forms import SubmitForm
from problems.models import Problem
# Create your views here.

def show_problem_list( request, page = 1 ):
    
    try:
        page = int(page)
    except ValueError:
        raise Http404()
    start = (page-1)*10+1
    end = page*10
    pagenum = int(Problem.objects.order_by('-id')[0].id) / 10
    pagenum = range(1,pagenum+2)
    
    problems = models.Problem.objects.filter(id__range=(start,end))
    
    return render_to_response( "problemlist.html", locals() )

def show_problem( request, problem_id ):
    item = models.Problem.objects.get( id = int(problem_id) )
    if ( not item or not item.UseAble ):
        return HttpResponse("have no this problem.")
    problem = item
    form = SubmitForm()
    return render_to_response( "problemInfo.html", locals() )

