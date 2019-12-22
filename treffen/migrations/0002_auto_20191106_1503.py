# Generated by Django 2.2.6 on 2019-11-06 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treffen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treffen',
            name='anmeldungen',
            field=models.ManyToManyField(blank=True, related_name='anmeldungen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treffen',
            name='eingeladen',
            field=models.ManyToManyField(blank=True, related_name='einladungen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treffen',
            name='teilnehmer',
            field=models.ManyToManyField(blank=True, related_name='teilnehmer', to=settings.AUTH_USER_MODEL),
        ),
    ]