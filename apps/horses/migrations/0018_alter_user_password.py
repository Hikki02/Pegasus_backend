# Generated by Django 4.1.2 on 2022-11-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0017_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$OCDXpsWSVXIUnwUeIT41de$i722TDyVPdLga4505vKGZvOKztpiy4Fctpt0JPHbmB4=', max_length=128),
        ),
    ]
