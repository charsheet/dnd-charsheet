from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse

#from django.contrib.auth.models import User
from djangae.contrib.gauth.datastore.models import GaeDatastoreUser
from djangae import fields

from .tools.modified_fields import modified_field as mf

# Create your models here.

@python_2_unicode_compatible
class Character(models.Model):
    """
    This is the main model for character sheets
    """

    LAWFUL_GOOD = 'LG'
    NEUTRAL_GOOD = 'NG'
    CHAOTIC_GOOD = 'CG'
    LAWFUL_NEUTRAL = 'LN'
    TRUE_NEUTRAL = 'TN'
    CHAOTIC_NEUTRAL = 'CN'
    LAWFUL_EVIL = 'LE'
    NEUTRAL_EVIL = 'NE'
    CHAOTIC_EVIL = 'CE'
    ALIGNMENT_CHOICES = (
        (LAWFUL_GOOD, 'Lawful Good'),
        (NEUTRAL_GOOD, 'Nuetral Good'),
        (CHAOTIC_GOOD, 'Chaotic Good'),
        (LAWFUL_NEUTRAL, 'Lawful Neutral'),
        (TRUE_NEUTRAL, 'True Neutral'),
        (CHAOTIC_NEUTRAL, 'Chaotic Neutral'),
        (LAWFUL_EVIL, 'Lawful Evil'),
        (NEUTRAL_EVIL, 'Neutral Evil'),
        (CHAOTIC_EVIL, 'Chaotic Evil'),
    )

    user = models.ForeignKey(GaeDatastoreUser, blank=True, null=True)
    users_with_access = fields.RelatedSetField(GaeDatastoreUser)

    # Char Details
    player_name = models.CharField(max_length=100, blank=True)
    character_name = models.CharField(max_length=100)
    background = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=200, blank=True)
    alignment = models.CharField(max_length=2, choices=ALIGNMENT_CHOICES, default=TRUE_NEUTRAL)
    experience_points = models.IntegerField(null=True, blank=True)
    max_hit_points = models.IntegerField(null=True, blank=True)
    current_hit_points = models.IntegerField(null=True, blank=True)
    temporary_hit_points = models.IntegerField(null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True, default=25)
    inspiration = models.IntegerField(null=True, blank=True)
    proficiency_bonus = models.IntegerField(null=True, blank=True)

    # Hit Dice
    hit_dice_total = models.IntegerField(null=True, blank=True)
    hit_dice = models.CharField(max_length=200, blank=True)

    # Death Saves - I may switch this to a many to many field, but for now
    # I don't think it's worth it.
    death_save_success_1 = models.BooleanField(default=False)
    death_save_success_2 = models.BooleanField(default=False)
    death_save_success_3 = models.BooleanField(default=False)
    death_save_failure_1 = models.BooleanField(default=False)
    death_save_failure_2 = models.BooleanField(default=False)
    death_save_failure_3 = models.BooleanField(default=False)

    # Char Description
    age = models.IntegerField(null=True, blank=True)
    height = models.CharField(max_length=200, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    eyes = models.CharField(max_length=200, blank=True)
    skin = models.CharField(max_length=200, blank=True)
    hair = models.CharField(max_length=200, blank=True)
    character_appearance = models.TextField(blank=True)
    character_backstory = models.TextField(blank=True)
    allies_and_organizations = models.TextField(blank=True)
    additional_features_and_traits = models.TextField(blank=True)

    treasure = models.TextField(blank=True) # Not sure if i want this to be a TextField

    # Main Stats
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)

    # Skills
    acrobatics = models.BooleanField(default=False)
    animal_handling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleight_of_hand = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)

    # Saving Throws
    strength_save = models.BooleanField(default=False)
    dexterity_save = models.BooleanField(default=False)
    constitution_save = models.BooleanField(default=False)
    intelligence_save = models.BooleanField(default=False)
    wisdom_save = models.BooleanField(default=False)
    charisma_save = models.BooleanField(default=False)

    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)

    features_and_traits = models.TextField(blank=True)
    other_proficiencies_and_languages = models.TextField(blank=True)

    # Spell Casting Saves
    spell_casting_class = models.CharField(max_length=50, blank=True)
    spellcasting_ability = models.CharField(max_length=50, blank=True)
    spell_save_dc = models.IntegerField(null=True, blank=True)
    spell_attack_bonus = models.IntegerField(null=True, blank=True)

    @property
    def strength_modifier(self):
        return (self.strength - 10) / 2

    @property
    def dexterity_modifier(self):
        return (self.dexterity - 10) / 2

    @property
    def constitution_modifier(self):
        return (self.constitution - 10) / 2

    @property
    def intelligence_modifier(self):
        return (self.intelligence - 10) / 2

    @property
    def wisdom_modifier(self):
        return (self.wisdom - 10) / 2

    @property
    def charisma_modifier(self):
        return (self.charisma - 10) / 2

    @property
    def strength_save_modifier(self):
        return mf(self.strength_save, self.strength_modifier, 2)

    @property
    def dexterity_save_modifier(self):
        return mf(self.dexterity_save, self.dexterity_modifier, 2)

    @property
    def constitution_save_modifier(self):
        return mf(self.constitution_save, self.constitution_modifier, 2)

    @property
    def intelligence_save_modifier(self):
        return mf(self.intelligence_save, self.intelligence_modifier, 2)

    @property
    def wisdom_save_modifier(self):
        return mf(self.wisdom_save, self.wisdom_modifier, 2)

    @property
    def charisma_save_modifier(self):
        return mf(self.charisma_save, self.charisma_modifier, 2)

    @property
    def acrobatics_modifier(self):
        return mf(self.acrobatics, self.dexterity_modifier, 2)

    @property
    def animal_handling_modifier(self):
        return mf(self.animal_handling, self.wisdom_modifier, 2)

    @property
    def arcana_modifier(self):
        return mf(self.arcana, self.intelligence_modifier, 2)

    @property
    def athletics_modifier(self):
        return mf(self.athletics, self.strength_modifier, 2)

    @property
    def deception_modifier(self):
        return mf(self.deception, self.charisma_modifier, 2)

    @property
    def history_modifier(self):
        return mf(self.history, self.intelligence_modifier, 2)

    @property
    def insight_modifier(self):
        return mf(self.insight, self.wisdom_modifier, 2)

    @property
    def intimidation_modifier(self):
        return mf(self.intimidation, self.charisma_modifier, 2)

    @property
    def investigation_modifier(self):
        return mf(self.investigation, self.intelligence_modifier, 2)

    @property
    def medicine_modifier(self):
        return mf(self.medicine, self.wisdom_modifier, 2)

    @property
    def nature_modifier(self):
        return mf(self.nature, self.intelligence_modifier, 2)

    @property
    def perception_modifier(self):
        return mf(self.perception, self.wisdom_modifier, 2)

    @property
    def performance_modifier(self):
        return mf(self.performance, self.charisma_modifier, 2)

    @property
    def persuasion_modifier(self):
        return mf(self.persuasion, self.charisma_modifier, 2)

    @property
    def religion_modifier(self):
        return mf(self.religion, self.intelligence_modifier, 2)

    @property
    def sleight_of_hand_modifier(self):
        return mf(self.sleight_of_hand, self.dexterity_modifier, 2)

    @property
    def stealth_modifier(self):
        return mf(self.stealth, self.dexterity_modifier, 2)

    @property
    def survival_modifier(self):
        return mf(self.survival, self.wisdom_modifier, 2)

    @property
    def initiative(self):
        return self.dexterity_modifier

    @property
    def passive_perception(self):
        return self.perception_modifier + 10

    def __str__(self):
        return self.character_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class CharacterClass(models.Model):
    """
    Character Class models, Many to One field for character classes
    """
    character = models.ForeignKey(Character)
    char_class = models.CharField(max_length=200)
    level = models.IntegerField(null=True, blank=True)

class Equipment(models.Model):
    character = models.ForeignKey(Character)
    value = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)

class AttacksAndSpellcasting(models.Model):
    character = models.ForeignKey(Character)
    attack = models.CharField(max_length=50)
    bonus = models.IntegerField(null=True, blank=True)
    damage = models.CharField(max_length=50)
    damage_type = models.CharField(max_length=50)

class Spells(models.Model):
    character = models.ForeignKey(Character)
    level_or_cantrip = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    prepared = models.BooleanField()
