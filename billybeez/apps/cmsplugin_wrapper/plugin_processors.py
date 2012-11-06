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
            'wrapper_plugin': instance,     # the main wrapper plugin
            'context': original_context,    # request original data
            'plugins': [],                  # will contain the rendered_content of the plugins to wrap
            'plugin_counter': 0             # countier for the plugins added so far
        }
        # default values : 'at_index': None and 'index': []
        wrap_holder['at_index'] = wrap_holder['at_index'] and wrap_holder['at_index'] + 1 or 0
        wrap_holder['index'].append(wrap_info)
        return u''
    # for other plugins wrapper by the WrapperPlugin   
    elif wrap_holder['at_index'] is not None and not (instance._render_meta.text_enabled and instance.parent):
        wrap_info = wrap_holder['index'][wrap_holder['at_index']]
        # increment the plugins countier by one, then added to the plugins container
        wrap_info['plugin_counter'] = wrap_info['plugin_counter'] + 1
        wrap_info['plugins'].append(rendered_content)
        # if the number of the wrapped plugins is reached, output the final wrapped content 
        if wrap_info['plugin_counter'] == wrap_info['wrapper_plugin'].number or \
            wrap_info['plugin_counter'] == instance._render_meta.total:
            filename = wrap_info['wrapper_plugin'].template
            # check that this template file exists
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
            wrap_holder['at_index'] = None
            return template.render(context)
        else:
            return u''
    # for plugins outside the WrapperPlugin - regular
    return rendered_content