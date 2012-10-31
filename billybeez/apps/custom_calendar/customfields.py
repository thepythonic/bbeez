from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.db import models

class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'custom_calendar/css/colorPicker.css',
            )
        }
        js = (
            settings.STATIC_URL + 'custom_calendar/js/colorpicker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').ColorPicker({
                onSubmit: function(hsb, hex, rgb, el) {
                   $(el).val(hex);
                   $(el).ColorPickerHide();
            },
                onBeforeShow: function () {
                 $(this).ColorPickerSetColor(this.value);
            },

            })
            .bind('keyup', function(){
               $(this).ColorPickerSetColor(this.value);
            });



            </script>''' % name)

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)
