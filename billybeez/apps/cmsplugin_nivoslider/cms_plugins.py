# coding: utf-8

from cms.plugin_base import CMSPluginBase
from .models import SliderPlugin
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool


class CMSSliderPlugin(CMSPluginBase):
    model = SliderPlugin
    name = _('Slider')
    render_template = 'nivo/slider.html'
    text_enabled = False
    admin_preview = False
    fieldsets = (
        (None, {
            'fields': ('title', 'album', ('theme', 'effect',),
                       ('anim_speed', 'pause_time',), ('width', 'height',),),
        }),
        (_('Controls'), {
            'fields': (('manual_advance', 'pause_on_hover',),
                       ('arrows', 'thumbnails',), 'random_start',),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'images': instance.images,
        })
        return context

plugin_pool.register_plugin(CMSSliderPlugin)
