from django.db import models
from django.contrib.admin import ModelAdmin

def getFilePath(instance, filename):
    
    return "DataSet/ProblemData/"

class DataFile(models.Model):
    name = models.CharField(max_length=10, unique=True)
    in_file = models.FileField(upload_to="problemset/datafile")
    out_file = models.FileField(upload_to="problemset/datafile")
    #author = models.ForeignKey(User)
    def __unicode__(self):
        return u"%s" % ( self.name )

class Problem( models.Model ):
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
    
    TestFile = models.ManyToManyField( DataFile, blank = True )

    accept = models.IntegerField( default = 0, editable = False )
    submit = models.IntegerField( default = 0, editable = False )
    WA = models.IntegerField( default = 0, editable = False )
    TLE = models.IntegerField( default = 0, editable = False )
    MLE = models.IntegerField( default = 0, editable = False )
    PE = models.IntegerField( default = 0, editable = False )
    CE = models.IntegerField(default = 0, editable = False )
    Ratio = models.FloatField( default = 0, editable = False )
    
    # Total Submit imformation
    #ContestInfo = models.ForeignKey( TotalInfo )
    #ExerciseInfo = models.OneToOneField( TotalInfo )
    #ExerciseInfo = models.ForeignKey( TotalInfo, editable = False, primary_key=True )
    # level    
    #level = models.IntegerField()
    
    def __unicode__( self ):
        return u'%s' % ( self.id )