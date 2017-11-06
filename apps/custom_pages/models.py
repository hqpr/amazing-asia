from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=128)
    text = HTMLField(
        verbose_name=u'Text',
    )
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('single_page', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return self.get_url()

    def __str__(self):
        return '%s' % self.title
