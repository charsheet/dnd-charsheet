from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic

from .models import Character
from .forms import CharacterForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'charsheet_list'

    def get_queryset(self):
        """ Return the users Character List """
        return Character.objects.order_by('-id')

class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'detail.html'

class CharacterUpdateView(generic.UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'update.html'
    success_url = 'update'
