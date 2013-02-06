from django.db import models

# Create your models here.
'''
class TotalInfo( models.Model ):
    id = models.AutoField( 'ID', primary_key=True )
    accept = models.IntegerField( default = 0 )
    submit = models.IntegerField( default = 0 )
    WA = models.IntegerField( default = 0 )
    TLE = models.IntegerField( default = 0 )
    MLE = models.IntegerField( default = 0 )
    PE = models.IntegerField( default = 0 )
    Ratio = models.FloatField( default = 0 )
'''
class DataFile(models.Model):
    name = models.CharField(max_length=10, unique=True)
    in_file = models.FileField(upload_to="problemset/datafile")
    out_file = models.FileField(upload_to="problemset/datafile")
    #author = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s" % ( unicode(self.name) )

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
    
    #te = models.Manager()
    TestFile = models.ManyToManyField( DataFile, blank = True )

    accept = models.IntegerField( default = 0, editable = False )
    submit = models.IntegerField( default = 0, editable = False )
    WA = models.IntegerField( default = 0, editable = False )
    TLE = models.IntegerField( default = 0, editable = False )
    MLE = models.IntegerField( default = 0, editable = False )
    PE = models.IntegerField( default = 0, editable = False )
    Ratio = models.FloatField( default = 0, editable = False )
    
    # Total Submit imformation
    #ContestInfo = models.ForeignKey( TotalInfo )
    #ExerciseInfo = models.OneToOneField( TotalInfo )
    #ExerciseInfo = models.ForeignKey( TotalInfo, editable = False, primary_key=True )
    # level    
    #level = models.IntegerField()
    
    def __unicode__( self ):
        return u'%s' % ( self.title )