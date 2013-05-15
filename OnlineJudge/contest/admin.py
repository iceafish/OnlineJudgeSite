from django.contrib import admin
from contest.models import Problem,Contest,Contest2Problem

'''
class Contest2ProblemInline(admin.TabularInline):
    model = Contest2Problem
    extra = 1
    
class ContestAdmin(admin.ModelAdmin):
    inlines = (Contest2ProblemInline,)
#class ProblemAdmin(admin.ModelAdmin):
#    inlines = (Contest2ProblemInline,)

admin.site.register(Contest,ContestAdmin)
admin.site.register(Problem)
#admin.site.register(Problem,ProblemAdmin)
'''
