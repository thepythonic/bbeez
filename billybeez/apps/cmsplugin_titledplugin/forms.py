from django import forms
from django.forms.models import ModelForm

from cms.utils.html import clean_html

from cmsplugin_titledplugin.models import TitledPlugin

class TitledPluginForm(ModelForm):
	""" form model for titled plugin, specific fields order """
	body = forms.CharField()
	
	class Meta:
		model = TitledPlugin
		exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
		fields = ('span', 'title', 'body')