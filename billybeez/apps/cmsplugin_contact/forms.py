from django import forms
#import settings
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    """ form for contact us form plugin, specific fields """
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Name')}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Mobile')}))
    subject = forms.ChoiceField(choices=settings.CONTACT_US_SUBJECT_CHOICHES)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 35, 'rows': 5}))

  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
