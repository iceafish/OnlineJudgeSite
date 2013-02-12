from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
from myadmin.models import AdminUser
from django.template import RequestContext
# Create your views here.
'''
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
'''
# myAdmin
def show_manage( request ):
    if "admin_username" not in request.session:
        info = AdminUser.objects.all()
        if not info:
            return HttpResponseRedirect('/myadmin/reg/')
        else:
            return HttpResponseRedirect("/myadmin/login/")
    else:
        return HttpResponseRedirect("/myadmin/index/")
    
def reg(request):
    if not AdminUser.objects.all():
        if request.method != "POST":
            return render_to_response('myadmin/reg.html',context_instance=RequestContext(request))
        else:
            AdminUser(username = request.POST['username'],password = request.POST['password'] ).save()
            request.session['admin_username'] = request.POST['username']
            return HttpResponseRedirect("/myadmin/index/")
    else:
        raise Http404("There is a Account.Don't open register")
        


def login(request):
    if "admin_username" in request.session:
        # is already login
        return HttpResponseRedirect("/myadmin/index/")
    if request.method == "POST":
        if "username" not in request.POST or "password" not in request.POST:
            raise Http404("Please input username and password!")
        try:
            u=AdminUser.objects.get(username=request.POST['username'],password=request.POST['password'])
        except AdminUser.DoesNotExist:
            raise Http404("Login Failed!")
        request.session["admin_username"] = u.username
        return HttpResponseRedirect("/myadmin/index/")
    else:
        return render_to_response("myadmin/login.html",context_instance=RequestContext(request))
    
def logout(request):
    if "admin_username" in request.session:
        del request.session['admin_username']
    return HttpResponseRedirect('/myadmin/')       

def show_index(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    
    return render_to_response("myadmin/index.html",locals())
