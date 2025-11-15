import tkinter as tk
import pytest
from tkinter import messagebox, filedialog
import types


# Try to detect whether Tk can be created in this environment at test-collection time
try:
    _tmp = tk.Tk()
    _tmp.withdraw()
    _tmp.destroy()
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False


# Fake GUI helper classes for headless testing
class FakeMenu:
    def __init__(self, *a, **k):
        pass
    def add_cascade(self, *a, **k):
        pass
    def add_command(self, *a, **k):
        pass
    def add_separator(self, *a, **k):
        pass


class FakeEntry:
    def __init__(self):
        self._value = ''
    def insert(self, _idx, value):
        self._value = value
    def get(self):
        return self._value
    def delete(self, a, b=None):
        self._value = ''


class FakeLabel:
    def __init__(self):
        self._text = ''
        self._config = {}
    def config(self, **kwargs):
        if 'text' in kwargs:
            self._text = kwargs['text']
        self._config.update(kwargs)
    def cget(self, key):
        if key == 'text':
            return self._text
        return self._config.get(key)


class FakeRoot:
    def withdraw(self):
        pass
    def destroy(self):
        pass
    def title(self, *a, **k):
        pass
    def geometry(self, *a, **k):
        pass
    def config(self, *a, **k):
        pass
    def bind(self, *a, **k):
        pass
    def protocol(self, *a, **k):
        pass
    def focus_force(self):
        pass
    def mainloop(self):
        pass
    def quit(self):
        pass


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


@pytest.fixture
def dummy_gui(monkeypatch):
    # Provide a fake Menu class to avoid native menu allocation in headless tests
    monkeypatch.setattr(tk, 'Menu', FakeMenu)

    if not TK_AVAILABLE:
        pytest.skip("Tkinter is not fully functional in this environment; skipping GUI tests.")

    try:
        root = tk.Tk()
        root.withdraw()
    except tk.TclError:
        pytest.skip("Tkinter can't be instantiated at runtime in this environment; skipping GUI tests.")
    # Create an instance of CharacterSheetGUI with a real tk root
    from character_sheet_gui import CharacterSheetGUI
    gui = CharacterSheetGUI(root)

    # Patch out messagebox and filedialog to avoid GUI popups
    monkeypatch.setattr(messagebox, "askyesnocancel", lambda *a, **k: False)
    monkeypatch.setattr(messagebox, "showinfo", lambda *a, **k: None)
    monkeypatch.setattr(messagebox, "showerror", lambda *a, **k: None)
    monkeypatch.setattr(messagebox, "showwarning", lambda *a, **k: None)
    monkeypatch.setattr(filedialog, "asksaveasfilename", lambda *a, **k: "testfile.json")
    monkeypatch.setattr(filedialog, "askopenfilename", lambda *a, **k: "testfile.json")

    # Provide minimal DummyCharacter for stable test outputs
    class DummyCharacter:
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

    # Provide minimal entries and labels on the GUI
    gui.entries = {k: tk.Entry(root) for k in [
        'name', 'player', 'level', 'race', 'alignment', 'deity', 'gender', 'height', 'weight',
        'hair_color', 'eye_color', 'max_hp', 'current_hp', 'armor_bonus', 'shield_bonus',
        'natural_armor', 'deflection_bonus', 'misc_ac_bonus', 'fort_base', 'fort_misc',
        'ref_base', 'ref_misc', 'will_base', 'will_misc', 'bab', 'initiative_misc',
        'spell_resistance'
    ]}
    for entry in gui.entries.values():
        try:
            entry.insert(0, "1")
        except Exception:
            try:
                entry.insert(None, "1")
            except Exception:
                pass

    gui.labels = {k: tk.Label(root) for k in [
        'strength_mod', 'dexterity_mod', 'constitution_mod', 'intelligence_mod', 'wisdom_mod', 'charisma_mod',
        'fort_total', 'ref_total', 'will_total', 'fort_ability', 'ref_ability', 'will_ability',
        'ac_total', 'touch_ac', 'flatfooted_ac', 'dex_ac', 'initiative', 'melee_attack', 'ranged_attack'
    ]}

    # Patch the Character to a dummy so tests have stable outputs.
    gui.character = DummyCharacter()

    # Patch tab attributes to avoid heavy UI actions
    gui.main_tab = types.SimpleNamespace(update_class_display=lambda: None, update_ac_components=lambda *a: None, update_save_components=lambda *a: None, refresh_weapons=lambda: None)
    gui.skills_tab = types.SimpleNamespace(refresh_skills_display=lambda: None)
    gui.inventory_tab = types.SimpleNamespace(update_inventory_display=lambda: None, load_currency=lambda: None)
    gui.spells_tab = types.SimpleNamespace(update=lambda: None)
    gui.feats_tab = types.SimpleNamespace(update_feats_display=lambda: None, update_abilities_display=lambda: None)
    gui.magic_items_tab = types.SimpleNamespace(refresh_magic_items=lambda: None)
    return gui
