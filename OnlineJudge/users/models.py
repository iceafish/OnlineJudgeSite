from django.db import models
#from django.contrib.auth.models import User

class UserModel(models.Model):
    #user = models.OneToOneField(User)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    accept = models.IntegerField(default=0)
    submit = models.IntegerField(default=0)
    
    '''gender = models.BooleanField(blank = True)'''
    #school = models.CharField(max_length=128, blank=True)
    
    '''
    school can set manytomany type, usr can choose one of these.
    if databases not exist, use can create a new one.
    but now just design a base system.
    '''
    '''info = models.TextField(blank=True)'''

    def __unicode__(self):
        return u"%s" % (unicode(self.username))
