import tkinter as tk
from gui_tabs import MagicItemsTab
from dialogs.magic_item_dialog import MagicItemDialog


def test_magic_item_dialog_ui_ability_description(dummy_gui, monkeypatch):
    gui = dummy_gui
    saved = {}

    def on_save(mi, idx=None):
        saved['mi'] = mi

    # Create and interact with a real dialog to add an ability with description
    # Monkeypatch grab_set to avoid 'another application has grab' errors in headless tests
    monkeypatch.setattr(tk.Toplevel, 'grab_set', lambda self: None)
    try:
        dialog = MagicItemDialog(gui.root, gui.character, None, None, on_save, gui)
        # Set ability fields
        dialog.ability_name_var.set('Divine Burst')
        dialog.ability_cost_var.set(4)
        dialog.ability_desc_text.insert('1.0', 'A spectacular burst of divine energy')
        dialog.name_var.set('Test UI Item')

        # Helper to recursively find button by text
        def find_button_by_text(root_widget, text):
            for child in root_widget.winfo_children():
                try:
                    if getattr(child, 'cget', lambda k: None)('text') == text:
                        return child
                except Exception:
                    pass
                res = find_button_by_text(child, text)
                if res:
                    return res
            return None

        # Find the Add Ability button and invoke it
        add_btn = find_button_by_text(dialog.dialog, 'Add Ability')
        assert add_btn is not None
        add_btn.invoke()

        # Find Save button and invoke
        save_btn = find_button_by_text(dialog.dialog, 'Save')
        assert save_btn is not None
        save_btn.invoke()
    finally:
        try:
            dialog.dialog.destroy()
        except Exception:
            pass

    assert 'mi' in saved
    assert 'abilities' in saved['mi']
    assert len(saved['mi']['abilities']) == 1
    assert saved['mi']['abilities'][0]['name'] == 'Divine Burst'
    assert saved['mi']['abilities'][0]['cost'] == 4
    assert saved['mi']['abilities'][0]['description'] == 'A spectacular burst of divine energy'
