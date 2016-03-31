from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Character(models.Model):
    character_name = models.CharField(max_length=100)
    char_class = models.CharField()
    player_name = models.CharField(max_length=100)
    race = models.CharField()
    alignment = models.CharField()
    experience_points = models.IntegerField()


class Character_Class(models.Model):
    char_class = models.CharField()
    level = models.IntegerField()
    character = models.ForeignKey(Character)
