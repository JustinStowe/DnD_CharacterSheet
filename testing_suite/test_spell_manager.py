from character import Character


def test_spell_modifiers_and_dc():
    c = Character()
    # Use intelligence as spellcasting ability
    c.spellcasting_ability = 'intelligence'
    c.intelligence = 18
    m = c.spell_manager

    assert m.get_spellcasting_modifier() == 4
    assert m.get_spell_dc(2) == 10 + 2 + 4


def test_bonus_and_total_spells_per_day_and_slots_update():
    c = Character()
    c.character_class = 'Bard'
    c.level = 2
    c.spellcasting_ability = 'charisma'
    c.charisma = 18
    m = c.spell_manager

    # Base spells for Bard level 2 for 1st level spells is 1
    base = m.get_base_spells_per_day(1)
    assert base == 1

    # Bonus spells should be >0 due to high charisma
    bonus = m.get_bonus_spells(1)
    assert bonus >= 1

    # Total spells per day should include bonus
    total = m.get_total_spells_per_day(1)
    assert total == base + bonus

    # Update slots and verify max slot increment
    c.spell_slots_max = {i: 0 for i in range(10)}
    m.update_spell_slots_from_class()
    assert c.spell_slots_max[1] == total


def test_add_and_remove_spell():
    c = Character()
    m = c.spell_manager
    assert len(c.spells) == 0
    m.add_spell('Magic Missile', 1)
    assert len(c.spells) == 1
    assert c.spells[0]['name'] == 'Magic Missile'
    m.remove_spell(0)
    assert len(c.spells) == 0
