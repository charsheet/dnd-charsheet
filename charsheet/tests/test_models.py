from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
User = get_user_model()

from google.appengine.ext import testbed

from charsheet.models import Character

class CharacterModelTest(TestCase):

    def setUp(self):
        """Initalise GAE test stubs before each test is run."""
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        test_user = User.objects.pre_create_google_user(email='testcase@example.com')
        self.character_data = {
            'user': test_user,
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

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

        test_user = User.objects.pre_create_google_user(email='test@example.com')
        self.character_data = {
            'user': test_user,
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

    def create_character(self, **kwargs):
        return Character.objects.create(**kwargs)

    def test_character_creation(self):
        character = self.create_character(**self.character_data)
        self.assertTrue(isinstance(character, Character))
        self.assertEqual(character.__unicode__(), character.character_name)

    def test_modified_fields(self):
        character = self.create_character(**self.character_data)

        self.assertEqual(character.strength_modifier, 3)
        self.assertEqual(character.intelligence_modifier, -2)
        self.assertEqual(character.wisdom_modifier, 4)
        self.assertEqual(character.dexterity_modifier, 2)
        self.assertEqual(character.constitution_modifier, -1)
        self.assertEqual(character.charisma_modifier, 1)

        self.assertEqual(character.strength_save_modifier, 5)
        self.assertEqual(character.dexterity_save_modifier, 2)
        self.assertEqual(character.intelligence_save_modifier, 0)
        self.assertEqual(character.wisdom_save_modifier, 6)
        self.assertEqual(character.constitution_save_modifier, -1)
        self.assertEqual(character.charisma_save_modifier, 1)

        self.assertEqual(character.acrobatics_modifier, 4)
        self.assertEqual(character.animal_handling_modifier, 6)
        self.assertEqual(character.arcana_modifier, -2)
        self.assertEqual(character.athletics_modifier, 3)
        self.assertEqual(character.deception_modifier, 1)
        self.assertEqual(character.history_modifier, 0)
        self.assertEqual(character.insight_modifier, 4)
        self.assertEqual(character.intimidation_modifier, 1)
        self.assertEqual(character.investigation_modifier, -2)
        self.assertEqual(character.medicine_modifier, 6)
        self.assertEqual(character.nature_modifier, 0)
        self.assertEqual(character.performance_modifier, 1)
        self.assertEqual(character.persuasion_modifier, 3)
        self.assertEqual(character.religion_modifier, -2)
        self.assertEqual(character.sleight_of_hand_modifier, 2)
        self.assertEqual(character.stealth_modifier, 2)
        self.assertEqual(character.survival_modifier, 6)
