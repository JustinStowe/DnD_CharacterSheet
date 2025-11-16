"""
D&D 3rd Edition Character Model
Handles all character statistics and automatic calculations
"""

from prestige_classes.prestige_classes import (
    PRESTIGE_CLASS_DEFINITIONS, 
    check_prestige_class_requirements,
    get_prestige_class_info,
    is_prestige_class
)
from Epic_levels.epic_levels import (
    is_epic_level,
    get_epic_level_info,
    get_epic_bab_bonus,
    get_epic_save_bonus,
    calculate_epic_skill_max_ranks,
    get_epic_xp_for_level,
    get_epic_feat_progression,
    get_all_epic_feats,
    check_epic_feat_prerequisites
)
from character_parts.equipment import EquipmentManager
from character_parts.abilities import AbilityManager
from character_parts.saves import SaveManager
from character_parts.ac import ACManager
from character_parts.leveling import LevelManager
from character_parts.feats import FeatManager
from character_parts.spells import SpellManager
from character_parts.ac import ACManager
from character_parts.leveling import LevelManager

# D&D 3e Class definitions
CLASS_DEFINITIONS = {
    'Fighter': {
        'hit_die': 10,
        'bab_progression': 'full',  # BAB = level
        'fort_progression': 'good',  # 2 + level/2
        'ref_progression': 'poor',   # 0 + level/3
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None
    },
    'Barbarian': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None
    },
    'Ranger': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 6,
        'spellcasting_ability': 'wisdom'
    },
    'Paladin': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': 'wisdom'
    },
    'Cleric': {
        'hit_die': 8,
        'bab_progression': 'medium',  # BAB = level * 3/4
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'wisdom'
    },
    'Druid': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'wisdom'
    },
    'Monk': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None
    },
    'Rogue': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 8,
        'spellcasting_ability': None
    },
    'Bard': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 6,
        'spellcasting_ability': 'charisma'
    },
    'Wizard': {
        'hit_die': 4,
        'bab_progression': 'poor',  # BAB = level/2
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'intelligence'
    },
    'Sorcerer': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'charisma'
    }
}

# Spells per day by class and level (D&D 3e)
# Format: {level: {spell_level: spells_per_day}}
SPELL_PROGRESSION = {
    'Bard': {
        1: {0: 2, 1: 0},
        2: {0: 3, 1: 1},
        3: {0: 3, 1: 2},
        4: {0: 3, 1: 3, 2: 0},
        5: {0: 3, 1: 3, 2: 1},
        6: {0: 3, 1: 3, 2: 2},
        7: {0: 3, 1: 3, 2: 3, 3: 0},
        8: {0: 3, 1: 3, 2: 3, 3: 1},
        9: {0: 3, 1: 3, 2: 3, 3: 2},
        10: {0: 3, 1: 3, 2: 3, 3: 3, 4: 0},
        11: {0: 3, 1: 3, 2: 3, 3: 3, 4: 1},
        12: {0: 3, 1: 3, 2: 3, 3: 3, 4: 2},
        13: {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 0},
        14: {0: 4, 1: 3, 2: 3, 3: 3, 4: 3, 5: 1},
        15: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
        16: {0: 4, 1: 4, 2: 4, 3: 3, 4: 3, 5: 3, 6: 0},
        17: {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 1},
        18: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 3, 6: 2},
        19: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 3},
        20: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4}
    },
    'Cleric': {
        1: {0: 3, 1: 1},
        2: {0: 4, 1: 2},
        3: {0: 4, 1: 2, 2: 1},
        4: {0: 5, 1: 3, 2: 2},
        5: {0: 5, 1: 3, 2: 2, 3: 1},
        6: {0: 5, 1: 3, 2: 3, 3: 2},
        7: {0: 6, 1: 4, 2: 3, 3: 2, 4: 1},
        8: {0: 6, 1: 4, 2: 3, 3: 3, 4: 2},
        9: {0: 6, 1: 4, 2: 4, 3: 3, 4: 2, 5: 1},
        10: {0: 6, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2},
        11: {0: 6, 1: 5, 2: 4, 3: 4, 4: 3, 5: 2, 6: 1},
        12: {0: 6, 1: 5, 2: 4, 3: 4, 4: 3, 5: 3, 6: 2},
        13: {0: 6, 1: 5, 2: 5, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1},
        14: {0: 6, 1: 5, 2: 5, 3: 4, 4: 4, 5: 3, 6: 3, 7: 2},
        15: {0: 6, 1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 2, 8: 1},
        16: {0: 6, 1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 3, 8: 2},
        17: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 4, 6: 4, 7: 3, 8: 2, 9: 1},
        18: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 4, 6: 4, 7: 3, 8: 3, 9: 2},
        19: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 3, 9: 3},
        20: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 4, 9: 4}
    },
    'Druid': {
        1: {0: 3, 1: 1},
        2: {0: 4, 1: 2},
        3: {0: 4, 1: 2, 2: 1},
        4: {0: 5, 1: 3, 2: 2},
        5: {0: 5, 1: 3, 2: 2, 3: 1},
        6: {0: 5, 1: 3, 2: 3, 3: 2},
        7: {0: 6, 1: 4, 2: 3, 3: 2, 4: 1},
        8: {0: 6, 1: 4, 2: 3, 3: 3, 4: 2},
        9: {0: 6, 1: 4, 2: 4, 3: 3, 4: 2, 5: 1},
        10: {0: 6, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2},
        11: {0: 6, 1: 5, 2: 4, 3: 4, 4: 3, 5: 2, 6: 1},
        12: {0: 6, 1: 5, 2: 4, 3: 4, 4: 3, 5: 3, 6: 2},
        13: {0: 6, 1: 5, 2: 5, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1},
        14: {0: 6, 1: 5, 2: 5, 3: 4, 4: 4, 5: 3, 6: 3, 7: 2},
        15: {0: 6, 1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 2, 8: 1},
        16: {0: 6, 1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 3, 8: 2},
        17: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 4, 6: 4, 7: 3, 8: 2, 9: 1},
        18: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 4, 6: 4, 7: 3, 8: 3, 9: 2},
        19: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 3, 9: 3},
        20: {0: 6, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 4, 9: 4}
    },
    'Paladin': {
        1: {0: 0},
        2: {0: 0},
        3: {0: 0},
        4: {0: 0, 1: 0},
        5: {0: 0, 1: 0},
        6: {0: 0, 1: 1},
        7: {0: 0, 1: 1},
        8: {0: 0, 1: 1, 2: 0},
        9: {0: 0, 1: 1, 2: 0},
        10: {0: 0, 1: 1, 2: 1},
        11: {0: 0, 1: 1, 2: 1, 3: 0},
        12: {0: 0, 1: 1, 2: 1, 3: 0},
        13: {0: 0, 1: 1, 2: 1, 3: 1},
        14: {0: 0, 1: 2, 2: 1, 3: 1, 4: 0},
        15: {0: 0, 1: 2, 2: 1, 3: 1, 4: 0},
        16: {0: 0, 1: 2, 2: 2, 3: 1, 4: 1},
        17: {0: 0, 1: 2, 2: 2, 3: 2, 4: 1},
        18: {0: 0, 1: 3, 2: 2, 3: 2, 4: 1},
        19: {0: 0, 1: 3, 2: 3, 3: 3, 4: 2},
        20: {0: 0, 1: 3, 2: 3, 3: 3, 4: 3}
    },
    'Ranger': {
        1: {0: 0},
        2: {0: 0},
        3: {0: 0},
        4: {0: 0, 1: 0},
        5: {0: 0, 1: 0},
        6: {0: 0, 1: 1},
        7: {0: 0, 1: 1},
        8: {0: 0, 1: 1, 2: 0},
        9: {0: 0, 1: 1, 2: 0},
        10: {0: 0, 1: 1, 2: 1},
        11: {0: 0, 1: 1, 2: 1, 3: 0},
        12: {0: 0, 1: 1, 2: 1, 3: 0},
        13: {0: 0, 1: 1, 2: 1, 3: 1},
        14: {0: 0, 1: 2, 2: 1, 3: 1, 4: 0},
        15: {0: 0, 1: 2, 2: 1, 3: 1, 4: 0},
        16: {0: 0, 1: 2, 2: 2, 3: 1, 4: 1},
        17: {0: 0, 1: 2, 2: 2, 3: 2, 4: 1},
        18: {0: 0, 1: 3, 2: 2, 3: 2, 4: 1},
        19: {0: 0, 1: 3, 2: 3, 3: 3, 4: 2},
        20: {0: 0, 1: 3, 2: 3, 3: 3, 4: 3}
    },
    'Sorcerer': {
        1: {0: 5, 1: 3},
        2: {0: 6, 1: 4},
        3: {0: 6, 1: 5},
        4: {0: 6, 1: 6, 2: 3},
        5: {0: 6, 1: 6, 2: 4},
        6: {0: 6, 1: 6, 2: 5, 3: 3},
        7: {0: 6, 1: 6, 2: 6, 3: 4},
        8: {0: 6, 1: 6, 2: 6, 3: 5, 4: 3},
        9: {0: 6, 1: 6, 2: 6, 3: 6, 4: 4},
        10: {0: 6, 1: 6, 2: 6, 3: 6, 4: 5, 5: 3},
        11: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 4},
        12: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 5, 6: 3},
        13: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 4},
        14: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 5, 7: 3},
        15: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 4},
        16: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 5, 8: 3},
        17: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 4},
        18: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 5, 9: 3},
        19: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 6, 9: 4},
        20: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 6, 9: 6}
    },
    'Wizard': {
        1: {0: 3, 1: 1},
        2: {0: 4, 1: 2},
        3: {0: 4, 1: 2, 2: 1},
        4: {0: 4, 1: 3, 2: 2},
        5: {0: 4, 1: 3, 2: 2, 3: 1},
        6: {0: 4, 1: 3, 2: 3, 3: 2},
        7: {0: 4, 1: 4, 2: 3, 3: 2, 4: 1},
        8: {0: 4, 1: 4, 2: 3, 3: 3, 4: 2},
        9: {0: 4, 1: 4, 2: 4, 3: 3, 4: 2, 5: 1},
        10: {0: 4, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2},
        11: {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 2, 6: 1},
        12: {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 2},
        13: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1},
        14: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 3, 6: 3, 7: 2},
        15: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 3, 7: 2, 8: 1},
        16: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 3, 7: 3, 8: 2},
        17: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 3, 8: 2, 9: 1},
        18: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 3, 8: 3, 9: 2},
        19: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 3, 9: 3},
        20: {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4}
    }
}


class Character:
    """Represents a D&D 3e character with auto-calculating stats"""
    
    def __init__(self):
        # Basic Info
        self.name = ""
        self.player = ""
        self.character_class = "Fighter"  # Primary class for backward compatibility
        self.level = 1  # Total character level
        self.race = ""
        self.alignment = ""
        self.deity = ""
        self.size = "Medium"
        self.age = 0
        self.gender = ""
        self.height = ""
        self.weight = ""
        self.hair_color = ""
        self.eye_color = ""
        
        # Multiclass support
        self.classes = [{'name': 'Fighter', 'level': 1}]  # List of {'name': str, 'level': int}
        
        # Level tracking
        self.experience = 0
        self.next_level_xp = 1000  # XP needed for level 2
        
        # Ability Scores (base values)
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        
        # Ability Score Modifiers (temporary)
        self.str_temp_mod = 0
        self.dex_temp_mod = 0
        self.con_temp_mod = 0
        self.int_temp_mod = 0
        self.wis_temp_mod = 0
        self.cha_temp_mod = 0
        
        # Hit Points
        self.max_hp = 0
        self.current_hp = 0
        self.hit_dice = []  # List of dice rolled for each level: [(die_size, roll), ...]
        
        # Armor Class modifiers
        self.armor_bonus = 0
        self.shield_bonus = 0
        self.natural_armor = 0
        self.deflection_bonus = 0
        self.misc_ac_bonus = 0
        
        # Saves (base modifiers from class/race/feats)
        self.fort_base = 2  # Good save starts at 2
        self.ref_base = 0
        self.will_base = 0
        self.fort_misc = 0
        self.ref_misc = 0
        self.will_misc = 0
        
        # Combat
        self.base_attack_bonus = 1  # Fighter starts at +1
        self.initiative_misc = 0
        self.spell_resistance = 0
        
        # Skills (only storing ranks, modifiers calculated)
        self.skill_points_available = 0  # Unspent skill points
        self.skills = {
            'Alchemy': 0,
            'Animal Empathy': 0,
            'Appraise': 0,
            'Balance': 0,
            'Bluff': 0,
            'Climb': 0,
            'Concentration': 0,
            'Craft': 0,
            'Decipher Script': 0,
            'Diplomacy': 0,
            'Disable Device': 0,
            'Disguise': 0,
            'Escape Artist': 0,
            'Forgery': 0,
            'Gather Information': 0,
            'Handle Animal': 0,
            'Heal': 0,
            'Hide': 0,
            'Innuendo': 0,
            'Intimidate': 0,
            'Jump': 0,
            'Knowledge (Arcana)': 0,
            'Knowledge (Religion)': 0,
            'Knowledge (Nature)': 0,
            'Knowledge (Planes)': 0,
            'Knowledge (Engineering)': 0,
            'Knowledge (Nobility & Royalty)': 0,
            'Knowledge (___________)': 0,
            'Listen': 0,
            'Move Silently': 0,
            'Open Lock': 0,
            'Perform': 0,
            'Profession': 0,
            'Ride': 0,
            'Search': 0,
            'Sense Motive': 0,
            'Sleight of Hand': 0,
            'Spellcraft': 0,
            'Spot': 0,
            'Survival': 0,
            'Swim': 0,
            'Tumble': 0,
            'Use Magic Device': 0,
            'Use Rope': 0,
            'Wilderness Lore': 0
        }
        
        # Skill ability mapping (which ability score affects each skill)
        self.skill_abilities = {
            'Alchemy': 'int',
            'Animal Empathy': 'cha',
            'Appraise': 'int',
            'Balance': 'dex',
            'Bluff': 'cha',
            'Climb': 'str',
            'Concentration': 'con',
            'Craft': 'int',
            'Decipher Script': 'int',
            'Diplomacy': 'cha',
            'Disable Device': 'int',
            'Disguise': 'cha',
            'Escape Artist': 'dex',
            'Forgery': 'int',
            'Gather Information': 'cha',
            'Handle Animal': 'cha',
            'Heal': 'wis',
            'Hide': 'dex',
            'Innuendo': 'wis',
            'Intimidate': 'cha',
            'Jump': 'str',
            'Knowledge (Arcana)': 'int',
            'Knowledge (Religion)': 'int',
            'Knowledge (Nature)': 'int',
            'Knowledge (Planes)': 'int',
            'Knowledge (Engineering)': 'int',
            'Knowledge (Nobility & Royalty)': 'int',
            'Knowledge (___________)': 'int',
            'Listen': 'wis',
            'Move Silently': 'dex',
            'Open Lock': 'dex',
            'Perform': 'cha',
            'Profession': 'cha',
            'Ride': 'dex',
            'Search': 'int',
            'Sense Motive': 'wis',
            'Sleight of Hand': 'dex',
            'Spellcraft': 'int',
            'Spot': 'wis',
            'Survival': 'wis',
            'Swim': 'str',
            'Tumble': 'dex',
            'Use Magic Device': 'cha',
            'Use Rope': 'dex',
            'Wilderness Lore' : 'wis'
        }
        
        # Skill misc modifiers
        self.skill_misc = {skill: 0 for skill in self.skills.keys()}
        
        # Inventory
        self.inventory = []  # List of dicts. For containers: {'name','weight','quantity','notes','is_container':bool,'capacity_lbs', 'count_contents_toward_carry', 'contents': [item,...]}
        
        # Currency (D&D 3e standard denominations)
        self.currency = {
            'platinum': 0,  # pp (1 pp = 10 gp)
            'gold': 0,      # gp (standard)
            'silver': 0,    # sp (10 sp = 1 gp)
            'copper': 0     # cp (100 cp = 1 gp)
        }
        
        # Spellcasting
        self.spellcasting_ability = 'intelligence'  # 'intelligence', 'wisdom', or 'charisma'
        self.spell_slots_max = {
            0: 0,  # Cantrips/Orisons
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        self.spell_slots_used = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        # Spell list: list of dicts with spell information
        self.spells = []
        # Each spell: {
        #   'name': str,
        #   'level': int,
        #   'school': str,
        #   'casting_time': str,
        #   'range': str,
        #   'components': str,
        #   'duration': str,
        #   'saving_throw': str,
        #   'spell_resistance': str,
        #   'description': str,
        #   'prepared': bool (for prepared casters)
        # }
        
        # Feats
        self.feats = []
        # Each feat: {
        #   'name': str,
        #   'type': str (General, Metamagic, Item Creation, etc.),
        #   'description': str,
        #   'prerequisites': str,
        #   'benefit': str
        # }
        
        # Special Abilities
        self.special_abilities = []
        # Each ability: {
        #   'name': str,
        #   'source': str (Racial, Class, Feat, etc.),
        #   'description': str,
        #   'uses_per_day': int (0 for at-will/passive),
        #   'uses_remaining': int
        # }
        
        # Weapons
        self.weapons = []
        # Each weapon: {
        #   'name': str,
        #   'type': str,  # 'melee' or 'ranged'
        #   'damage': str,  # e.g., '1d8', '2d6'
        #   'critical': str,  # e.g., '19-20/x2', 'x3'
        #   'range': str,  # e.g., '30 ft', 'melee'
        #   'damage_type': str,  # Slashing, Piercing, Bludgeoning, etc.
        #   'size': str,  # Fine, Diminutive, Tiny, Small, Medium, Large, etc.
        #   'weight': float,  # Weight in lbs
        #   'attack_bonus': int,  # Enhancement bonus (e.g., +1, +2)
        #   'misc_attack': int,  # Other attack bonuses
        #   'damage_bonus': int,  # Additional damage bonus beyond STR/DEX
        #   'notes': str
        # }
        
        # Magic Items
        self.magic_items = []
        # Each item: {
        #   'name': str,
        #   'type': str,  # Weapon, Armor, Ring, Wondrous, Potion, Scroll, Wand, Rod, Staff, etc.
        #   'slot': str,  # Head, Eyes, Neck, Shoulders, Body, Torso, Arms, Hands, Ring, Waist, Feet, None
        #   'caster_level': int,
        #   'description': str,
        #   'properties': str,  # Special abilities/bonuses
        #   'charges': int,  # For items with charges (0 for non-charged items)
        #   'max_charges': int
        # }
        
        # Epic Level Tracking
        self.epic_feats = []  # List of epic feat names
        self.epic_ability_increases = {  # Track which abilities have been increased at epic levels
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        }
        # Equipment manager (encapsulates equipment/magic item logic)
        self.equipment_manager = EquipmentManager(self)
        # Ability manager
        self.ability_manager = AbilityManager(self)
        # Save manager
        self.save_manager = SaveManager(self)
        # AC manager
        self.ac_manager = ACManager(self)
        # Leveling manager
        self.level_manager = LevelManager(self)
        # Feats Manager
        self.feat_manager = FeatManager(self)
        # Spells Manager
        self.spell_manager = SpellManager(self)
    
    def get_equipment_bonus(self, bonus_type):
        """Compatibility wrapper: delegate to equipment manager."""
        return self.equipment_manager.get_equipment_bonus(bonus_type)
    
    def get_all_equipment_bonuses(self):
        """Compatibility wrapper: delegate to equipment manager."""
        return self.equipment_manager.get_all_equipment_bonuses()
        
    def get_ability_modifier(self, ability_score):
        """Calculate ability modifier from score"""
        return self.ability_manager.get_ability_modifier(ability_score)
    
    def get_str_modifier(self):
        """Get Strength modifier"""
        return self.ability_manager.get_str_modifier()
    
    def get_dex_modifier(self):
        """Get Dexterity modifier"""
        return self.ability_manager.get_dex_modifier()
    
    def get_con_modifier(self):
        """Get Constitution modifier"""
        return self.ability_manager.get_con_modifier()
    
    def get_int_modifier(self):
        """Get Intelligence modifier"""
        return self.ability_manager.get_int_modifier()
    
    def get_wis_modifier(self):
        """Get Wisdom modifier"""
        return self.ability_manager.get_wis_modifier()
    
    def get_cha_modifier(self):
        """Get Charisma modifier"""
        return self.ability_manager.get_cha_modifier()
    
    def has_feat(self, feat_name):
        """Check if character has a specific feat (case-insensitive)"""
        return self.feat_manager.has_feat(feat_name)
    
    def has_class(self, class_name):
        """Check if character has levels in a specific class"""
        return self.get_class_level(class_name) > 0
    
    def has_special_ability(self, ability_name):
        """Check if character has a specific special ability (case-insensitive)"""
        ability_name_lower = ability_name.lower()
        return any(a['name'].lower() == ability_name_lower for a in self.special_abilities)
    
    def get_fortitude_save(self):
        """Calculate total Fortitude save"""
        return self.save_manager.get_fortitude_save()
    
    def get_reflex_save(self):
        """Calculate total Reflex save"""
        return self.save_manager.get_reflex_save()
    
    def get_will_save(self):
        """Calculate total Will save"""
        return self.save_manager.get_will_save()
    
    def get_ac(self):
        """Calculate total Armor Class"""
        return self.ac_manager.get_ac()
    
    def get_touch_ac(self):
        return self.ac_manager.get_touch_ac()
    
    def get_flat_footed_ac(self):
        return self.ac_manager.get_flat_footed_ac()
    
    def get_initiative(self):
        """Calculate initiative"""
        return self.ac_manager.get_initiative()
    
    def get_skill_total(self, skill_name):
        """Calculate total skill bonus"""
        if skill_name not in self.skills:
            return 0
        
        ranks = self.skills[skill_name]
        ability = self.skill_abilities[skill_name]
        
        # Get the appropriate ability modifier
        if ability == 'str':
            ability_mod = self.get_str_modifier()
        elif ability == 'dex':
            ability_mod = self.get_dex_modifier()
        elif ability == 'con':
            ability_mod = self.get_con_modifier()
        elif ability == 'int':
            ability_mod = self.get_int_modifier()
        elif ability == 'wis':
            ability_mod = self.get_wis_modifier()
        elif ability == 'cha':
            ability_mod = self.get_cha_modifier()
        else:
            ability_mod = 0
        
        misc = self.skill_misc.get(skill_name, 0)
        
        return ranks + ability_mod + misc
    
    def get_total_level(self):
        """Calculate total character level from all classes"""
        return sum(c['level'] for c in self.classes)
    
    def get_class_level(self, class_name):
        """Get the level in a specific class"""
        for c in self.classes:
            if c['name'] == class_name:
                return c['level']
        return 0
    
    def add_class(self, class_name, level=1):
        """Add a new class or increase level in existing class"""
        for c in self.classes:
            if c['name'] == class_name:
                c['level'] += level
                return
        self.classes.append({'name': class_name, 'level': level})
        # Update primary class for backward compatibility
        if not hasattr(self, 'character_class') or not self.character_class:
            self.character_class = self.classes[0]['name']
    
    def remove_class(self, class_name):
        """Remove a class entirely"""
        self.classes = [c for c in self.classes if c['name'] != class_name]
        if not self.classes:  # Always have at least one class
            self.classes = [{'name': 'Fighter', 'level': 1}]
        # Update primary class for backward compatibility
        self.character_class = self.classes[0]['name'] if self.classes else 'Fighter'
    
    def get_class_info(self, class_name=None):
        """
        Get class information from CLASS_DEFINITIONS or PRESTIGE_CLASS_DEFINITIONS
        If no class_name provided, uses primary class
        """
        if class_name is None:
            class_name = self.character_class
        
        # Check prestige classes first
        if is_prestige_class(class_name):
            return get_prestige_class_info(class_name)
        
        # Otherwise check base classes
        return CLASS_DEFINITIONS.get(class_name, CLASS_DEFINITIONS['Fighter'])
    
    def check_prestige_requirements(self, prestige_class_name):
        """
        Check if character meets requirements for a prestige class.
        Returns (eligible, list of requirements/unmet requirements)
        """
        return check_prestige_class_requirements(self, prestige_class_name)
    
    def get_base_attack_bonus_from_class(self):
        """Calculate BAB based on all classes (multiclass stacking, including prestige and epic levels)"""
        total_bab = 0
        for class_entry in self.classes:
            class_name = class_entry['name']
            class_level = class_entry['level']
            
            # Get class info (works for both base and prestige classes)
            class_info = self.get_class_info(class_name)
            progression = class_info['bab_progression']
            
            # Calculate BAB for levels 1-20
            standard_level = min(class_level, 20)
            
            if progression == 'full':
                total_bab += standard_level
            elif progression == 'medium':
                total_bab += (standard_level * 3) // 4
            else:  # poor
                total_bab += standard_level // 2
            
            # Add epic BAB for levels 21+
            if class_level > 20:
                epic_levels = class_level - 20
                total_bab += get_epic_bab_bonus(class_name, epic_levels)
        
        return total_bab
    
    def get_base_save_from_class(self, save_type):
        """Calculate base save bonus from all classes (multiclass stacking, including prestige and epic levels)
        Args:
            save_type: 'fort', 'ref', or 'will'
        """
        total_save = 0
        for class_entry in self.classes:
            class_name = class_entry['name']
            class_level = class_entry['level']
            
            # Get class info (works for both base and prestige classes)
            class_info = self.get_class_info(class_name)
            progression_key = f'{save_type}_progression'
            progression = class_info[progression_key]
            
            # Calculate saves for levels 1-20
            standard_level = min(class_level, 20)
            
            if progression == 'good':
                total_save += 2 + (standard_level // 2)
            else:  # poor
                total_save += standard_level // 3
            
            # Add epic save bonus for levels 21+
            if class_level > 20:
                epic_levels = class_level - 20
                total_save += get_epic_save_bonus(progression, epic_levels)
        
        return total_save
    
    def sync_hit_dice_with_levels(self):
        # Delegate to the LevelManager
        return self.level_manager.sync_hit_dice_with_levels()
    
    def recalculate_hp(self):
        return self.level_manager.recalculate_hp()
    
    def recalculate_skill_points(self):
        return self.level_manager.recalculate_skill_points()
    
    def update_class_based_stats(self):
        """Update BAB and saves based on current classes and levels"""
        # Update total level
        self.level = self.get_total_level()
        
        # Sync hit dice with current level and recalculate HP
        self.sync_hit_dice_with_levels()
        self.recalculate_hp()
        
        # Calculate multiclass BAB and saves
        self.base_attack_bonus = self.get_base_attack_bonus_from_class()
        self.fort_base = self.get_base_save_from_class('fort')
        self.ref_base = self.get_base_save_from_class('ref')
        self.will_base = self.get_base_save_from_class('will')
        
        # Update spellcasting ability based on primary class
        class_info = self.get_class_info()
        if class_info['spellcasting_ability']:
            self.spellcasting_ability = class_info['spellcasting_ability']
        
        # Recalculate skill points
        self.recalculate_skill_points()
    
    def get_skill_points_per_level(self):
        """Calculate skill points gained per level"""
        class_info = self.get_class_info()
        base_points = class_info['skill_points']
        int_mod = self.get_int_modifier()
        
        # Minimum 1 skill point per level
        return max(1, base_points + int_mod)
    
    def level_up(self, hp_roll=None):
        """
        Advance character to next level
        Args:
            hp_roll: Optional HP roll (if None, will use average)
        Returns:
            dict with level-up information
        """
        return self.level_manager.level_up(hp_roll)
    
    def get_melee_attack_bonus(self):
        """Calculate melee attack bonus"""
        return self.base_attack_bonus + self.get_str_modifier()
    
    def get_ranged_attack_bonus(self):
        """Calculate ranged attack bonus"""
        return self.base_attack_bonus + self.get_dex_modifier()
    
    def get_carrying_capacity(self):
        """
        Calculate carrying capacity based on Strength score (D&D 3e rules)
        Returns: dict with 'light', 'medium', 'heavy', 'max' in pounds
        """
        str_score = self.strength + self.str_temp_mod
        
        # Base carrying capacity table (for Medium size creatures)
        if str_score <= 10:
            base_values = {1: 3, 2: 6, 3: 10, 4: 13, 5: 16, 6: 20, 7: 23, 8: 26, 9: 30, 10: 33}
            light = base_values.get(str_score, 33)
        elif str_score <= 20:
            # For STR 11-20, use formula
            base_values = {11: 38, 12: 43, 13: 50, 14: 58, 15: 66, 16: 76, 17: 86, 18: 100, 19: 116, 20: 133}
            light = base_values.get(str_score, 133)
        elif str_score <= 29:
            # For STR 21-29
            base_values = {21: 153, 22: 173, 23: 200, 24: 233, 25: 266, 26: 306, 27: 346, 28: 400, 29: 466}
            light = base_values.get(str_score, 466)
        else:
            # For very high strength, use progression
            base = 466
            multiplier = 4
            for s in range(30, str_score + 1):
                if s % 10 == 0:
                    multiplier *= 4
                base = int(base * 1.5) if s % 5 == 0 else base
            light = base
        
        # Calculate load ranges
        medium = light * 2
        heavy = light * 3
        max_load = light * 3  # Maximum load = heavy load limit
        
        return {
            'light': light,
            'medium': medium,
            'heavy': heavy,
            'max': max_load
        }
    
    def get_total_weight_carried(self):
        """Calculate total weight of all items in inventory, honoring container content counting rules."""
        total = 0
        for item in self.inventory:
            base_weight = item.get('weight', 0) * item.get('quantity', 1)
            total += base_weight
            if item.get('is_container') and item.get('contents'):
                # Sum contents weight
                contents_weight = sum(c.get('weight', 0) * c.get('quantity', 1) for c in item.get('contents', []))
                # Add contents weight only if the container has the flag set
                if item.get('count_contents_toward_carry', True):
                    total += contents_weight
        return total
    
    def get_current_load(self):
        """
        Determine current encumbrance level
        Returns: 'light', 'medium', 'heavy', or 'overloaded'
        """
        weight = self.get_total_weight_carried()
        capacity = self.get_carrying_capacity()
        
        if weight <= capacity['light']:
            return 'light'
        elif weight <= capacity['medium']:
            return 'medium'
        elif weight <= capacity['heavy']:
            return 'heavy'
        else:
            return 'overloaded'
    
    def get_encumbrance_penalties(self):
        """
        Get encumbrance penalties based on current load
        Returns: dict with 'max_dex', 'check_penalty', 'speed_reduction'
        """
        load = self.get_current_load()
        
        if load == 'light':
            return {'max_dex': None, 'check_penalty': 0, 'speed_reduction': 0}
        elif load == 'medium':
            return {'max_dex': 3, 'check_penalty': -3, 'speed_reduction': 10}
        elif load == 'heavy':
            return {'max_dex': 1, 'check_penalty': -6, 'speed_reduction': 10}
        else:  # overloaded
            return {'max_dex': 0, 'check_penalty': -6, 'speed_reduction': 10}
    
    def add_item(self, name, weight, quantity=1, notes='', is_container=False, capacity_lbs=0.0, count_contents_toward_carry=True, contents=None):
        """Add an item to inventory. If `is_container` is True, you can provide `capacity_lbs` and `contents` (list of inventory dicts)."""
        item = {
            'name': name,
            'weight': weight,
            'quantity': quantity,
            'notes': notes
        }
        if is_container:
            item['is_container'] = True
            item['capacity_lbs'] = float(capacity_lbs or 0)
            item['count_contents_toward_carry'] = bool(count_contents_toward_carry)
            item['contents'] = contents.copy() if contents else []
        self.inventory.append(item)
    
    def remove_item(self, index):
        """Remove an item from inventory by index"""
        if 0 <= index < len(self.inventory):
            self.inventory.pop(index)
    
    def get_spellcasting_modifier(self):
        """Get the modifier for the spellcasting ability"""
        if self.spellcasting_ability == 'intelligence':
            return self.get_int_modifier()
        elif self.spellcasting_ability == 'wisdom':
            return self.get_wis_modifier()
        elif self.spellcasting_ability == 'charisma':
            return self.get_cha_modifier()
        return 0
    
    def get_spell_dc(self, spell_level):
        """Calculate spell save DC for a given spell level"""
        return 10 + spell_level + self.get_spellcasting_modifier()
    
    def get_bonus_spells(self, spell_level):
        """
        Calculate bonus spells per day for a given spell level based on ability modifier
        Bonus spells are granted if: ability modifier >= spell level
        Number of bonus spells = 1 + ((ability modifier - spell level) // 4)
        """
        if spell_level == 0:
            return 0  # No bonus spells for cantrips/orisons
        
        modifier = self.get_spellcasting_modifier()
        
        # Must have high enough ability score to cast spells of this level
        # (ability score must be at least 10 + spell level)
        if modifier < spell_level:
            return 0
        
        # Calculate bonus spells: 1 + (modifier - spell_level) // 4
        # Examples: 
        #   1st level spell, 16 ability (+3): 1 + (3-1)//4 = 1 + 0 = 1 bonus spell
        #   1st level spell, 18 ability (+4): 1 + (4-1)//4 = 1 + 0 = 1 bonus spell
        #   1st level spell, 20 ability (+5): 1 + (5-1)//4 = 1 + 1 = 2 bonus spells
        #   2nd level spell, 16 ability (+3): 1 + (3-2)//4 = 1 + 0 = 1 bonus spell
        bonus = 1 + ((modifier - spell_level) // 4)
        return bonus
    
    def get_base_spells_per_day(self, spell_level):
        """
        Get base spells per day for a given spell level from class progression table
        Returns 0 if class doesn't cast spells or level is too low
        """
        # Check if class has spellcasting
        if self.character_class not in SPELL_PROGRESSION:
            return 0
        
        # Get progression for this class
        class_progression = SPELL_PROGRESSION[self.character_class]
        
        # Check if character level is in the table
        if self.level not in class_progression:
            return 0
        
        # Get spells for this spell level
        level_spells = class_progression[self.level]
        return level_spells.get(spell_level, 0)
    
    def get_total_spells_per_day(self, spell_level):
        """
        Calculate total spells per day (base + bonus) for a given spell level
        """
        base = self.get_base_spells_per_day(spell_level)
        
        # Only add bonus spells if character can actually cast this spell level
        if base > 0:
            bonus = self.get_bonus_spells(spell_level)
            return base + bonus
        
        return 0
    
    def update_spell_slots_from_class(self):
        """
        Update all spell slots based on current class, level, and ability scores
        """
        for spell_level in range(10):
            self.spell_slots_max[spell_level] = self.get_total_spells_per_day(spell_level)
    
    def add_spell(self, name, level, school='', casting_time='', range_='', 
                  components='', duration='', saving_throw='', spell_resistance='', 
                  description='', reference='', prepared=False):
        """Add a spell to the spell list"""
        return self.spell_manager.add_spell(name=name, level=level, school=school, casting_time=casting_time, range_=range_, components=components, duration=duration, saving_throw=saving_throw, spell_resistance=spell_resistance, description=description, reference=reference, prepared=prepared)
    
    def remove_spell(self, index):
        """Remove a spell from the spell list by index"""
        return self.spell_manager.remove_spell(index)
    
    def reset_spell_slots(self):
        """Reset all used spell slots to 0 (for resting)"""
        for level in self.spell_slots_used:
            self.spell_slots_used[level] = 0
    
    def add_feat(self, name, feat_type='General', description='', prerequisites='', benefit=''):
        return self.feat_manager.add_feat(name, feat_type, description, prerequisites, benefit)
    
    def remove_feat(self, index):
        return self.feat_manager.remove_feat(index)
    
    def add_special_ability(self, name, source='Class', description='', uses_per_day=0):
        """Add a special ability"""
        self.special_abilities.append({
            'name': name,
            'source': source,
            'description': description,
            'uses_per_day': uses_per_day,
            'uses_remaining': uses_per_day
        })
    
    def remove_special_ability(self, index):
        """Remove a special ability by index"""
        if 0 <= index < len(self.special_abilities):
            self.special_abilities.pop(index)
    
    def use_special_ability(self, index):
        """Use one charge of a special ability"""
        if 0 <= index < len(self.special_abilities):
            ability = self.special_abilities[index]
            if ability['uses_remaining'] > 0:
                ability['uses_remaining'] -= 1
                return True
        return False
    
    def reset_special_abilities(self):
        """Reset all special ability uses (for resting)"""
        for ability in self.special_abilities:
            ability['uses_remaining'] = ability['uses_per_day']
    
    def to_dict(self):
        """Convert character to dictionary for saving"""
        # Get primary class for backward compatibility
        primary_class = self.classes[0]['name'] if self.classes else 'Fighter'
        
        return {
            # Basic Info
            'name': self.name,
            'player': self.player,
            'character_class': primary_class,
            'level': self.level,
            'race': self.race,
            'alignment': self.alignment,
            'deity': self.deity,
            'size': self.size,
            'age': self.age,
            'gender': self.gender,
            'height': self.height,
            'weight': self.weight,
            'hair_color': self.hair_color,
            'eye_color': self.eye_color,
            
            # Multiclass
            'classes': self.classes.copy() if hasattr(self, 'classes') else [{'name': primary_class, 'level': self.level}],
            
            # Leveling
            'experience': self.experience,
            'next_level_xp': self.next_level_xp,
            'hit_dice': self.hit_dice,
            
            # Ability Scores
            'strength': self.strength,
            'dexterity': self.dexterity,
            'constitution': self.constitution,
            'intelligence': self.intelligence,
            'wisdom': self.wisdom,
            'charisma': self.charisma,
            
            # Ability Score Modifiers
            'str_temp_mod': self.str_temp_mod,
            'dex_temp_mod': self.dex_temp_mod,
            'con_temp_mod': self.con_temp_mod,
            'int_temp_mod': self.int_temp_mod,
            'wis_temp_mod': self.wis_temp_mod,
            'cha_temp_mod': self.cha_temp_mod,
            
            # Hit Points
            'max_hp': self.max_hp,
            'current_hp': self.current_hp,
            
            # Skills
            'skill_points_available': self.skill_points_available,
            
            # Armor Class
            'armor_bonus': self.armor_bonus,
            'shield_bonus': self.shield_bonus,
            'natural_armor': self.natural_armor,
            'deflection_bonus': self.deflection_bonus,
            'misc_ac_bonus': self.misc_ac_bonus,
            
            # Saves
            'fort_base': self.fort_base,
            'ref_base': self.ref_base,
            'will_base': self.will_base,
            'fort_misc': self.fort_misc,
            'ref_misc': self.ref_misc,
            'will_misc': self.will_misc,
            
            # Combat
            'base_attack_bonus': self.base_attack_bonus,
            'initiative_misc': self.initiative_misc,
            'spell_resistance': self.spell_resistance,
            
            # Skills
            'skills': self.skills.copy(),
            'skill_misc': self.skill_misc.copy(),
            
            # Inventory
            'inventory': self.inventory.copy(),
            
            # Currency
            'currency': self.currency.copy() if hasattr(self, 'currency') else {
                'platinum': 0, 'gold': 0, 'silver': 0, 'copper': 0
            },
            
            # Spellcasting
            'spellcasting_ability': self.spellcasting_ability,
            'spell_slots_max': self.spell_slots_max.copy(),
            'spell_slots_used': self.spell_slots_used.copy(),
            'spells': self.spells.copy(),
            
            # Feats and Special Abilities
            'feats': self.feats.copy(),
            'special_abilities': self.special_abilities.copy(),
            
            # Weapons and Magic Items
            'weapons': self.weapons.copy(),
            'magic_items': self.magic_items.copy(),
            
            # Epic Level Data
            'epic_feats': self.epic_feats.copy() if hasattr(self, 'epic_feats') else [],
            'epic_ability_increases': self.epic_ability_increases.copy() if hasattr(self, 'epic_ability_increases') else {
                'strength': 0, 'dexterity': 0, 'constitution': 0,
                'intelligence': 0, 'wisdom': 0, 'charisma': 0
            }
        }
    
    def from_dict(self, data):
        """Load character from dictionary"""
        # Basic Info
        self.name = data.get('name', '')
        self.player = data.get('player', '')
        self.character_class = data.get('character_class', 'Fighter')
        self.level = data.get('level', 1)
        self.race = data.get('race', '')
        self.alignment = data.get('alignment', '')
        self.deity = data.get('deity', '')
        self.size = data.get('size', 'Medium')
        self.age = data.get('age', 0)
        self.gender = data.get('gender', '')
        self.height = data.get('height', '')
        self.weight = data.get('weight', '')
        self.hair_color = data.get('hair_color', '')
        self.eye_color = data.get('eye_color', '')
        
        # Multiclass - backward compatibility with old save files
        if 'classes' in data:
            self.classes = data['classes'].copy()
            # Update character_class to match primary class
            if self.classes:
                self.character_class = self.classes[0]['name']
        else:
            # Old save file format - convert to multiclass format
            self.classes = [{'name': self.character_class, 'level': self.level}]
        
        # Leveling
        self.experience = data.get('experience', 0)
        self.next_level_xp = data.get('next_level_xp', 1000)
        self.hit_dice = data.get('hit_dice', [])
        
        # Ability Scores
        self.strength = data.get('strength', 10)
        self.dexterity = data.get('dexterity', 10)
        self.constitution = data.get('constitution', 10)
        self.intelligence = data.get('intelligence', 10)
        self.wisdom = data.get('wisdom', 10)
        self.charisma = data.get('charisma', 10)
        
        # Ability Score Modifiers
        self.str_temp_mod = data.get('str_temp_mod', 0)
        self.dex_temp_mod = data.get('dex_temp_mod', 0)
        self.con_temp_mod = data.get('con_temp_mod', 0)
        self.int_temp_mod = data.get('int_temp_mod', 0)
        self.wis_temp_mod = data.get('wis_temp_mod', 0)
        self.cha_temp_mod = data.get('cha_temp_mod', 0)
        
        # Hit Points
        self.max_hp = data.get('max_hp', 0)
        self.current_hp = data.get('current_hp', 0)
        
        # Skills
        self.skill_points_available = data.get('skill_points_available', 0)
        
        # Armor Class
        self.armor_bonus = data.get('armor_bonus', 0)
        self.shield_bonus = data.get('shield_bonus', 0)
        self.natural_armor = data.get('natural_armor', 0)
        self.deflection_bonus = data.get('deflection_bonus', 0)
        self.misc_ac_bonus = data.get('misc_ac_bonus', 0)
        
        # Saves
        self.fort_base = data.get('fort_base', 0)
        self.ref_base = data.get('ref_base', 0)
        self.will_base = data.get('will_base', 0)
        self.fort_misc = data.get('fort_misc', 0)
        self.ref_misc = data.get('ref_misc', 0)
        self.will_misc = data.get('will_misc', 0)
        
        # Combat
        self.base_attack_bonus = data.get('base_attack_bonus', 0)
        self.initiative_misc = data.get('initiative_misc', 0)
        self.spell_resistance = data.get('spell_resistance', 0)
        
        # Skills
        if 'skills' in data:
            self.skills.update(data['skills'])
        if 'skill_misc' in data:
            self.skill_misc.update(data['skill_misc'])
        
        # Inventory
        self.inventory = data.get('inventory', [])
        
        # Currency - with backward compatibility for old save files
        if 'currency' in data:
            self.currency = data['currency'].copy()
        else:
            # Old save file - initialize with default currency
            self.currency = {
                'platinum': 0,
                'gold': 0,
                'silver': 0,
                'copper': 0
            }
        
        # Spellcasting
        self.spellcasting_ability = data.get('spellcasting_ability', 'intelligence')
        if 'spell_slots_max' in data:
            self.spell_slots_max.update(data['spell_slots_max'])
        if 'spell_slots_used' in data:
            self.spell_slots_used.update(data['spell_slots_used'])
        self.spells = data.get('spells', [])
        
        # Feats and Special Abilities
        self.feats = data.get('feats', [])
        self.special_abilities = data.get('special_abilities', [])
        
        # Weapons and Magic Items
        self.weapons = data.get('weapons', [])
        self.magic_items = data.get('magic_items', [])
        
        # Epic Level Data
        self.epic_feats = data.get('epic_feats', [])
        self.epic_ability_increases = data.get('epic_ability_increases', {
            'strength': 0, 'dexterity': 0, 'constitution': 0,
            'intelligence': 0, 'wisdom': 0, 'charisma': 0
        })
    
    # ===== EPIC LEVEL METHODS =====
    
    def is_epic_level(self):
        """Check if character is at epic level (21+)"""
        return is_epic_level(self.get_total_level())
    
    def get_epic_info(self):
        """Get comprehensive epic level information"""
        return self.feat_manager.get_epic_info()
    
    def get_max_skill_ranks(self):
        """Get maximum skill ranks (level + 3, works for epic levels too)"""
        return self.feat_manager.get_max_skill_ranks()
    
    def get_epic_feats_available(self):
        """Get number of epic feats character should have at current level"""
        return self.feat_manager.get_epic_feats_available()
    
    def add_epic_feat(self, feat_name):
        return self.feat_manager.add_epic_feat(feat_name)
    
    def remove_epic_feat(self, feat_name):
        return self.feat_manager.remove_epic_feat(feat_name)
    
    def check_epic_feat_requirements(self, feat_name):
        return self.feat_manager.check_epic_feat_requirements(feat_name)
    
    def get_all_epic_feats_list(self):
        return self.feat_manager.get_all_epic_feats_list()
    
    def apply_epic_ability_increase(self, ability_name):
        return self.feat_manager.apply_epic_ability_increase(ability_name)
    
    def update_xp_for_epic_level(self):
        return self.feat_manager.update_xp_for_epic_level()

