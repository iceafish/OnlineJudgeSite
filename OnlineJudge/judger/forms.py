from django import forms

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
            destination = open('./judger/tmp/'+file.name, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()