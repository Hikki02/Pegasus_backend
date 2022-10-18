from django.db import models

from apps.horses.models import Horse

from .utils import MedicineStatus


class Medication(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    title = models.CharField()
    data = models.DateField()
    status = models.CharField(max_length=5, default=MedicineStatus.taken, choices=MedicineStatus)


class Vaccine(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    title = models.CharField()
    data = models.DateField()
    status = models.CharField(max_length=5, default=MedicineStatus.taken, choices=MedicineStatus)

