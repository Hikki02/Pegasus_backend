from django.contrib import admin
from .models import User, HorseImage


@admin.register(User)
class HorseAdmin(admin.ModelAdmin):
    ...


@admin.register(HorseImage)
class HorseAdmin(admin.ModelAdmin):
    ...


