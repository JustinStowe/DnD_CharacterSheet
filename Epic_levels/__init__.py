"""
Epic Levels Package
Contains Epic Level Handbook rules for D&D 3e characters level 21+
"""

from .epic_levels import (
    EPIC_FEATS,
    is_epic_level,
    get_epic_level_info,
    get_epic_bab_bonus,
    get_epic_save_bonus,
    calculate_epic_skill_max_ranks,
    get_epic_xp_for_level,
    get_epic_feat_progression,
    get_all_epic_feats,
    check_epic_feat_prerequisites,
    get_epic_level_description
)

__all__ = [
    'EPIC_FEATS',
    'is_epic_level',
    'get_epic_level_info',
    'get_epic_bab_bonus',
    'get_epic_save_bonus',
    'calculate_epic_skill_max_ranks',
    'get_epic_xp_for_level',
    'get_epic_feat_progression',
    'get_all_epic_feats',
    'check_epic_feat_prerequisites',
    'get_epic_level_description'
]
