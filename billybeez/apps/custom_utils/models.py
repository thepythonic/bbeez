from django.db import models
from django.utils.translation import ugettext_lazy as _

SPAN = (
		("", _("--select--")),
		("span1", "span1"),
		("span2", "span2"),
		("span3", "span3"),
		("span4", "span4"),
		("span5", "span5"),
		("span6", "span6"),
		("span7", "span7"),
		("span8", "span8"),
		("span9", "span9"),
		("span10", "span10"),
		("span11", "span11"),
		("span12", "span12"),
		)

class VariableWidth(models.Model):
	""" Text plugin Class with a title field """
	span = models.CharField(max_length=50, default='Width', choices=SPAN )
	
	def __unicode__(self):
		return u"%s" % self.span

	class Meta:
		abstract = True