import uuid
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin, AbstractUser
)
from django.db import models

from pegasus import settings


class HorseManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, name, password: str, **extra) -> None:
        self._validate(email=email, name=name, password=password)
        user = self.model(email=self.normalize_email(email), name=name,
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    name: str,
                    password: str) -> None:
        self._create(email, name, password, )

    def create_superuser(self,
                         email: str,
                         name: str,
                         password: str) -> None:
        self._create(email, name, password, is_staff=True, is_superuser=True, is_active=True)


# Create your models here.
class Horse(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    birth_day = models.DateField(null=True)
    weight = models.FloatField(null=True)
    examined_at = models.DateField(null=True)

    password = models.CharField(max_length=128, default=make_password(settings.DEFAULT_PASSWORD))

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('',)

    class Meta:
        app_label = 'horses'
        db_table = 'horse'
        verbose_name = "Horse"
        verbose_name_plural = "Horses"

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(Horse, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    objects = HorseManager()


class HorseImage(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    images = models.ImageField()

    def __str__(self):
        return f'{self.images}'
