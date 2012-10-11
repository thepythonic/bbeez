from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.utils.translation import ugettext as _

from cms.plugins.text.models import AbstractText

from custom_utils.models import VariableWidth


class TextVariableWidth(AbstractText, VariableWidth):
	
	def __unicode__(self):
		return u"%s" % (truncate_words(strip_tags(self.body), 3)[:30]+"...")