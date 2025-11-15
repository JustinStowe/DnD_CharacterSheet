import tkinter as tk
from gui_tabs import MagicItemsTab


def test_magic_items_tab_smoke_instantiation(dummy_gui):
    # Create a minimal DummyGUI with a character and necessary callbacks
    class DummyCharacter:
        def __init__(self):
            self.magic_items = [{'name': 'Ring of Strength', 'equipped': True, 'bonuses': [{'type': 'Strength', 'value': 2}], 'charges': 0, 'max_charges': 0, 'properties': ''}]

    dummy_gui.character = DummyCharacter()
    gui = dummy_gui
    try:
        frame = tk.Frame(gui.root)
        mt = MagicItemsTab(frame, gui)
        mt.build()
        # Should be able to refresh items without raising
        mt.refresh_magic_items()
    finally:
        gui.root.destroy()
