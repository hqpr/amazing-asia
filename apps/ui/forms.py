from django import forms
from django.core.mail import EmailMessage

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone', 'residence', 'body')

    def save(self):
        contact = Contact(
            first_name=self.cleaned_data['first_name'],
            email=self.cleaned_data['email1'],
            body=self.cleaned_data['body']
        )
        cont = contact.save()

        body = 'From: {}\n Name: {}\n Body: {}'.format(self.cleaned_data['email1'],
                                                       self.cleaned_data['first_name'],
                                                       self.cleaned_data['body'])

        email = EmailMessage(
            'Contact Form',
            body,
            self.cleaned_data['email1'],
            ['contact@mygunlab.com', ],
            ['adubnyak@gmail.com', 'mygunlab@gmail.com'],
            reply_to=['mygunlab@gmail.com'],
        )

        email.send()
        return cont
