# Django settings for billybeez project.

import os

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
   ('Test', 'Billybeeztest@scitecs.com'),
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'scitecs123456'
# TODO YF change email settings
EMAIL_HOST_USER = 'Billybeeztest@scitecs.com'
EMAIL_SUBJECT_PREFIX = 'billybeez - '
EMAIL_USE_TLS = True

CONTACT_US_SUBJECT_CHOICHES = (
    ('-Choose-', '-Choose-'),
    ('Question', 'Question'),
    ('Business proposal', 'Business proposal'),
    ('Advertising', 'Advertising'),
    ('Complaint', 'Complaint'),
)

CONTACT_US_SUBJECT_PREFIX = '[Billy Beez Contact Us Form]'

CMS_PLUGIN_PROCESSORS = (
    'cmsplugin_wrapper.plugin_processors.wrap_plugin',
)

WRAPPER_PLUGIN_TEMPLATES = (
    ('default.html', 'default'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'billybeez_dev',      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
]

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0ots!#jf=q22wqv5y04_!+)ovk!q12n18%tg_$w%-ub(4hp7_='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    #'multihost.middleware.MultiHostMiddleware',

    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)
#MULTIHOST_AUTO_WWW = False
MULTIHOST_REDIRECT_URL = '/'
LOCALE_PATHS = (
     os.path.join(PROJECT_PATH, 'locale'),
)

ROOT_URLCONF = 'billybeez.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'billybeez.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'cmsplugin_wrapper.context_processors.cmsplugin_wrapper',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'django.contrib.sitemaps',
    # our themes
    'bstheme',
    #'bluetheme',

    'cms', 
    'mptt', 
    'menus', 
    'south',
    'sekizai', 

    # 'cms.plugins.file',
    'cms.plugins.flash',                # FlashPlugin
    'cms.plugins.googlemap',            # GoogleMapPlugin
    'cms.plugins.link',                 # LinkPlugin
    # 'cms.plugins.picture',
    'cms.plugins.snippet',              # SnippetPlugin
    # 'cms.plugins.teaser',
    'cms.plugins.text',                 # TextPlugin
    # 'cms.plugins.video',
    'cms.plugins.twitter',              # TwitterSearchPlugin
    
    'easy_thumbnails',

    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'rosetta',

    # Our Custom plugins
    'cmsplugin_text_variable_width',    # CMSTextVariableWidth
    'cmsplugin_bootstrap_carousel',     # CarouselPlugin
    'cmsplugin_titledplugin',           # TitledPlugin
    'cmsplugin_gallery',                # CMSGalleryPlugin
    #'cmsplugin_billybeezgames',         # BillybeezGamePlugin
    'cmsplugin_contact',                # ContactPlugin
    'cmsplugin_wrapper',                # CMSWrapperPlugin
    'cmsplugin_nivoslider',             # CMSSliderPlugin
    'custom_calendar',                  # CustomCalendarPlugin
)


CMS_TEMPLATES = (
    ('main.html', 'Home'),
    ('plan.html', 'Plan your visit'),
    ('play.html', 'Playgrounds'),
    ('tab.html', 'Tab Template'),
    ('contact.html', 'Contact Us'),
    ('general.html', 'General Template'),
)

#http://django-filer.readthedocs.org/en/latest/installation.html#subject-location-aware-cropping
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'cmsplugin_nivoslider.thumbnail_processors.pad_image',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CMS_SEO_FIELDS = True

CMS_PLACEHOLDER_CONF = {
    'content_top': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'CarouselPlugin', 'CMSWrapperPlugin'],
        'name':gettext("Homepage Slider"),
    },
    'content_center': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'TitledPlugin', 'CMSGalleryPlugin', 'Custom_Calendar'],
        'name':gettext("Welcome Box"),
    },
    'block_left': {
        'plugins': ['CMSTextVariableWidth', 'TitledPlugin'],
        'name':gettext("Left Block"),
    },
    'block_middle': {
        'plugins': ['CMSTextVariableWidth', 'TitledPlugin'],
        'name':gettext("Middle Block"),
    },
    'block_right': {
        'plugins': ['CMSTextVariableWidth', 'TitledPlugin'],
        'name':gettext("Right Block"),
    },
    'banner': {
        'plugins': ['FilerImagePlugin'],
        'name':gettext("Banner"),
    },
    'text_box': {
        'plugins': ['CMSTextVariableWidth', 'TitledPlugin'],
        'name':gettext("Textbox"),
    },
    'content_tab': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'TitledPlugin', 'ContactPlugin', 'CMSWrapperPlugin'],
        'name':gettext("Main Content"),
    },
    'content_playground': {
        'plugins': ['CMSTextVariableWidth', 'CMSGalleryPlugin', 'FilerImagePlugin', 'TitledPlugin', 'CMSWrapperPlugin'],
        'name':gettext("Playground Games Block"),
    },
    'google_map': {
        'plugins': ['GoogleMapPlugin'],
        'name':gettext("Site Map Block"),
    },
    'site_info': {
        'plugins': ['CMSTextVariableWidth'],
        'name':gettext("Site Info Block"),
    },
    'contact_form': {
        'plugins': ['ContactPlugin'],
        'name':gettext("Contact Us Form Block"),
    },
}

try:
    from local_settings import *
except ImportError:
    print "Exception"
