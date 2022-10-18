import uuid

from django.db import models


class Horse(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    birth_day = models.DateField()
    weight = models.FloatField()
    email = models.EmailField()

    class Meta:
        verbose_name = "Horse"
        verbose_name_plural = "Horses"

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(Horse, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class HorseImage(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    images = models.ImageField()

    def __str__(self):
        return f'{self.images}'
