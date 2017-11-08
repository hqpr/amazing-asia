from django.db import models


class OfferManager(models.Manager):

    def featured(self, position):
        try:
            return self.get(is_featured=True, featured_position=position)
        except Offer.DoesNotExist:
            if self.filter(is_active=True).count() > 4:
                return Offer.objects.order_by('?').first()
            else:
                return None


class Offer(models.Model):

    POSITION_CHOICES = (
        (0, 'Top left'),
        (1, 'Top right'),
        (2, 'Bottom left'),
        (3, 'Bottom center')
    )

    name = models.CharField(max_length=255)
    offer_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    stays_from = models.DateField(blank=True, null=True)
    stays_to = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='offers/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    featured_position = models.IntegerField(choices=POSITION_CHOICES, blank=True, null=True)

    objects = OfferManager()

    def __str__(self):
        return "%s" % self.name
