import os
import sys

sys.path.append('/srv/bbeez/venv/lib/python2.7/site-packages/')
sys.path.append('/srv/bbeez/venv/bbeez/billybeez/')
sys.path.append('/srv/bbeez/venv/bbeez/billybeez/apps/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'billybeez.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
