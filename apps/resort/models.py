from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name


class Resort(models.Model):
    destination = models.ForeignKey(Destination)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    villa_view = models.TextField(blank=True, null=True)
    max_occupancy = models.IntegerField(blank=True, null=True)
    image = models.ForeignKey('ResortImage', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.name


class ResortImage(models.Model):
    image = models.ImageField(upload_to='resorts/')

    def __str__(self):
        return "%s" % self.image