from django.contrib import admin
from .models import User, Image, UserImage


class UserImageInlines(admin.TabularInline):
    model = UserImage
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [UserImageInlines]


admin.site.register(Image)
admin.site.register(User, UserAdmin)
