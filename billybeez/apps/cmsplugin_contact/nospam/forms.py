from django import forms
from django.conf import settings

from cmsplugin_contact.nospam import utils

from fields import HoneypotField
from widgets import RecaptchaChallenge, RecaptchaResponse
from django.utils.translation import ugettext_lazy as _



class BaseForm(forms.Form):
    
    def __init__(self, request, *args, **kwargs):
        self._request = request
        super(BaseForm, self).__init__(*args, **kwargs)
        



class AkismetForm(BaseForm):
    
    akismet_fields = {
            'comment_author': 'name',
            'comment_author_email': 'email',
            'comment_author_url': 'url',
            'comment_content': 'comment',
            }
    akismet_api_key = None
    
    def akismet_check(self):
        fields = {}
        for key, value in self.akismet_fields.items():
            fields[key] = self.cleaned_data[value]
        return utils.akismet_check(self._request, akismet_api_key=self.akismet_api_key, **fields)


class RecaptchaForm(BaseForm):
    recaptcha_challenge_field = forms.CharField(widget=RecaptchaChallenge)
    recaptcha_response_field = forms.CharField(
                widget = RecaptchaResponse,
                label = _('Please enter the two words on the image separated by a space:'),
                error_messages = {
                    'required': _('You did not enter any of the words.')
            })
    recaptcha_always_validate = False
    
    def __init__(self, *args, **kwargs):
        # Because the ReCAPTCHA library requires the fields to be named a
        # certain way, using a form prefix will break the validation unless we
        # modify the received POST and rename the keys accordingly
        if ('data' in kwargs or len(args) > 1) and 'prefix' in kwargs:
            data = kwargs.get('data', args[1]).__copy__()
            data['%s-recaptcha_challenge_field' % kwargs['prefix']] = \
                data.pop('recaptcha_challenge_field', [u''])[0]
            data['%s-recaptcha_response_field' % kwargs['prefix']] = \
                data.pop('recaptcha_response_field', [u''])[0]
            data._mutable = False
            # Since data could have been passed eith as an arg or kwarg, set
            # the right one to the new data
            if 'data' in kwargs:
                kwargs['data'] = data
            else:
                args = (args[0], data) + args[2:]
                
        super(RecaptchaForm, self).__init__(*args, **kwargs)
        self._recaptcha_public_key = getattr(self, 'recaptcha_public_key', getattr(settings, 'RECAPTCHA_PUBLIC_KEY', None))
        self._recaptcha_private_key = getattr(self, 'recaptcha_private_key', getattr(settings, 'RECAPTCHA_PRIVATE_KEY', None))
        self._recaptcha_theme = getattr(self, 'recaptcha_theme', getattr(settings, 'RECAPTCHA_THEME', 'clean'))
        self.fields['recaptcha_response_field'].widget.public_key = self._recaptcha_public_key
        self.fields['recaptcha_response_field'].widget.theme = self._recaptcha_theme
        # Move the ReCAPTCHA fields to the end of the form
        self.fields['recaptcha_challenge_field'] = self.fields.pop('recaptcha_challenge_field')
        self.fields['recaptcha_response_field'] = self.fields.pop('recaptcha_response_field')

       
    def clean_recaptcha_response_field(self):
        if 'recaptcha_challenge_field' in self.cleaned_data:
            self._validate_captcha()
        return self.cleaned_data['recaptcha_response_field']

    def clean_recaptcha_challenge_field(self):
        if 'recaptcha_response_field' in self.cleaned_data:
            self._validate_captcha()
        return self.cleaned_data['recaptcha_challenge_field']
    
    def _validate_captcha(self):
        if not self.recaptcha_always_validate:
            rcf = self.cleaned_data['recaptcha_challenge_field']
            rrf = self.cleaned_data['recaptcha_response_field']
            if rrf == '':
                raise forms.ValidationError(_('You did not enter the two words shown in the image.'))
            else:
                from recaptcha.client import captcha as recaptcha
                ip = self._request.META['REMOTE_ADDR']
                check = recaptcha.submit(rcf, rrf, self._recaptcha_private_key, ip)
                if not check.is_valid:
                    raise forms.ValidationError(_('The words you entered did not match the image.'))

class HoneyPotForm(BaseForm):
    accept_terms = HoneypotField()
    


class SuperSpamKillerForm(RecaptchaForm, HoneyPotForm, AkismetForm):
    pass
