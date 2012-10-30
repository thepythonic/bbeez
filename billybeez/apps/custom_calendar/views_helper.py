from django.db.models import Q
from models import Entry
import time
import datetime
import calendar


#def get_month_entries(year, month):
#	cal = calendar.Calendar()
#	month_days = cal.itermonthdays(year, month)
#
#	nyear, nmonth, nday = time.localtime()[:3]
#	month_days_lst = [[]]
#	week = 0
#
#	for day in month_days:
#		entries = current = False
#		if day:
#			entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
#			if day == nday and year == nyear and month == nmonth:
#				current = True
#
#		month_days_lst[week].append((day, entries, current))
#		
#		if len(month_days_lst[week]) == 7:
#			month_days_lst.append([])
#			week += 1
#
#	return month_days_lst


def get_month_entries(year, month):
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)

	nyear, nmonth, nday = time.localtime()[:3]
	month_days_lst = [[]]
	
	
	week = 0

	query = Q(start_date__year=year, start_date__month=month) |  Q(end_date__year=year, end_date__month=month) | \
			(Q(start_date__lte=datetime.date(year, month, 1)) & Q(end_date__gte=datetime.date(year,month, 1))) 

	all_entries = Entry.objects.filter(query).order_by('start_date')

	for day in month_days:
		total = []
		event_period = []
		entries = current = start = False
		if day:
			entries  = Entry.objects.filter(start_date__lte=datetime.date(year, month, day), end_date__gte=datetime.date( year, month, day))
			for entry in entries:
				rng  = entry.duration()
				
				for date in rng:
					event_period.append((date,entry))
				
			if day == nday and year == nyear and month == nmonth:
				current = True

		

		for days, ent in event_period:
			if(days.day == day and days.month == month and days.year == year and ent ):
				total.append(ent)
			if(day == ent.start_date):
				start = True

		month_days_lst[week].append((day, total, current, start))

		if len(month_days_lst[week]) == 7:
			month_days_lst.append([])
			week += 1

	return month_days_lst, all_entries


def get_correct_year_month_or_redirect(year, month):
	year, month, redirect = int(year), int(month), False

	if month > 12:
		year +=1
		month = month % 12
		redirect = True
	elif month < 1:
		year -= 1
		month = month % 12
		if month == 0:
			month = 12 

		redirect = True


	return year, month, redirect