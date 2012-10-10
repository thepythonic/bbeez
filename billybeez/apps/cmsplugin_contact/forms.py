from django import forms
#import settings
from django.conf import settings
from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    subject = forms.ChoiceField(choices=settings.SUBJECT_CHOICHES)
    content = forms.CharField(widget=forms.Textarea())

  
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
