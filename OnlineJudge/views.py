from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

from problems.models import *

def show_index( request ):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    else:
        user_id = 0
    return render_to_response("index.html", locals() )

# Home Contests Problems Status Ranklist F.A.Qs
def submit_code( request, problem_id = 0 ):
    return render_to_response("submit.html")


# just define
def show_faq( request ):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    else:
        user_id = 0
    return render_to_response("faq.html", locals() )

def show_contest( Response ):
    return HttpResponse( "this is Response." )
    
def show_ranklist( Response ):
    return HttpResponse("this is ranklist.")

def show_status( Response ):
    return HttpResponse( "this is servers status" )