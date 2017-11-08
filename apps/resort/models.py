from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name


class ResortManager(models.Manager):

    def featured(self, position):
        try:
            return self.get(is_featured=True, featured_position=position)
        except Resort.DoesNotExist:
            if self.filter(is_active=True).count() > 4:
                return Resort.objects.order_by('?').first()
            else:
                return None


class ResortOption(models.Model):
    resort = models.ForeignKey('Resort')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    villa_view = models.TextField(blank=True, null=True)
    max_occupancy = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        abstract = True


class Resort(models.Model):

    POSITION_CHOICES = (
        (0, 'Top left'),
        (1, 'Top right'),
        (2, 'Bottom left'),
        (3, 'Bottom center')
    )

    destination = models.ForeignKey(Destination)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    villa_view = models.TextField(blank=True, null=True)
    max_occupancy = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    featured_position = models.IntegerField(choices=POSITION_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    objects = ResortManager()

    def __str__(self):
        return "%s" % self.name


class ResortImage(models.Model):
    image = models.ImageField(upload_to='resorts/')
    resort = models.ForeignKey('Resort')

    def __str__(self):
        return "%s" % self.image


class VillaSuite(ResortOption):
    pass


class VillaSuiteImage(models.Model):
    image = models.ImageField(upload_to='villas/')
    option = models.ForeignKey('VillaSuite')

    def __str__(self):
        return "%s" % self.image


class WineDine(ResortOption):
    pass


class WineDineImage(models.Model):
    image = models.ImageField(upload_to='winedine/')
    option = models.ForeignKey('WineDine')

    def __str__(self):
        return "%s" % self.image


class Wellness(ResortOption):
    pass


class WellnessImage(models.Model):
    image = models.ImageField(upload_to='wellness/')
    option = models.ForeignKey('Wellness')

    def __str__(self):
        return "%s" % self.image


class Experience(ResortOption):
    pass


class ExperienceImage(models.Model):
    image = models.ImageField(upload_to='experience/')
    option = models.ForeignKey('Experience')

    def __str__(self):
        return "%s" % self.image