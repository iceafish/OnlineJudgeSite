from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from users.models import UserModel
from django.contrib.auth.models import User
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
        try:
            u = User.objects.get(username = username)
        except:
            u=None
        if not u and password==password2:
            u = User(username=username,email=email)
            u.set_password(password)
            u.save()
            UserModel(user=u).save()
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            raise Http404('Error!Please Check!OR USERNAME REPEAT!')
    else:
        return render_to_response("users/reg.html",context_instance=RequestContext(request))
        #return render_to_response("users/reg.html",request)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
    #return render_to_response("users/logout.html",context_instance=RequestContext(request))
def change_password(request):
    if not request.user.is_authenticated():
        return HttpResponse("Please Login First.")
    
    if request.method == 'POST':
        if 'old_password' not in request.POST or 'new_password' not in request.POST or 'new_password2' not in request.POST:
            return HttpResponse("ERROR")
        user = User.objects.get(username = request.user.username )
        if user.check_password(request.POST['old_password']):
            if request.POST['new_password'] == request.POST['new_password2']:
                user.set_password(request.POST['new_password'])
                user.save()
                return HttpResponse("Change Password Successful!")
            else:
                return HttpResponse("New Password Confirm ERROR!")
        else:
            return HttpResponse("Old Password ERROR!")
        
    else:
        return render_to_response("users/changepass.html",locals())
    
def find_password(request):
    pass

def my_info(request):
    if not request.user.is_authenticated():
        return HttpResponse("Please Login First.")
    try:
        u = User.objects.get(id = request.user.id)
    except:
        return HttpResponse("Not Exist This user.")
    try:
        user = u.usermodel
    except:
        user = UserModel(user = u)
    solved_list = user.problems.all()
    unsolved_list = user.unsolved_problems.all()
    
    return render_to_response("users/myinfo.html",locals())
