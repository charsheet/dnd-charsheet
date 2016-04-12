from django.contrib.auth import get_user_model
from django.test import TestCase

from charsheet.forms import CharacterForm
from charsheet.models import Character


User = get_user_model()


class CharacterFormTest(TestCase):

    form_data = {
        #'user': self.test_user,
        'player_name': 'Test Player',
        'character_name': 'Test Character',
        'background': "A Character's background",
        'race': 'Human',
        'alignment': 'TN',
        'experience_points': 500,
        'max_hit_points': 10,
        'current_hit_points': 8,
        'temporary_hit_points': 6,
        'armor_class': 12,
        'initiative': 5,
        'speed': 25,
        'inspiration': 1,
        'proficiency_bonus': 3,

        'hit_dice_total': 2,
        'hit_dice': '1d6',

        'death_save_success_1': True,
        'death_save_success_2': True,
        'death_save_success_3': False,
        'death_save_failure_1': True,
        'death_save_failure_2': True,
        'death_save_failure_3': False,

        'age': 28,
        'height': '''5'6"''',
        'weight': 190,
        'eyes': 'Green',
        'skin': 'Purple',
        'hair': 'Orange',
        'character_appearance': 'More Character Appearance information',
        'character_backstory': 'Some Backstory info',
        'allies_and_organizations': 'Ally #1',
        'additional_features_and_traits': 'Other Stuff',

        'treasure': 'Golden spoon made of honey',

        'strength': 16,
        'dexterity': 14,
        'constitution': 8,
        'intelligence': 6,
        'wisdom': 18,
        'charisma': 12,

        'acrobatics': True,
        'animal_handling': True,
        'arcana': False,
        'athletics': False,
        'deception': False,
        'history': True,
        'insight': False,
        'intimidation': False,
        'investigation': False,
        'medicine': True,
        'nature': True,
        'perception': False,
        'performance': False,
        'persuasion': True,
        'religion': False,
        'sleight_of_hand': False,
        'stealth': False,
        'survival': True,

        'strength_save': True,
        'dexterity_save': False,
        'constitution_save': False,
        'intelligence_save': True,
        'wisdom_save': True,
        'charisma_save': False,

        'personality_traits': 'Personality Field and such',
        'ideals': 'Idealistic Ideals',
        'bonds': 'Bonds, James Bonds',
        'flaws': 'I have none',

        'features_and_traits': '6 foot tall dwarf',
        'other_proficiencies_and_languages': 'Dwarvish',

        'spell_casting_class': 'Earth, wind and Fire',
        'spellcasting_ability': 'Sweet ass-horns',
        'spell_save_dc': 8,
        'spell_attack_bonus': 3,
    }


    def test_valid_data(self):
        form = CharacterForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        character = form.save(commit=False)
        character.user = User.objects.create(username='TestUser',
                                             email='testuser@example.com',
                                             password='l33tpassword')
        character.save()
        self.assertEqual(character.character_name, self.form_data['character_name'])

    def test_blank_data(self):
        form = CharacterForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'character_name': [u'This field is required.'],
            'alignment': [u'This field is required.'],
        })
