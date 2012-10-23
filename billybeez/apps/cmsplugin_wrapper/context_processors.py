from django.conf import settings

def cmsplugin_wrapper(request=None):
    """
    Simple context processor which makes sure that the dict is
    available in all templates.
    """
    varname = getattr(settings, 'CMSPLUGIN_WRAPPER_VARNAME', 'CMSPLUGIN_WRAPPER_HOLDER')
    return {varname: {'at_index': None, 'index': []}}