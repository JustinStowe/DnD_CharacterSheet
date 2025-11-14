"""

D&D 3rd Edition Prestige Classes from Complete Champion

Prestige classes for champions of good and righteous warriors

"""

COMPLETE_CHAMPION_PRESTIGE_CLASSES = {

    'Apostle of Peace': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any non-evil and peaceful',
            'skills': {'Diplomacy': 8, 'Knowledge (religion)': 4},
            'feats': ['Dodge'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Peaceful clerics dedicated to stopping violence without causing death.'
    },

    'Champion of Comeliness': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'attributes': 'Cha 15',
            'skills': {'Diplomacy': 8, 'Perform': 8},
            'feats': ['Persuasive'],
            'special': 'Good alignment'
        },
        'description': 'Charismatic champions who spread goodness through charm and inspiration.'
    },

    'Divine Disciple': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Must match deity',
            'skills': {'Knowledge (religion)': 8},
            'feats': ['Any two divine metamagic feats'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Devoted clerics who channel special divine powers from their patron deity.'
    },

    'Dread Knight': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Lawful Good',
            'bab': 6,
            'feats': ['Mounted Combat', 'Weapon Focus (any)'],
            'special': 'Good aligned special mount'
        },
        'description': 'Mounted paladins of terrible justice who strike fear in the hearts of evil.'
    },

    'Enforcer of the Faith': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Lawful Good',
            'bab': 7,
            'skills': {'Knowledge (religion)': 8},
            'feats': ['Great Cleave']
        },
        'description': 'Righteous warriors who enforce divine law and punish transgressors.'
    },

    'Fey Prankster': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Chaotic Good',
            'skills': {'Perform': 6, 'Spellcraft': 4},
            'feats': ['Dodge'],
            'special': 'Fey heritage or fey magic'
        },
        'description': 'Mischievous fey and their allies who use trickery for good.'
    },

    'Holy Liberator': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Chaotic Good',
            'bab': 7,
            'skills': {'Escape Artist': 8, 'Knowledge (religion)': 4},
            'feats': ['Great Fortitude'],
            'special': 'Freedom domain access'
        },
        'description': 'Chaotic good revolutionaries who free the oppressed and fight tyranny.'
    },

    'Holy Knight': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Lawful Good',
            'bab': 6,
            'feats': ['Weapon Focus (any)'],
            'spellcasting': 'Ability to cast 2nd-level divine spells'
        },
        'description': 'Righteous knights bound by oath and blessed with divine power.'
    },

    'Paladin of Tyranny': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Lawful Neutral or Lawful Good',
            'bab': 6,
            'feats': ['Weapon Focus (any)'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Disciplined warriors who impose order and lawful conduct.'
    },

    'Radiant Servant of Pelor': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Chaotic Good, Neutral Good, or Lawful Good',
            'skills': {'Heal': 8, 'Knowledge (religion)': 4},
            'feats': ['Blind-Fight'],
            'special': 'Must worship Pelor or similar sun deity'
        },
        'description': 'Divine servants of sun and light deities.'
    },

    'Rogue Apostle': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 6,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'skills': {'Escape Artist': 8, 'Hide': 8, 'Move Silently': 8},
            'feats': ['Evasion'],
            'special': 'Rogue level 6th, good alignment divine connection'
        },
        'description': 'Roguish divine agents who serve good causes through stealth and cunning.'
    },

    'Sacred Exorcist': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (religion)': 8, 'Spellcraft': 8},
            'feats': ['Improved Initiative'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Divine warriors trained to battle possession and eliminate undead.'
    },

    'Thaumaturgist': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Diplomacy': 4, 'Knowledge (planes)': 6, 'Spellcraft': 6},
            'feats': ['Any three item creation feats'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Divine masters of planar magic and celestial artifacts.'
    },

    'Warpriest': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Knowledge (religion)': 4},
            'feats': ['Weapon Focus (deity\'s favored weapon)'],
            'spellcasting': 'Ability to cast 2nd-level divine spells'
        },
        'description': 'Holy warriors who combine divine magic with martial expertise.'
    }

}
