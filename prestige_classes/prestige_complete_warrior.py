"""

D&D 3rd Edition Prestige Classes from Complete Warrior

Prestige classes for fighters, barbarians, and combat specialists

"""

COMPLETE_WARRIOR_PRESTIGE_CLASSES = {

    'Abjurant Champion': {
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
            'bab': 4,
            'skills': {'Spellcraft': 6},
            'feats': ['Combat Casting'],
            'spellcasting': 'Ability to cast abjuration spells'
        },
        'description': 'Fighters who blend abjuration magic with martial combat.'
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
        'description': 'Evil paladins who channel dark divine power in combat.'
    },

    'Champion': {
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
            'alignment': 'Good',
            'bab': 7,
            'skills': {'Knowledge (religion)': 4},
            'feats': ['Great Cleave', 'Weapon Focus (any)']
        },
        'description': 'Righteous warriors dedicated to fighting evil and protecting the innocent.'
    },

    'Dragon Disciple': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'bab': 7,
            'skills': {'Knowledge (arcana)': 8},
            'feats': ['Dodge', 'Str 13'],
            'special': 'Must possess draconic heritage or be descended from dragons'
        },
        'description': 'Warriors with draconic blood who gain dragon-like abilities.'
    },

    'Duelist': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'skills': {'Perform': 3, 'Tumble': 5},
            'feats': ['Dodge', 'Expertise', 'Weapon Finesse']
        },
        'description': 'Highly skilled swordsmen who dance in combat with finesse and style.'
    },

    'Dwarven Defender': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'race': ['Dwarf'],
            'bab': 7,
            'feats': ['Toughness'],
            'special': 'Combat Training'
        },
        'description': 'Dwarven elite warriors trained in defensive fighting and fortress tactics.'
    },

    'Frenzied Berserker': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 7,
            'feats': ['Cleave', 'Power Attack'],
            'special': 'Rage class feature'
        },
        'description': 'Barbarians who enter devastating frenzies of uncontrolled rage.'
    },

    'Kensai': {
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
            'bab': 7,
            'skills': {'Craft (weaponsmithing)': 4, 'Perform': 4},
            'feats': ['Weapon Focus (any)', 'Expertise']
        },
        'description': 'Warrior-monks who dedicate themselves to perfecting their chosen weapon.'
    },

    'Paladin': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': False,
        'requirements': {},
        'description': 'Holy warriors bound by oath and divine power.'
    },

    'Samurai': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Craft (weaponsmithing)': 3, 'Knowledge (nobility)': 4},
            'feats': ['Improved Initiative', 'Weapon Focus (any)']
        },
        'description': 'Eastern warriors bound by honor codes and martial discipline.'
    },

    'Swashbuckler': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Perform': 3, 'Tumble': 5},
            'feats': ['Dodge', 'Weapon Finesse']
        },
        'description': 'Dashing swordsmen known for acrobatic combat and roguish charm.'
    },

    'Thug': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 3,
            'skills': {'Intimidate': 6, 'Survival': 3},
            'feats': ['Cleave', 'Power Attack']
        },
        'description': 'Brutal enforcers and intimidating warriors who rely on fear and strength.'
    }

}
