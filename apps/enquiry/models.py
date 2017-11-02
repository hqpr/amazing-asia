from django.db import models


class Enquiry(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    residence = models.CharField(max_length=255)
    property_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    arrival_date = models.DateField()
    num_of_nights = models.IntegerField()
    num_adults = models.IntegerField()
    num_children = models.IntegerField()
    num_infants = models.IntegerField()

    def __str__(self):
        return "%s" % self.full_name
