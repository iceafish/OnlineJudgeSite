from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
from myadmin.models import AdminUser
from django.template import RequestContext
from users.models import *
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

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

def add_user(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        accept = request.POST['accept']
        submit = request.POST['submit']
        score = request.POST['score']
        try:
            UserModel.objects.get(username = username)
        except:
            UserModel(username=username,password=password,accept=accept,submit=submit,score=score).save()
        else:
            raise Http404("Username is repeat.")
        return HttpResponse(ur'Add User is success <a href="/myadmin/index/">Index</a>')
    else:
        return render_to_response("myadmin/user/add.html",locals())

def alter_user(request,id):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    u=UserModel.objects.get(id=id)
    print u
    if request.method == 'POST':
        UserModel(id=u.id,username=u.username,password=request.POST['password'],submit=request.POST['submit'],accept=request.POST['accept'],score=request.POST['score']).save()
        return HttpResponse(ur'Alter user info success <a href="/myadmin/index/">Index</a>')
        
    else:
        return render_to_response("myadmin/user/alteruser.html",locals())
def show_user(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    u=UserModel.objects.all()
    return render_to_response("myadmin/user/showuser.html",locals())
def show_super_user(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    u=SuperUserModel.objects.all()
    return render_to_response("myadmin/superuser/showuser.html",locals())
def add_super_user(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    if request.method != "POST":
        return render_to_response('myadmin/reg.html',context_instance=RequestContext(request))
    else:
        AdminUser(username = request.POST['username'],password = request.POST['password'] ).save()
        return HttpResponseRedirect("/myadmin/index/")
def alter_super_user(request):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
    if request.method != "POST":
        return render_to_response('myadmin/reg.html',context_instance=RequestContext(request))
    else:
        try:
            u=AdminUser.objects.get(username=request.POST['username'])
        except:
            return HttpResponse('Not found this SuperUsername')
        AdminUser(username = request.POST['username'],password = request.POST['password'] ).save()
        return HttpResponse('Alter supername is success.<a href="/myadmin/index/">To->Index</a>')
    #HttpResponseRedirect("/myadmin/index/")

'''
def add_object(request,table_name):
    if "admin_username" not in request.session:
        #is not login
        return HttpResponseRedirect("/myadmin/")
'''
