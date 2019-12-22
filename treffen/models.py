from random import sample

from django.db import models
from django.conf import settings
from django.utils.dateformat import format


class Treffen(models.Model):
    datum = models.DateField(db_index=True)
    einladungen = models.PositiveSmallIntegerField(default=12)

    teilnehmer = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='teilnehmer',
        blank=True,
    )

    eingeladen = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='einladungen',
        blank=True,
    )

    anmeldungen = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='anmeldungen',
        blank=True,
    )

    def __str__(self):
        return format(self.datum, 'j. F Y')

    def invite(self):
        ids = self.anmeldungen.values_list('id', flat=True)
        print(ids)
        ids = list(ids)
        sample_size = min(len(ids), self.einladungen)
        rand_ids = sample(ids, sample_size)
        self.eingeladen.set(self.anmeldungen.filter(id__in=rand_ids))
        self.save()
