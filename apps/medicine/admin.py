from django.contrib import admin
from .models import Medication, Vaccine


@admin.register(Medication)
class MedicineAdmin(admin.ModelAdmin):

    ...


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    ...


