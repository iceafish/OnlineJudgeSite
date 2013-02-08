
from django.http import HttpResponse
from django.shortcuts import render_to_response
def login(request):
    return HttpResponse("loggin have no this problem.")
    
def reg(request):
    
    return render_to_response("users/reg.html")
    
