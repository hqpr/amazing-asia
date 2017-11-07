from django import forms
from django.core.mail import EmailMessage

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone', 'residence', 'body')

    def save(self):
        contact = Contact(
            full_name=self.cleaned_data['full_name'],
            email=self.cleaned_data['email'],
            body=self.cleaned_data['body'],
            phone=self.cleaned_data['phone'],
            residence=self.cleaned_data['residence'],
        )
        cont = contact.save()

        body = 'From: {}\n Name: {}\n Body: {}'.format(self.cleaned_data['email'],
                                                       self.cleaned_data['full_name'],
                                                       self.cleaned_data['phone'],
                                                       self.cleaned_data['residence'],
                                                       self.cleaned_data['body'])

        email = EmailMessage(
            'Contact Form',
            body,
            self.cleaned_data['email'],
            ['contact@mygunlab.com', ],
            ['adubnyak@gmail.com', 'mygunlab@gmail.com'],
            reply_to=['mygunlab@gmail.com'],
        )

        email.send()
        return cont
