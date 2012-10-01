from titledplugin.models import TitledPlugin
from cms.utils.html import clean_html
from django import forms
from django.forms.models import ModelForm

class TitledPluginForm(ModelForm):
	body = forms.CharField()
	
	class Meta:
		model = TitledPlugin
		exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
		fields = ('title', 'body')