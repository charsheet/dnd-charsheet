from django.contrib import admin

# Register your models here.
from .models import Character, CharacterClass, Spells, Equipment, AttacksAndSpellcasting, CharsheetAccess

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'id', 'player_name')

admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterClass)
admin.site.register(Equipment)
admin.site.register(Spells)
admin.site.register(AttacksAndSpellcasting)
admin.site.register(CharsheetAccess)
