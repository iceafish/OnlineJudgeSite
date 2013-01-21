#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

from problems.models import *
def show_index( request ):
    
    return render_to_response("index.html", locals() )

# Home Contests Problems Status Ranklist F.A.Qs

def show_faq( request ):
    
    return render_to_response("faq.html", locals() )


def show_problem_list(request,page):
    try:
        page=int(page)
    except ValueError:
        raise Http404()
    start = (page-1)*100
    end = page*100+1
    problems = Problem.objects.filter(id__range=(start,end))
    return render_to_response("problemlist.html",locals() )
def show_problem(request):
    
    
    return render_to_response("problem.html",locals() )