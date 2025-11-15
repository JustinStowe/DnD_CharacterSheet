import pytest
from character import Character


def test_feat_manager_add_remove():
    c = Character()
    # No feats initially
    assert not c.has_feat('Power Attack')

    # Add feat
    c.add_feat('Power Attack')
    assert c.has_feat('Power Attack')

    # Remove feat
    c.remove_feat(0)
    assert not c.has_feat('Power Attack')


def test_epic_feat_management_and_ability_increase():
    c = Character()
    # Epic feats list empty
    assert 'Epic Power Attack' not in c.epic_feats

    c.add_epic_feat('Epic Power Attack')
    assert 'Epic Power Attack' in c.epic_feats

    c.remove_epic_feat('Epic Power Attack')
    assert 'Epic Power Attack' not in c.epic_feats

    # Test epic ability increase applies correctly
    c.strength = 10
    before = c.epic_ability_increases['strength']
    c.apply_epic_ability_increase('strength')
    assert c.epic_ability_increases['strength'] == before + 1
    assert c.strength == 11
