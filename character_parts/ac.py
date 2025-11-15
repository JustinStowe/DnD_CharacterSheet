"""
AC (Armor Class) manager encapsulates the logic for AC calculations.
"""

class ACManager:
    def __init__(self, character):
        self.character = character

    def get_ac(self):
        """Calculate total Armor Class"""
        magic_armor = self.character.get_equipment_bonus('Armor')
        magic_shield = self.character.get_equipment_bonus('Shield')
        magic_natural = self.character.get_equipment_bonus('Natural Armor')
        magic_deflection = self.character.get_equipment_bonus('Deflection')

        return (10 + self.character.armor_bonus + magic_armor +
                self.character.shield_bonus + magic_shield +
                self.character.get_dex_modifier() +
                self.character.natural_armor + magic_natural +
                self.character.deflection_bonus + magic_deflection +
                self.character.misc_ac_bonus)

    def get_touch_ac(self):
        """Calculate Touch AC (no armor/shield/natural)"""
        magic_deflection = self.character.get_equipment_bonus('Deflection')
        return (10 + self.character.get_dex_modifier() +
                self.character.deflection_bonus + magic_deflection +
                self.character.misc_ac_bonus)

    def get_flat_footed_ac(self):
        """Calculate Flat-footed AC (no dex bonus)"""
        magic_armor = self.character.get_equipment_bonus('Armor')
        magic_shield = self.character.get_equipment_bonus('Shield')
        magic_natural = self.character.get_equipment_bonus('Natural Armor')
        magic_deflection = self.character.get_equipment_bonus('Deflection')

        return (10 + self.character.armor_bonus + magic_armor +
                self.character.shield_bonus + magic_shield +
                self.character.natural_armor + magic_natural +
                self.character.deflection_bonus + magic_deflection +
                self.character.misc_ac_bonus)

    def get_initiative(self):
        """Calculate initiative"""
        return self.character.get_dex_modifier() + self.character.initiative_misc
