from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import UserModel

class UserModelInline(admin.StackedInline):
    model = UserModel
    can_delete = False
    verbose_name_plural = 'usermodels'

class UserAdmin(UserAdmin):
    inlines = (UserModelInline,)
    
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

