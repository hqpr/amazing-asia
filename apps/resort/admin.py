from django.contrib import admin

from .models import Destination, Resort, ResortImage


class ResortImageInline(admin.StackedInline):
    model = ResortImage
    extra = 1


class ResortAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_featured')

    inlines = [
        ResortImageInline,
    ]


admin.site.register(Destination)
admin.site.register(Resort, ResortAdmin)
admin.site.register(ResortImage)
