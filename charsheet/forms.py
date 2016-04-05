from django import forms
from models import Character

class CharacterForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Character
        #fields = []
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CharacterForm, self).clean()
        return cleaned_data
