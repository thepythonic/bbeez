from django import forms
from django.forms.models import ModelForm

from cms.utils.html import clean_html

from cmsplugin_text_variable_width.models import TextVariableWidth

class TextVariableWidthForm(ModelForm):
	""" form model for titled plugin, specific fields order """
	body = forms.CharField()
	
	class Meta:
		model = TextVariableWidth
		exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
		fields = ('span', 'body')