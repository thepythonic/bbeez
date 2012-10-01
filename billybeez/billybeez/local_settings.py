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