from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
# Create your views here.

# myAdmin
def show_manage( Response ):
    return HttpResponse( "adminstrator page." )