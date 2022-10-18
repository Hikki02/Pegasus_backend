# Generated by Django 4.1.2 on 2022-10-18 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('birth_day', models.DateField()),
                ('weight', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Horse',
                'verbose_name_plural': 'Horses',
            },
        ),
        migrations.CreateModel(
            name='HorseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horses.horse')),
            ],
        ),
    ]