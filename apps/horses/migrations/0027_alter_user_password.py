# Generated by Django 4.1.2 on 2022-11-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0026_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$u3nSpYVseOajLa6WYHvF46$PrJTmADNqWoSYz2RhAerE22xSrN1UKd1LgRcXk+539A=', max_length=128),
        ),
    ]
