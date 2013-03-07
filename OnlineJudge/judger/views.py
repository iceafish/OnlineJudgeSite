from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from requestQue.models import RequestList
from time import ctime
import datetime
from socket import *
from setting import *
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def submit_code( request, problem_id = 0 ):
    host = judge_server
    port = judge_post
    s = socket(AF_INET, SOCK_DGRAM)
    #s.sendto('', (host, port))
    #buf = s.recvfrom(2048)[0]
    if request.method == 'POST':
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            #save imfo just for test
            file = request.FILES['file']
            form.save( file )
            RList = RequestList( user = request.session['user_name'], 
                                 problemID = problem_id,
                                 result = 'Waiting',
                                 timeUsed = -1,
                                 languageTypeID = request.POST['Language'],
                                 submitTime = datetime.datetime.now(),
                                 codeFile = "/judger/tmp/"+file.name)
            #print RList.languageTypeID
            RList.save()
            s.sendto('', (host, port))
            ReturnRes = s.recvfrom(1024)
            print ReturnRes
            RList.result = ReturnRes
            RList.save()
            return HttpResponseRedirect("/status/")
        else:
            form = SubmitForm()
    return HttpResponseRedirect( "/problem/"+problem_id )