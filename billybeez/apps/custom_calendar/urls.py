from django.conf.urls import patterns, include, url


urlpatterns = patterns('custom_calendar.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "main"),
   (r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"^month$", "month"),
   (r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
 )