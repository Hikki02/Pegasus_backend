import uuid

from django.db import models

from apps.horses.models import User

from .utils import MedicineStatus


class Medication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    horse = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    data = models.DateField()
    status = models.CharField(max_length=20, default=MedicineStatus.taken, choices=MedicineStatus.choice())

    def __str__(self):
        return f'{self.title}'


class Vaccine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    horse = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    data = models.DateField()
    status = models.CharField(max_length=20, default=MedicineStatus.taken, choices=MedicineStatus.choice())

    def __str__(self):
        return f'{self.title}'

