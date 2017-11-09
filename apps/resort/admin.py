from django.contrib import admin

from .models import (Destination, Resort, ResortImage, VillaSuite, VillaSuiteImage, WineDine, WineDineImage,
                     Wellness, WellnessImage, Experience, ExperienceImage)


class ResortImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'resort')


class ResortImageInline(admin.StackedInline):
    model = ResortImage
    extra = 1


class VillaSuiteInline(admin.StackedInline):
    model = VillaSuite
    extra = 1


class VillaSuiteImageInline(admin.StackedInline):
    model = VillaSuiteImage
    extra = 1


class WineDineInline(admin.StackedInline):
    model = WineDine
    extra = 1


class WineDineImageInline(admin.StackedInline):
    model = WineDineImage
    extra = 1


class WellnessInline(admin.StackedInline):
    model = Wellness
    extra = 1


class WellnessImageInline(admin.StackedInline):
    model = WellnessImage
    extra = 1


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1


class ExperienceImageInline(admin.StackedInline):
    model = ExperienceImage
    extra = 1


class ResortAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'is_active', 'is_featured')

    inlines = [
        ResortImageInline,
        VillaSuiteInline,
        WineDineInline,
        WellnessInline,
        ExperienceInline,
    ]


class VillaSuiteAdmin(admin.ModelAdmin):
    inlines = [VillaSuiteImageInline, ]


class WineDineAdmin(admin.ModelAdmin):
    inlines = [WineDineImageInline, ]


class WellnessAdmin(admin.ModelAdmin):
    inlines = [WellnessImageInline, ]


class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceImageInline, ]


admin.site.register(Destination)
admin.site.register(Resort, ResortAdmin)
admin.site.register(ResortImage, ResortImageAdmin)
admin.site.register(VillaSuite, VillaSuiteAdmin)
admin.site.register(WineDine, WineDineAdmin)
admin.site.register(Wellness, WellnessAdmin)
admin.site.register(Experience, ExperienceAdmin)
