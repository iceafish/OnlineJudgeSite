from django import forms
from judger.models import RequestList
import random
class SubmitForm( forms.Form ):
    Language = forms.ChoiceField(
                               widget   = forms.Select(), 
                               choices  = (
                                           ('1', 'GNU C',),
                                           ('2', 'GNU C++ 4.7',), 
                                           ('3', 'Microsoft Visual C++ 2010',), 
                                           ('4', 'Java',)
                                          ), 
                               initial='1'
                              )
    file = forms.FileField()
    def save( self, file ):
        if file:
            try:
                id = RequestList.objects.order_by('-id')[0]
                id = id.id
            except:
                id=0
            id = int(id)+1
            #randnum=str(random.randint(0,999999))
            #file_name=str(id)+"_"+randnum+".cpp"
            file_name = str(id)+".cpp"
            #destination = open('./judger/tmp/'+file.name, 'wb+')
            destination = open('./judger/user_code/'+file_name, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return file_name