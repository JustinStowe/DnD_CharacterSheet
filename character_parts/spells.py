"""
Spell management for Character: spell lists, slots, and spell DC calculations.
"""

from typing import List
 # Removed top-level import of SPELL_PROGRESSION

class SpellManager:
    def __init__(self, character):
        self.character = character

    def get_spellcasting_modifier(self):
        if self.character.spellcasting_ability == 'intelligence':
            return self.character.get_int_modifier()
        elif self.character.spellcasting_ability == 'wisdom':
            return self.character.get_wis_modifier()
        elif self.character.spellcasting_ability == 'charisma':
            return self.character.get_cha_modifier()
        return 0

    def get_spell_dc(self, spell_level):
        return 10 + spell_level + self.get_spellcasting_modifier()

    def get_bonus_spells(self, spell_level):
        if spell_level == 0:
            return 0
        modifier = self.get_spellcasting_modifier()
        if modifier < spell_level:
            return 0
        return 1 + ((modifier - spell_level) // 4)

    def get_base_spells_per_day(self, spell_level):
        # Import SPELL_PROGRESSION lazily to avoid circular import problems
        from character import SPELL_PROGRESSION
        if self.character.character_class not in SPELL_PROGRESSION:
            return 0
        class_progression = SPELL_PROGRESSION[self.character.character_class]
        if self.character.level not in class_progression:
            return 0
        level_spells = class_progression[self.character.level]
        return level_spells.get(spell_level, 0)

    def get_total_spells_per_day(self, spell_level):
        base = self.get_base_spells_per_day(spell_level)
        if base > 0:
            return base + self.get_bonus_spells(spell_level)
        return 0

    def update_spell_slots_from_class(self):
        for spell_level in range(10):
            self.character.spell_slots_max[spell_level] = self.get_total_spells_per_day(spell_level)

    def add_spell(self, name, level, school='', casting_time='', range_='',
                  components='', duration='', saving_throw='', spell_resistance='',
                  description='', reference='', prepared=False):
        self.character.spells.append({
            'name': name,
            'level': level,
            'school': school,
            'casting_time': casting_time,
            'range': range_,
            'components': components,
            'duration': duration,
            'saving_throw': saving_throw,
            'spell_resistance': spell_resistance,
            'description': description,
            'reference': reference,
            'prepared': prepared
        })

    def remove_spell(self, index):
        if 0 <= index < len(self.character.spells):
            self.character.spells.pop(index)

    def reset_spell_slots(self):
        for level in self.character.spell_slots_used:
            self.character.spell_slots_used[level] = 0
