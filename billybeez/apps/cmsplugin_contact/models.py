from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Feel free to extend this class instead of Contact.
class BaseContact(CMSPlugin):
    SPAM_PROTECTION_CHOICES = (
        (0, 'Honeypot'),
        (1, 'Akismet'),
        (2, 'ReCAPTCHA'),
    )
    
    THEME_CHOICES = (
        ('clean', 'Clean'),
        ('red', 'Red'),
        ('white', 'White'),
        ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
    )
    
    site_email = models.EmailField(_('Default email recipient'), help_text=_('Email to recieve the sent emails'))

    name_label = models.CharField(_('User Name'), default=('NAME'), max_length=30,
                                    help_text=_('Label for the user name input field'))

    email_label = models.CharField(_('Email sender label'), default=_('E-MAIL'), max_length=100,
                                    help_text=_('Label for the user email input field'))

    mobile_label = models.CharField(_('User Mobile Phone'), default=('MOBILE'), max_length=14,
                                     help_text=_('Label for the user mobile input field'))

    subject_label = models.CharField(_('Subject label'), default=_('SUBJECT'), max_length=200,
                                    help_text=_('Label for the email subject select options'))

    content_label = models.CharField(_('Message content label'), default=_('MESSAGE'), max_length=100,
                                    help_text=_('Label for the email message content field'))

    thanks = models.TextField(verbose_name=_("Thanks message"), default=_('Thank you for your message.'), max_length=200,
                                    help_text=_('Message displayed on successful submit'),)

    submit = models.CharField(_('Submit button value'), default=_('Submit'), max_length=30,
                                    help_text=_('Value to display on the submit button'))

    reset = models.CharField(_('Reset button value'), default=_('Reset'), max_length=30,
                                    help_text=_('Value to display on the reset button'))

    spam_protection_method = models.SmallIntegerField(verbose_name=_('Spam protection method'),
                                                    choices=SPAM_PROTECTION_CHOICES, default=0)
    
    akismet_api_key = models.CharField(max_length=255, blank=True)
    
    recaptcha_public_key = models.CharField(max_length=255, blank=True)
    recaptcha_private_key = models.CharField(max_length=255, blank=True)
    recaptcha_theme = models.CharField(max_length=20, choices=THEME_CHOICES,
                                       default='clean', verbose_name=_('ReCAPTCHA theme'))

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.site_email

class Contact(BaseContact):
    pass
