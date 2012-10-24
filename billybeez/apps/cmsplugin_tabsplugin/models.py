"""tabs CMS plugins models"""

from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from inline_ordering.models import Orderable
from cmsplugin_tabsplugin import utils

TYPES = (('tabs', _('Horizontal Tab')),
        ('accordion', _('Accordion')),)

TEMPLATE_CHOICES = utils.autodiscover_templates()

class TabPlugin(CMSPlugin):
    """Tab Django-CMS plugin model"""

    template_filename = models.CharField(_("Template filename used for this tab"), max_length=255, 
        help_text=_("If changed, use customize template"), choices=TEMPLATE_CHOICES)

    type = models.CharField(_('Tab type'), max_length=24, choices=TYPES, help_text=_("Graphical representation"),)

    @property
    def template(self):
        """return path to template filename"""
        return '%s' % (self.template_filename)

    def __unicode__(self):
        """return TabPlugin string representation"""
        return u'%d tab(s)' % self.tab_set.count()

class Tab(Orderable):
    """Tab Content"""
    group = models.ForeignKey(TabPlugin)
    title = models.CharField(_("Tab title"), max_length=255, help_text=_("Title"),)
    body = models.TextField(_("Tab content"), help_text=_("HTML Content"), )

    def __unicode__(self):
        return self.title