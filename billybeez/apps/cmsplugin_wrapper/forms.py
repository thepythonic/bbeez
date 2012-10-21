from django.conf import settings
from django import forms
from django.forms.models import ModelForm
from cmsplugin_wrapper.models import WrapperPlugin

class WrapperPluginForm(ModelForm):
	""" form model for wrapper plugin, specific fields widgets and order """
	template = forms.ChoiceField(choices=settings.WRAPPER_PLUGIN_TEMPLATES)

	class Meta:
		model = WrapperPlugin
		exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
		fields = ('number', 'template')