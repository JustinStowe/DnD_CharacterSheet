"""
Feature and epic-level management for Character
"""

from Epic_levels.epic_levels import (
    get_epic_feat_progression,
    get_all_epic_feats,
    check_epic_feat_prerequisites,
    get_epic_level_info,
    calculate_epic_skill_max_ranks,
    get_epic_xp_for_level
)

class FeatManager:
    def __init__(self, character):
        self.character = character

    def has_feat(self, feat_name):
        feat_name_lower = feat_name.lower()
        return any(f['name'].lower() == feat_name_lower for f in self.character.feats)

    def add_feat(self, name, feat_type='General', description='', prerequisites='', benefit=''):
        self.character.feats.append({
            'name': name,
            'type': feat_type,
            'description': description,
            'prerequisites': prerequisites,
            'benefit': benefit
        })

    def remove_feat(self, index):
        if 0 <= index < len(self.character.feats):
            self.character.feats.pop(index)

    # Epic feats behaviors
    def get_epic_info(self):
        return get_epic_level_info(self.character.get_total_level())

    def get_max_skill_ranks(self):
        return calculate_epic_skill_max_ranks(self.character.get_total_level())

    def get_epic_feats_available(self):
        return get_epic_feat_progression(self.character.get_total_level())

    def add_epic_feat(self, feat_name):
        if feat_name not in self.character.epic_feats:
            self.character.epic_feats.append(feat_name)

    def remove_epic_feat(self, feat_name):
        if feat_name in self.character.epic_feats:
            self.character.epic_feats.remove(feat_name)

    def check_epic_feat_requirements(self, feat_name):
        return check_epic_feat_prerequisites(feat_name, self.character)

    def get_all_epic_feats_list(self):
        return get_all_epic_feats()

    def apply_epic_ability_increase(self, ability_name):
        if ability_name in self.character.epic_ability_increases:
            self.character.epic_ability_increases[ability_name] += 1
            current_score = getattr(self.character, ability_name)
            setattr(self.character, ability_name, current_score + 1)

    def update_xp_for_epic_level(self):
        current_level = self.character.get_total_level()
        if current_level >= 20:
            self.character.next_level_xp = get_epic_xp_for_level(current_level + 1)
        else:
            self.character.next_level_xp = (current_level + 1) * 1000