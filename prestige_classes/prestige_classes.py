"""
D&D 3rd Edition Prestige Classes
Defines prestige classes with their requirements and progressions

Prestige classes are organized by sourcebook:
- Core DMG: 12 prestige classes (Arcane Archer, Arcane Trickster, etc.)
- Magic of Faerûn: 19 prestige classes (Harper Scout, Red Wizard, etc.)
- Tome and Blood: 12 prestige classes (Bladesinger, Pale Master, etc.)
- Sword and Fist: 14 prestige classes (Cavalier, Kensai, etc.)
- Song and Silence: 13 prestige classes (Battle Dancer, Master of Masks, etc.)

Total: 70 prestige classes
"""

# Import prestige classes from each sourcebook
from prestige_tome_and_blood import TOME_AND_BLOOD_PRESTIGE_CLASSES
from prestige_sword_and_fist import SWORD_AND_FIST_PRESTIGE_CLASSES
from prestige_song_and_silence import SONG_AND_SILENCE_PRESTIGE_CLASSES
from prestige_magic_of_faerun import MAGIC_OF_FAERUN_PRESTIGE_CLASSES

# Core DMG and Magic of Faerûn prestige classes
CORE_PRESTIGE_CLASS_DEFINITIONS = {
    'Arcane Archer': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'race': ['Elf', 'Half-Elf'],  # Must be elf or half-elf
            'bab': 6,
            'feats': ['Point Blank Shot', 'Precise Shot', 'Weapon Focus (longbow or shortbow)'],
            'spellcasting': 'Ability to cast 1st-level arcane spells'
        },
        'description': 'Masters of both bow and magic who imbue their arrows with spell energy.'
    },
    'Arcane Trickster': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': 'intelligence',
        'spellcasting_advancement': True,  # Advances arcane spellcasting
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any nonlawful',
            'skills': {'Decipher Script': 7, 'Disable Device': 7, 'Escape Artist': 7, 'Knowledge (arcana)': 4},
            'spellcasting': 'Ability to cast mage hand and at least one 3rd-level arcane spell',
            'special': 'Sneak attack +2d6'
        },
        'description': 'Rogues who dabble in magic or spellcasters who enhance their skills with stealth.'
    },
    'Assassin': {
        'hit_die': 6,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any evil',
            'skills': {'Disguise': 4, 'Hide': 8, 'Move Silently': 8},
            'special': 'Must kill someone for no other reason than to join the Assassins'
        },
        'description': 'Masters of dealing quick, lethal blows from the shadows.'
    },
    'Blackguard': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 2,
        'spellcasting_ability': 'wisdom',
        'is_prestige': True,
        'requirements': {
            'alignment': 'Any evil',
            'bab': 6,
            'skills': {'Hide': 5},
            'feats': ['Cleave', 'Improved Sunder', 'Power Attack'],
            'special': 'Must have made peaceful contact with an evil outsider who holds HD equal to character level'
        },
        'description': 'Fallen paladins or evil warriors who serve dark powers.'
    },
    'Dragon Disciple': {
        'hit_die': 12,
        'bab_progression': 'medium',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': 'charisma',
        'spellcasting_advancement': True,  # Advances arcane spellcasting
        'is_prestige': True,
        'requirements': {
            'race': 'Any nondragon',
            'skills': {'Knowledge (arcana)': 8},
            'spellcasting': 'Ability to cast arcane spells without preparation',
            'special': 'Sorcerer level 5+'
        },
        'description': 'Sorcerers who embrace their draconic heritage and gain dragon-like abilities.'
    },
    'Duelist': {
        'hit_die': 10,
        'bab_progression': 'full',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'bab': 6,
            'skills': {'Perform': 3, 'Tumble': 5},
            'feats': ['Dodge', 'Mobility', 'Weapon Finesse']
        },
        'description': 'Light-armored warriors who rely on mobility and precision.'
    },
    'Dwarven Defender': {
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
            'feats': ['Dodge', 'Endurance', 'Toughness']
        },
        'description': 'Dwarven warriors who specialize in defensive combat.'
    },
    'Eldritch Knight': {
        'hit_die': 6,
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
            'spellcasting': 'Ability to cast 3rd-level arcane spells'
        },
        'description': 'Warriors who blend martial prowess with arcane magic.'
    },
    'Horizon Walker': {
        'hit_die': 8,
        'bab_progression': 'full',
        'fort_progression': 'good',
        'ref_progression': 'poor',
        'will_progression': 'poor',
        'skill_points': 4,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (geography)': 8}
        },
        'description': 'Travelers who master different terrains and planar environments.'
    },
    'Loremaster': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 4,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,  # Advances spellcasting
        'is_prestige': True,
        'requirements': {
            'skills': {
                'Knowledge (any two)': 10,
                'Knowledge (third type)': 10
            },
            'feats': ['Any three metamagic or item creation feats'],
            'spellcasting': 'Ability to cast seven different divination spells, one of which must be 3rd level or higher'
        },
        'description': 'Scholars who seek magical knowledge and secrets.'
    },
    'Mystic Theurge': {
        'hit_die': 4,
        'bab_progression': 'poor',
        'fort_progression': 'poor',
        'ref_progression': 'poor',
        'will_progression': 'good',
        'skill_points': 2,
        'spellcasting_ability': None,
        'spellcasting_advancement': True,  # Advances both arcane and divine
        'is_prestige': True,
        'requirements': {
            'skills': {'Knowledge (arcana)': 6, 'Knowledge (religion)': 6},
            'spellcasting': 'Ability to cast 2nd-level arcane spells and 2nd-level divine spells'
        },
        'description': 'Spellcasters who master both arcane and divine magic.'
    },
    'Shadowdancer': {
        'hit_die': 8,
        'bab_progression': 'medium',
        'fort_progression': 'poor',
        'ref_progression': 'good',
        'will_progression': 'poor',
        'skill_points': 6,
        'spellcasting_ability': None,
        'is_prestige': True,
        'requirements': {
            'skills': {'Move Silently': 8, 'Hide': 10, 'Perform (dance)': 5},
            'feats': ['Combat Reflexes', 'Dodge', 'Mobility']
        },
        'description': 'Stealthy performers who manipulate shadows and darkness.'
    },
    
    # Magic of Faerûn Prestige Classes
    
}

# Merge all prestige class dictionaries
PRESTIGE_CLASS_DEFINITIONS = {
    **CORE_PRESTIGE_CLASS_DEFINITIONS,
    **TOME_AND_BLOOD_PRESTIGE_CLASSES,
    **SWORD_AND_FIST_PRESTIGE_CLASSES,
    **SONG_AND_SILENCE_PRESTIGE_CLASSES,
    **MAGIC_OF_FAERUN_PRESTIGE_CLASSES
}



def check_prestige_class_requirements(character, prestige_class_name):
    """
    Check if a character meets the requirements for a prestige class.
    
    Args:
        character: Character object
        prestige_class_name: Name of the prestige class
    
    Returns:
        tuple: (bool eligible, list of unmet requirements)
    """
    if prestige_class_name not in PRESTIGE_CLASS_DEFINITIONS:
        return False, [f"Unknown prestige class: {prestige_class_name}"]
    
    prestige_class = PRESTIGE_CLASS_DEFINITIONS[prestige_class_name]
    requirements = prestige_class.get('requirements', {})
    unmet = []
    
    # Check race requirement
    if 'race' in requirements:
        allowed_races = requirements['race']
        if character.race not in allowed_races:
            unmet.append(f"Race must be one of: {', '.join(allowed_races)} (current: {character.race or 'None'})")
    
    # Check alignment requirement
    if 'alignment' in requirements:
        alignment_req = requirements['alignment']
        if alignment_req != 'Any nonlawful' and alignment_req != 'Any evil' and alignment_req != 'Any lawful':
            # Specific alignment check would go here
            pass
        else:
            # Simplified alignment check - would need more logic for "nonlawful", "evil", etc.
            if alignment_req == 'Any evil' and character.alignment:
                if 'Evil' not in character.alignment:
                    unmet.append(f"Alignment must be evil (current: {character.alignment})")
            elif alignment_req == 'Any lawful' and character.alignment:
                if 'Lawful' not in character.alignment:
                    unmet.append(f"Alignment must be lawful (current: {character.alignment})")
            elif alignment_req == 'Any nonlawful' and character.alignment:
                if 'Lawful' in character.alignment:
                    unmet.append(f"Alignment must be nonlawful (current: {character.alignment})")
    
    # Check BAB requirement
    if 'bab' in requirements:
        required_bab = requirements['bab']
        if character.base_attack_bonus < required_bab:
            unmet.append(f"Base Attack Bonus must be at least +{required_bab} (current: +{character.base_attack_bonus})")
    
    # Check skill requirements
    if 'skills' in requirements:
        skill_reqs = requirements['skills']
        for skill_name, required_ranks in skill_reqs.items():
            if isinstance(required_ranks, int):
                current_ranks = character.skills.get(skill_name, 0)
                if current_ranks < required_ranks:
                    unmet.append(f"{skill_name} must have at least {required_ranks} ranks (current: {current_ranks})")
            else:
                # Handle special cases like "Any three" or descriptive requirements
                unmet.append(f"Skill requirement: {skill_name} - {required_ranks}")
    
    # Check feat requirements (simplified - just lists them)
    if 'feats' in requirements:
        feat_list = requirements['feats']
        # Since we don't track individual feats in detail, just list the requirement
        unmet.append(f"Required feats: {', '.join(feat_list)}")
    
    # Check spellcasting requirements (simplified description)
    if 'spellcasting' in requirements:
        spell_req = requirements['spellcasting']
        unmet.append(f"Spellcasting requirement: {spell_req}")
    
    # Check special requirements (just informational)
    if 'special' in requirements:
        special_req = requirements['special']
        unmet.append(f"Special requirement: {special_req}")
    
    # Check weapon proficiency requirements
    if 'weapon_proficiency' in requirements:
        prof_req = requirements['weapon_proficiency']
        unmet.append(f"Weapon proficiency requirement: {prof_req}")
    
    # If there are unmet requirements, return False
    # Note: Some requirements (feats, spells, special) are always added as informational
    # A true implementation would need to track these
    eligible = len([req for req in unmet if not req.startswith('Required feats:') 
                    and not req.startswith('Spellcasting requirement:')
                    and not req.startswith('Special requirement:')
                    and not req.startswith('Weapon proficiency requirement:')]) == 0
    
    return eligible, unmet


def get_prestige_class_info(prestige_class_name):
    """Get information about a prestige class."""
    return PRESTIGE_CLASS_DEFINITIONS.get(prestige_class_name)


def get_all_prestige_classes():
    """Get list of all prestige class names."""
    return list(PRESTIGE_CLASS_DEFINITIONS.keys())


def is_prestige_class(class_name):
    """Check if a class name is a prestige class."""
    return class_name in PRESTIGE_CLASS_DEFINITIONS
