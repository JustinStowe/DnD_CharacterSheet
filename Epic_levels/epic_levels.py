"""
D&D 3e Epic Level Handbook Support
Handles epic level progression (level 21+)
"""

try:
    # Use the canonical epic feats list from the feats package
    from feats.feats_epic import EPIC_FEATS as EPIC_FEATS
except Exception:
    # Fallback: no epic feats available
    EPIC_FEATS = {}



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
