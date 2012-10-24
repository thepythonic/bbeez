from django.conf.urls import patterns, include, url


urlpatterns = patterns('custom_calendar.views',
	(r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
	
	(r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
	(r"^month/(\d+)/(\d+)/$", "month"),

	
	(r"^month$", "month"),

	(r"^(\d+)/$", "main"),
	(r"^$", "main"),
 )
