"""
Ability modifiers computations encapsulation.
"""

class AbilityManager:
    """Compute ability modifiers including temporary mods and equipment bonuses.

    This manager references the Character to access base scores, temp modifiers,
    and uses `Character.get_equipment_bonus` to incorporate equipment bonuses.
    """

    def __init__(self, character):
        self.character = character

    def get_ability_modifier(self, ability_score):
        return (ability_score - 10) // 2

    def _get_total_for_ability(self, ability_name, base_attr, temp_attr, equipment_key):
        base_value = getattr(self.character, base_attr, 0)
        temp_mod = getattr(self.character, temp_attr, 0)
        equip_bonus = self.character.get_equipment_bonus(equipment_key)
        return base_value + temp_mod + equip_bonus

    def get_str_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('strength', 'strength', 'str_temp_mod', 'Strength'))

    def get_dex_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('dexterity', 'dexterity', 'dex_temp_mod', 'Dexterity'))

    def get_con_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('constitution', 'constitution', 'con_temp_mod', 'Constitution'))

    def get_int_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('intelligence', 'intelligence', 'int_temp_mod', 'Intelligence'))

    def get_wis_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('wisdom', 'wisdom', 'wis_temp_mod', 'Wisdom'))

    def get_cha_modifier(self):
        return self.get_ability_modifier(self._get_total_for_ability('charisma', 'charisma', 'cha_temp_mod', 'Charisma'))
