from cms.models.pluginmodel import CMSPlugin
from cmsplugin_gallery.models import GalleryPlugin
from cmsplugin_titledplugin.models import TitledPlugin
from cmsplugin_filer_image.models import FilerImage
from filer.fields.image import FilerImageField
from django.db import models

class BillybeezGame(CMSPlugin):
   gallery_plugin = models.ForeignKey(GalleryPlugin)
   #TODO rename the following field
   titiled_plugin = models.ForeignKey(TitledPlugin)
   image_plugin =FilerImageField(null=True, blank=True)

   def __unicode__(self):
   	return u'billy beez games'
