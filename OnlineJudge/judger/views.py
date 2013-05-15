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
from problems.models import Problem
from users.models import *
import threading
lock = threading.Lock()
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
    s = socket(AF_INET, SOCK_STREAM)
    
    if request.method == 'POST':
        
        form = SubmitForm(request.POST,request.FILES)
        if form.is_valid():
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
            
            try:
                s.connect((host, port))
            except error:
                print "Error connecting server %s." % host
                return
            
            s.sendall('%d' % RList.id)
            ReturnRes = s.recv(2048)
            s.close()
            
            lock.release()
            
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