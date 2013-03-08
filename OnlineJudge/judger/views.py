from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from requestQue.models import RequestList
from time import ctime
import datetime
from socket import *
from setting import *
from struct import unpack
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def send_msg():
    print 'sending msg...'

def submit_code( request, problem_id = 0 ):
    if problem_id == 0:
        return  
    host = judge_server
    port = judge_post
    s = socket(AF_INET, SOCK_DGRAM)
    if request.method == 'POST':
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            form.save( file )
            RList = RequestList( user = request.session['user_name'],
                                 problemID = problem_id,
                                 result = 'Waiting',
                                 timeUsed = -1,
                                 languageTypeID = request.POST['Language'],
                                 submitTime = datetime.datetime.now(),
                                 codeFile = "/judger/tmp/"+file.name)
            RList.save()
            s.sendto('', (host, port))
            ReturnRes = s.recvfrom(2048)[0]
            res, timeuse = unpack('ii', ReturnRes)
            print res ,timeuse
            save_res(RList,res,timeuse)
            return HttpResponseRedirect("/status/")
        else:
            form = SubmitForm()
    return HttpResponseRedirect( "/problem/"+problem_id )

def save_res(RList,res,timeuse):
    anws = {
            1 : 'Accepted',
            2 : 'Wrong Answer',
            3 : 'Presentation Error',
            4 : 'Time Limit Exceeded',
            5 : 'Memory Limit Exceeded',
            6 : 'Runtime Error',
            7 : 'Output Limit Exceeded',
            8 : 'Compile Error',
            9 : 'Validator Error' }
    if  0<res<10 :
        RList.result = anws[ res ]
        RList.timeUsed = timeuse
    else:
        RList.result = 'System Error'
    RList.save()
    