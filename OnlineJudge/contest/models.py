from django.db import models

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
    contest_id = models.IntegerField(default = 0)

class Contest(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    problemset = models.ManyToManyField(Problem,blank = True)