import pytest
import tkinter as tk
from gui_tabs import MagicItemsTab, SpellsTab


def test_spell_double_click_mapping():
    # Minimal dummy character with out-of-order spell insertion
    class DummyCharacter:
        def __init__(self):
            # Create spells in non-alphabetical insertion order
            self.spells = [
                {'name': 'Accuracy', 'level': 0},
                {'name': 'Alarm', 'level': 0},
                {'name': 'Arcane Sensitivity', 'level': 0},
                {'name': 'Burning Hands', 'level': 0},
                {'name': 'Comprehend Languages', 'level': 0}
            ]
            self.spell_slots_max = {}
            self.spell_slots_used = {}
            self.spellcasting_ability = 'intelligence'

    class DummyGUI:
        def __init__(self):
            self.character = DummyCharacter()
            self.root = tk.Tk()
            self.root.withdraw()
            self.entries = {}
            self.labels = {}
            self.update_all_calculated_fields = lambda *a, **k: None
            self.update_ac_display = lambda *a, **k: None
            self.update_saves_display = lambda *a, **k: None
            self.mark_modified = lambda *a, **k: None

    gui = DummyGUI()
    try:
        frame = tk.Frame(gui.root)
        st = SpellsTab(frame, gui)
        st.build()
        # Populate GUI display
        st.update_spell_list_display()

        # Get the displayed names in the tree for level 0
        tree = st.spell_level_trees[0]
        displayed = [tree.item(item)['values'][0] for item in tree.get_children()]

        # Compute the expected sorted names
        expected_sorted = sorted([s['name'] for s in gui.character.spells])

        assert displayed == expected_sorted

        # Find index of Comprehend Languages in displayed list
        idx = displayed.index('Comprehend Languages')

        # Verify that mapping from index to sorted list yields the correct spell
        level_spells_sorted = sorted([s for s in gui.character.spells if s['level'] == 0], key=lambda x: x['name'])
        assert level_spells_sorted[idx]['name'] == 'Comprehend Languages'
    finally:
        gui.root.destroy()
