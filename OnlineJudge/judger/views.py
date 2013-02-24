from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from requestQue.models import RequestList
import datetime
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def submit_code( request, problem_id = 0 ):
    if request.method == 'POST':
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            #save imfo just for test
            file = request.FILES['file']
            form.save( file )
            '''
            judge file and judge problem
            judge complate
                save judge info(requestQue)
            else 
                delete all file
                save log
            '''
            ReturnRes = "Accept"
            RList = RequestList( user = request.session['user_name'], 
                                 problemID = problem_id,
                                 result = ReturnRes,
                                 timeUsed = 0,
                                 languageTypeID = request.POST['Language'],
                                 submitTime = datetime.datetime.now(),
                                 codeFile = "/judger/tmp/"+file.name)
            print RList.languageTypeID
            RList.save()
            return HttpResponseRedirect("/status/")
        else:
            form = SubmitForm()
    return HttpResponseRedirect( "/problem/"+problem_id )