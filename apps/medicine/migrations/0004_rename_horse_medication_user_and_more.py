# Generated by Django 4.1.2 on 2022-11-01 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_rename_data_medication_date_rename_data_vaccine_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medication',
            old_name='horse',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='horse',
            new_name='user',
        ),
    ]
