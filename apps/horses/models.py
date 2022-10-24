import os
import uuid
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin, AbstractUser
)
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework_simplejwt.tokens import RefreshToken

from pegasus import settings

def get_upload_path(instance, filename):
    return os.path.join('horse/images/', datetime.now().date().strftime("%Y/%m/%d"), filename)



class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, password: str, **extra) -> None:
        self._validate(email=email, password=password)
        user = self.model(email=self.normalize_email(email),
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    password: str) -> None:
        self._create(email, password, )

    def create_superuser(self,
                         email: str,
                         password: str) -> None:
        self._create(email, password, is_staff=True, is_superuser=True, is_active=True)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
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


    class Meta:
        app_label = 'horses'
        db_table = 'horse'
        verbose_name = "Horse"
        verbose_name_plural = "Horses"

    def __str__(self):
        return f'{self.email}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    objects = UserManager()


class HorseImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='horse')
    image = models.ImageField(upload_to=get_upload_path, null=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.image}'


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f"Перейдите по ссылке для восстановления пароля: " \
                              f"\n http://localhost:3000/?#/resetPassword/?token={reset_password_token.key}"
    send_mail(
        # title:
        "Password Reset for {title}".format(title=reset_password_token.user),
        # message:
        email_plaintext_message,
        # from:
        "hikki2506@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
