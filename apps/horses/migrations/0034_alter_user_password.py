# Generated by Django 4.1.2 on 2022-11-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0033_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$QrRopRMTNfc90rBL9TkFmG$1NqVST+YQ91A2ot9aVATwmWIN0ajr9ehVlNveollzVA=', max_length=128),
        ),
    ]