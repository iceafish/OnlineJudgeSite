from django.db import models

# Create your models here.
class TotalInfo( models.Model ):
    accept = models.IntegerField()
    submit = models.IntegerField()
    WA = models.IntegerField()
    TLE = models.IntegerField()
    MLE = models.IntegerField()
    PE = models.IntegerField()
    Ratio = models.FloatField()


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
    
    
    # Total Submit imformation
    #ContestInfo = models.ForeignKey( TotalInfo )
    ExerciseInfo = models.ForeignKey( TotalInfo, editable = False )
    
    # level
    #level = models.IntegerField()
    
    def __unicode__( self ):
        return u'%s | %s' % ( self.id, self.title )