from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
)

handler404 = 'billybeez.views.billybeez_404_view'
handler500 = 'billybeez.views.billybeez_500_view'

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if settings.DEBUG:
    urlpatterns = patterns('',
    	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
   		url(r'', include('django.contrib.staticfiles.urls')),
	) + urlpatterns