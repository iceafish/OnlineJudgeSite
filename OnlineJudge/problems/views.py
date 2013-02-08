from django.http import HttpResponse
from django.shortcuts import render_to_response
from problems import models
# Create your views here.
'''
def show_problem_list( Response ):
    return HttpResponse( "show problem list" )
'''
def show_problem_list( request, page = 1 ):
    '''
    try:
        page = int(page)
    except ValueError:
        raise Http404()
    start = (page-1)*100
    end = page*100+1
    '''
    problems = models.Problem.objects.filter()
    
    return render_to_response( "problemlist.html", { 'problems': problems } )

def show_problem( request, problem_id ):

    item = models.Problem.objects.get( id = int(problem_id) )
    if ( not item or not item.UseAble ):
        return HttpResponse("have no this problem.")
    
    return render_to_response( "problemInfo.html", { 'problem': item } )