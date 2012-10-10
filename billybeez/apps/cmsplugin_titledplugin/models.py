from django.db import models
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.html import clean_html
from cms.plugins.text.utils import (plugin_admin_html_to_tags, plugin_tags_to_admin_html, plugin_tags_to_id_list, replace_plugin_tags)
from cms.plugins.text.models import AbstractText

from custom_utils.models import VariableWidth

_old_tree_cache = {}

class TitledPlugin(AbstractText, VariableWidth):
	""" Text plugin Class with a title field """
	title = models.CharField(max_length=50, default='Title')
	
	def __unicode__(self):
		return u"%s" % (truncate_words(strip_tags(self.title), 3)[:30]+"...")
