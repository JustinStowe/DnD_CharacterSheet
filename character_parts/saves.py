"""
Save calculations encapsulation for Fortitude, Reflex, and Will saves.
"""

class SaveManager:
    def __init__(self, character):
        self.character = character

    def get_fortitude_save(self):
        magic_resistance = self.character.get_equipment_bonus('Resistance (All Saves)')
        base_save = self.character.fort_base + self.character.get_con_modifier() + self.character.fort_misc + magic_resistance

        # Divine Grace: Paladin adds Charisma modifier to all saves
        if self.character.has_class('Paladin') and self.character.get_class_level('Paladin') >= 2:
            base_save += max(0, self.character.get_cha_modifier())

        return base_save

    def get_reflex_save(self):
        magic_resistance = self.character.get_equipment_bonus('Resistance (All Saves)')
        base_save = self.character.ref_base + self.character.get_dex_modifier() + self.character.ref_misc + magic_resistance

        # Divine Grace: Paladin adds Cha modifier to all saves
        if self.character.has_class('Paladin') and self.character.get_class_level('Paladin') >= 2:
            base_save += max(0, self.character.get_cha_modifier())

        return base_save

    def get_will_save(self):
        magic_resistance = self.character.get_equipment_bonus('Resistance (All Saves)')

        if self.character.has_feat('Force of Personality'):
            ability_mod = self.character.get_cha_modifier()
        else:
            ability_mod = self.character.get_wis_modifier()

        base_save = self.character.will_base + ability_mod + self.character.will_misc + magic_resistance

        # Divine Grace: Paladin adds Cha modifier to all saves
        if self.character.has_class('Paladin') and self.character.get_class_level('Paladin') >= 2:
            base_save += max(0, self.character.get_cha_modifier())

        return base_save
