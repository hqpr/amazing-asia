from django.contrib import admin

from .models import Destination, Resort, ResortImage


class ResortAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_featured')


admin.site.register(Destination)
admin.site.register(Resort, ResortAdmin)
admin.site.register(ResortImage)
