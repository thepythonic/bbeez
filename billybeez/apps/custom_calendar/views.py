import time
import calendar
from datetime import date, datetime, timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory
from django.template import RequestContext

from custom_calendar.models import *
from views_helper import get_month_entries


mnames_string = "January February March April May June July August September October November December"
mnames = mnames_string.split()



#@login_required

def reminders(request):
    """Return the list of reminders for today and tomorrow."""
    year, month, day = time.localtime()[:3]
    reminders = Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day, remind=True)
    tomorrow = datetime.now() + timedelta(days=1)
    year, month, day = tomorrow.timetuple()[:3]
    return list(reminders) + list(Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day,  remind=True))

#@login_required
def main(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Entry.objects.filter(date__year=y, date__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
        lst.append((y, mlst))

    return render_to_response("custom_calendar/main.html", dict(years=lst, year=year,reminders=reminders(request)), context_instance=RequestContext(request))

#@login_required
def month(request, year, month, change=None):
    """Listing of days in `month`."""
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    lst = get_month_entries(year, month)

    return render_to_response("custom_calendar/month.html", dict(year=year, month=month,
                        month_days=lst, mname=mnames[month-1], reminders=reminders(request)), context_instance=RequestContext(request))

#@login_required
def day(request, year, month, day):
    """Entries for the day."""
        # display  existing enties
    entries = Entry.objects.filter(date__year=year,date__month=month, date__day=day)
    return render_to_response("custom_calendar/day.html", dict(entries=entries, year=year,
            month=month, day=day, reminders=reminders(request)), context_instance=RequestContext(request))


def plugin_month(request, year, month, change=None):
    """Listing of days in `month`."""
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta


        year, month = (now+mod).timetuple()[:2]

    # init variables
    lst = get_month_entries(year, month)

    return render_to_response("custom_calendar/plugin_main.html", dict(year=year, month=month,
                        month_days=lst, mname=mnames[month-1], reminders=reminders(request)), context_instance=RequestContext(request))
