# Generated by Django 4.1.2 on 2022-11-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0027_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$kCIEbD0yo1D5uQbugPjJLN$Rpy3JtU2VnxyBA2o4sFMwy3sCirgjrLiWy5qSf9ZNXQ=', max_length=128),
        ),
    ]