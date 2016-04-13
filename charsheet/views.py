from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.http import Http404

from .models import Character, CharacterClass
from .forms import CharacterForm, CharacterClassFormset, EquipmentFormset, AttacksAndSpellcastingFormset, SpellsFormset
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


class CharacterCreateView(generic.CreateView):
    model = Character
    template_name = 'create.html'
    #fields = ['character_name']
    form_class = CharacterForm


    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        characterclass_form = CharacterClassFormset()
        equipment_form = EquipmentFormset()
        attacksandspellcasting_form = AttacksAndSpellcastingFormset()
        spells_form = SpellsFormset()

        return self.render_to_response(self.get_context_data(form=form,
               equipment_form = equipment_form,
               attacksandspellcasting_form = attacksandspellcasting_form,
               spells_form = spells_form,
               characterclass_form=characterclass_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        characterclass_form = CharacterClassFormset(self.request.POST)
        equipment_form = EquipmentFormset(self.request.POST)
        attacksandspellcasting_form = AttacksAndSpellcastingFormset(self.request.POST)
        spells_form = SpellsFormset(self.request.POST)

        if (form.is_valid() and
            characterclass_form.is_valid() and
            equipment_form.is_valid() and
            attacksandspellcasting_form.is_valid(),
            spells_form.is_valid):

            return self.form_valid(form,
                characterclass_form,
                equipment_form,
                attacksandspellcasting_form,
                spells_form)
        else:
            return self.form_invalid(form,
                characterclass_form,
                equipment_form,
                attacksandspellcasting_form,
                spells_form)

    def form_valid(self, form, characterclass_form, equipment_form, attacksandspellcasting_form, spells_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        characterclass_form.instance = self.object
        characterclass_form.save()

        equipment_form.instance = self.object
        equipment_form.save()

        attacksandspellcasting_form.instance = self.object
        attacksandspellcasting_form.save()

        spells_form.instance = self.object
        spells_form.save()

        user = self.request.user
        form.instance.user = user

        return super(CharacterCreateView, self).form_valid(form)
        #return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, characterclass_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                characterclass_form=characterclass_form,
                equipment_form=equipment_form,
                attacksandspellcasting_form=attacksandspellcasting_form,
                spells_form=spells_form))


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'detail.html'


class CharacterUpdateView(generic.UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'update.html'
    success_url = 'update'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        characterclass_form = CharacterClassFormset()
        equipment_form = EquipmentFormset()
        attacksandspellcasting_form = AttacksAndSpellcastingFormset()
        spells_form = SpellsFormset()

        return self.render_to_response(self.get_context_data(form=form,
               equipment_form = equipment_form,
               attacksandspellcasting_form = attacksandspellcasting_form,
               spells_form = spells_form,
               characterclass_form=characterclass_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        characterclass_form = CharacterClassFormset(self.request.POST)
        equipment_form = EquipmentFormset(self.request.POST)
        attacksandspellcasting_form = AttacksAndSpellcastingFormset(self.request.POST)
        spells_form = SpellsFormset(self.request.POST)

        if (form.is_valid() and
            characterclass_form.is_valid() and
            equipment_form.is_valid() and
            attacksandspellcasting_form.is_valid(),
            spells_form.is_valid):

            return self.form_valid(form,
                characterclass_form,
                equipment_form,
                attacksandspellcasting_form,
                spells_form)
        else:
            return self.form_invalid(form,
                characterclass_form,
                equipment_form,
                attacksandspellcasting_form,
                spells_form)

    def form_valid(self, form, characterclass_form, equipment_form, attacksandspellcasting_form, spells_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        characterclass_form.instance = self.object
        characterclass_form.save()

        equipment_form.instance = self.object
        equipment_form.save()

        attacksandspellcasting_form.instance = self.object
        attacksandspellcasting_form.save()

        spells_form.instance = self.object
        spells_form.save()

        user = self.request.user
        form.instance.user = user

        return super(CharacterUpdateView, self).form_valid(form)
        #return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, characterclass_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                characterclass_form=characterclass_form,
                equipment_form=equipment_form,
                attacksandspellcasting_form=attacksandspellcasting_form,
                spells_form=spells_form))

    def get_queryset(self):
        try:
            base_qs = super(CharacterUpdateView, self).get_queryset()
            return base_qs.filter(user=self.request.user)
        except:
            raise Http404('Only the creator may edit this character')
