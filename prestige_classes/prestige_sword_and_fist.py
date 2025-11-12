"""
D&D 3rd Edition Prestige Classes from Sword and Fist
Fighter and monk prestige classes
"""

SWORD_AND_FIST_PRESTIGE_CLASSES = {
    'Cavalier': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'skills': {'Handle Animal': 4, 'Ride': 8},
            'feats': ['Mounted Combat', 'Weapon Focus (lance)'],
            'special': 'Must own a heavy warhorse or similar mount'
        },
        'description': 'Elite mounted warriors who charge into battle with lance and steed.'
    },
    'Darkwood Stalker': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'race': ['Elf', 'Half-Elf'],
            'bab': 5,
            'skills': {'Hide': 8, 'Move Silently': 8, 'Wilderness Lore': 4},
            'feats': ['Point Blank Shot', 'Track'],
            'special': 'Woodland stride ability'
        },
        'description': 'Elven rangers who defend the forests with stealth and deadly archery.'
    },
    'Drunken Master': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'skills': {'Balance': 5, 'Perform (act)': 3, 'Tumble': 5},
            'feats': ['Dodge', 'Great Fortitude', 'Improved Unarmed Strike'],
            'special': 'Evasion ability, flurry of blows ability'
        },
        'description': 'Unconventional monks who fight while seemingly intoxicated, confusing opponents.'
    },
    'Exotic Weapon Master': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'feats': ['Exotic Weapon Proficiency (any)', 'Weapon Focus (same exotic weapon)', 'Weapon Specialization (same exotic weapon)']
        },
        'description': 'Specialists who master exotic weapons and develop unique combat techniques.'
    },
    'Frenzied Berserker': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nonlawful',
            'bab': 6,
            'feats': ['Cleave', 'Intimidating Rage', 'Power Attack'],
            'special': 'Rage ability'
        },
        'description': 'Barbarians who enter a supernatural frenzy, becoming unstoppable in battle.'
    },
    'Gladiator': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'skills': {'Intimidate': 4, 'Perform': 2},
            'feats': ['Exotic Weapon Proficiency (net)', 'Improved Unarmed Strike']
        },
        'description': 'Arena combatants trained to fight for the entertainment of crowds.'
    },
    'Ironguard': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'race': ['Dwarf'],
            'bab': 7,
            'feats': ['Cleave', 'Endurance', 'Great Cleave', 'Power Attack', 'Toughness']
        },
        'description': 'Elite dwarven defenders known for their incredible toughness and battle prowess.'
    },
    'Kensai': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Concentration': 8},
            'feats': ['Weapon Focus (any melee)', 'Weapon Specialization (same melee weapon)']
        },
        'description': 'Weapon masters who achieve perfection with a single chosen blade.'
    },
    'Monk of the Enabled Hand': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any lawful',
            'bab': 5,
            'skills': {'Diplomacy': 4, 'Heal': 4},
            'feats': ['Improved Unarmed Strike', 'Stunning Fist'],
            'special': 'Flurry of blows ability, Ki strike ability'
        },
        'description': 'Monks dedicated to healing and helping others through martial discipline.'
    },
    'Ravager': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nongood',
            'bab': 5,
            'skills': {'Intimidate': 4, 'Survival': 4},
            'feats': ['Cleave', 'Power Attack'],
            'special': 'Rage ability'
        },
        'description': 'Destructive barbarians who specialize in devastating charges and property damage.'
    },
    'Reaping Mauler': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 5,
            'skills': {'Escape Artist': 2},
            'feats': ['Improved Grapple', 'Improved Unarmed Strike']
        },
        'description': 'Grappling specialists who use wrestling and chokeholds to subdue opponents.'
    },
    'Stonelord': {
        'hit_die': 12,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'race': ['Dwarf'],
            'alignment': 'Any lawful',
            'bab': 7,
            'skills': {'Concentration': 4},
            'feats': ['Endurance', 'Great Fortitude', 'Toughness']
        },
        'description': 'Dwarven warriors who bond with stone and earth, gaining earth elemental powers.'
    },
    'War Chanter': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'skills': {'Perform (chant or sing)': 6},
            'feats': ['Combat Reflexes', 'Leadership']
        },
        'description': 'Battlefield leaders who inspire allies through powerful war songs and chants.'
    },
    'Wildrunner': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 6,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'race': ['Elf', 'Half-Elf'],
            'bab': 5,
            'skills': {'Handle Animal': 4, 'Knowledge (nature)': 4, 'Survival': 8},
            'feats': ['Endurance', 'Run', 'Track']
        },
        'description': 'Elven wilderness warriors who run tirelessly through forests, protecting nature.'
    }
}
