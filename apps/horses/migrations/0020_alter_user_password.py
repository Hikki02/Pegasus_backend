# Generated by Django 4.1.2 on 2022-10-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0019_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$Fvzm6BxnXSgaoaWLB7DXgT$eYgkirdvmGBQqQMZOnaWWZaR6mpJy1kbHssi+ZfY3+E=', max_length=128),
        ),
    ]
