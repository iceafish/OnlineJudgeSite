from django.contrib import admin
from problems.models import Problem,DataFile

class problemShowStatus( admin.ModelAdmin ):
    list_display = ( 'id', 'title' )
    search_fields = ( 'id', 'title' )
    ordering = ('id',)
admin.site.register( Problem, problemShowStatus )
admin.site.register( DataFile )
#admin.site.register( TotalInfo )