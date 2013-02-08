from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from users.models import UserModel

def login(request):
    if request.method == 'POST':
        if username not in request.POST or password not in request.POST:
            raise Http404('Please input username and password')
        if user_id not in request.session:
            try:
                u = UserModel.objects.get(username = username)
            except:
                raise Http404('Not exist this username')
            if u.password == request.POST['password'] : 
                request.session['user_id'] = u.id
            else:
                raise Http404('Password is Error')
        else:
            raise Http404("You are logged in.")
        
        return render_to_response("user/success.html",context_instance=RequestContext(request))
    raise Http404("Only post allow")

def reg(request):
    if request.method == 'POST':
        if 'username' not in request.POST or 'password' not in request.POST:
            raise Http404('username or password not in POST')
        
        username = request.POST['username']
        password = request.POST['password']
        ''' if exsit username-->'''
        if is_ok(username,password):
            UserModel(username=username, password=password).save()
            return HttpResponse("success.")
        else:
            raise Http404('username Error!')
        
    else:
        return render_to_response("users/reg.html",context_instance=RequestContext(request))
    
def is_ok(username,password):
    if username == "" or password == "":
        return False
    else:
        try:
            UserModel.objects.get(username = username)
        except UserModel.DoesNotExist:
            return True
        return False
    
            