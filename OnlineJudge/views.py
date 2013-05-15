from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from judger.models import RequestList
from problems.models import *
from users.models import UserModel
def show_index( request ):
    return render_to_response("index.html", locals() )

# Home Contests Problems Status Ranklist F.A.Qs
def show_faq( request ):
    return render_to_response("faq.html", locals() )

def show_contest( Response ):
    return HttpResponse( "this is Response." )
    
def show_ranklist( request ):
    u=UserModel.objects.order_by("-solved")
    return render_to_response("ranklist/index.html",locals())

def show_status( request ):
    statuslist = RequestList.objects.order_by("-id")
    return render_to_response( "status.html" ,locals() )