from django.db import models
from cms.models import CMSPlugin

class WrapperPlugin(CMSPlugin):
    template = models.TextField()
    number = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        """return WrapperPlugin string representation"""
        return u'%d plugins(s)' % self.number