from django.conf import settings
from cms.utils import cms_static_url

# Uses TinyMCE as editor (no inline plugins). Requires django-tinymce app. 
# If false, then WYMEditor is used. 
USE_TINYMCE = False		# getattr(settings, 'CMS_USE_TINYMCE', "tinymce" in settings.INSTALLED_APPS)

WYM_TOOLS = []			# WYM_TOOLS = getattr(settings, "WYM_TOOLS", WYM_TOOLS)

WYM_CONTAINERS = []		# WYM_CONTAINERS = getattr(settings, "WYM_CONTAINERS", WYM_CONTAINERS)

WYM_CLASSES = []		# WYM_CLASSES = getattr(settings, "WYM_CLASSES", WYM_CLASSES)

WYM_STYLES = []			# WYM_STYLES = getattr(settings, "WYM_STYLES", WYM_STYLES)


#Advantageously replaces WYM_CLASSES and WYM_STYLES
##Prepare url for wymeditor.css
WYM_STYLESHEET = getattr(settings, "WYM_STYLESHEET",  '"%s"' % cms_static_url('css/wymeditor.css'))