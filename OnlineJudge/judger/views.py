from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from judger.forms import SubmitForm
from judger.models import RequestList
from time import ctime
import datetime
from socket import *
from setting import *
from struct import unpack
from JudgeQue import put,pull,getSize,getReq,isEmpty
from problems.models import Problem
from users.models import *
import threading
import time
    
            
lock = threading.Lock()
mythread = MyThread()
mythread.start()


#-----start__threading--------------------------------#

#-----------------------------------------------------#
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
    temp_prob = None
    if problem_id == 0 and not isEmpty():
        temp_prob = pull()
    
    host = JUDGE_HOST
    port = JUDGE_POST
    
    
    if (request and request.method == 'POST') or temp_prob!=None:
        if problem_id != 0:
            form = SubmitForm(request.POST,request.FILES)
        else:
            form = None
        if ( form and form.is_valid() ) or temp_prob:
            if form and form.is_valid():
                lock.acquire() # ----------------------------------------------
                file = request.FILES['file']
                file_name = form.save( file )
                RList = RequestList( user = request.user.username,
                                     problemID = problem_id,
                                     result = 'Waiting',
                                     timeUsed = -1,
                                     languageTypeID = request.POST['Language'],
                                     submitTime = datetime.datetime.now(),
                                     codeFile = "./judger/user_code/"+file_name)
                RList.save()
                curprob = Problem.objects.get( id = problem_id )
                u = User.objects.get(username = RList.user)
                curuser = u.usermodel
                curprob.submit += 1
                curuser.submit += 1
                curprob.save()
                curuser.save()
                
                lock.release()#<---------------------------------------------
            else:
                lock.acquire() # ----------------------------------------------
                RList = temp_prob
                curprob = Problem.objects.get( id = RList.problemID )
                u = User.objects.get(username = RList.user)
                curuser = u.usermodel
                lock.release()
            
            s = socket(AF_INET, SOCK_STREAM)
            try:
                s.connect((host, port))
            except error:
                put(RList)
                return HttpResponseRedirect("/status/")
            
            s.sendall('%d' % RList.id)
            ReturnRes = s.recv(2048)
            s.close()
            
            
            res, timeuse = unpack('ii', ReturnRes)
            #save_res(RList,res,timeuse,curprob,curuser)
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
            if  0 < res < 10:
                RList.result = anws[ res ]
                RList.timeUsed = timeuse
                if res == 1:
                    if  not curuser.problems.filter(id = curprob.id):
                        curuser.solved += 1
                        curuser.problems.add(curprob)
                        if curuser.unsolved_problems.filter(id = curprob.id):
                            curuser.unsolved_problems.remove(curprob)
                    curuser.accept += 1
                    curuser.save()
                    curprob.accept += 1

                elif res == 2:
                    if  not curuser.problems.filter(id = curprob.id):
                        if not curuser.unsolved_problems.filter(id = curprob.id):
                            curuser.unsolved_problems.add(curprob)
                            curuser.save()
                    curprob.WA += 1
                elif res == 3:
                    if  not curuser.problems.filter(id = curprob.id):
                        if not curuser.unsolved_problems.filter(id = curprob.id):
                            curuser.unsolved_problems.add(curprob)
                            curuser.save()
                    curprob.PE += 1
                elif res == 4:
                    if  not curuser.problems.filter(id = curprob.id):
                        if not curuser.unsolved_problems.filter(id = curprob.id):
                            curuser.unsolved_problems.add(curprob)
                            curuser.save()
                    curprob.TLE += 1
                elif res == 8:
                    if  not curuser.problems.filter(id = curprob.id):
                        if not curuser.unsolved_problems.filter(id = curprob.id):
                            curuser.unsolved_problems.add(curprob)
                            curuser.save()
                    curprob.CE += 1
            else:
                RList.result = 'System Error'
            curprob.save()
            RList.save()
            print curprob
            print RList
            
            return HttpResponseRedirect("/status/")
        else:
            form = SubmitForm()
    return HttpResponseRedirect( "/problem/"+problem_id )