from django.contrib import admin

from .models import Destination, Resort, ResortImage

admin.site.register(Destination)
admin.site.register(Resort)
admin.site.register(ResortImage)
