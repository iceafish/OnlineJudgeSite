from django.shortcuts import render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def submit_code( request, problem_id = 0 ):
    '''
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save() #@UnusedVariable
            return HttpResponseRedirect('/accounts/login')
    else:
        form = RegisterForm()
    return render_to_response('user/signup.html',
        {'form':form,},
        context_instance=RequestContext(request))
    '''
    print request
    '''
    if 'sourceFile' in request.POST:
        print 'df'
    '''
    return HttpResponseRedirect("/status/")