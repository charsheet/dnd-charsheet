from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.http import Http404

from .models import Character
from .forms import CharacterForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'charsheet_list'

    def get_queryset(self):
        """ Return the users Character List """
        if self.request.user.is_authenticated():
            return Character.objects.filter(user=self.request.user)
        else:
            return

class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'detail.html'

class CharacterUpdateView(generic.UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'update.html'
    success_url = 'update'

    def get_queryset(self):
        try:
            base_qs = super(CharacterUpdateView, self).get_queryset()
            return base_qs.filter(user=self.request.user)
        except:
            raise Http404('Only the creator may edit this character')
