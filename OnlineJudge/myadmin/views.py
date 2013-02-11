from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
from myadmin.models import AdminUser
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# myAdmin
def show_manage( request ):
    return render_to_response("myadmin/login.html")
def login(request):
    if "admin_username" in request.session:
        # is already login
        return HttpResponseRedirect("/myadmin/index/")
    if request.method == "POST":
        if "username" not in request.POST or "password" not in request.POST:
            raise Http404("Please input username and password!")
        try:
            u=AdminUser.objects.get(username=username,password=password)
        except AdminUser.DoesNotExist:
            raise Http404("Login Failed!")
        request.session["admin_uesrname"] = u.username
        return HttpResponseRedirect("/myadmin/index/")
    else:
        return HttpResponseRedirect("/myadmin/")
    
def show_index(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    #
    #
    #
    #
    #
    #
    return render_to_response("myadmin/index.html",locals())