from django.db import models
from cms.models import CMSPlugin

class WrapperPlugin(CMSPlugin):
    template = models.TextField()
    number = models.PositiveIntegerField(default=0)
