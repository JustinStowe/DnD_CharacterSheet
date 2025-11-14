"""

D&D 3rd Edition Prestige Classes from Complete Divine

Prestige classes for clerics, druids, and divine spellcasters

"""

COMPLETE_DIVINE_PRESTIGE_CLASSES = {

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
            'alignment': 'Any peaceful non-evil',
            'skills': {'Diplomacy': 8, 'Knowledge (religion)': 4},
            'feats': ['Nonlethal substitution'],
            'spellcasting': 'Ability to cast 3rd-level divine spells',
            'special': 'Must refuse to use lethal combat'
        },
        'description': 'Pacifist clerics dedicated to stopping violence without killing.'
    },

    'Arch Druid': {
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
            'bab': 5,
            'skills': {'Knowledge (nature)': 12, 'Survival': 12},
            'feats': ['Alertness'],
            'special': 'Druid level 6th minimum'
        },
        'description': 'High druids who command primal nature and gain transformation powers.'
    },

    'Blackguard': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Non-good',
            'bab': 6,
            'skills': {'Knowledge (religion)': 4},
            'feats': ['Cleave', 'Power Attack'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Evil paladins who wield dark divine powers.'
    },

    'Cloistered Cleric': {
        'hit_die': 6,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (any three)': 8, 'Spellcraft': 8},
            'feats': ['Any two metamagic feats'],
            'spellcasting': 'Ability to cast 4th-level divine spells',
            'special': 'Cleric level 6th minimum'
        },
        'description': 'Scholarly clerics who focus on knowledge and spell casting over combat.'
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
            'special': 'Access to any freedom-related domain'
        },
        'description': 'Chaotic good champions who free prisoners and fight oppression.'
    },

    'Hierophant': {
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
            'skills': {'Knowledge (religion)': 12, 'Spellcraft': 12},
            'feats': ['Any two metamagic feats'],
            'spellcasting': 'Ability to cast 7th-level divine spells',
            'special': 'Knowledge (religion) check DC 40'
        },
        'description': 'High priests and religious leaders of immense divine power.'
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
        'description': 'Lawful good paladins and clerics who fight darkness with discipline.'
    },

    'Mystic Theurge': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (arcana)': 6, 'Knowledge (religion)': 6},
            'spellcasting': 'Ability to cast 2nd-level arcane and divine spells'
        },
        'description': 'Rare masters of both arcane and divine spellcasting.'
    },

    'Oathbow Initiate': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'skills': {'Craft (bowmaking)': 6, 'Knowledge (religion)': 4},
            'feats': ['Point Blank Shot', 'Weapon Focus (longbow)'],
            'special': 'Oath to protect something specific'
        },
        'description': 'Divine archers bound by sacred oath to protect their charges.'
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
            'special': 'Rogue level 6th and divine spellcasting'
        },
        'description': 'Roguish divine spellcasters who use cunning and stealth in service of faith.'
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
        'description': 'Divine specialists trained to combat evil spirits and possess creatures.'
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
        'description': 'Divine specialists in planar magic and celestial artifacts.'
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
        'description': 'Divine warriors who combine clerical spells with martial prowess.'
    }

}
