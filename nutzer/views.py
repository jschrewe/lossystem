from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from treffen.models import Treffen


class ProfileView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moegliche_treffen'] = Treffen.objects.exclude(
            anmeldungen=self.request.user
        )
        context['angemeldet'] = Treffen.objects.filter(
            anmeldungen=self.request.user
        )
        return context


@login_required
def anmelden(request, id):
    treffen = get_object_or_404(Treffen, pk=id)
    treffen.anmeldungen.add(request.user)
    treffen.save()
    return redirect('profile')


@login_required
def abmelden(request, id):
    treffen = get_object_or_404(Treffen, pk=id)
    treffen.anmeldungen.remove(request.user)
    treffen.save()
    return redirect('profile')
