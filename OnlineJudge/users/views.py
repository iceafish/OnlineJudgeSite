from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from users.models import UserModel

from django.contrib.auth import authenticate, login, logout




from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def login_view(request):
    if request.method == 'POST':
        if 'username' not in request.POST or 'password' not in request.POST:
            raise Http404('Please input username and password')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect("/")
            else:
                raise Http404("Don't welcome you!")
        else:
            raise Http404("Login in failed!")
        return HttpResponseRedirect("/")
       # return render_to_response("users/success.html",context_instance=RequestContext(request))
    raise Http404("Only post allow")

def reg(request):
    if request.user.is_authenticated():
        return HttpResponse("You are logged in.can't register.")
    
    if request.method == 'POST':
        if 'username' not in request.POST or 'password' not in request.POST or 'password2' not in request.POST or 'email' not in request.POST:
            raise Http404('Please fill in the blank!')
        
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        ''' if exsit username-->'''
        if is_ok(username,password):
            UserModel(username=username, password=password).save()
            return HttpResponse("success.")
        else:
            raise Http404('username Error!')
        
    else:
        return render_to_response("users/reg.html",context_instance=RequestContext(request))
        #return render_to_response("users/reg.html",request)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
    #return render_to_response("users/logout.html",context_instance=RequestContext(request))
