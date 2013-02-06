#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

from problems.models import *
def show_index( request ):
    
    return render_to_response("index.html", locals() )

# Home Contests Problems Status Ranklist F.A.Qs

def show_faq( request ):
    
    return render_to_response("faq.html", locals() )


