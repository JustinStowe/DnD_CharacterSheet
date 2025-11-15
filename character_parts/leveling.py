"""
Leveling/HP manager for Character: sync hit dice, recalculate HP, manage level up and skill points.
"""

from Epic_levels.epic_levels import get_epic_xp_for_level

class LevelManager:
    """Encapsulate logic for level-based operations and HP calculations.

    This manager manipulates the Character's fields and keeps the logic
    related to leveling isolated.
    """

    def __init__(self, character):
        self.character = character

    def sync_hit_dice_with_levels(self):
        """Ensure hit_dice list matches total character level"""
        converted_dice = []
        for hit_die_data in self.character.hit_dice:
            if isinstance(hit_die_data, tuple) and len(hit_die_data) == 2:
                converted_dice.append(hit_die_data)
            elif isinstance(hit_die_data, dict):
                die_size = hit_die_data.get('die', hit_die_data.get('die_size', 10))
                hp_roll = hit_die_data.get('roll', hit_die_data.get('hp_roll', (die_size // 2) + 1))
                converted_dice.append((die_size, hp_roll))
            elif isinstance(hit_die_data, (int, float)):
                die_size = int(hit_die_data)
                avg_hp = (die_size // 2) + 1
                converted_dice.append((die_size, avg_hp))
            else:
                converted_dice.append((10, 6))
        self.character.hit_dice = converted_dice

        total_level = self.character.get_total_level()
        current_dice_count = len(self.character.hit_dice)

        if current_dice_count < total_level:
            class_info = self.character.get_class_info()
            hit_die = class_info.get('hit_die', 10)
            for _ in range(total_level - current_dice_count):
                avg_hp = (hit_die // 2) + 1
                self.character.hit_dice.append((hit_die, avg_hp))

        elif current_dice_count > total_level:
            self.character.hit_dice = self.character.hit_dice[:total_level]

    def recalculate_hp(self):
        """Recalculate max HP based on hit dice and CON modifier"""
        total_hp = 0
        con_mod = self.character.get_con_modifier()

        for level_num, hit_die_data in enumerate(self.character.hit_dice, start=1):
            if isinstance(hit_die_data, tuple) and len(hit_die_data) == 2:
                die_size, hp_roll = hit_die_data
            elif isinstance(hit_die_data, dict):
                die_size = hit_die_data.get('die', hit_die_data.get('die_size', 10))
                hp_roll = hit_die_data.get('roll', hit_die_data.get('hp_roll', (die_size // 2) + 1))
            elif isinstance(hit_die_data, (int, float)):
                die_size = int(hit_die_data)
                hp_roll = (die_size // 2) + 1
            else:
                die_size = 10
                hp_roll = 6

            if level_num == 1:
                total_hp += max(1, die_size + con_mod)
            else:
                total_hp += max(1, hp_roll + con_mod)

        old_max = self.character.max_hp
        self.character.max_hp = total_hp

        if old_max > 0 and self.character.current_hp >= old_max:
            self.character.current_hp = self.character.max_hp
        elif self.character.current_hp > self.character.max_hp:
            self.character.current_hp = self.character.max_hp

    def recalculate_skill_points(self):
        """Recalculate total skill points available based on all class levels"""
        total_points = 0
        current_level = 0

        for class_info in self.character.classes:
            class_name = class_info['name']
            class_level = class_info['level']

            # Use Character.get_class_info() to support prestige classes, defaults, and avoid module-level
            # constant access from inside the LevelManager to prevent circular imports.
            class_def = self.character.get_class_info(class_name)

            base_skill_points = class_def.get('skill_points', 2)
            int_mod = self.character.get_int_modifier()
            points_per_level = max(1, base_skill_points + int_mod)

            for level in range(class_level):
                current_level += 1
                if current_level == 1:
                    total_points += points_per_level * 4
                else:
                    total_points += points_per_level

        spent_points = sum(self.character.skills.values())
        self.character.skill_points_available = total_points - spent_points

    def level_up(self, hp_roll=None):
        """
        Advance character to next level
        Returns a dict with level-up information
        """
        self.character.level += 1

        class_info = self.character.get_class_info()
        hit_die = class_info['hit_die']

        if hp_roll is None:
            hp_gain = (hit_die // 2) + 1
        else:
            hp_gain = max(1, hp_roll)

        hp_gain += self.character.get_con_modifier()
        hp_gain = max(1, hp_gain)

        self.character.max_hp += hp_gain
        self.character.current_hp = self.character.max_hp
        self.character.hit_dice.append((hit_die, hp_roll or hp_gain))

        self.character.update_class_based_stats()

        skill_points = self.character.get_skill_points_per_level()
        if self.character.level == 1:
            skill_points *= 4
        self.character.skill_points_available += skill_points

        self.character.next_level_xp = self.character.level * 1000

        return {
            'new_level': self.character.level,
            'hp_gain': hp_gain,
            'hit_die': hit_die,
            'skill_points': skill_points,
            'bab': self.character.base_attack_bonus,
            'fort': self.character.fort_base,
            'ref': self.character.ref_base,
            'will': self.character.will_base
        }
