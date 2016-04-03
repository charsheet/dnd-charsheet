from django.contrib import admin

# Register your models here.
from .models import Character, CharacterClass, Spells, Equipment, AttacksAndSpellcasting

admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(Equipment)
admin.site.register(Spells)
admin.site.register(AttacksAndSpellcasting)
