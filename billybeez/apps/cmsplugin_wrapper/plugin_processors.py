import os
from django.conf import settings
from django.template import Template
from cmsplugin_wrapper.models import WrapperPlugin

varname = getattr(settings, 'CMSPLUGIN_WRAPPER_VARNAME', 'CMSPLUGIN_WRAPPER_HOLDER')
TEMPLATES_PATH = os.path.abspath(os.path.dirname(__file__)) + "/templates/cmsplugin_wrapper/"

def wrap_plugin(instance, placeholder, rendered_content, original_context):
    
    wrap_holder = original_context[varname]
    if isinstance(instance, WrapperPlugin):
        wrap_info = {
            'wrapper_plugin': instance,
            'context': original_context,
            'plugins': [],
            'plugin_counter': 0
        }
        wrap_holder['at_index'] = wrap_holder['at_index'] and wrap_holder['at_index'] + 1 or 0
        wrap_holder['index'].append(wrap_info)
        
        
    elif wrap_holder['at_index'] is not None and not (instance._render_meta.text_enabled and instance.parent):
        wrap_info = wrap_holder['index'][wrap_holder['at_index']]
        wrap_info['plugin_counter'] = wrap_info['plugin_counter'] + 1
        wrap_info['plugins'].append(rendered_content)
         
        if wrap_info['plugin_counter'] == wrap_info['wrapper_plugin'].number or \
            wrap_info['plugin_counter'] == instance._render_meta.total:
            filename = wrap_info['wrapper_plugin'].template
            print filename
            # check that this file exists
            try:
                f = open(TEMPLATES_PATH+filename)
                template = f.read()
                f.close()
            except IOError:
                template = ''

            template = Template(template)
            context = wrap_info['context']
            context['plugins'] = wrap_info['plugins']
            wrap_holder['index'].pop()
            wrap_holder['at_index'] = wrap_holder['at_index'] == 0 and None or wrap_holder['at_index'] - 1
            
            return template.render(context)
    return u' '