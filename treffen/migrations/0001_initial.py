# Generated by Django 2.2.6 on 2019-11-06 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treffen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(db_index=True)),
                ('einladungen', models.PositiveSmallIntegerField(default=12)),
                ('anmeldungen', models.ManyToManyField(related_name='anmeldungen', to=settings.AUTH_USER_MODEL)),
                ('eingeladen', models.ManyToManyField(related_name='einladungen', to=settings.AUTH_USER_MODEL)),
                ('teilnehmer', models.ManyToManyField(related_name='teilnehmer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
