import glob
import os

from django.conf import settings

TEMPLATES = tuple()

def autodiscover_templates():
    """ Autodiscovers cmsplugin_tabs templates the way
    'django.template.loaders.filesystem.Loader' and
    'django.template.loaders.app_directories.Loader' work."""
    def sorted_templates(templates):
        """ Sorts templates """
        TEMPLATES = sorted(templates, key=lambda template: template[1])
        return TEMPLATES

    # obviously, cache for better performance
    if TEMPLATES:
        return TEMPLATES

    #override templates from settings
    override_dir = getattr(settings, 'CMSPLUGIN_TABS_TEMPLATES', None)
    if override_dir:
        return sorted_templates(override_dir)

    templates = []
#    templates = [('cms/plugins/tabs/header.html', 'header.html'),]

    dirs_to_scan = []
    if 'django.template.loaders.app_directories.Loader' in settings.TEMPLATE_LOADERS:
        for app in settings.INSTALLED_APPS:
            _ = __import__(app)
            dir = os.path.dirname(_.__file__)
            if not dir in dirs_to_scan:
                #append 'templates' for app directories
                dirs_to_scan.append(os.path.join(dir, 'templates'))

    if 'django.template.loaders.filesystem.Loader' in settings.TEMPLATE_LOADERS:
        for dir in settings.TEMPLATE_DIRS:
            if not dir in dirs_to_scan:
                #filesystem loader assumes our templates in 'templates' already
                dirs_to_scan.append(dir)

    for dir in dirs_to_scan:
        dir_glob = 'tabsplugin/tabs'
        found = glob.glob(os.path.join(dir, '{}/*.html'.format(dir_glob)))
        for file in found:
            dir, file = os.path.split(file)
            dir_count = len(dir_glob.split("/"))
            key, value = os.path.join(*dir.split('/')[-dir_count:] + [file]), file
            f = False
            for _, template in templates:
                if template == file:
                    f = True
            if not f:
                templates.append((key, value,))

    return sorted_templates(templates)
