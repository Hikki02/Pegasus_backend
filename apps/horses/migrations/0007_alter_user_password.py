# Generated by Django 4.1.2 on 2022-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$SJx5WObm9myrKo5jeMscTa$JxLhO/aDal4/wdx+q1CuAkfU2Y+fHVfQkEEju/6Xc2M=', max_length=128),
        ),
    ]
