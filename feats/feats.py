"""
D&D 3rd Edition Feats
Defines feats with their prerequisites and benefits

Feats are organized by sourcebook:
- Player's Handbook: General, Combat, Metamagic, Item Creation, and Special feats

You can add more sourcebooks by creating new files in the feats/ directory
"""

# Import feats from each sourcebook
from .feats_players_handbook import PLAYERS_HANDBOOK_FEATS
from .feats_tome_and_blood import TOME_AND_BLOOD_FEATS
from .feats_magic_of_faerun import MAGIC_OF_FAERUN_FEATS
from .feats_song_and_silence import SONG_AND_SILENCE_FEATS
from .feats_sword_and_fist import SWORD_AND_FIST_FEATS
from .feats_epic import EPIC_FEATS
from .feats_complete_adventurer import COMPLETE_ADVENTURER_FEATS
from .feats_complete_arcane import COMPLETE_ARCANE_FEATS
from .feats_complete_champion import COMPLETE_CHAMPION_FEATS
from .feats_complete_divine import COMPLETE_DIVINE_FEATS
from .feats_complete_mage import COMPLETE_MAGE_FEATS
from .feats_complete_warrior import COMPLETE_WARRIOR_FEATS


# Combine all feats into one dictionary
ALL_FEATS = {}
ALL_FEATS.update(PLAYERS_HANDBOOK_FEATS)
ALL_FEATS.update(TOME_AND_BLOOD_FEATS)
ALL_FEATS.update(MAGIC_OF_FAERUN_FEATS)
ALL_FEATS.update(SONG_AND_SILENCE_FEATS)
ALL_FEATS.update(SWORD_AND_FIST_FEATS)
ALL_FEATS.update(EPIC_FEATS)
ALL_FEATS.update(COMPLETE_ADVENTURER_FEATS)
ALL_FEATS.update(COMPLETE_ARCANE_FEATS)
ALL_FEATS.update(COMPLETE_CHAMPION_FEATS)
ALL_FEATS.update(COMPLETE_DIVINE_FEATS)
ALL_FEATS.update(COMPLETE_MAGE_FEATS)
ALL_FEATS.update(COMPLETE_WARRIOR_FEATS)

# Add more sourcebook feats here as they are created
# Example:
# from .feats_complete_warrior import COMPLETE_WARRIOR_FEATS
# ALL_FEATS.update(COMPLETE_WARRIOR_FEATS)


def get_feat_info(feat_name):
    """
    Get information about a specific feat
    
    Args:
        feat_name: Name of the feat
        
    Returns:
        Dictionary with feat information or None if not found
    """
    return ALL_FEATS.get(feat_name)


def get_all_feats_list():
    """
    Get a sorted list of all feat names
    
    Returns:
        Sorted list of feat names
    """
    return sorted(ALL_FEATS.keys())


def get_feats_by_type(feat_type):
    """
    Get all feats of a specific type
    
    Args:
        feat_type: Type of feat (e.g., 'General', 'Combat', 'Metamagic', 'Item Creation')
        
    Returns:
        Dictionary of feats matching the type
    """
    return {name: info for name, info in ALL_FEATS.items() 
            if info.get('type', '').lower() == feat_type.lower()}
