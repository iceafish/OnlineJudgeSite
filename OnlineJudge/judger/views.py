from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from requestQue.models import RequestList
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def submit_code( request, problem_id = 0 ):
    if request.method == 'POST':
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save( request.FILES['file'] )
            '''
            judge file and judge problem
            judge complate
                save judge info(requestQue)
            else 
                delete all file
                save log
            '''
            return HttpResponseRedirect("/status/")
        else:
            form = SubmitForm()
    return HttpResponseRedirect( "/problem/"+problem_id )