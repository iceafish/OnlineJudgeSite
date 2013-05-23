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

def show_status( request ,page=0):
    #statuslist = RequestList.objects.order_by("-id")[0]
    try:
        page = int(page)
    except ValueError:
        raise Http404()
    if page!=0:
        start = (page-1)*10+1
        end = page*10
    pagenum1 = int(RequestList.objects.order_by('-id')[0].id) / 10
    pagenum = range(1,pagenum1+2)
    if page == 0:
        start = (pagenum1)*10+1
        end = (pagenum1+1)*10
    statuslist = RequestList.objects.filter(id__range=(start,end))
    return render_to_response( "status.html" ,locals() )