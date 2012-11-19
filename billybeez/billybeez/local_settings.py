import os
import settings
CMS_SEO_FIELDS = True


if settings.DEBUG:
	INTERNAL_IPS = ('127.0.0.1',)
	settings.MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
	settings.INSTALLED_APPS += ("debug_toolbar",)
	DEBUG_TOOLBAR_PANELS = (
	    'debug_toolbar.panels.version.VersionDebugPanel',
	    'debug_toolbar.panels.timer.TimerDebugPanel',
	    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
	    'debug_toolbar.panels.headers.HeaderDebugPanel',
	    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
	    'debug_toolbar.panels.template.TemplateDebugPanel',
	    'debug_toolbar.panels.sql.SQLDebugPanel',
	    'debug_toolbar.panels.signals.SignalDebugPanel',
	    'debug_toolbar.panels.logger.LoggingPanel',
	)
	DEBUG_TOOLBAR_CONFIG = {
	    'INTERCEPT_REDIRECTS': False,
	    'HIDE_DJANGO_SQL': False,
	    'TAG': 'div',
	    'ENABLE_STACKTRACES' : True,
	    'SHOW_TEMPLATE_CONTEXT': True,
	    'SHOW_TOOLBAR_CALLBACK': lambda request: settings.DEBUG,
	}
	# sqlite dev database data
	settings.DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	       'NAME': os.path.join(settings.PROJECT_PATH, 'dev.db'),                      # Or path to database file if using sqlite3.
	        'USER': '',                      # Not used with sqlite3.
	        'PASSWORD': '',                  # Not used with sqlite3.
	        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	    }
	}
