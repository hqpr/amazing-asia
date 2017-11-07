from django.db import models

from django.core.mail import EmailMessage


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    residence = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    is_sent = models.BooleanField(default=False)
    from_email = models.EmailField(default='no-reply@amasing-asia.com')
    reply_text = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.is_sent:
            if self.reply_text:

                body = 'Hi {}\n\n {}\n\n amasing-asia.com'.format(self.full_name, self.reply_text)

                email = EmailMessage(
                    'Response from amasing-asia',
                    body,
                    self.from_email,
                    [self.email, ],
                    ['adubnyak@gmail.com', ],
                    reply_to=['amasing-asia@amasing-asia.com'],
                )
                email.send()
                self.is_sent = True
        super().save(*args, **kwargs)

    def __str__(self):
        return "Message from {}".format(self.full_name)
