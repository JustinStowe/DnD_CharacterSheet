import tkinter as tk
from gui_tabs import MagicItemsTab


def test_magic_items_tab_smoke_instantiation(dummy_gui):
    # Create a minimal DummyGUI with a character and necessary callbacks
    class DummyCharacter:
        def __init__(self):
            self.magic_items = [{'name': 'Ring of Strength', 'equipped': True, 'bonuses': [{'type': 'Strength', 'value': 2}], 'charges': 0, 'max_charges': 0, 'properties': ''}]

    # Update the existing dummy character's magic_items instead of replacing the object
    dummy_gui.character.magic_items = DummyCharacter().magic_items
    gui = dummy_gui
    try:
        frame = tk.Frame(gui.root)
        mt = MagicItemsTab(frame, gui)
        mt.build()
        # Should be able to refresh items without raising
        mt.refresh_magic_items()
    finally:
        gui.root.destroy()


def test_use_charges_with_abilities(dummy_gui, monkeypatch):
    class DummyCharacter:
        def __init__(self):
            self.magic_items = [{
                'name': 'Staff of the Hierophant',
                'equipped': True,
                'bonuses': [],
                'charges': 20,
                'max_charges': 20,
                'properties': '',
                'abilities': [
                    {'name': 'Cure Wounds', 'cost': 1},
                    {'name': 'Summon Ally', 'cost': 3}
                ]
            }]

    # Update the existing dummy character's magic_items instead of replacing the object
    dummy_gui.character.magic_items = DummyCharacter().magic_items
    gui = dummy_gui
    try:
        frame = tk.Frame(gui.root)
        mt = MagicItemsTab(frame, gui)
        mt.build()
        mt.refresh_magic_items()

        # Select the first item
        items = mt.magic_items_tree.get_children()
        mt.magic_items_tree.selection_set(items[0])

        # Monkeypatch selection dialog to always choose the ability 'Summon Ally' costing 3
        monkeypatch.setattr(mt, '_select_magic_item_ability', lambda mi: mi['abilities'][1])
        # Use charge - should cost 3
        mt.use_magic_item_charge()
        assert dummy_gui.character.magic_items[0]['charges'] == 17

        # Recharge should reset to max
        mt.recharge_magic_item()
        assert dummy_gui.character.magic_items[0]['charges'] == 20
    finally:
        gui.root.destroy()


def test_use_charge_without_abilities(dummy_gui):
    class DummyCharacter:
        def __init__(self):
            self.magic_items = [{
                'name': 'Ring of Warding',
                'equipped': True,
                'bonuses': [],
                'charges': 5,
                'max_charges': 5,
                'properties': ''
            }]

    dummy_gui.character.magic_items = DummyCharacter().magic_items
    gui = dummy_gui
    try:
        frame = tk.Frame(gui.root)
        mt = MagicItemsTab(frame, gui)
        mt.build()
        mt.refresh_magic_items()

        items = mt.magic_items_tree.get_children()
        mt.magic_items_tree.selection_set(items[0])
        mt.use_magic_item_charge()
        assert dummy_gui.character.magic_items[0]['charges'] == 4
    finally:
        gui.root.destroy()
