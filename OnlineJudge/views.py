from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from requestQue.models import RequestList
from problems.models import *

def show_index( request ):
    return render_to_response("index.html", locals() )

# Home Contests Problems Status Ranklist F.A.Qs
# just define
def show_faq( request ):
    return render_to_response("faq.html", locals() )

def show_contest( Response ):
    return HttpResponse( "this is Response." )
    
def show_ranklist( request ):
    return render_to_response("ranklist/index.html",locals())

def show_status( request ):
    
    statuslist = RequestList.objects.filter()
    return render_to_response( "status.html" ,locals() )