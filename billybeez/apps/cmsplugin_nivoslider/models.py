# coding: utf-8

from django.db.models import BooleanField, PositiveIntegerField, CharField
from cms.models import CMSPlugin
from filer.fields.folder import FilerFolderField
from django.contrib.staticfiles.finders import find as staticfiles_find
from django.utils.translation import ugettext, ugettext_lazy as _
import os


EFFECTS = """
    sliceDown
    sliceDownLeft
    sliceUp
    sliceUpLeft
    sliceUpDown
    sliceUpDownLeft
    fold
    fade
    random
    slideInRight
    slideInLeft
    boxRandom
    boxRain
    boxRainReverse
    boxRainGrow
    boxRainGrowReverse
"""
EFFECT_CHOICES = ((e, e) for e in EFFECTS.split())


def find_themes():
    themedirs = staticfiles_find("nivo/themes/", all=True)
    for dir in themedirs:
        for theme in os.listdir(dir):
            yield theme

THEME_CHOICES = ((t, t) for t in set(find_themes()))


class SliderPlugin(CMSPlugin):
    title = CharField(_('title'), max_length=255, null=True, blank=True)
    album = FilerFolderField(verbose_name=_('album'), 
                        help_text=_("Best image size 600x300"))
    theme = CharField(_('theme'), choices=THEME_CHOICES, max_length=50,
                      default="default")
    effect = CharField(_('effect'), choices=EFFECT_CHOICES, max_length=50,
                       default="random")
    manual_advance = BooleanField(_('manual advance'))
    anim_speed = PositiveIntegerField(_('anim speed'), default=500,
                                      help_text=_("Animation Speed (ms)"))
    pause_time = PositiveIntegerField(_('pause time'), default=3000,
                                      help_text=_("Pause time (ms)"))
    width = PositiveIntegerField(_('width'), null=True, blank=True,
                                 help_text=_("Width of the plugin (px)"))
    height = PositiveIntegerField(_('height'), null=True, blank=True,
                                  help_text=_("Height of the plugin (px)"))
    arrows = BooleanField(_('arrows'), default=True,
                          help_text=_('Arrow buttons for navigation'))
    thumbnails = BooleanField(_('thumbnails'),
                              help_text=_('Thumbnails for navigation [only '
                                          'works with the default theme!]'))
    random_start = BooleanField(_('random start'))
    pause_on_hover = BooleanField(_('pause on mouse hover'), default=True)

    def __unicode__(self):
        if self.title:
            return self.title
        return unicode(self.album)

    @property
    def images(self):
        if not hasattr(self, '__images'):
            files = self.album.files
            self.__images = [f for f in files if f.file_type == 'Image']
            self.__images.sort()
        return self.__images

    @property
    def size(self):
        if self.width and self.height:
            return self.width, self.height

    search_fields = ('title', 'album__title',)
