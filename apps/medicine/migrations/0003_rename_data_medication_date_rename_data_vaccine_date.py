# Generated by Django 4.1.2 on 2022-10-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_medication_id_alter_vaccine_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medication',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='data',
            new_name='date',
        ),
    ]
