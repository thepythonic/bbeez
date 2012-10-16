from cms.models.pluginmodel import CMSPlugin
from cmsplugin_gallery.models import GalleryPlugin
from cmsplugin_titledplugin.models import TitledPlugin
from django.db import models

class BillybeezGame(CMSPlugin):
   gallery_plugin = models.ForeignKey(GalleryPlugin)
   #TODO rename the following field
   titiled_plugin = models.ForeignKey(TitledPlugin)

   def __unicode__(self):
   	return u'billy beez games'
