from django.shortcuts import render_to_response,RequestContext
from django.http import Http404,HttpResponse,HttpResponseRedirect
from JRequest.models import RequestList
import threading
from JRequest.forms import SubmitForm
from django.http import HttpResponseRedirect
from datetime import datetime
from users.models import *
from problems.models import Problem

lock = threading.Lock()

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def submit_code(request, problem_id=0):
    
    if problem_id == 0:
        raise Http404()
    
    if request.method=='POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            lock.acquire()
            file  = request.FILES['file']
            file_name = form.save(file)
    
            Rlist = RequestList(user = request.user.username,
                                problemID = problem_id,
                                result = 'Waiting',
                                timeUsed = 0,
                                languageTypeID = request.POST['Language'],
                                submitTime = datetime.now(),
                                codeFile = "./JudgeSite/RequestCode/" + file_name
                                )
            Rlist.save()
            curProblem = Problem.objects.get( id = problem_id )
            curUser = User.objects.get( username = Rlist.user ).usermodel
            curProblem.submit += 1
            curUser.submit += 1
            curProblem.save()
            curUser.save()
            lock.release()
        else:
            return HttpResponseRedirect( "/problem/"+problem_id )
    else:
        return HttpResponseRedirect( "/problem/"+problem_id )
        
    return HttpResponseRedirect( "/status/" )