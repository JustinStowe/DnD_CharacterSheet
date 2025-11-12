"""
D&D 3e Epic Level Handbook Support
Handles epic level progression (level 21+)
"""

# Epic Feat Definitions
EPIC_FEATS = {
    'Epic Weapon Focus': {
        'type': 'Epic',
        'prerequisites': 'Fighter level 8th, Weapon Focus',
        'benefit': '+2 bonus on attack rolls with one weapon type (stacks with Weapon Focus)',
        'special': 'Can be taken multiple times for different weapons'
    },
    'Epic Weapon Specialization': {
        'type': 'Epic',
        'prerequisites': 'Fighter level 12th, Weapon Specialization',
        'benefit': '+4 bonus on damage rolls with one weapon type (stacks with Weapon Specialization)',
        'special': 'Can be taken multiple times for different weapons'
    },
    'Epic Toughness': {
        'type': 'Epic',
        'prerequisites': 'Constitution 21+',
        'benefit': '+30 hit points',
        'special': 'Can be taken multiple times'
    },
    'Epic Fortitude': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Fortitude saves',
        'special': 'Can be taken multiple times'
    },
    'Epic Reflexes': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Reflex saves',
        'special': 'Can be taken multiple times'
    },
    'Epic Will': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Will saves',
        'special': 'Can be taken multiple times'
    },
    'Armor Skin': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 natural armor bonus to AC',
        'special': 'Can be taken multiple times (max +10)'
    },
    'Blinding Speed': {
        'type': 'Epic',
        'prerequisites': 'Dexterity 25+',
        'benefit': 'Act as if affected by haste for 5 rounds per day',
        'special': 'Can be taken multiple times (adds 5 rounds each)'
    },
    'Combat Insight': {
        'type': 'Epic',
        'prerequisites': 'Wisdom 21+, BAB +15',
        'benefit': 'Add Wisdom modifier to melee attack rolls',
        'special': 'Does not stack with other Wisdom bonuses to attack'
    },
    'Damage Reduction': {
        'type': 'Epic',
        'prerequisites': 'Constitution 21+',
        'benefit': 'Gain DR 3/—',
        'special': 'Can be taken multiple times (adds DR 3/—)'
    },
    'Devastating Critical': {
        'type': 'Epic',
        'prerequisites': 'Str 25+, Cleave, Great Cleave, Improved Critical, Power Attack, BAB +20',
        'benefit': 'When you score a critical hit with the chosen weapon, target must make Fort save (DC 10 + 1/2 HD + Str mod) or die instantly',
        'special': 'Choose one weapon type'
    },
    'Epic Dodge': {
        'type': 'Epic',
        'prerequisites': 'Dex 25+, Dodge, Defensive Roll, Improved Evasion, BAB +15',
        'benefit': 'Once per round, automatically avoid one attack that would hit you',
        'special': 'You must be aware of attack'
    },
    'Epic Endurance': {
        'type': 'Epic',
        'prerequisites': 'Constitution 25+, Endurance',
        'benefit': '+10 bonus on Concentration checks, sleep in armor without fatigue',
        'special': None
    },
    'Epic Prowess': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 bonus on all attack rolls',
        'special': 'Can be taken multiple times'
    },
    'Epic Reputation': {
        'type': 'Epic',
        'prerequisites': 'Charisma 25+',
        'benefit': '+4 bonus on Bluff, Diplomacy, Gather Information, Intimidate, Perform checks',
        'special': None
    },
    'Epic Skill Focus': {
        'type': 'Epic',
        'prerequisites': 'Skill Focus with the skill, 20 ranks in skill',
        'benefit': '+10 bonus to the chosen skill (stacks with Skill Focus)',
        'special': 'Can be taken multiple times for different skills'
    },
    'Epic Speed': {
        'type': 'Epic',
        'prerequisites': 'Dexterity 21+',
        'benefit': 'Base land speed increases by 30 feet',
        'special': 'Can be taken multiple times'
    },
    'Epic Spell Focus': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Focus in the school, ability to cast 9th-level spells',
        'benefit': '+1 bonus to the DC of all spells from the chosen school (stacks with Spell Focus and Greater Spell Focus)',
        'special': 'Can be taken multiple times for different schools'
    },
    'Epic Spell Penetration': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Penetration, ability to cast 9th-level spells',
        'benefit': '+2 bonus on caster level checks to overcome spell resistance (stacks with Spell Penetration)',
        'special': 'Can be taken multiple times'
    },
    'Epic Spellcasting': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 24 ranks, Knowledge (arcana) 24 ranks (or Knowledge (religion) for divine), ability to cast 9th-level spells',
        'benefit': 'Can develop and cast epic spells',
        'special': 'Most powerful epic feat for spellcasters'
    },
    'Fast Healing': {
        'type': 'Epic',
        'prerequisites': 'Constitution 25+',
        'benefit': 'Gain fast healing 3',
        'special': 'Can be taken multiple times (adds fast healing 3)'
    },
    'Great Constitution': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Constitution',
        'special': 'Can be taken multiple times'
    },
    'Great Dexterity': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Dexterity',
        'special': 'Can be taken multiple times'
    },
    'Great Intelligence': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Intelligence',
        'special': 'Can be taken multiple times'
    },
    'Great Strength': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Strength',
        'special': 'Can be taken multiple times'
    },
    'Great Wisdom': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Wisdom',
        'special': 'Can be taken multiple times'
    },
    'Great Charisma': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Charisma',
        'special': 'Can be taken multiple times'
    },
    'Great Smiting': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Smite evil class ability',
        'benefit': 'Add Charisma bonus to damage when using smite evil (in addition to level)',
        'special': None
    },
    'Improved Aura of Courage': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Aura of courage class ability',
        'benefit': 'Aura of courage grants immunity to fear instead of +4 bonus',
        'special': None
    },
    'Improved Combat Casting': {
        'type': 'Epic',
        'prerequisites': 'Combat Casting, Concentration 25 ranks',
        'benefit': '+4 bonus on Concentration checks to cast defensively, no attacks of opportunity when casting',
        'special': None
    },
    'Improved Combat Reflexes': {
        'type': 'Epic',
        'prerequisites': 'Dex 21+, Combat Reflexes',
        'benefit': 'No limit to attacks of opportunity per round',
        'special': 'Still limited by reach'
    },
    'Improved Ki Strike': {
        'type': 'Epic',
        'prerequisites': 'Wis 21+, Ki strike class ability',
        'benefit': 'Ki strike counts as +1 enhancement bonus higher for overcoming DR',
        'special': 'Can be taken multiple times'
    },
    'Improved Sneak Attack': {
        'type': 'Epic',
        'prerequisites': 'Sneak attack +8d6',
        'benefit': '+1d6 to sneak attack damage',
        'special': 'Can be taken multiple times'
    },
    'Improved Spell Capacity': {
        'type': 'Epic',
        'prerequisites': 'Ability to cast spells of the normal maximum spell level in at least one class',
        'benefit': 'Gain one spell slot of up to 10th-13th level (10th with first feat, 11th with second, etc.)',
        'special': 'Can be taken multiple times, choose spell level each time'
    },
    'Improved Stunning Fist': {
        'type': 'Epic',
        'prerequisites': 'Dex 19+, Wis 19+, Stunning Fist, BAB +15',
        'benefit': '+2 DC for stunning fist attacks',
        'special': 'Can be taken multiple times'
    },
    'Improved Whirlwind Attack': {
        'type': 'Epic',
        'prerequisites': 'Int 13+, Dex 23+, Combat Expertise, Dodge, Mobility, Spring Attack, Whirlwind Attack, BAB +25',
        'benefit': 'Can make one extra attack at your highest BAB during Whirlwind Attack',
        'special': None
    },
    'Infinite Deflection': {
        'type': 'Epic',
        'prerequisites': 'Dex 25+, Deflect Arrows, Improved Unarmed Strike, BAB +25',
        'benefit': 'Deflect any number of ranged attacks per round',
        'special': 'Must be aware and have hand free'
    },
    'Instant Reload': {
        'type': 'Epic',
        'prerequisites': 'Quick Draw, Rapid Reload, Weapon Focus (crossbow)',
        'benefit': 'Reload any crossbow as a free action',
        'special': None
    },
    'Legendary Commander': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Epic Leadership, Leadership',
        'benefit': 'Attract cohort and followers as if character level is 4 levels higher',
        'special': None
    },
    'Legendary Rider': {
        'type': 'Epic',
        'prerequisites': 'Ride 24 ranks',
        'benefit': '+10 to Ride checks, can make Ride check as free action',
        'special': None
    },
    'Legendary Tracker': {
        'type': 'Epic',
        'prerequisites': 'Wis 25+, Track, 30 ranks in Survival',
        'benefit': 'Track creatures across water, through air, or through solid rock',
        'special': None
    },
    'Overwhelming Critical': {
        'type': 'Epic',
        'prerequisites': 'Str 23+, Cleave, Great Cleave, Improved Critical, Power Attack, BAB +20',
        'benefit': 'When you score a critical hit, target takes +1d6 damage per die of weapon base damage',
        'special': 'Choose one weapon type'
    },
    'Perfect Health': {
        'type': 'Epic',
        'prerequisites': 'Con 25+, Great Fortitude',
        'benefit': 'Immune to all non-magical diseases, +4 to saves vs magical diseases',
        'special': None
    },
    'Permanent Emanation': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 25 ranks, ability to cast the spell',
        'benefit': 'One spell with area "emanation from you" becomes permanent',
        'special': 'Can be taken multiple times for different spells'
    },
    'Polyglot': {
        'type': 'Epic',
        'prerequisites': 'Int 25+, Speak Language (10 languages)',
        'benefit': 'Can speak all languages',
        'special': None
    },
    'Spell Knowledge': {
        'type': 'Epic',
        'prerequisites': 'Ability to cast spells',
        'benefit': 'Learn one additional spell of any level you can cast',
        'special': 'Can be taken multiple times'
    },
    'Spell Opportunity': {
        'type': 'Epic',
        'prerequisites': 'Combat Casting, Spellcraft 25 ranks',
        'benefit': 'Cast a quickened spell as an attack of opportunity',
        'special': None
    },
    'Spell Stowaway': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 24 ranks, caster level 15th',
        'benefit': 'When targeted by a spell, can make Spellcraft check to "catch" the spell and cast it later',
        'special': None
    },
    'Spontaneous Spell': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 25 ranks, ability to cast the spell',
        'benefit': 'Cast one chosen spell spontaneously by sacrificing a prepared spell',
        'special': 'For prepared spellcasters. Can be taken multiple times'
    },
    'Superior Initiative': {
        'type': 'Epic',
        'prerequisites': 'Improved Initiative',
        'benefit': '+8 bonus on initiative checks (stacks with Improved Initiative for total +12)',
        'special': None
    },
    'Swarm of Arrows': {
        'type': 'Epic',
        'prerequisites': 'Dex 23+, Point Blank Shot, Rapid Shot, Manyshot, BAB +25',
        'benefit': 'As full attack, fire arrows at full BAB at all targets in 30 ft. area',
        'special': None
    },
    'Tenacious Magic': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 15 ranks',
        'benefit': 'Choose one spell you can cast, it requires two successful dispels to remove',
        'special': 'Can be taken multiple times for different spells'
    },
    'Uncanny Accuracy': {
        'type': 'Epic',
        'prerequisites': 'Dex 21+, Point Blank Shot, Precise Shot, BAB +20',
        'benefit': 'Ranged attacks ignore miss chance from concealment (except total concealment)',
        'special': None
    }
}


def is_epic_level(total_level):
    """Check if a character is at epic level (21+)"""
    return total_level >= 21


def get_epic_feat_progression(total_level):
    """
    Calculate when a character gains epic feats.
    Characters gain an epic feat at 21st level and every 2 levels thereafter.
    Returns the total number of epic feats earned.
    """
    if total_level < 21:
        return 0
    
    # Epic feat at 21, then every 2 levels (23, 25, 27, etc.)
    return 1 + (total_level - 21) // 2


def get_epic_ability_score_increases(total_level):
    """
    Calculate ability score increases at epic levels.
    Characters still gain +1 to any ability score every 4 levels (24, 28, 32, etc.)
    Returns the number of ability score increases earned at epic levels only.
    """
    if total_level < 24:
        return 0
    
    # Count increases at 24, 28, 32, etc.
    return ((total_level - 20) // 4)


def get_epic_level_info(total_level):
    """
    Get comprehensive epic level information for a character.
    Returns a dictionary with all epic level bonuses and features.
    """
    if total_level < 21:
        return {
            'is_epic': False,
            'epic_feats': 0,
            'epic_ability_increases': 0,
            'next_epic_feat_level': 21,
            'next_ability_increase_level': 24
        }
    
    epic_feats = get_epic_feat_progression(total_level)
    ability_increases = get_epic_ability_score_increases(total_level)
    
    # Calculate next milestone levels
    next_epic_feat = total_level + (2 - ((total_level - 21) % 2)) if (total_level - 21) % 2 != 0 else total_level + 2
    next_ability = total_level + (4 - ((total_level - 20) % 4)) if (total_level - 20) % 4 != 0 else total_level + 4
    
    return {
        'is_epic': True,
        'epic_feats': epic_feats,
        'epic_ability_increases': ability_increases,
        'next_epic_feat_level': next_epic_feat,
        'next_ability_increase_level': next_ability,
        'epic_level': total_level - 20  # How many epic levels
    }


def get_epic_bab_bonus(class_name, epic_levels):
    """
    Calculate BAB for epic levels beyond 20.
    Epic level BAB progression:
    - Full BAB (+1/level): Continues at +1 per level
    - Medium BAB (+3/4 level): Continues at +1 every 2 levels (alternating)
    - Poor BAB (+1/2 level): Continues at +1 every 2 levels (alternating)
    """
    if epic_levels <= 0:
        return 0
    
    from character import CLASS_DEFINITIONS
    from prestige_classes import PRESTIGE_CLASS_DEFINITIONS
    
    # Get BAB progression type
    if class_name in CLASS_DEFINITIONS:
        bab_progression = CLASS_DEFINITIONS[class_name]['bab_progression']
    elif class_name in PRESTIGE_CLASS_DEFINITIONS:
        bab_progression = PRESTIGE_CLASS_DEFINITIONS[class_name]['bab']
    else:
        return 0
    
    if bab_progression == 'full':
        return epic_levels
    elif bab_progression == 'medium':
        # At level 20, medium BAB is +15, then +1 every 2 levels
        return (epic_levels + 1) // 2
    else:  # poor
        # At level 20, poor BAB is +10, then +1 every 2 levels
        return epic_levels // 2


def get_epic_save_bonus(save_progression, epic_levels):
    """
    Calculate save bonus for epic levels beyond 20.
    Epic level save progression:
    - Good saves (+2 + 1/2 level): +1 every 2 levels after 20th
    - Poor saves (+1/3 level): +1 every 3 levels after 20th
    """
    if epic_levels <= 0:
        return 0
    
    if save_progression == 'good':
        # At level 20, good save is +12, then +1 every 2 levels
        return (epic_levels + 1) // 2
    else:  # poor
        # At level 20, poor save is +6, then +1 every 3 levels
        return (epic_levels + 2) // 3


def get_all_epic_feats():
    """Return a list of all epic feat names"""
    return sorted(EPIC_FEATS.keys())


def get_epic_feat_info(feat_name):
    """Get detailed information about an epic feat"""
    return EPIC_FEATS.get(feat_name, None)


def check_epic_feat_prerequisites(feat_name, character):
    """
    Check if a character meets the prerequisites for an epic feat.
    Returns (eligible, list_of_requirements)
    
    Note: This is a simplified check. Full implementation would need
    to parse prerequisites more thoroughly.
    """
    feat_info = EPIC_FEATS.get(feat_name)
    if not feat_info:
        return False, ["Feat not found"]
    
    prereq = feat_info['prerequisites']
    requirements = [f"Prerequisites: {prereq}"]
    
    # Simple checks - in a full implementation, would parse prerequisites
    if 'BAB' in prereq:
        # Extract BAB requirement (simplified)
        if '+25' in prereq and character.base_attack_bonus < 25:
            return False, requirements + ["❌ Insufficient BAB"]
        elif '+20' in prereq and character.base_attack_bonus < 20:
            return False, requirements + ["❌ Insufficient BAB"]
        elif '+15' in prereq and character.base_attack_bonus < 15:
            return False, requirements + ["❌ Insufficient BAB"]
    
    # Check for epic level
    if character.get_total_level() < 21:
        return False, requirements + ["❌ Must be epic level (21+)"]
    
    # Simplified check - assumes prerequisites are met
    return True, requirements


def get_epic_bonus_spells_per_day(spell_level, epic_caster_levels):
    """
    Calculate bonus spell slots from epic caster levels.
    Epic casters continue to gain bonus spell slots based on their primary
    spellcasting ability modifier.
    
    This follows the normal bonus spells per day table but for epic levels.
    """
    # Epic casters continue to use the same bonus spell formula
    # This is handled by the normal bonus spell system in character.py
    # No additional bonuses just for being epic level
    return 0


def calculate_epic_skill_max_ranks(total_level):
    """
    Calculate maximum skill ranks at epic level.
    Max ranks = Total Character Level + 3
    """
    return total_level + 3


def get_epic_xp_for_level(level):
    """
    Calculate XP required to reach a given epic level.
    At epic levels, XP progression continues with increasing gaps.
    Each level requires: (current level) × 1000 XP
    """
    if level <= 20:
        return level * 1000
    
    # Epic level XP requirements
    # This is simplified - the actual D&D 3e epic XP table is more complex
    total_xp = 20 * 1000  # XP to reach level 20
    
    for lvl in range(21, level + 1):
        total_xp += lvl * 1000
    
    return total_xp


def get_epic_level_description(total_level):
    """
    Get a description of what epic level means for this character.
    """
    if total_level < 21:
        return "Not yet at epic level. Epic levels begin at 21st level."
    
    epic_info = get_epic_level_info(total_level)
    
    description = f"Epic Level {epic_info['epic_level']} (Total Level {total_level})\n\n"
    description += "Epic Benefits:\n"
    description += f"• Epic Feats Gained: {epic_info['epic_feats']}\n"
    description += f"• Epic Ability Score Increases: {epic_info['epic_ability_increases']}\n"
    description += f"• Next Epic Feat at Level: {epic_info['next_epic_feat_level']}\n"
    description += f"• Next Ability Increase at Level: {epic_info['next_ability_increase_level']}\n\n"
    description += "Epic characters have transcended the normal limits of their class.\n"
    description += "They gain epic feats, can achieve ability scores above 20, and\n"
    description += "continue to grow in power through epic progression."
    
    return description
