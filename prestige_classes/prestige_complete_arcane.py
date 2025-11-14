"""

D&D 3rd Edition Prestige Classes from Complete Arcane

Prestige classes for arcane spellcasters

"""

COMPLETE_ARCANE_PRESTIGE_CLASSES = {

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
        'description': 'Fighters who blend abjuration magic with martial combat for superior defense.'
    },

    'Alienist': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (the planes)': 8, 'Spellcraft': 8},
            'feats': ['Spell Focus (conjuration)'],
            'spellcasting': 'Ability to cast 4th-level arcane spells'
        },
        'description': 'Wizards devoted to summoning and binding creatures from other planes.'
    },

    'Arcane Trickster': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Bluff': 4, 'Spellcraft': 4, 'Tumble': 5},
            'feats': ['Dodge'],
            'spellcasting': 'Ability to cast mage hand',
            'special': 'Sneak attack +1d6'
        },
        'description': 'Cunning spellcasters who blend illusion magic with roguish deception.'
    },

    'Artificer': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'skills': {'Craft (any magical item)': 8, 'Spellcraft': 4},
            'feats': ['Any item creation feat'],
            'spellcasting': 'Ability to cast 1st-level arcane spells'
        },
        'description': 'Masters of magical item creation and arcane crafting.'
    },

    'Bladesinger': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Balance': 3, 'Perform': 3, 'Spellcraft': 6},
            'feats': ['Combat Casting', 'Dodge', 'Weapon Finesse'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Arcane spellcasters trained in combat, blending sword and spell.'
    },

    'Dweomerkeeper': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Appraise': 4, 'Spellcraft': 10},
            'feats': ['Any metamagic feat'],
            'spellcasting': 'Ability to cast 4th-level arcane spells'
        },
        'description': 'Wizards who study and manipulate magical auras and enchantments.'
    },

    'Eldritch Knight': {
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
            'bab': 5,
            'skills': {'Spellcraft': 4},
            'feats': ['Weapon Focus (any)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Warriors who enhance their combat prowess with arcane magic.'
    },

    'Enchantment Specialist': {
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
            'skills': {'Bluff': 6, 'Diplomacy': 6, 'Sense Motive': 3},
            'feats': ['Spell Focus (enchantment)'],
            'spellcasting': 'Ability to cast 4th-level arcane spells'
        },
        'description': 'Specialized wizards who master enchantment spells and mind control.'
    },

    'Geometer': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Craft (any)': 3, 'Knowledge (nature)': 3, 'Spellcraft': 6},
            'feats': ['Spell Focus (any)'],
            'special': 'Druid spells'
        },
        'description': 'Wizards trained in druidic geometry and natural magic.'
    },

    'Lore Master': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (any three): 8, Spellcraft': 4},
            'feats': ['Any metamagic feat'],
            'special': 'Wizard level 8th'
        },
        'description': 'Master scholars who accumulate and manipulate magical knowledge.'
    },

    'Magister': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Diplomacy': 8, 'Spellcraft': 8},
            'feats': ['Spell Focus (any)', 'Enlarge Spell or other metamagic'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Respected leaders in magical academia and political sorcery.'
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
            'feats': ['Any'],
            'spellcasting': 'Ability to cast 2nd-level arcane and divine spells'
        },
        'description': 'Rare practitioners of both arcane and divine magic.'
    },

    'Pale Master': {
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
            'skills': {'Spellcraft': 8},
            'feats': ['Spell Focus (necromancy)'],
            'spellcasting': 'Ability to cast chill touch',
            'special': 'Must be nongood'
        },
        'description': 'Necromancers who gain undead properties through dark study.'
    },

    'Rage Mage': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Spellcraft': 6},
            'feats': ['Combat Casting'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells',
            'special': 'Rage or frenzy ability'
        },
        'description': 'Fighters who channel magic through their rage for devastating power.'
    },

    'Red Wizard': {
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
            'skills': {'Spellcraft': 8},
            'feats': ['Spell Focus (any school)', 'Spell Focus (evocation)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Elite wizards from Thay who specialize in transmutation and rituals.'
    },

    'Shadowcaster': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Hide': 6, 'Spellcraft': 6},
            'feats': ['Any'],
            'special': 'Must worship Shar or similar shadow deity'
        },
        'description': 'Shadow magic practitioners who work in darkness and deception.'
    },

    'Spellwarden': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': False,
        'is_prestige': True,
        'requirements': {
            'bab': 3,
            'skills': {'Spellcraft': 6},
            'feats': ['Magic Weapon'],
            'spellcasting': 'Ability to cast 1st-level spells'
        },
        'description': 'Guardians who combine martial prowess with spell protection.'
    },

    'Spellsword': {
        'hit_die': 8,
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
            'skills': {'Spellcraft': 4},
            'feats': ['Weapon Focus (any)', 'Combat Casting'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells'
        },
        'description': 'Warriors who channel magic through weapons for enhanced combat.'
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
        'description': 'Divine spellcasters versed in planar magic and divine artifacts.'
    },

    'War Mage': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'bab': 2,
            'skills': {'Spellcraft': 4},
            'feats': ['Combat Casting'],
            'spellcasting': 'Ability to cast 1st-level arcane spells'
        },
        'description': 'Wizards trained in battlefield magic and tactical casting.'
    }

}
