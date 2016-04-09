from django import forms
from models import Character, CharacterClass, Equipment, Spells, AttacksAndSpellcasting
from django.forms import inlineformset_factory

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ['id']

class CharacterClassForm(forms.ModelForm):
    # TODO: Define form fields here

    class Meta:
        model = CharacterClass
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(CharacterClassForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CharacterClassForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(CharacterClassForm, self).clean()

CharacterClassFormset = inlineformset_factory(
                        Character,
                        CharacterClass,
                        fields=(
                            'char_class',
                            'level'))

EquipmentFormset = inlineformset_factory(
                        Character,
                        Equipment,
                        fields=(
                            'quantity',
                            'name',
                            'description',
                            'weight',
                            'value'))

AttacksAndSpellcastingFormset = inlineformset_factory(
                        Character,
                        AttacksAndSpellcasting,
                        fields=(
                            'attack',
                            'bonus',
                            'damage',
                            'damage_type'))

SpellsFormset = inlineformset_factory(
                        Character,
                        Spells,
                        fields=(
                            'level_or_cantrip',
                            'name',
                            'description',
                            'prepared'))
