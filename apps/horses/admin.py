from django.contrib import admin
from .models import Horse, HorseImage


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    ...


@admin.register(HorseImage)
class HorseAdmin(admin.ModelAdmin):
    ...


