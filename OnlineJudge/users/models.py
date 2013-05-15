from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem
from contest.models import Contest

class UserModel(models.Model):
    user = models.OneToOneField(User)
    score = models.IntegerField(default=0,editable = False)
    accept = models.IntegerField(default=0,editable = False)
    submit = models.IntegerField(default=0,editable = False)
    solved = models.IntegerField(default=0,editable=False)
    problem_submit = models.IntegerField(default=0,editable=False)
    
    problems = models.ManyToManyField(Problem)#show User has solved problems(Exercise)
    contests = models.ManyToManyField(Contest)#show User has registered Contest.
    
    '''gender = models.BooleanField(blank = True)'''
    #school = models.CharField(max_length=128, blank=True)
    '''
    school can set manytomany type, usr can choose one of these.
    if databases not exist, use can create a new one.
    but now just design a base system.
    '''
    '''info = models.TextField(blank=True)'''
'''
    def __unicode__(self):
        return u"%s" % (unicode(self.username))
'''
