from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
def login(request):
    return HttpResponse("loggin have no this problem.")
    
def reg(request):
    if request.method == 'POST':
        if 'username' not in request.POST or 'password' not in request.POST:
            raise Http404('username or password not in POST')
        
        username = request.POST['username']
        password = request.POST['password']
        
        
    else:
        return render_to_response("users/reg.html")
    
