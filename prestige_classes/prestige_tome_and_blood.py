"""
D&D 3rd Edition Prestige Classes from Tome and Blood
Arcane and divine caster prestige classes
"""

TOME_AND_BLOOD_PRESTIGE_CLASSES = {
    'Abjurer': {
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
            'skills': {'Knowledge (arcana)': 8, 'Spellcraft': 8},
            'feats': ['Spell Focus (Abjuration)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Specialists in protective magic who excel at dispelling and counterspelling.'
    },
    'Alienist': {
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
            'alignment': 'Any nongood',
            'skills': {'Knowledge (the planes)': 8, 'Knowledge (arcana)': 4},
            'feats': ['Spell Focus (Conjuration)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells including summon monster III'
        },
        'description': 'Summoners who traffic with aberrations from the Far Realm, gaining alien powers.'
    },
    'Bladesinger': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'race': ['Elf', 'Half-Elf'],
            'bab': 5,
            'skills': {'Concentration': 4, 'Perform (sing, dance, or chant)': 2},
            'feats': ['Combat Casting', 'Dodge', 'Mobility', 'Weapon Focus (longsword or rapier)'],
            'spellcasting': 'Ability to cast 2nd-level arcane spells'
        },
        'description': 'Elven warrior-mages who blend swordplay with spellcasting in a martial art.'
    },
    'Blood Magus': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Concentration': 8, 'Spellcraft': 8},
            'feats': ['Endurance', 'Toughness'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Mages who sacrifice their own life force to power devastating spells.'
    },
    'Candle Caster': {
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
            'skills': {'Concentration': 8, 'Craft (candlemaking)': 4},
            'feats': ['Craft Wondrous Item'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Spellcasters who craft magical candles to enhance their spellcasting abilities.'
    },
    'Geomancer': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'wisdom',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (nature)': 8, 'Survival': 4},
            'feats': ['Spell Focus (any)'],
            'spellcasting': 'Ability to cast 2nd-level divine spells'
        },
        'description': 'Divine spellcasters who draw power from specific terrain types and nodes.'
    },
    'Master Transmogrifist': {
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
            'skills': {'Concentration': 8, 'Knowledge (arcana)': 8},
            'feats': ['Spell Focus (Transmutation)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells including polymorph'
        },
        'description': 'Transmuters who master shapeshifting and bodily transformation magic.'
    },
    'Pale Master': {
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
            'alignment': 'Any nongood',
            'skills': {'Knowledge (religion)': 4, 'Knowledge (arcana)': 8},
            'feats': ['Spell Focus (Necromancy)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Necromancers who embrace undeath, replacing body parts with undead grafts.'
    },
    'Ruathar': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': 'wisdom',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'race': ['Elf', 'Half-Elf'],
            'bab': 5,
            'skills': {'Handle Animal': 2, 'Ride': 4},
            'feats': ['Mounted Combat', 'Weapon Focus (lance or longbow)'],
            'spellcasting': 'Ability to cast 1st-level divine spells'
        },
        'description': 'Elven cavalry who combine mounted combat with divine magic and nature lore.'
    },
    'Seeker of the Song': {
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
            'alignment': 'Any chaotic',
            'skills': {'Knowledge (arcana)': 8, 'Perform (sing)': 8, 'Spellcraft': 8},
            'feats': ['Spell Focus (any)'],
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Arcane spellcasters who discover the primal song of creation to enhance their magic.'
    },
    'Void Disciple': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'wisdom',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nongood',
            'skills': {'Concentration': 8, 'Knowledge (religion)': 4},
            'feats': ['Spell Focus (Necromancy)'],
            'spellcasting': 'Ability to cast 3rd-level divine spells'
        },
        'description': 'Dark priests who channel the power of oblivion and the negative energy plane.'
    },
    'Waverider': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': 'wisdom',
        'spellcasting_advancement': True,
        'is_prestige': True,
        'requirements': {
            'skills': {'Balance': 4, 'Profession (sailor)': 8, 'Swim': 8},
            'feats': ['Athletic'],
            'spellcasting': 'Ability to cast 2nd-level divine spells'
        },
        'description': 'Divine spellcasters who master water magic and specialize in nautical pursuits.'
    }
}
