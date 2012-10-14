from django.conf import settings
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from cms.plugins.text.utils import plugin_tags_to_user_html

from cmsplugin_titledplugin.models import TitledPlugin
from cmsplugin_titledplugin.forms import TitledPluginForm
from cmsplugin_titledplugin.settings import USE_TINYMCE


class TitledPlugin(CMSPluginBase):
	model = TitledPlugin
	name = _("Titled Plugin")
	form = TitledPluginForm
	render_template = "cmsplugin_titledplugin/titledplugin.html"
	change_form_template = "cmsplugin_titledplugin/titledplugin_change_form.html"	

	def get_editor_widget(self, request, plugins):
		""" Returns the Django form Widget to be used for the titled plugin """
		if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
			from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
			return TinyMCEEditor(installed_plugins=plugins)
		else:
			return WYMEditor(installed_plugins=plugins)

	def get_form_class(self, request, plugins):
		""" Returns a subclass of Form to be used by this plugin """
		# We avoid mutating the Form declared above by subclassing
		class TextPluginForm(self.form):
			pass
		widget = self.get_editor_widget(request, plugins)
		TextPluginForm.declared_fields["body"] = CharField(widget=widget, required=False)
		return TextPluginForm
		
	def get_form(self, request, obj=None, **kwargs):
		plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)
		form = self.get_form_class(request, plugins)
		kwargs['form'] = form # override standard form
		return super(TitledPlugin, self).get_form(request, obj, **kwargs)

	def render(self, context, instance, placeholder):
		context.update({
			'span': instance.span,
			'title': instance.title,
			'font': instance.font,
			'body': plugin_tags_to_user_html(instance.body, context, placeholder), 
			'placeholder': placeholder,
			'object': instance
		})
		return context
	
	def save_model(self, request, obj, form, change):
		obj.clean_plugins()
		super(TitledPlugin, self).save_model(request, obj, form, change)

plugin_pool.register_plugin(TitledPlugin)