from django.db import models
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.plugins.text.models import AbstractText

from custom_utils.models import VariableWidth

_old_tree_cache = {}

FONT = (
		("", _("--select--")),
		("h1", "Main Site Title"),
		("h2", "Secondary Site Title"),
		)

class TitledPlugin(AbstractText, VariableWidth):
	""" Text plugin Class with a title field plus body and span"""
	title = models.CharField(max_length=50, default='Title')
	font = models.CharField(max_length=50, default='h2', choices=FONT)
	
	def __unicode__(self):
		return u"%s" % (truncate_words(strip_tags(self.title), 3)[:30]+"...")
