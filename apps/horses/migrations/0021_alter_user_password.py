# Generated by Django 4.1.2 on 2022-10-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0020_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$6TlyW4lyCXU56fbIxXRvC5$71D9UY0t7d+4xd104zRgR20FYD4+/VlJ8JajYMoA2nA=', max_length=128),
        ),
    ]