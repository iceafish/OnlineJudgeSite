from django.db import models
from users.models import UserModel
# Create your models here.

class RequestList( models.Model ):
    #Run ID    User    Problem    Result      Time    Language    Submit Time
    user = models.CharField(max_length=50)
    problemID = models.IntegerField()
    result = models.CharField(max_length=50)
    timeUsed = models.FloatField(blank=True)
    languageTypeID = models.IntegerField()
    submitTime = models.DateTimeField()
    codeFile = models.CharField(max_length=256)