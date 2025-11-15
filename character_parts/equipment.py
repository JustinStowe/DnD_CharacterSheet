"""
Equipment manager for Character: encapsulates logic for magic item bonuses.
"""

class EquipmentManager:
    """Manage equipped magic items and their bonuses.

    The manager references the Character instance and provides helper
    methods used across Character's calculations.
    """

    def __init__(self, character):
        self.character = character

    def get_equipment_bonus(self, bonus_type):
        """Return the highest bonus value for the given bonus_type among all equipped magic items."""
        bonuses = []
        for item in getattr(self.character, 'magic_items', []) or []:
            if item.get('equipped', False) and 'bonuses' in item:
                for bonus in item['bonuses']:
                    if bonus.get('type') == bonus_type:
                        bonuses.append(bonus.get('value', 0))
        return max(bonuses) if bonuses else 0

    def get_all_equipment_bonuses(self):
        """Return a dict mapping bonus_type -> highest bonus value for equipped items."""
        bonus_summary = {}
        for item in getattr(self.character, 'magic_items', []) or []:
            if item.get('equipped', False) and 'bonuses' in item:
                for bonus in item['bonuses']:
                    bonus_type = bonus.get('type')
                    bonus_value = bonus.get('value', 0)
                    if bonus_type not in bonus_summary or bonus_value > bonus_summary[bonus_type]:
                        bonus_summary[bonus_type] = bonus_value
        return bonus_summary
