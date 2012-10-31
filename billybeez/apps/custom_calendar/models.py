from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from customfields import  ColorField

from cms.models import CMSPlugin

from custom_utils.date_utils import daterange

class Entry(CMSPlugin):
	
	title        	   = models.CharField(max_length=40)
	snippet       	   = models.CharField(max_length=150 , blank = False)
	body         	   = models.TextField(max_length=10000 , blank = False)
	created      	   = models.DateTimeField(auto_now_add=True)
	start_date         = models.DateField(blank=False)
	end_date           = models.DateField(blank=False)
	creator            = models.ForeignKey(User , blank=True , null=True)
	remind             = models.BooleanField(default=False)
	cal_colour         = ColorField(blank=False)


	def __unicode__(self):
		if self.title:
			return unicode(self.creator) + u" - " + self.title
		else:
			return unicode(self.creator) + u" - " + self.snippet[:40]

	def short(self):
		if self.snippet:
			return "<i>%s</i> - %s" % (self.title,self.snippet)
		else:
			return self.title
	short.allow_tags = True

	def duration(self):
		return daterange(self.start_date, self.end_date)


	class Meta:
		verbose_name_plural = "entries"

###Admin

class EntryAdmin(admin.ModelAdmin):
	list_display = ["creator" , "start_date" , "end_date", "title" , "snippet","cal_colour"]
	list_filter  = ["creator"]

	

#admin.site.register(Entry, EntryAdmin)

