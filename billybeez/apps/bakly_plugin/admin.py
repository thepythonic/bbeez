from bakly_plugin.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3

class PollAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields':['question']}),
		('Date Information', {'fields': ['pub_date']}),
	]
	inlines=[ChoiceInline]
	list_display=('question','pub_date')
	
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)