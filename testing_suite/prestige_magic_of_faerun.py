"""
D&D 3rd edition Prestige classes from Magic of Faerun
    Prestige classes themed around the Forgotten Realms setting
"""
    
MAGIC_OF_FAERUN_PRESTIGE_CLASSES = {
    'Harper Scout': {
    'hit_die': 6,
    'bab_progression': 'medium',
    'fort_progression': 'poor',
    'ref_progression': 'good',
    'will_progression': 'good',
    'skill_points': 4,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances arcane or divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any nonevil',
        'bab': 4,
        'skills': {'Bluff': 4, 'Diplomacy': 8, 'Knowledge (local)': 4, 'Sense Motive': 2, 'Survival': 2},
        'feats': ['Alertness', 'Iron Will'],
        'spellcasting': 'Ability to cast 1st-level arcane or divine spells',
        'special': 'Must contact the Harpers and be accepted'
    },
    'description': 'Secret agents of the Harpers who work to maintain balance in Faerûn.'
},
'Spellsword': {
    'hit_die': 8,
    'bab_progression': 'full',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'poor',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances arcane spellcasting
    'is_prestige': True,
    'requirements': {
        'weapon_proficiency': 'All martial weapons',
        'feats': ['Weapon Focus (any)'],
        'spellcasting': 'Ability to cast 2nd-level arcane spells'
    },
    'description': 'Warriors who channel magic through their weapons to enhance combat prowess.'
},
'Red Wizard': {
    'hit_die': 4,
    'bab_progression': 'poor',
    'fort_progression': 'poor',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': 'intelligence',
    'spellcasting_advancement': True,  # Advances arcane spellcasting
    'is_prestige': True,
    'requirements': {
        'race': ['Human', 'Half-Elf'],
        'alignment': 'Any nongood',
        'skills': {'Spellcraft': 8},
        'feats': ['Spell Focus (any school)', 'Tattoo Focus (matches Spell Focus school)'],
        'spellcasting': 'Ability to cast 3rd-level arcane spells',
        'special': 'Thayan nationality or special permission'
    },
    'description': 'Elite wizards of Thay who specialize in school magic and sport iconic tattoos.'
},
'Guild Thief': {
    'hit_die': 6,
    'bab_progression': 'medium',
    'fort_progression': 'poor',
    'ref_progression': 'good',
    'will_progression': 'poor',
    'skill_points': 8,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'skills': {'Appraise': 4, 'Bluff': 4, 'Gather Information': 4, 'Hide': 8, 'Move Silently': 8},
        'feats': ['Skill Focus (any Rogue class skill)'],
        'special': 'Must have made a successful deal with a thieves guild'
    },
    'description': 'Professional thieves who operate within organized criminal networks.'
},
'Shadow Adept': {
    'hit_die': 4,
    'bab_progression': 'poor',
    'fort_progression': 'poor',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances arcane or divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any nongood',
        'skills': {'Knowledge (arcana)': 8, 'Spellcraft': 8},
        'feats': ['Shadow Weave Magic'],
        'spellcasting': 'Ability to cast 3rd-level arcane or divine spells'
    },
    'description': 'Spellcasters who draw power from the Shadow Weave instead of the Weave.'
},
'Arcane Devotee': {
    'hit_die': 4,
    'bab_progression': 'poor',
    'fort_progression': 'poor',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'skills': {'Knowledge (arcana)': 8, 'Knowledge (religion)': 8, 'Spellcraft': 8},
        'feats': ['Spell Focus (any school)'],
        'spellcasting': 'Ability to cast 3rd-level divine spells',
        'special': 'Must worship Azuth, Mystra, Savras, or Velsharoon'
    },
    'description': 'Divine spellcasters devoted to deities of magic who blend arcane techniques with faith.'
},
'Divine Champion': {
    'hit_die': 10,
    'bab_progression': 'full',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'poor',
    'skill_points': 2,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'alignment': 'Must match deity',
        'bab': 7,
        'feats': ['Weapon Focus (deity\'s favored weapon)'],
        'spellcasting': 'Ability to cast 1st-level divine spells',
        'special': 'Must complete a quest on behalf of deity'
    },
    'description': 'Holy warriors chosen by their deity to be divine champions in battle.'
},
'Divine Disciple': {
    'hit_die': 8,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Must match deity',
        'skills': {'Knowledge (religion)': 8},
        'feats': ['Any two divine metamagic feats'],
        'spellcasting': 'Ability to cast 3rd-level divine spells'
    },
    'description': 'Devoted clerics who gain special powers from their deity through intense faith.'
},
'Harper Priest': {
    'hit_die': 8,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 4,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any nonevil',
        'skills': {'Diplomacy': 8, 'Knowledge (local)': 8, 'Knowledge (religion)': 4},
        'feats': ['Alertness'],
        'spellcasting': 'Ability to cast 2nd-level divine spells',
        'special': 'Must be a member of the Harpers and worship Mielikki, Mystra, or Selûne'
    },
    'description': 'Divine spellcasters who serve the Harper cause through faith and magic.'
},
'Runecaster': {
    'hit_die': 6,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 4,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'race': ['Dwarf'],
        'skills': {'Craft (any)': 8, 'Spellcraft': 8},
        'feats': ['Scribe Scroll'],
        'spellcasting': 'Ability to cast 3rd-level divine spells'
    },
    'description': 'Dwarven clerics who inscribe magical runes to enhance their divine power.'
},
'Silverstar': {
    'hit_die': 8,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Chaotic Good',
        'skills': {'Heal': 8, 'Knowledge (religion)': 4},
        'feats': ['Improved Unarmed Strike'],
        'spellcasting': 'Ability to cast 3rd-level divine spells',
        'special': 'Must worship Selûne'
    },
    'description': 'Holy warriors of Selûne who fight lycanthropes and undead with moon magic.'
},
'Hospitaler': {
    'hit_die': 8,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 4,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances divine spellcasting
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any good',
        'skills': {'Heal': 8, 'Knowledge (religion)': 4},
        'feats': ['Skill Focus (Heal)'],
        'spellcasting': 'Ability to cast 2nd-level divine spells'
    },
    'description': 'Divine healers dedicated to providing care and medical aid to those in need.'
},
'Incantatrix': {
    'hit_die': 4,
    'bab_progression': 'poor',
    'fort_progression': 'poor',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': 'intelligence',
    'spellcasting_advancement': True,  # Advances arcane spellcasting
    'is_prestige': True,
    'requirements': {
        'gender': 'Female',
        'skills': {'Knowledge (arcana)': 8, 'Spellcraft': 10},
        'feats': ['Any three metamagic feats'],
        'spellcasting': 'Ability to cast 3rd-level arcane spells'
    },
    'description': 'Female wizards who master metamagic and specialize in dispelling and manipulating spells.'
},
'Acolyte of the Ego': {
    'hit_die': 4,
    'bab_progression': 'poor',
    'fort_progression': 'poor',
    'ref_progression': 'poor',
    'will_progression': 'good',
    'skill_points': 2,
    'spellcasting_ability': None,
    'spellcasting_advancement': True,  # Advances psionic manifesting
    'is_prestige': True,
    'requirements': {
        'skills': {'Knowledge (psionics)': 8, 'Psicraft': 8},
        'feats': ['Psionic Talent'],
        'special': 'Manifester level 5th'
    },
    'description': 'Psionic specialists who focus on enhancing the power of their own minds.'
},
'Acolyte of the Skin': {
    'hit_die': 10,
    'bab_progression': 'full',
    'fort_progression': 'good',
    'ref_progression': 'poor',
    'will_progression': 'poor',
    'skill_points': 2,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any evil',
        'skills': {'Intimidate': 8, 'Knowledge (the planes)': 4},
        'feats': ['Great Fortitude'],
        'spellcasting': 'Ability to summon a fiend with a spell or spell-like ability',
        'special': 'Must make a pact with a fiend and survive the ritual'
    },
    'description': 'Evil warriors who wear the skin of demons, gaining fiendish powers.'
},
'Shaaryan Hunter': {
    'hit_die': 8,
    'bab_progression': 'full',
    'fort_progression': 'good',
    'ref_progression': 'good',
    'will_progression': 'poor',
    'skill_points': 6,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'skills': {'Handle Animal': 4, 'Knowledge (nature)': 4, 'Survival': 8, 'Track': 8},
        'feats': ['Endurance', 'Track'],
        'special': 'Must be from Shaar region'
    },
    'description': 'Expert trackers and hunters from the Shaar grasslands of Faerûn.'
},
'Monk of the Long Death': {
    'hit_die': 8,
    'bab_progression': 'medium',
    'fort_progression': 'good',
    'ref_progression': 'good',
    'will_progression': 'good',
    'skill_points': 4,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any nongood',
        'skills': {'Hide': 8, 'Move Silently': 8},
        'feats': ['Stunning Fist', 'Improved Unarmed Strike'],
        'special': 'Flurry of blows class feature'
    },
    'description': 'Dark monks who study death and channel negative energy through martial arts.'
},
'Zhentarim Soldier': {
    'hit_die': 10,
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
        'feats': ['Improved Initiative', 'Weapon Focus (any)'],
        'special': 'Must be a member of the Zhentarim'
    },
    'description': 'Elite soldiers and mercenaries serving the Zhentarim organization.'
},
'Zhentarim Spy': {
    'hit_die': 6,
    'bab_progression': 'medium',
    'fort_progression': 'poor',
    'ref_progression': 'good',
    'will_progression': 'poor',
    'skill_points': 8,
    'spellcasting_ability': None,
    'is_prestige': True,
    'requirements': {
        'alignment': 'Any nongood',
        'skills': {'Bluff': 8, 'Disguise': 4, 'Gather Information': 4, 'Hide': 4},
        'special': 'Sneak attack +2d6, must be a member of the Zhentarim'
    },
    'description': 'Covert agents who gather intelligence for the Zhentarim network.'
}
}