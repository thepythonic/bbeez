from django.conf.urls import patterns, include, url


urlpatterns = patterns('custom_calendar.views',
	(r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
	
	url(r"^month/(\d+)/(\d+)/$", "month", name="cal_month"),
		
	url(r"^month$", "month"),

	(r"^(\d+)/$", "main"),
	(r"^$", "main"),
 )
