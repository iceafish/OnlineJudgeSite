from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from judger.models import RequestList
from time import ctime
import datetime
from socket import *
from setting import *
from struct import unpack
from JudgeQue import put,pull,getSize

def add_judge_request( RList ):
    if getSize() < JUDGEQUE_SIZE:
        put( RList )
        print 'now queue size is',getSize()
    else:
        print 'err'
    print 'sending msg...'


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def submit_code( request, problem_id = 0 ):
    if problem_id == 0:
        return  
    host = JUDGE_HOST
    port = JUDGE_POST
    s = socket(AF_INET, SOCK_DGRAM)
    if request.method == 'POST':
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = form.save( file )
            RList = RequestList( user = request.session['user_name'],
                                 problemID = problem_id,
                                 result = 'Waiting',
                                 timeUsed = -1,
                                 languageTypeID = request.POST['Language'],
                                 submitTime = datetime.datetime.now(),
                                 codeFile = "/judger/user_code/"+file_name)
            RList.save()
            ########
            add_judge_request(RList)
            print getSize()
            
            
            
            s.sendto('', (host, port))
            print 111
            ReturnRes = s.recvfrom(2048)[0]
            print 222
            res, timeuse = unpack('ii', ReturnRes)
            print 333
            print res
            print timeuse
            save_res(RList,res,timeuse)
            print 2
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
    