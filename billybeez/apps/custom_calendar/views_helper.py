from models import Entry
import time
import calendar


def get_month_entries(year, month):
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)

	nyear, nmonth, nday = time.localtime()[:3]
	month_days_lst = [[]]
	week = 0

	for day in month_days:
		entries = current = False
		if day:
			entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
			if day == nday and year == nyear and month == nmonth:
				current = True

		month_days_lst[week].append((day, entries, current))
		
		if len(month_days_lst[week]) == 7:
			month_days_lst.append([])
			week += 1

	return month_days_lst
