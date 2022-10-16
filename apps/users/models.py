import uuid

from django.db import models


parametersForNull = {
    'null': True,
    'blank': True
}


class User(models.Model):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.name}'

    avatar = models.ImageField(verbose_name="Фото пользователя", upload_to='images/', **parametersForNull)
    user_bg = models.ImageField(verbose_name="Background", upload_to='images/', **parametersForNull)
    name = models.CharField(verbose_name="ФИО", max_length=200, **parametersForNull)
    position = models.CharField(verbose_name="Должность", max_length=200, **parametersForNull)
    description = models.TextField(verbose_name="О себе", max_length=2000, **parametersForNull)
    email = models.EmailField(verbose_name="eMail", **parametersForNull)
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, **parametersForNull)
    workPhone = models.CharField(verbose_name="Рабочий Номер телефона", max_length=30, **parametersForNull)

    instagram = models.URLField(verbose_name="Ссылка на Instagram", **parametersForNull)
    facebook = models.URLField(verbose_name="Ссылка на Facebook", **parametersForNull)
    twitter = models.URLField(verbose_name="Ссылка на Twitter", **parametersForNull)
    telegram = models.URLField(verbose_name="Ссылка на Telegram", **parametersForNull)
    linkedin = models.URLField(verbose_name="Ссылка на LinkedIn", **parametersForNull)
    youtube = models.URLField(verbose_name="Ссылка на YouTube", **parametersForNull)
    whatsapp = models.URLField(verbose_name="Ссылка на WhatsApp", **parametersForNull)
    behance = models.URLField(verbose_name="Ссылка на Behance", **parametersForNull)

    other_link = models.URLField(verbose_name="Другая ссылка", **parametersForNull)
    unique_id = models.UUIDField(blank=True, null=True)
    key = models.CharField(blank=True, null=True, max_length=8)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.unique_id = uuid.uuid4()
            self.key = uuid.uuid4().__str__()[0:8]

        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Image(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/dop_images')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Доп_Фотографии'

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user = models.ForeignKey(User, verbose_name="Продукт", on_delete=models.CASCADE)
    images = models.ForeignKey(Image, verbose_name="Фотография", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.images}'