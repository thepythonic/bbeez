"""cmsplugin_tabsplugin.cms_plugins Django-CMS integration"""

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_tabsplugin.models import TabPlugin
from cmsplugin_tabsplugin.admin import TabInline

class CMSTabPlugin(CMSPluginBase):
    """Link between Django-CMS and Tabs"""
    model = TabPlugin
    name = _("Tabs")
    inlines = [TabInline,]

    def render(self, context, instance, placeholder):
        """render template"""
        context.update({
            'group': instance,
            'tabs': instance.tab_set.all()
        })
        self.render_template = instance.template
        return context

plugin_pool.register_plugin(CMSTabPlugin)