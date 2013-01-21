#from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def show_problem_list( request ):
    return HttpResponse( "show problem list" )