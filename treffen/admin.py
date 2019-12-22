from django.contrib import admin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from admin_actions.admin import ActionsModelAdmin

from .models import Treffen


class TreffenAdmin(ActionsModelAdmin):
    model = Treffen
    filter_horizontal = ('anmeldungen', 'eingeladen', 'teilnehmer')

    actions_detail = ('einladen', )

    def einladen(self, request, pk):
        treffen = get_object_or_404(self.model, pk=pk)
        treffen.invite()
        return redirect(reverse_lazy('admin:treffen_treffen_change', args=(pk,)))
    einladen.short_description = 'Einladungen ermitteln'
    einladen.url_path = 'einladen'


admin.site.register(Treffen, TreffenAdmin)
