from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cmsplugin_billybeezgames.models import BillybeezGame

class BillybeezGamePlugin(CMSPluginBase):
    model = BillybeezGame
    name = _("Billy Beez Game Plugin")
    render_template = "billybeezgames.html"

    def render(self, context, instance, placeholder):
    	print instance.gallery_plugin
    	print instance.titiled_plugin
    	context.update({
			'titled': instance.titiled_plugin,
			'gallery': instance.gallery_plugin,
			'placeholder': placeholder,
			'object': instance
		})
        return context

plugin_pool.register_plugin(BillybeezGamePlugin)