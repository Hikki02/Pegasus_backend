# Generated by Django 4.1.2 on 2022-11-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$DGGXGHpUV7XfUENKklCHm1$mHCCpcuYdh9F+mCQJk1hLoigVdGAdE2atpEwXS/NCig=', max_length=128),
        ),
    ]