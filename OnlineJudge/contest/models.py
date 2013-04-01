from django.db import models
from users.models import UserModel
# Create your models here.
class Problem(models.Model):
    title = models.CharField( max_length = 50 )
    TimeLimit = models.IntegerField( default = 1 )
    MemoryLimit = models.IntegerField( default = 64 )
    UseAble = models.BooleanField()
    description = models.TextField( blank = True )
    input = models.TextField( blank = True )
    output = models.TextField( blank = True )
    SampleInput = models.TextField( blank = True )
    SampleOutput = models.TextField( blank = True )
    hint = models.TextField( blank = True )
    source = models.CharField( max_length = 256, blank = True )
    accept = models.IntegerField( default = 0, editable = False )
    submit = models.IntegerField( default = 0, editable = False )
    WA = models.IntegerField( default = 0, editable = False )
    TLE = models.IntegerField( default = 0, editable = False )
    MLE = models.IntegerField( default = 0, editable = False )
    PE = models.IntegerField( default = 0, editable = False )
    Ratio = models.FloatField( default = 0, editable = False )
    in_file = models.FileField(upload_to="problemset/contestfile",blank=True)
    out_file = models.FileField(upload_to="problemset/contestfile",blank=True)
    
    contest_id = models.IntegerField(default = 0,editable = False)
    problem_id = models.IntegerField(default = 0,editable = False)
    
    def __unicode__( self ):
        return u'Problem %s' % ( self.id )
class Contest(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20,choices=( ('pending','pending'),('registing','registing'),('accept','accept'))  )
    problemset = models.ManyToManyField(Problem , through = 'Contest2Problem')
    users = models.ManyToManyField(UserModel,blank = True)
    
    def __unicode__( self ):
        return u'Contest %s' % ( self.id )
class Contest2Problem(models.Model):
    problem = models.ForeignKey(Problem)
    contest = models.ForeignKey(Contest)
    problemID = models.IntegerField()
    
    