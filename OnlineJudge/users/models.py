from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    GENDER_TYPE = (
        ('M','Male'),
        ('F','Female'),
    )

    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    follow = models.ManyToManyField(User, related_name='follow', blank=True)
    photo = models.ImageField(upload_to="photo", blank=True)
    school = models.CharField(max_length=128, blank=True)
    area = models.CharField(max_length=512, blank=True)
    info = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (
            unicode(self.user.username),)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
