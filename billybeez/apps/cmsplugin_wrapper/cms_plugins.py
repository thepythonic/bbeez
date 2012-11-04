from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_wrapper.models import WrapperPlugin
from cmsplugin_wrapper.forms import WrapperPluginForm

class CMSWrapperPlugin(CMSPluginBase):
	model = WrapperPlugin
	name = _("Wrapper Plugin")
	form = WrapperPluginForm
	admin_preview = False
	render_template = 'cmsplugin_wrapper/default.html'

	def render(self, context, instance, placeholder):
		return context
            
plugin_pool.register_plugin(CMSWrapperPlugin)
