# Generated by Django 4.1.2 on 2022-11-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0015_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$cWUA09Emdzz71w1ZIuPApo$Yp6XurUm9ajTMqJ7g6pZFZcPVtPDXP5qoNQrxeqKUO0=', max_length=128),
        ),
    ]
