
"""
D&D 3rd Edition Interactive Character Sheet GUI
Main application file - Modular tab structure
Organized, efficient, and easy to follow.
"""

# --- Standard Library Imports ---
import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# --- Project Imports ---
from character import Character, CLASS_DEFINITIONS
from dialogs.character_creation_dialog import CharacterCreationDialog
from dialogs.startup_dialog import StartupDialog
from prestige_classes.prestige_classes import (
    PRESTIGE_CLASS_DEFINITIONS,
    get_all_prestige_classes,
    is_prestige_class
)
from Epic_levels.epic_levels import (
    EPIC_FEATS,
    get_epic_level_info,
    get_epic_level_description,
    get_all_epic_feats
)
from gui_tabs import MainTab, SkillsTab, InventoryTab, SpellsTab, FeatsTab, MagicItemsTab

# --- Tab Manager Class ---
class TabManager:
    """
    Manages static tabs for the character sheet GUI.
    Handles notebook creation, tab frame setup, and tab access.
    """
    def __init__(self, root, tab_defs):
        """
        root: parent Tk widget
        tab_defs: list of tuples (tab_name, tab_class)
        """
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        self.tabs = {}
        self.frames = {}
        for name, tab_class in tab_defs:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=name)
            self.frames[name] = frame
            self.tabs[name] = tab_class(frame)

    def get_tab(self, name):
        return self.tabs.get(name)

    def get_frame(self, name):
        return self.frames.get(name)

    def build_all(self):
        for tab in self.tabs.values():
            if hasattr(tab, 'build'):
                tab.build()

    def update_tab(self, name):
        tab = self.get_tab(name)
        if tab and hasattr(tab, 'update'):
            tab.update()

    def get_notebook(self):
        return self.notebook

# --- Main GUI Class ---


class CharacterSheetGUI:
    """
    Main GUI for the D&D 3e Character Sheet
    Organized by: Initialization, Menu, Dialogs, Tab Setup, Update, Save/Load, Utility
    """

    # --- Initialization ---
    def __init__(self, root):
        self.root = root
        self.root.title("D&D 3rd Edition Character Sheet")
        self.root.geometry("1200x800")
        
        # Create character instance
        self.character = Character()
        
        # Track current file
        self.current_file = None
        self.is_modified = False
        
        # Storage for entry widgets to update them
        self.entries = {}
        self.labels = {}
        
        # Create menu bar
        self.create_menu()
        
        # Tab definitions: (tab name, tab class)
        tab_defs = [
            ('Main', lambda frame: MainTab(frame, self)),
            ('Skills', lambda frame: SkillsTab(frame, self)),
            ('Inventory', lambda frame: InventoryTab(frame, self)),
            ('Spells', lambda frame: SpellsTab(frame, self)),
            ('Feats & Abilities', lambda frame: FeatsTab(frame, self)),
            ('Magic Items', lambda frame: MagicItemsTab(frame, self)),
        ]
        self.tab_manager = TabManager(root, tab_defs)

        # Assign tab instances for compatibility
        self.main_tab = self.tab_manager.get_tab('Main')
        self.skills_tab = self.tab_manager.get_tab('Skills')
        self.inventory_tab = self.tab_manager.get_tab('Inventory')
        self.spells_tab = self.tab_manager.get_tab('Spells')
        self.feats_tab = self.tab_manager.get_tab('Feats & Abilities')
        self.magic_items_tab = self.tab_manager.get_tab('Magic Items')

        # Build all tabs using modular architecture
        self.tab_manager.build_all()
        
        # Initial update - delegate to main tab
        if hasattr(self.main_tab, 'update_class_display'):
            self.main_tab.update_class_display()
        self.update_all_calculated_fields()
        
        # Set up window close protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    # --- Menu Bar ---
    def create_menu(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="New Character", command=self.new_character, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.load_character, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_character, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_character_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_character())
        self.root.bind('<Control-o>', lambda e: self.load_character())
        self.root.bind('<Control-s>', lambda e: self.save_character())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_character_as())
    
    # --- Window Close Handling ---
    def on_closing(self):
        """Handle window close event"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "Do you want to save changes before closing?"
            )
            if response is True:  # Yes
                self.save_character()
                self.root.destroy()
            elif response is False:  # No
                self.root.destroy()
            # None/Cancel - do nothing
        else:
            self.root.destroy()
    
    # --- Modification Tracking ---
    def mark_modified(self):
        """Mark the character as modified"""
        if not self.is_modified:
            self.is_modified = True
            self.update_title()
    
    # --- Title Update ---
    def update_title(self):
        """Update window title with file name and modified status"""
        title = "D&D 3rd Edition Character Sheet"
        if self.current_file:
            filename = os.path.basename(self.current_file)
            title = f"{filename} - {title}"
        if self.is_modified:
            title = f"*{title}"
        self.root.title(title)
    
    # --- Character Creation ---
    def new_character(self):
        """Create a new character"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "Do you want to save changes before creating a new character?"
            )
            if response is True:  # Yes
                self.save_character()
            elif response is None:  # Cancel
                return
        
        # Show character creation dialog
        if self.show_character_creation_dialog():
            # Update all tabs' character references
            self.main_tab.character = self.character
            self.skills_tab.character = self.character
            self.inventory_tab.character = self.character
            self.spells_tab.character = self.character
            self.feats_tab.character = self.character
            self.magic_items_tab.character = self.character
            
            # Reset GUI after character creation
            self.current_file = None
            self.is_modified = False
            self.populate_fields_from_character()
            self.update_all_calculated_fields()
            
            # Update class display
            if hasattr(self.main_tab, 'update_class_display'):
                self.main_tab.update_class_display()
            
            # Refresh skills display
            if hasattr(self.skills_tab, 'refresh_skills_display'):
                self.skills_tab.refresh_skills_display()
            
            self.update_title()
    
    # --- Character Creation Dialog ---
    def show_character_creation_dialog(self):
        """Show dialog for creating a new character. Returns True if character was created."""
        dialog = CharacterCreationDialog(
            self.root,
            Character,
            CLASS_DEFINITIONS,
            self.bind_mousewheel
        )
        result = dialog.show()
        
        if result['created']:
            self.character = result['character']
            return True
        return False
    
    def load_character(self):
        """Load character from file"""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "Do you want to save changes before loading a character?"
            )
            if response is True:  # Yes
                self.save_character()
            elif response is None:  # Cancel
                return
        
        if filename := filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("Character Files", "*.json"), ("All Files", "*.*")],
            title="Load Character"
        ):
            self.load_from_file(filename)
    
    def load_from_file(self, filename):
        """Load character data from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Load data into character
            self.character.from_dict(data)
            
            # Update all tabs' character references (in case object was recreated)
            self.main_tab.character = self.character
            self.skills_tab.character = self.character
            self.inventory_tab.character = self.character
            self.spells_tab.character = self.character
            self.feats_tab.character = self.character
            self.magic_items_tab.character = self.character
            
            # Update GUI
            self.populate_fields_from_character()
            self.update_all_calculated_fields()
            
            # Update class display
            if hasattr(self.main_tab, 'update_class_display'):
                self.main_tab.update_class_display()
            
            # Refresh displays in tabs
            if hasattr(self.skills_tab, 'refresh_skills_display'):
                self.skills_tab.refresh_skills_display()
            if hasattr(self.inventory_tab, 'update_inventory_display'):
                self.inventory_tab.update_inventory_display()
            if hasattr(self.inventory_tab, 'load_currency'):
                self.inventory_tab.load_currency()
            
            self.current_file = filename
            self.is_modified = False
            self.update_title()
            messagebox.showinfo("Success", f"Character loaded from {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load character: {str(e)}")
    
    # --- Save Character ---
    def save_character(self):
        """Save character to current file or prompt for new file"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_character_as()
    
    def save_character_as(self):
        """Save character to a new file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Character Files", "*.json"), ("All Files", "*.*")],
            title="Save Character"
        )
        if filename:
            self.save_to_file(filename)
    
    def save_to_file(self, filename):
        """Save character data to JSON file"""
        try:
            # Update character from GUI fields
            self.update_character_from_gui()
            
            # Save to file
            with open(filename, 'w') as f:
                json.dump(self.character.to_dict(), f, indent=2)
            
            self.current_file = filename
            self.is_modified = False
            self.update_title()
            messagebox.showinfo("Success", f"Character saved to {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save character: {str(e)}")
    
    # --- Update from GUI ---
    def update_character_from_gui(self):
        """Update character object from all GUI fields"""
        # Basic info
        self.character.name = self.entries['name'].get()
        self.character.player = self.entries['player'].get()
        # Class is now managed through multiclass system, not a simple entry field
        self.character.level = self.get_entry_int('level', 1)
        self.character.race = self.entries['race'].get()
        self.character.alignment = self.entries['alignment'].get()
        
        # Additional character details
        if 'deity' in self.entries:
            self.character.deity = self.entries['deity'].get()
        if 'gender' in self.entries:
            self.character.gender = self.entries['gender'].get()
        if 'height' in self.entries:
            self.character.height = self.entries['height'].get()
        if 'weight' in self.entries:
            self.character.weight = self.entries['weight'].get()
        if 'hair_color' in self.entries:
            self.character.hair_color = self.entries['hair_color'].get()
        if 'eye_color' in self.entries:
            self.character.eye_color = self.entries['eye_color'].get()
        
        # Ability scores (already updated through individual handlers)
        # HP
        self.character.max_hp = self.get_entry_int('max_hp', 0)
        self.character.current_hp = self.get_entry_int('current_hp', 0)
        
        # AC components - read base values only (not including magic bonuses)
        self.character.armor_bonus = self.get_entry_int('armor_bonus', 0)
        self.character.shield_bonus = self.get_entry_int('shield_bonus', 0)
        self.character.natural_armor = self.get_entry_int('natural_armor', 0)
        self.character.deflection_bonus = self.get_entry_int('deflection_bonus', 0)
        self.character.misc_ac_bonus = self.get_entry_int('misc_ac_bonus', 0)
        
        # Saving throw components - read base values only (not including magic bonuses)
        self.character.fort_base = self.get_entry_int('fort_base', 0)
        self.character.fort_misc = self.get_entry_int('fort_misc', 0)
        self.character.ref_base = self.get_entry_int('ref_base', 0)
        self.character.ref_misc = self.get_entry_int('ref_misc', 0)
        self.character.will_base = self.get_entry_int('will_base', 0)
        self.character.will_misc = self.get_entry_int('will_misc', 0)
        
        # Skills and other fields are already updated through their handlers
    
    # --- Populate GUI from Character ---
    def populate_fields_from_character(self):
        """Populate all GUI fields from character object"""
        # Basic info
        self.set_entry('name', self.character.name)
        self.set_entry('player', self.character.player)
        if hasattr(self, 'class_var'):
            self.class_var.set(self.character.character_class)
        # For multiclass, use get_total_level if available
        if hasattr(self.character, 'get_total_level') and callable(self.character.get_total_level):
            self.set_entry('level', str(self.character.get_total_level()))
        else:
            self.set_entry('level', str(self.character.level))
        self.set_entry('race', self.character.race)
        self.set_entry('alignment', self.character.alignment)
        
        # Additional character details
        if 'deity' in self.entries:
            self.set_entry('deity', self.character.deity)
        if 'gender' in self.entries:
            self.set_entry('gender', self.character.gender)
        if 'height' in self.entries:
            self.set_entry('height', self.character.height)
        if 'weight' in self.entries:
            self.set_entry('weight', self.character.weight)
        if 'hair_color' in self.entries:
            self.set_entry('hair_color', self.character.hair_color)
        if 'eye_color' in self.entries:
            self.set_entry('eye_color', self.character.eye_color)
        
        # XP
        if 'experience' in self.entries:
            self.set_entry('experience', str(self.character.experience))
        if 'next_level_xp' in self.labels:
            self.labels['next_level_xp'].config(text=str(self.character.next_level_xp))
        
        # Ability scores
        abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        for ability in abilities:
            score = getattr(self.character, ability)
            self.set_entry(ability, str(score))
            
            temp_mod = getattr(self.character, f'{ability[0:3]}_temp_mod')
            self.set_entry(f'{ability}_temp', str(temp_mod))
        
        # HP
        self.set_entry('max_hp', str(self.character.max_hp))
        self.set_entry('current_hp', str(self.character.current_hp))
        
        # Saves
        self.set_entry('fort_base', str(self.character.fort_base))
        self.set_entry('ref_base', str(self.character.ref_base))
        self.set_entry('will_base', str(self.character.will_base))
        self.set_entry('fort_misc', str(self.character.fort_misc))
        self.set_entry('ref_misc', str(self.character.ref_misc))
        self.set_entry('will_misc', str(self.character.will_misc))
        
        # AC
        self.set_entry('armor_bonus', str(self.character.armor_bonus))
        self.set_entry('shield_bonus', str(self.character.shield_bonus))
        self.set_entry('natural_armor', str(self.character.natural_armor))
        self.set_entry('deflection_bonus', str(self.character.deflection_bonus))
        self.set_entry('misc_ac_bonus', str(self.character.misc_ac_bonus))
        
        # Combat
        self.set_entry('bab', str(self.character.base_attack_bonus))
        self.set_entry('initiative_misc', str(self.character.initiative_misc))
        self.set_entry('spell_resistance', str(self.character.spell_resistance))
        
        # Skills
        for skill_name, ranks in self.character.skills.items():
            skill_ranks_key = f'skill_ranks_{skill_name}'
            skill_misc_key = f'skill_misc_{skill_name}'
            if skill_ranks_key in self.entries:
                self.set_entry(skill_ranks_key, str(ranks))
            if skill_misc_key in self.entries:
                misc = self.character.skill_misc.get(skill_name, 0)
                self.set_entry(skill_misc_key, str(misc))
        
        # Update skill points displays
        if 'skill_points_available' in self.labels:
            self.labels['skill_points_available'].config(text=str(self.character.skill_points_available))
        if 'skill_points_spent' in self.labels:
            total_spent = sum(self.character.skills.values())
            self.labels['skill_points_spent'].config(text=str(total_spent))
        
        # Spellcasting (delegate to spells tab if available)
        if hasattr(self, 'spells_tab'):
            if hasattr(self.spells_tab, 'update') and callable(self.spells_tab.update):
                self.spells_tab.update()
            else:
                raise NotImplementedError(
                    "spells_tab must implement an 'update' method. "
                    "Please ensure the spells_tab object provides an 'update()' method for proper integration."
                )
        
        # Feats and Abilities
        if hasattr(self, 'feats_tab'):
            if hasattr(self.feats_tab, 'update_feats_display'):
                self.feats_tab.update_feats_display()
            if hasattr(self.feats_tab, 'update_abilities_display'):
                self.feats_tab.update_abilities_display()
        
        # Weapons and Magic Items (delegate to tabs if available)
        if hasattr(self, 'main_tab') and hasattr(self.main_tab, 'refresh_weapons'):
            self.main_tab.refresh_weapons()
        if hasattr(self, 'magic_items_tab') and hasattr(self.magic_items_tab, 'refresh_magic_items'):
            self.magic_items_tab.refresh_magic_items()
        
        # Update AC display to show magic item bonuses
        self.update_ac_display()
        
        # Update saving throw display to show magic item bonuses
        self.update_saves_display()
    
    # --- Entry Helpers ---
    def set_entry(self, key, value):
        """Set the value of an entry widget"""
        if key in self.entries:
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)
    
    def create_labeled_entry(self, parent, label_text, row, col, width=10, state='normal'):
        """Helper to create a label and entry pair"""
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, sticky='e', padx=2, pady=2)
        
        entry = ttk.Entry(parent, width=width, state=state)
        entry.grid(row=row, column=col+1, sticky='w', padx=2, pady=2)
        
        return entry
    
    def create_labeled_readonly(self, parent, label_text, row, col, width=10):
        """Helper to create a label and readonly entry pair"""
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, sticky='e', padx=2, pady=2)
        
        entry = ttk.Entry(parent, width=width, state='readonly')
        entry.grid(row=row, column=col+1, sticky='w', padx=2, pady=2)
        
        return entry
    
    # --- Mousewheel Binding ---
    def bind_mousewheel(self, canvas):
        """Bind mouse wheel scrolling to a canvas"""
        def on_mousewheel(event):
            # Check if canvas still exists
            try:
                if canvas.winfo_exists():
                    # Windows and MacOS have different scroll event values
                    if event.num == 5 or event.delta < 0:
                        # Scroll down
                        canvas.yview_scroll(1, "units")
                    elif event.num == 4 or event.delta > 0:
                        # Scroll up
                        canvas.yview_scroll(-1, "units")
            except:
                # Canvas no longer exists, ignore
                pass
        
        def on_enter(event):
            # Bind mouse wheel when mouse enters the canvas
            canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows
            canvas.bind_all("<Button-4>", on_mousewheel)     # Linux scroll up
            canvas.bind_all("<Button-5>", on_mousewheel)     # Linux scroll down
        
        def on_leave(event):
            # Unbind mouse wheel when mouse leaves the canvas
            try:
                canvas.unbind_all("<MouseWheel>")
                canvas.unbind_all("<Button-4>")
                canvas.unbind_all("<Button-5>")
            except:
                pass
        
        # Bind enter/leave events
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
    
    # build_main_tab() removed - now using modular MainTab
    
    # --- Utility: Entry Integer ---
    def get_entry_int(self, key, default=0):
        """Get integer value from entry widget. Logs errors for debugging."""
        try:
            value = self.entries[key].get()
            return int(value) if value else default
        except KeyError:
            print(f"[get_entry_int] KeyError: '{key}' not found in entries.")
            return default
        except ValueError:
            print(f"[get_entry_int] ValueError: '{key}' value '{self.entries[key].get()}' is not an int.")
            return default
    
    # --- Ability Score Update ---
    def update_ability_score(self, ability):
        """Update ability score and all dependent fields"""
        # Delegate to main_tab if it exists
        if hasattr(self, 'main_tab') and hasattr(self.main_tab, 'update_ability_score'):
            self.main_tab.update_ability_score(ability)
        self.update_all_calculated_fields()
    
    # --- Update from Entry ---
    def update_from_entry(self, field_name):
        """Update a character field from entry widget, with dynamic whitelist validation."""
        # Dynamically generate allowed fields from character attributes
        allowed_fields = set(vars(self.character).keys())
        if field_name not in allowed_fields:
            print(f"[update_from_entry] Attempt to set disallowed field: {field_name}")
            return
        value = self.entries[field_name].get()
        try:
            value = int(value)
        except ValueError:
            pass  # Keep as string
        setattr(self.character, field_name, value)
        self.update_all_calculated_fields()
    
    # --- Calculated Field Updates ---
    def update_all_calculated_fields(self):
        """Update all calculated/derived fields"""
        # Update ability modifiers
        abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        ability_funcs = [
            self.character.get_str_modifier,
            self.character.get_dex_modifier,
            self.character.get_con_modifier,
            self.character.get_int_modifier,
            self.character.get_wis_modifier,
            self.character.get_cha_modifier
        ]
        
        # Map of canonical ability names to equipment bonus keys
        equip_map = {
            'strength': 'Strength',
            'dexterity': 'Dexterity',
            'constitution': 'Constitution',
            'intelligence': 'Intelligence',
            'wisdom': 'Wisdom',
            'charisma': 'Charisma'
        }
        for ability, func in zip(abilities, ability_funcs):
            mod = func()
            mod_str = f"+{mod}" if mod >= 0 else str(mod)
            self.labels[f'{ability}_mod'].config(text=mod_str)

            # Equipment bonus for ability - show a blue label if non-zero
            equip_key = equip_map.get(ability, ability.capitalize())
            equip_val = self.character.get_equipment_bonus(equip_key)
            equip_label_key = f'{ability}_equip'
            if equip_label_key in self.labels:
                if equip_val != 0:
                    if equip_val > 0:
                        text = f"+{equip_val} (magic)"
                        color = 'blue'
                    else:
                        text = f"{equip_val} (magic)"
                        color = 'red'
                    try:
                        self.labels[equip_label_key].config(text=text, foreground=color)
                    except Exception:
                        self.labels[equip_label_key].config(text=text, fg=color)
                else:
                    self.labels[equip_label_key].config(text="")
        
        # Update saving throws
        # Read base values only from entry fields (not including magic bonuses)
        self.character.fort_base = self.get_entry_int('fort_base', 0)
        self.character.ref_base = self.get_entry_int('ref_base', 0)
        self.character.will_base = self.get_entry_int('will_base', 0)
        self.character.fort_misc = self.get_entry_int('fort_misc', 0)
        self.character.ref_misc = self.get_entry_int('ref_misc', 0)
        self.character.will_misc = self.get_entry_int('will_misc', 0)
        
        # Update save displays
        fort = self.character.get_fortitude_save()
        ref = self.character.get_reflex_save()
        will = self.character.get_will_save()
        
        fort_str = f"+{fort}" if fort >= 0 else str(fort)
        ref_str = f"+{ref}" if ref >= 0 else str(ref)
        will_str = f"+{will}" if will >= 0 else str(will)
        
        self.labels['fort_total'].config(text=fort_str)
        self.labels['ref_total'].config(text=ref_str)
        self.labels['will_total'].config(text=will_str)
        
        # Update ability contributions to saves
        con_mod = self.character.get_con_modifier()
        dex_mod = self.character.get_dex_modifier()
        wis_mod = self.character.get_wis_modifier()
        
        self.labels['fort_ability'].config(text=f"+{con_mod}" if con_mod >= 0 else str(con_mod))
        self.labels['ref_ability'].config(text=f"+{dex_mod}" if dex_mod >= 0 else str(dex_mod))
        self.labels['will_ability'].config(text=f"+{wis_mod}" if wis_mod >= 0 else str(wis_mod))
        
        # Update AC - only read base values from entry fields
        # Equipment bonuses are added separately in get_ac()
        self.character.armor_bonus = self.get_entry_int('armor_bonus', 0)
        self.character.shield_bonus = self.get_entry_int('shield_bonus', 0)
        self.character.natural_armor = self.get_entry_int('natural_armor', 0)
        self.character.deflection_bonus = self.get_entry_int('deflection_bonus', 0)
        self.character.misc_ac_bonus = self.get_entry_int('misc_ac_bonus', 0)
        
        ac = self.character.get_ac()
        touch_ac = self.character.get_touch_ac()
        flat_ac = self.character.get_flat_footed_ac()
        
        self.labels['ac_total'].config(text=str(ac))
        self.labels['touch_ac'].config(text=str(touch_ac))
        self.labels['flatfooted_ac'].config(text=str(flat_ac))
        self.labels['dex_ac'].config(text=f"+{dex_mod}" if dex_mod >= 0 else str(dex_mod))
        
        # Update Initiative
        self.character.initiative_misc = self.get_entry_int('initiative_misc', 0)
        initiative = self.character.get_initiative()
        init_str = f"+{initiative}" if initiative >= 0 else str(initiative)
        self.labels['initiative'].config(text=init_str)
        
        # Update Attack Bonuses
        self.character.base_attack_bonus = self.get_entry_int('bab', 0)
        melee = self.character.get_melee_attack_bonus()
        ranged = self.character.get_ranged_attack_bonus()
        
        melee_str = f"+{melee}" if melee >= 0 else str(melee)
        ranged_str = f"+{ranged}" if ranged >= 0 else str(ranged)
        
        self.labels['melee_attack'].config(text=melee_str)
        self.labels['ranged_attack'].config(text=ranged_str)
        
        # Update Skills (delegate to skills tab if available)
        if hasattr(self, 'skills_tab') and hasattr(self.skills_tab, 'refresh_skills_display'):
            self.skills_tab.refresh_skills_display()
        
        # Update AC displays
        self.update_ac_display()
        
        # Update saving throw displays
        self.update_saves_display()
        
        # Update spell DCs (if spells tab exists)
        if hasattr(self, 'spells_tree'):
            self.update_spell_dcs()
        
        # Update weapons display (attack bonuses depend on BAB and ability scores)
        if hasattr(self, 'main_tab') and hasattr(self.main_tab, 'refresh_weapons'):
            self.main_tab.refresh_weapons()
    
    # --- AC Display Update ---
    def update_ac_display(self):
        """Update all AC-related displays"""
        # Only update if labels exist (they may not be created yet during init)
        if 'ac_total' not in self.labels:
            return
            
        # Calculate AC values
        ac = self.character.get_ac()
        touch_ac = self.character.get_touch_ac()
        flat_footed_ac = self.character.get_flat_footed_ac()
        
        # Update total AC labels
        self.labels['ac_total'].config(text=str(ac))
        if 'touch_ac' in self.labels:
            self.labels['touch_ac'].config(text=str(touch_ac))
        if 'flatfooted_ac' in self.labels:
            self.labels['flatfooted_ac'].config(text=str(flat_footed_ac))
        
        # Update individual component labels to show magic bonuses
        magic_armor = self.character.get_equipment_bonus('Armor')
        magic_shield = self.character.get_equipment_bonus('Shield')
        magic_natural = self.character.get_equipment_bonus('Natural Armor')
        magic_deflection = self.character.get_equipment_bonus('Deflection')
        
        # Update magic bonus display labels
        if hasattr(self, 'main_tab') and hasattr(self.main_tab, 'update_ac_components'):
            self.main_tab.update_ac_components(magic_armor, magic_shield, magic_natural, magic_deflection)
    
    # --- Saving Throw Display Update ---
    def update_saves_display(self):
        """Update all saving throw displays including magic bonuses"""
        # Only update if labels exist
        if 'fort_total' not in self.labels:
            return
        
        # Calculate saving throw values
        fort = self.character.get_fortitude_save()
        ref = self.character.get_reflex_save()
        will = self.character.get_will_save()
        
        # Update total saving throw labels
        self.labels['fort_total'].config(text=f"+{fort}" if fort >= 0 else str(fort))
        self.labels['ref_total'].config(text=f"+{ref}" if ref >= 0 else str(ref))
        self.labels['will_total'].config(text=f"+{will}" if will >= 0 else str(will))
        
        # Get magic resistance bonus
        magic_resistance = self.character.get_equipment_bonus('Resistance (All Saves)')
        
        # Update magic bonus display labels
        if hasattr(self, 'main_tab') and hasattr(self.main_tab, 'update_save_components'):
            self.main_tab.update_save_components(magic_resistance)


def show_startup_dialog():
    """Show startup dialog to choose between new character or load existing"""
    dialog = StartupDialog()
    return dialog.show()
  

def main():
    """
    Main entry point for the D&D 3e Character Sheet GUI.
    Shows startup dialog, then launches main app window.
    """
    # Show startup dialog (choose new or load character)
    choice = show_startup_dialog()
    if choice['action'] is None:
        return  # User cancelled

    # Ensure dialog cleanup before main window
    import time
    time.sleep(0.1)

    # Create main window and app
    root = tk.Tk()
    app = CharacterSheetGUI(root)

    # Handle user choice
    if choice['action'] == 'new':
        app.new_character()  # Open character creation dialog immediately
    elif choice['action'] == 'load' and choice['file']:
        app.load_from_file(choice['file'])

    root.focus_force()
    root.mainloop()


if __name__ == '__main__':
    main()
