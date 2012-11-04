from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CustomCalendarApp(CMSApp):
    name = _("Custom Calendar App") # give your app a name, this is required
    urls = ["custom_calendar.urls"] # link your app to url configuration(s)

apphook_pool.register(CustomCalendarApp) # register your app