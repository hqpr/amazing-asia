from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    stays_from = models.DateField(blank=True, null=True)
    stays_to = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='offers/', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.name
