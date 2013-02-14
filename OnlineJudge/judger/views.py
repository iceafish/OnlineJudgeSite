from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def submit_code( request, problem_id = 1 ):
    print problem_id
    return render_to_response( "status.html" )