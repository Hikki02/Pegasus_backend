# Generated by Django 4.1.2 on 2022-11-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0011_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$tkIrOllE8XoNX4AJ54W1tQ$GijdPNInadnpOpCpEWFG7TLlfusk1TOpZYgY2MI272Y=', max_length=128),
        ),
    ]