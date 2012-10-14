from django.utils.translation import ugettext as _

from cms.plugins.text.utils import plugin_tags_to_user_html
from cms.plugins.text.cms_plugins import TextPlugin

from cms.plugin_pool import plugin_pool

from cmsplugin_text_variable_width.models import TextVariableWidth
from cmsplugin_text_variable_width.forms import TextVariableWidthForm

class CMSTextVariableWidth(TextPlugin):
	model = TextVariableWidth
	name = _("Text Variable Width")
	form = TextVariableWidthForm
	
	render_template = "cmsplugin_text_variable_width/text.html"
	change_form_template = "cmsplugin_text_variable_width/text_change_form.html"	

	def render(self, context, instance, placeholder):
		context.update({
			'span': instance.span,
			'body': plugin_tags_to_user_html(instance.body, context, placeholder), 
			'placeholder': placeholder,
			'object': instance
		})
		return context

plugin_pool.register_plugin(CMSTextVariableWidth)