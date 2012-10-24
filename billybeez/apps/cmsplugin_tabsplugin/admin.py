"""cmsplugin_tabsplugin.admin module"""

from cms.plugin_pool import plugin_pool
#from django.conf import settings
from inline_ordering.admin import OrderableStackedInline
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor

from cmsplugin_tabsplugin.models import Tab

class WYMEditorFull(WYMEditor):
    """WYMEditor class with all text plugins enabled"""
    def __init__(self, attrs=None):
        WYMEditor.__init__(self, attrs)
        self.installed_plugins = plugin_pool.get_text_enabled_plugins(None, None)

class TabInline(OrderableStackedInline):
    """Tab admin integration"""
    model = Tab
    extra = 1       #  number of extra empty tabs to show

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'body':
            kwargs.pop('request', None)
            kwargs['widget'] = WYMEditorFull
            return db_field.formfield(**kwargs)
        return OrderableStackedInline.formfield_for_dbfield(self, db_field, **kwargs)
