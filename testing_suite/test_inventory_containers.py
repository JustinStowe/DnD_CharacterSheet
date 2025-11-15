from character import Character


def test_container_contents_weight_counting():
    c = Character()
    # Add a normal item
    c.add_item('Rope', 5, 1)
    assert c.get_total_weight_carried() == 5

    # Add a container (bag) with its own weight 2, capacity 50, and contents 10
    contents = [{'name': 'Gem', 'weight': 10, 'quantity': 1, 'notes': ''}]
    c.add_item('Bag of Holding', 2, 1, 'Bag', is_container=True, capacity_lbs=50, count_contents_toward_carry=True, contents=contents)
    # Total should be rope 5 + bag 2 + contents 10 = 17
    assert c.get_total_weight_carried() == 17

    # Now toggle to not count contents toward carried weight
    c.inventory[-1]['count_contents_toward_carry'] = False
    # Now total should be rope 5 + bag 2 (contents excluded) = 7
    assert c.get_total_weight_carried() == 7
