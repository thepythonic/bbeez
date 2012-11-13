import os
import sys

sys.path.append('/home/yomna/Envs/billydemo/lib/python2.7/site-packages')
sys.path.append('/home/yomna/projects/billydemo/bbeez/billybeez/')
sys.path.append('/home/yomna/projects/billydemo/bbeez/billybeez/apps/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'billybeez.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
