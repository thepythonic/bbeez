
import datetime

# date range generator
def daterange(start_date, end_date):
	end_date += datetime.timedelta(days=1)
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)
