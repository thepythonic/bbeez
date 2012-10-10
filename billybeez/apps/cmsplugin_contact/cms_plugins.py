from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import CharField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.settings import USE_TINYMCE
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from models import Contact
from forms import ContactForm, AkismetContactForm, RecaptchaContactForm, HoneyPotContactForm
from admin import ContactAdminForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "cmsplugin_contact/contact.html"
    form = ContactAdminForm
    contact_form = ContactForm
    subject_template = "cmsplugin_contact/subject.txt"
    email_template = "cmsplugin_contact/email.txt"
    
    fieldsets = (
        (None, {
            'fields': ('site_email', 'name_label', 'email_label', 'mobile_label', 'subject_label', 'content_label', 'thanks', 'submit'),
        }),
        (_('Spam Protection'), {
            'fields': ('spam_protection_method', 'akismet_api_key', 'recaptcha_public_key', 'recaptcha_private_key', 'recaptcha_theme')
        })
    )
    
    change_form_template = "cmsplugin_contact/admin/plugin_change_form.html"

    def get_editor_widget(self, request, plugins):
        """
        Returns the Django form Widget to be used for
        the text area
        """
        if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
            from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
            return TinyMCEEditor(installed_plugins=plugins)
        else:
            return WYMEditor(installed_plugins=plugins)

    def get_form_class(self, request, plugins):
        """
        Returns a subclass of Form to be used by this plugin
        """
        # We avoid mutating the Form declared above by subclassing
        class TextPluginForm(self.form):
            pass
        widget = self.get_editor_widget(request, plugins)
        
        thanks_field = self.form.base_fields['thanks']
        
        TextPluginForm.declared_fields["thanks"] = CharField(widget=widget, required=False, label=thanks_field.label, help_text=thanks_field.help_text)
        return TextPluginForm


    def get_form(self, request, obj=None, **kwargs):
        plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)
        form = self.get_form_class(request, plugins)
        kwargs['form'] = form # override standard form
        return super(ContactPlugin, self).get_form(request, obj, **kwargs)

    def create_form(self, instance, request):
        if instance.get_spam_protection_method_display() == 'Akismet':
            AkismetContactForm.aksimet_api_key = instance.akismet_api_key
            class ContactForm(self.contact_form, AkismetContactForm):
                pass
            FormClass = ContactForm
        elif instance.get_spam_protection_method_display() == 'ReCAPTCHA':
            RecaptchaContactForm.recaptcha_public_key = getattr(
                settings, "RECAPTCHA_PUBLIC_KEY",
                instance.recaptcha_public_key)
            RecaptchaContactForm.recaptcha_private_key = getattr(
                settings, "RECAPTCHA_PRIVATE_KEY",
                instance.recaptcha_private_key)
            RecaptchaContactForm.recaptcha_theme = instance.recaptcha_theme
            class ContactForm(self.contact_form, RecaptchaContactForm):
                pass
            FormClass = ContactForm
        else:
            class ContactForm(self.contact_form, HoneyPotContactForm):
                pass
            FormClass = ContactForm
            
        if request.method == "POST":
            return FormClass(request, data=request.POST)
        else:
            return FormClass(request)


    def send(self, form, site_email):
        subject = form.cleaned_data['subject']
        if not subject:
            subject = _('No subject')
        email_message = EmailMessage(
            # The subject line of the e-mail
            render_to_string(self.subject_template, {
                'suject_prefix': '[Billy Beez Info]',
                'subject': subject,
            }).splitlines()[0],
            # The body text. This should be a plain text message.
            render_to_string(self.email_template, {
                'data': form.cleaned_data,
                'user_name': form.cleaned_data['name'],
                'user_email': form.cleaned_data['email'],
                'user_mobile': form.cleaned_data['mobile']
            }),
            # from_email: The sender's address. Both fred@example.com and Fred <fred@example.com> 
            # forms are legal. If omitted, the DEFAULT_FROM_EMAIL setting is used.
            form.cleaned_data['email'],
            # to: A list or tuple of recipient addresses
            [site_email],
            # bcc: A list or tuple of addresses used in the "Bcc" header when sending the e-mail.
            # A dictionary of extra headers to put on the message. The keys are the header name, values are the header values
            headers = {
                'Reply-To': form.cleaned_data['email']
            },)
        email_message.send(fail_silently=False)
    
    def render(self, context, instance, placeholder):
        request = context['request']

        form = self.create_form(instance, request)
    
        if request.method == "POST" and form.is_valid():
            self.send(form, instance.site_email)
            context.update( {
                'contact': instance,
            })
        else:
            context.update({
                'contact': instance,
                'form': form,
            })
            
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'spam_protection_method': obj.spam_protection_method if obj else 0,
            'recaptcha_settings': hasattr(settings, "RECAPTCHA_PUBLIC_KEY"),
            'akismet_settings': hasattr(settings, "AKISMET_API_KEY"),
        })
        
        return super(ContactPlugin, self).render_change_form(request, context, add, change, form_url, obj)
        
    
plugin_pool.register_plugin(ContactPlugin)
