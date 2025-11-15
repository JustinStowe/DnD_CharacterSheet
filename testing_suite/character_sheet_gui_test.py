import pytest
import tkinter as tk
from tkinter import messagebox, filedialog
import types
import os
import json

# Import the class under test
from character_sheet_gui import CharacterSheetGUI, show_startup_dialog

# Determine if Tk is usable in this environment. If not, we'll skip tests that require
# a real Tk instance to avoid failing in headless CI environments or systems without
# a configured Tcl/Tk runtime (which raises TclError on tk.Tk()).
try:
    _tmp_root = tk.Tk()
    _tmp_root.withdraw()
    _tmp_root.destroy()
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False
# dummy_gui fixture is provided centrally by testing_suite/conftest.py


class DummyCharacter:
    """Minimal stub for Character with required attributes and methods used by tests."""
    def __init__(self):
        self.name = ""
        self.player = ""
        self.race = ""
        self.alignment = ""
        self.deity = ""
        self.gender = ""
        self.height = ""
        self.weight = ""
        self.hair_color = ""
        self.eye_color = ""
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.level = 1
        self.character_class = "Fighter"
        self.classes = [{'name': 'Fighter', 'level': 1}]
        self.max_hp = 10
        self.current_hp = 10
        self.hit_dice = [10]
        self.experience = 0
        self.next_level_xp = 1000
        self.fort_base = 0
        self.fort_misc = 0
        self.ref_base = 0
        self.ref_misc = 0
        self.will_base = 0
        self.will_misc = 0
        self.armor_bonus = 0
        self.shield_bonus = 0
        self.natural_armor = 0
        self.deflection_bonus = 0
        self.misc_ac_bonus = 0
        self.base_attack_bonus = 0
        self.initiative_misc = 0
        self.spell_resistance = 0
        self.skills = {}
        self.skill_misc = {}
        self.skill_points_available = 0
        self.to_dict_called = False
        self.from_dict_called = False
        self.skill_points_spent = 0
        self.str_temp_mod = 0
        self.dex_temp_mod = 0
        self.con_temp_mod = 0
        self.int_temp_mod = 0
        self.wis_temp_mod = 0
        self.cha_temp_mod = 0

    def to_dict(self):
        self.to_dict_called = True
        return {"name": self.name}

    def from_dict(self, data):
        self.from_dict_called = True
        self.name = data.get("name", "")

    def get_con_modifier(self): return 0
    def get_str_modifier(self): return 0
    def get_dex_modifier(self): return 0
    def get_int_modifier(self): return 0
    def get_wis_modifier(self): return 0
    def get_cha_modifier(self): return 0
    def update_class_based_stats(self): pass
    def get_fortitude_save(self): return 1
    def get_reflex_save(self): return 2
    def get_will_save(self): return 3
    def get_ac(self): return 15
    def get_touch_ac(self): return 12
    def get_flat_footed_ac(self): return 13
    def get_initiative(self): return 1
    def get_melee_attack_bonus(self): return 2
    def get_ranged_attack_bonus(self): return 3
    def get_equipment_bonus(self, _): return 0


# --- Tests ---

@pytest.mark.parametrize(
    "is_modified, user_response, expected_destroy, test_id",
    [
        (True, True, True, "modified_yes_save"),
        (True, False, True, "modified_no_save"),
        (True, None, False, "modified_cancel"),
        (False, None, True, "not_modified"),
    ],
    ids=["modified_yes_save", "modified_no_save", "modified_cancel", "not_modified"]
)
def test_on_closing(monkeypatch, dummy_gui, is_modified, user_response, expected_destroy, test_id):
    # Arrange
    dummy_gui.is_modified = is_modified
    destroyed = []
    monkeypatch.setattr(dummy_gui.root, "destroy", lambda: destroyed.append(True))
    monkeypatch.setattr(messagebox, "askyesnocancel", lambda *a, **k: user_response)
    dummy_gui.save_character = lambda: destroyed.append("saved")

    # Act
    dummy_gui.on_closing()

    # Assert
    if expected_destroy:
        assert destroyed, f"{test_id}: Window should be destroyed"
    else:
        assert not destroyed, f"{test_id}: Window should not be destroyed"

@pytest.mark.parametrize(
    "current_file, expected_file, test_id",
    [
        ("file.json", "file.json", "has_current_file"),
        (None, "testfile.json", "no_current_file"),
    ],
    ids=["has_current_file", "no_current_file"]
)
def test_save_character(monkeypatch, dummy_gui, current_file, expected_file, test_id):
    # Arrange
    dummy_gui.current_file = current_file
    called = {}
    dummy_gui.save_to_file = lambda filename: called.setdefault("file", filename)
    dummy_gui.save_character_as = lambda: called.setdefault("as", True)

    # Act
    dummy_gui.save_character()

    # Assert
    if current_file:
        assert called["file"] == expected_file
    else:
        assert called["as"] is True

def test_save_character_as(monkeypatch, dummy_gui, tmp_path):
    # Arrange
    filename = str(tmp_path / "char.json")
    monkeypatch.setattr(filedialog, "asksaveasfilename", lambda **kwargs: filename)
    called = {}
    dummy_gui.save_to_file = lambda fn: called.setdefault("file", fn)

    # Act
    dummy_gui.save_character_as()

    # Assert
    assert called["file"] == filename

def test_save_to_file_success(monkeypatch, dummy_gui, tmp_path):
    # Arrange
    filename = str(tmp_path / "char.json")
    dummy_gui.character = DummyCharacter()
    dummy_gui.update_character_from_gui = lambda: None
    called = {}
    monkeypatch.setattr(messagebox, "showinfo", lambda *a, **k: called.setdefault("info", True))

    # Act
    dummy_gui.save_to_file(filename)

    # Assert
    assert os.path.exists(filename)
    with open(filename) as f:
        data = json.load(f)
    assert "name" in data
    assert called["info"]

def test_save_to_file_error(monkeypatch, dummy_gui):
    # Arrange
    dummy_gui.character = DummyCharacter()
    dummy_gui.update_character_from_gui = lambda: (_ for _ in ()).throw(Exception("fail"))
    called = {}
    monkeypatch.setattr(messagebox, "showerror", lambda *a, **k: called.setdefault("error", True))

    # Act
    dummy_gui.save_to_file("badfile.json")

    # Assert
    assert called["error"]

@pytest.mark.parametrize(
    "is_modified, user_response, expected_load, test_id",
    [
        (True, True, True, "modified_yes_save"),
        (True, None, False, "modified_cancel"),
        (False, None, True, "not_modified"),
    ],
    ids=["modified_yes_save", "modified_cancel", "not_modified"]
)
def test_load_character(monkeypatch, dummy_gui, is_modified, user_response, expected_load, test_id):
    # Arrange
    dummy_gui.is_modified = is_modified
    called = {}
    dummy_gui.save_character = lambda: called.setdefault("save", True)
    dummy_gui.load_from_file = lambda fn: called.setdefault("load", fn)
    monkeypatch.setattr(messagebox, "askyesnocancel", lambda *a, **k: user_response)
    monkeypatch.setattr(filedialog, "askopenfilename", lambda **kwargs: "testfile.json")

    # Act
    dummy_gui.load_character()

    # Assert
    if expected_load:
        assert "load" in called
    else:
        assert "load" not in called

def test_load_from_file_success(monkeypatch, dummy_gui, tmp_path):
    # Arrange
    filename = str(tmp_path / "char.json")
    with open(filename, "w") as f:
        json.dump({"name": "Test"}, f)
    dummy_gui.character = DummyCharacter()
    called = {}
    monkeypatch.setattr(messagebox, "showinfo", lambda *a, **k: called.setdefault("info", True))

    # Act
    dummy_gui.load_from_file(filename)

    # Assert
    assert dummy_gui.character.name == "Test"
    assert called["info"]

def test_load_from_file_error(monkeypatch, dummy_gui):
    # Arrange
    called = {}
    monkeypatch.setattr(messagebox, "showerror", lambda *a, **k: called.setdefault("error", True))

    # Act
    dummy_gui.load_from_file("nonexistent.json")

    # Assert
    assert called["error"]

@pytest.mark.parametrize(
    "entry_value, expected, test_id",
    [
        ("5", 5, "valid_int"),
        ("", 1, "empty_default"),
        ("abc", 1, "invalid_int"),
    ],
    ids=["valid_int", "empty_default", "invalid_int"]
)
def test_get_entry_int(dummy_gui, entry_value, expected, test_id):
    # Arrange
    dummy_gui.entries["level"].delete(0, tk.END)
    dummy_gui.entries["level"].insert(0, entry_value)

    # Act
    result = dummy_gui.get_entry_int("level", 1)

    # Assert
    assert result == expected

def test_set_entry(dummy_gui):
    # Arrange
    dummy_gui.entries["name"].delete(0, tk.END)

    # Act
    dummy_gui.set_entry("name", "Bob")

    # Assert
    assert dummy_gui.entries["name"].get() == "Bob"

def test_update_from_entry_valid(dummy_gui):
    # Arrange
    dummy_gui.entries["name"].delete(0, tk.END)
    dummy_gui.entries["name"].insert(0, "Alice")

    # Act
    dummy_gui.update_from_entry("name")

    # Assert
    assert dummy_gui.character.name == "Alice"

def test_update_from_entry_invalid(dummy_gui):
    # Arrange
    # Not in allowed_fields
    dummy_gui.entries["foo"] = tk.Entry(dummy_gui.root)
    dummy_gui.entries["foo"].insert(0, "bar")

    # Act
    dummy_gui.update_from_entry("foo")

    # Assert
    assert not hasattr(dummy_gui.character, "foo")

def test_update_all_calculated_fields(dummy_gui):
    # Arrange
    # All labels and entries are already set up in dummy_gui fixture

    # Act
    dummy_gui.update_all_calculated_fields()

    # Assert
    # Check that label text is updated (should be set to string values)
    assert dummy_gui.labels["ac_total"].cget("text") == "15"
    assert dummy_gui.labels["fort_total"].cget("text") == "+1"
    assert dummy_gui.labels["ref_total"].cget("text") == "+2"
    assert dummy_gui.labels["will_total"].cget("text") == "+3"

def test_update_ac_display(dummy_gui):
    # Arrange
    # All labels and main_tab are set up

    # Act
    dummy_gui.update_ac_display()

    # Assert
    assert dummy_gui.labels["ac_total"].cget("text") == "15"

def test_update_saves_display(dummy_gui):
    # Arrange
    # All labels and main_tab are set up

    # Act
    dummy_gui.update_saves_display()

    # Assert
    assert dummy_gui.labels["fort_total"].cget("text") == "+1"

@pytest.mark.skipif(not TK_AVAILABLE, reason="Tkinter not available")
def test_create_labeled_entry(dummy_gui):
    # Arrange
    parent = tk.Frame(dummy_gui.root)

    # Act
    entry = dummy_gui.create_labeled_entry(parent, "Test", 0, 0)

    # Assert
    assert isinstance(entry, tk.Entry)

@pytest.mark.skipif(not TK_AVAILABLE, reason="Tkinter not available")
def test_create_labeled_readonly(dummy_gui):
    # Arrange
    parent = tk.Frame(dummy_gui.root)

    # Act
    entry = dummy_gui.create_labeled_readonly(parent, "Test", 0, 0)

    # Assert
    assert isinstance(entry, tk.Entry)
    # tk.Entry.cget() may return an index object or a string depending on platform
    # so compare as string to be robust
    assert 'readonly' in str(entry.cget("state"))

@pytest.mark.skipif(not TK_AVAILABLE, reason="Tkinter not available")
def test_bind_mousewheel(dummy_gui):
    # Arrange
    canvas = tk.Canvas(dummy_gui.root)

    # Act
    dummy_gui.bind_mousewheel(canvas)

    # Assert
    # No exception means success
    assert True

def test_update_ability_score(dummy_gui):
    # Arrange
    called = {}
    dummy_gui.main_tab.update_ability_score = lambda ability: called.setdefault("called", ability)

    # Act
    dummy_gui.update_ability_score("strength")

    # Assert
    assert called["called"] == "strength"

def test_populate_fields_from_character(dummy_gui):
    # Arrange
    # All entries and labels are set up

    # Act
    dummy_gui.populate_fields_from_character()

    # Assert
    # Check that entry is set to character name
    assert dummy_gui.entries["name"].get() == ""

@pytest.mark.skipif(not TK_AVAILABLE, reason="Tkinter not available")
def test_show_startup_dialog(monkeypatch):
    # Arrange
    # Patch filedialog to avoid actual file dialog
    monkeypatch.setattr(filedialog, "askopenfilename", lambda **kwargs: "testfile.json")
    # Patch Tk/Toplevel with minimal fake implementations to avoid opening
    # real windows during tests and to avoid recursion in monkeypatching.
    class FakeRoot:
        def mainloop(self):
            return None
        def destroy(self):
            return None
        def withdraw(self):
            return None
        def title(self, *a, **k):
            return None
        def geometry(self, *a, **k):
            return None
        def quit(self):
            return None

    class FakeToplevel:
        def __init__(self, root):
            pass
        def title(self, text):
            return None
        def geometry(self, *a, **k):
            return None
        def update_idletasks(self):
            return None
        def winfo_screenwidth(self):
            return 800
        def winfo_width(self):
            return 400
        def winfo_screenheight(self):
            return 600
        def winfo_height(self):
            return 200
        def protocol(self, *a, **k):
            return None
        def destroy(self):
            return None

    monkeypatch.setattr(tk, "Tk", lambda: FakeRoot())
    monkeypatch.setattr(tk, "Toplevel", lambda root: FakeToplevel(root))
    # Patch dialog methods to simulate user action
    # Simulate user clicking "Create New Character"
    result = {}
    def fake_new_character():
        result["action"] = "new"
        raise SystemExit
    def fake_load_character():
        result["action"] = "load"
        result["file"] = "testfile.json"
        raise SystemExit
    monkeypatch.setattr("tkinter.ttk.Button", lambda *a, **k: type("B", (), {"pack": lambda *a, **k: None})())
    monkeypatch.setattr("tkinter.ttk.Label", lambda *a, **k: type("L", (), {"pack": lambda *a, **k: None})())
    monkeypatch.setattr("tkinter.ttk.Frame", lambda *a, **k: type("F", (), {"pack": lambda *a, **k: None})())
    # Act & Assert
    try:
        show_startup_dialog()
    except SystemExit:
        pass

@pytest.mark.parametrize(
    "field_name, value, expected, test_id",
    [
        ("name", "TestName", "TestName", "set_name"),
        ("level", "5", 5, "set_level"),
        ("max_hp", "20", 20, "set_max_hp"),
    ],
    ids=["set_name", "set_level", "set_max_hp"]
)
def test_update_character_from_gui(dummy_gui, field_name, value, expected, test_id):
    # Arrange
    dummy_gui.entries[field_name].delete(0, tk.END)
    dummy_gui.entries[field_name].insert(0, value)

    # Act
    dummy_gui.update_character_from_gui()

    # Assert
    if field_name == "name":
        assert dummy_gui.character.name == expected
    elif field_name == "level":
        assert dummy_gui.character.level == expected
    elif field_name == "max_hp":
        assert dummy_gui.character.max_hp == expected

@pytest.mark.parametrize(
    "current_file, is_modified, expected_title, test_id",
    [
        (None, False, "D&D 3rd Edition Character Sheet", "no_file_not_modified"),
        ("foo.json", False, "foo.json - D&D 3rd Edition Character Sheet", "file_not_modified"),
        ("foo.json", True, "*foo.json - D&D 3rd Edition Character Sheet", "file_modified"),
    ],
    ids=["no_file_not_modified", "file_not_modified", "file_modified"]
)
def test_update_title(dummy_gui, current_file, is_modified, expected_title, test_id):
    # Arrange
    dummy_gui.current_file = current_file
    dummy_gui.is_modified = is_modified
    dummy_gui.root.title("")

    # Act
    dummy_gui.update_title()

    # Assert
    assert dummy_gui.root.title() == expected_title

def test_mark_modified(dummy_gui):
    # Arrange
    dummy_gui.is_modified = False
    called = {}
    dummy_gui.update_title = lambda: called.setdefault("title", True)

    # Act
    dummy_gui.mark_modified()

    # Assert
    assert dummy_gui.is_modified
    assert called["title"]


def test_magic_item_dialog_integration(monkeypatch, dummy_gui):
    # Arrange
    from gui_tabs import MagicItemsTab
    mt = MagicItemsTab(dummy_gui.root, dummy_gui)
    mt.build()
    dummy_gui.character.magic_items = []

    class FakeMagicItemDialog:
        def __init__(self, parent, character, magic_item=None, item_index=None, on_save=None, gui=None):
            # Immediately call on_save to simulate user saving the dialog
            if on_save:
                mi = {
                    'name': 'Test Item',
                    'type': 'Other',
                    'slot': 'None',
                    'bonuses': [],
                    'charges': 0,
                    'max_charges': 0,
                    'properties': '',
                    'description': '',
                    'equipped': False
                }
                on_save(mi, item_index)

    import sys
    mitc = sys.modules.get(mt.__class__.__module__)
    assert mitc is not None
    monkeypatch.setattr(mitc, 'MagicItemDialog', FakeMagicItemDialog)

    # Act
    mt.show_create_magic_item_dialog()

    # Assert
    assert len(dummy_gui.character.magic_items) == 1
    assert dummy_gui.character.magic_items[0]['name'] == 'Test Item'


def test_magic_item_dialog_abilities_saved(monkeypatch, dummy_gui):
    from gui_tabs import MagicItemsTab
    mt = MagicItemsTab(dummy_gui.root, dummy_gui)
    mt.build()
    dummy_gui.character.magic_items = []

    class FakeMagicItemDialog:
        def __init__(self, parent, character, magic_item=None, item_index=None, on_save=None, gui=None):
            if on_save:
                mi = {
                    'name': 'Test Staff',
                    'type': 'Staff',
                    'slot': 'None',
                    'bonuses': [],
                    'charges': 10,
                    'max_charges': 10,
                    'properties': '',
                    'description': '',
                    'abilities': [{'name': 'Cure', 'cost': 1, 'description': 'Minor heal'}, {'name': 'Greater Cure', 'cost': 3, 'description': 'Larger heal'}],
                    'equipped': False
                }
                on_save(mi, item_index)

    import sys
    mitc = sys.modules.get(mt.__class__.__module__)
    assert mitc is not None
    monkeypatch.setattr(mitc, 'MagicItemDialog', FakeMagicItemDialog)

    # Act
    mt.show_create_magic_item_dialog()

    # Assert
    assert len(dummy_gui.character.magic_items) == 1
    assert dummy_gui.character.magic_items[0]['name'] == 'Test Staff'
    assert 'abilities' in dummy_gui.character.magic_items[0]
    assert len(dummy_gui.character.magic_items[0]['abilities']) == 2
    assert dummy_gui.character.magic_items[0]['abilities'][0]['description'] == 'Minor heal'
    assert dummy_gui.character.magic_items[0]['abilities'][1]['description'] == 'Larger heal'

