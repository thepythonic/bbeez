from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from custom_calendar.models import Entry
import time
import calendar
from datetime import date, datetime

from views import mnames
from views_helper import get_month_entries

class CustomCalendarPlugin(CMSPluginBase):
    model = Entry
    name = _("Custom Calendar")
    render_template = "custom_calendar/plugin_main.html"


    def render(self, context, instance, placeholder):
    	year, month, day = time.localtime()[:3]
    	month_days, entries = get_month_entries(year, month)
    	context.update({
			'year': year,
			'month':month,
			'month_days': month_days,
    		})
        return context

plugin_pool.register_plugin(CustomCalendarPlugin)