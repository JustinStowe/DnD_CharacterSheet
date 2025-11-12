"""
D&D 3rd Edition Prestige Classes from Song and Silence
Bard and rogue prestige classes
"""

SONG_AND_SILENCE_PRESTIGE_CLASSES = {
    'Battle Dancer': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 6,
        'spellcasting_ability': 'charisma',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Perform (dance)': 8, 'Tumble': 5},
            'feats': ['Combat Reflexes', 'Dodge'],
            'spellcasting': 'Ability to cast 1st-level arcane spells',
            'special': 'Bardic music ability'
        },
        'description': 'Bards who use acrobatic dance movements to enhance combat and magic.'
    },
    'Fochlucan Lyrist': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'charisma',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Neutral Good',
            'bab': 4,
            'skills': {'Diplomacy': 7, 'Knowledge (nature)': 7, 'Perform (string instruments)': 10, 'Sleight of Hand': 4, 'Survival': 4},
            'feats': ['Skill Focus (Perform)'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells and 1st-level divine spells',
            'special': 'Bardic music ability, druidic or ranger spellcasting'
        },
        'description': 'Members of an ancient bardic college who blend druidic and arcane magic.'
    },
    'Harper Agent': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 8,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nonevil',
            'skills': {'Bluff': 4, 'Diplomacy': 4, 'Gather Information': 8, 'Knowledge (local)': 4, 'Sense Motive': 2},
            'feats': ['Alertness', 'Iron Will'],
            'spellcasting': 'Ability to cast 2nd-level arcane or divine spells',
            'special': 'Must be invited to join the Harpers'
        },
        'description': 'Elite agents who work in secret to maintain balance and oppose tyranny. (Alternate version of Harper Scout)'
    },
    'Lyric Thaumaturge': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'charisma',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Concentration': 8, 'Knowledge (arcana)': 8, 'Perform (any)': 10, 'Spellcraft': 8},
            'feats': ['Combat Casting', 'Spell Focus (any)'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells',
            'special': 'Bardic music ability'
        },
        'description': 'Bards who develop the ability to combine spellcasting with bardic music.'
    },
    'Master of Masks': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 6,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'skills': {'Bluff': 8, 'Disguise': 8, 'Perform (act)': 4},
            'feats': ['Deceitful'],
            'special': 'Sneak attack +2d6 or bardic music ability'
        },
        'description': 'Masters of disguise who use magical masks to assume different personas and abilities.'
    },
    'Metalsmith': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Appraise': 4, 'Craft (armorsmithing or weaponsmithing)': 8},
            'feats': ['Craft Magic Arms and Armor', 'Skill Focus (Craft)']
        },
        'description': 'Master craftsmen who create superior weapons and armor with near-magical quality.'
    },
    'Nameless One': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 8,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nonlawful',
            'skills': {'Bluff': 8, 'Disguise': 8, 'Forgery': 4, 'Hide': 8},
            'special': 'Sneak attack +3d6'
        },
        'description': 'Rogues who erase their identity completely, becoming ghosts in society.'
    },
    'Justiciar': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any lawful',
            'bab': 5,
            'skills': {'Intimidate': 4, 'Sense Motive': 4},
            'feats': ['Alertness', 'Iron Will'],
            'special': 'Sneak attack +2d6'
        },
        'description': 'Lawful enforcers who blend combat skill with investigation and justice.'
    },
    'Master Specialist': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (arcana)': 10, 'Spellcraft': 10},
            'feats': ['Greater Spell Focus (any school)', 'Skill Focus (Spellcraft)', 'Spell Focus (same school)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells',
            'special': 'Must be a specialist wizard'
        },
        'description': 'Specialist wizards who achieve unparalleled mastery in their chosen school of magic.'
    },
    'Virtuoso': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 6,
        'spellcasting_ability': 'charisma',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Perform (any three)': 10},
            'feats': ['Skill Focus (Perform)'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells',
            'special': 'Bardic music ability'
        },
        'description': 'Master performers who achieve artistic perfection in multiple performance types.'
    },
    'Vigilante': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nonchaotic',
            'bab': 5,
            'skills': {'Intimidate': 4, 'Sense Motive': 2},
            'feats': ['Alertness', 'Improved Initiative'],
            'special': 'Sneak attack +2d6'
        },
        'description': 'Urban warriors who take justice into their own hands to protect the innocent.'
    },
    'Fortune\'s Friend': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 8,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any chaotic',
            'skills': {'Bluff': 8, 'Tumble': 4},
            'feats': ['Dodge', 'Lightning Reflexes'],
            'special': 'Evasion ability'
        },
        'description': 'Lucky rogues who seem blessed by fortune, able to escape danger through sheer chance.'
    },
    'Thief-Acrobat': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 6,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'skills': {'Balance': 8, 'Climb': 4, 'Jump': 4, 'Tumble': 8},
            'feats': ['Dodge', 'Mobility'],
            'special': 'Evasion ability, sneak attack +2d6'
        },
        'description': 'Athletic rogues who use acrobatics and agility to outmaneuver opponents.'
    }
}
