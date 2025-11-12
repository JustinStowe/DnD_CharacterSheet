"""
D&D 3rd Edition Interactive Character Sheet GUI
Main application file
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from character import Character, CLASS_DEFINITIONS
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


class CharacterSheetGUI:
    """Main GUI for the D&D 3e Character Sheet"""
    
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
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create tabs
        self.main_tab = ttk.Frame(self.notebook)
        self.skills_tab = ttk.Frame(self.notebook)
        self.inventory_tab = ttk.Frame(self.notebook)
        self.spells_tab = ttk.Frame(self.notebook)
        self.feats_tab = ttk.Frame(self.notebook)
        self.magic_items_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.main_tab, text='Main')
        self.notebook.add(self.skills_tab, text='Skills')
        self.notebook.add(self.inventory_tab, text='Inventory')
        self.notebook.add(self.spells_tab, text='Spells')
        self.notebook.add(self.feats_tab, text='Feats & Abilities')
        self.notebook.add(self.magic_items_tab, text='Magic Items')
        
        # Build the UI
        self.build_main_tab()
        self.build_skills_tab()
        self.build_inventory_tab()
        self.build_spells_tab()
        self.build_feats_tab()
        self.build_magic_items_tab()
        
        # Initial update
        self.update_class_display()
        self.update_all_calculated_fields()
        
        # Set up window close protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
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
    
    def mark_modified(self):
        """Mark the character as modified"""
        if not self.is_modified:
            self.is_modified = True
            self.update_title()
    
    def update_title(self):
        """Update window title with file name and modified status"""
        title = "D&D 3rd Edition Character Sheet"
        if self.current_file:
            filename = os.path.basename(self.current_file)
            title = f"{filename} - {title}"
        if self.is_modified:
            title = f"*{title}"
        self.root.title(title)
    
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
        
        # Create new character
        self.character = Character()
        self.current_file = None
        self.is_modified = False
        
        # Reset all GUI fields
        self.populate_fields_from_character()
        self.update_all_calculated_fields()
        self.update_inventory_display()
        self.update_title()
    
    def save_character(self):
        """Save character to current file or prompt for location"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_character_as()
    
    def save_character_as(self):
        """Save character to a new file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Character Files", "*.json"), ("All Files", "*.*")],
            title="Save Character As"
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
        
        filename = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("Character Files", "*.json"), ("All Files", "*.*")],
            title="Load Character"
        )
        
        if filename:
            self.load_from_file(filename)
    
    def load_from_file(self, filename):
        """Load character data from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Load data into character
            self.character.from_dict(data)
            
            # Update GUI
            self.populate_fields_from_character()
            self.update_all_calculated_fields()
            self.update_inventory_display()
            
            self.current_file = filename
            self.is_modified = False
            self.update_title()
            messagebox.showinfo("Success", f"Character loaded from {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load character: {str(e)}")
    
    def update_character_from_gui(self):
        """Update character object from all GUI fields"""
        # Basic info
        self.character.name = self.entries['name'].get()
        self.character.player = self.entries['player'].get()
        self.character.character_class = self.entries['class'].get()
        self.character.level = self.get_entry_int('level', 1)
        self.character.race = self.entries['race'].get()
        self.character.alignment = self.entries['alignment'].get()
        
        # Ability scores (already updated through individual handlers)
        # HP
        self.character.max_hp = self.get_entry_int('max_hp', 0)
        self.character.current_hp = self.get_entry_int('current_hp', 0)
        
        # Skills and other fields are already updated through their handlers
    
    def populate_fields_from_character(self):
        """Populate all GUI fields from character object"""
        # Basic info
        self.set_entry('name', self.character.name)
        self.set_entry('player', self.character.player)
        if hasattr(self, 'class_var'):
            self.class_var.set(self.character.character_class)
        self.set_entry('level', str(self.character.level))
        self.set_entry('race', self.character.race)
        self.set_entry('alignment', self.character.alignment)
        
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
            self.set_entry(f'skill_ranks_{skill_name}', str(ranks))
            misc = self.character.skill_misc.get(skill_name, 0)
            self.set_entry(f'skill_misc_{skill_name}', str(misc))
        
        # Update skill points displays
        if 'skill_points_available' in self.labels:
            self.labels['skill_points_available'].config(text=str(self.character.skill_points_available))
        if 'skill_points_spent' in self.labels:
            total_spent = sum(self.character.skills.values())
            self.labels['skill_points_spent'].config(text=str(total_spent))
        
        # Spellcasting
        if hasattr(self, 'spellcasting_ability_var'):
            self.spellcasting_ability_var.set(self.character.spellcasting_ability)
            
            for level in range(10):
                self.set_entry(f'spell_max_{level}', str(self.character.spell_slots_max.get(level, 0)))
                self.set_entry(f'spell_used_{level}', str(self.character.spell_slots_used.get(level, 0)))
                self.update_spell_slots(level)
            
            self.update_spell_list_display()
        
        # Feats and Abilities
        if hasattr(self, 'feats_tree'):
            self.update_feats_display()
            self.update_abilities_display()
        
        # Weapons and Magic Items
        if hasattr(self, 'weapons_tree'):
            self.refresh_weapons()
        if hasattr(self, 'magic_items_tree'):
            self.refresh_magic_items()
    
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
    
    def bind_mousewheel(self, canvas):
        """Bind mouse wheel scrolling to a canvas"""
        def on_mousewheel(event):
            # Windows and MacOS have different scroll event values
            if event.num == 5 or event.delta < 0:
                # Scroll down
                canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta > 0:
                # Scroll up
                canvas.yview_scroll(-1, "units")
        
        # Bind for different platforms
        canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows
        canvas.bind_all("<Button-4>", on_mousewheel)     # Linux scroll up
        canvas.bind_all("<Button-5>", on_mousewheel)     # Linux scroll down
    
    def build_main_tab(self):
        """Build the main character sheet tab"""
        # Create scrollable frame
        canvas = tk.Canvas(self.main_tab)
        scrollbar = ttk.Scrollbar(self.main_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        self.bind_mousewheel(canvas)
        
        # Basic Information Section
        basic_frame = ttk.LabelFrame(scrollable_frame, text="Basic Information", padding=10)
        basic_frame.grid(row=0, column=0, columnspan=4, sticky='ew', padx=5, pady=5)
        
        self.entries['name'] = self.create_labeled_entry(basic_frame, "Name:", 0, 0, width=20)
        self.entries['player'] = self.create_labeled_entry(basic_frame, "Player:", 0, 2, width=20)
        
        # Class display and management
        ttk.Label(basic_frame, text="Class:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        
        # Show classes (for display purposes - actual management done through dialog)
        self.class_display = ttk.Label(basic_frame, text="Fighter 1", relief='sunken', anchor='w', width=25)
        self.class_display.grid(row=1, column=1, columnspan=2, sticky='ew', padx=2, pady=2)
        
        # Manage Classes button
        self.manage_classes_button = ttk.Button(basic_frame, text="Manage Classes", command=self.show_manage_classes_dialog)
        self.manage_classes_button.grid(row=1, column=3, padx=5, pady=2)
        
        self.entries['level'] = self.create_labeled_entry(basic_frame, "Total Level:", 1, 4, width=5)
        
        # Level Up button
        self.level_up_button = ttk.Button(basic_frame, text="Level Up", command=self.show_level_up_dialog)
        self.level_up_button.grid(row=1, column=6, padx=5, pady=2)
        
        # XP tracking
        ttk.Label(basic_frame, text="XP:").grid(row=2, column=0, sticky='e', padx=2, pady=2)
        self.entries['experience'] = ttk.Entry(basic_frame, width=10)
        self.entries['experience'].grid(row=2, column=1, sticky='w', padx=2, pady=2)
        self.entries['experience'].insert(0, "0")
        self.entries['experience'].bind('<FocusOut>', lambda e: self.update_from_entry('experience'))
        self.entries['experience'].bind('<KeyRelease>', lambda e: self.mark_modified())
        
        ttk.Label(basic_frame, text="Next Level:").grid(row=2, column=2, sticky='e', padx=2, pady=2)
        self.labels['next_level_xp'] = ttk.Label(basic_frame, text="1000")
        self.labels['next_level_xp'].grid(row=2, column=3, sticky='w', padx=2, pady=2)
        
        self.entries['race'] = self.create_labeled_entry(basic_frame, "Race:", 3, 0, width=15)
        self.entries['alignment'] = self.create_labeled_entry(basic_frame, "Alignment:", 3, 2, width=15)
        
        # Bind update events for basic info
        for key in ['name', 'player', 'race', 'alignment']:
            self.entries[key].bind('<KeyRelease>', lambda e: self.mark_modified())
        
        # Bind update events for level (affects many things)
        self.entries['level'].bind('<FocusOut>', lambda e: self.update_from_entry('level'))
        
        # Ability Scores Section
        ability_frame = ttk.LabelFrame(scrollable_frame, text="Ability Scores", padding=10)
        ability_frame.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
        
        abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        ability_labels = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        
        for i, (ability, label) in enumerate(zip(abilities, ability_labels)):
            # Score entry
            score_label = ttk.Label(ability_frame, text=f"{label} Score:")
            score_label.grid(row=i, column=0, sticky='e', padx=2, pady=2)
            
            self.entries[ability] = ttk.Entry(ability_frame, width=5)
            self.entries[ability].grid(row=i, column=1, padx=2, pady=2)
            self.entries[ability].insert(0, "10")
            self.entries[ability].bind('<FocusOut>', lambda e, a=ability: self.update_ability_score(a))
            self.entries[ability].bind('<KeyRelease>', lambda e: self.mark_modified())
            
            # Modifier (readonly)
            mod_label = ttk.Label(ability_frame, text="Mod:")
            mod_label.grid(row=i, column=2, sticky='e', padx=2, pady=2)
            
            self.labels[f'{ability}_mod'] = ttk.Label(ability_frame, text="+0", width=5, relief='sunken')
            self.labels[f'{ability}_mod'].grid(row=i, column=3, padx=2, pady=2)
            
            # Temp modifier
            temp_label = ttk.Label(ability_frame, text="Temp:")
            temp_label.grid(row=i, column=4, sticky='e', padx=2, pady=2)
            
            self.entries[f'{ability}_temp'] = ttk.Entry(ability_frame, width=5)
            self.entries[f'{ability}_temp'].grid(row=i, column=5, padx=2, pady=2)
            self.entries[f'{ability}_temp'].insert(0, "0")
            self.entries[f'{ability}_temp'].bind('<FocusOut>', lambda e, a=ability: self.update_ability_score(a))
            self.entries[f'{ability}_temp'].bind('<KeyRelease>', lambda e: self.mark_modified())
        
        # Saving Throws Section
        saves_frame = ttk.LabelFrame(scrollable_frame, text="Saving Throws", padding=10)
        saves_frame.grid(row=1, column=2, columnspan=2, sticky='ew', padx=5, pady=5)
        
        saves = [
            ('Fortitude', 'fort', 'CON'),
            ('Reflex', 'ref', 'DEX'),
            ('Will', 'will', 'WIS')
        ]
        
        for i, (save_name, save_key, ability) in enumerate(saves):
            ttk.Label(saves_frame, text=f"{save_name}:", font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky='e', padx=2, pady=2)
            
            # Total (readonly)
            self.labels[f'{save_key}_total'] = ttk.Label(saves_frame, text="+0", width=5, relief='sunken', font=('Arial', 10, 'bold'))
            self.labels[f'{save_key}_total'].grid(row=i, column=1, padx=2, pady=2)
            
            # Base
            ttk.Label(saves_frame, text="Base:").grid(row=i, column=2, sticky='e', padx=2, pady=2)
            self.entries[f'{save_key}_base'] = ttk.Entry(saves_frame, width=5)
            self.entries[f'{save_key}_base'].grid(row=i, column=3, padx=2, pady=2)
            self.entries[f'{save_key}_base'].insert(0, "0")
            self.entries[f'{save_key}_base'].bind('<FocusOut>', lambda e: self.update_all_calculated_fields())
            
            # Ability mod (readonly)
            ttk.Label(saves_frame, text=f"{ability}:").grid(row=i, column=4, sticky='e', padx=2, pady=2)
            self.labels[f'{save_key}_ability'] = ttk.Label(saves_frame, text="+0", width=5, relief='sunken')
            self.labels[f'{save_key}_ability'].grid(row=i, column=5, padx=2, pady=2)
            
            # Misc
            ttk.Label(saves_frame, text="Misc:").grid(row=i, column=6, sticky='e', padx=2, pady=2)
            self.entries[f'{save_key}_misc'] = ttk.Entry(saves_frame, width=5)
            self.entries[f'{save_key}_misc'].grid(row=i, column=7, padx=2, pady=2)
            self.entries[f'{save_key}_misc'].insert(0, "0")
            self.entries[f'{save_key}_misc'].bind('<FocusOut>', lambda e: self.update_all_calculated_fields())
        
        # Add attack bonuses to saves frame
        ttk.Label(saves_frame, text="").grid(row=3, column=0, pady=5)  # Spacer
        
        ttk.Label(saves_frame, text="Melee Attack:", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky='e', padx=2, pady=2)
        self.labels['melee_attack'] = ttk.Label(saves_frame, text="+0", width=5, relief='sunken', font=('Arial', 10, 'bold'))
        self.labels['melee_attack'].grid(row=4, column=1, padx=2, pady=2)
        
        ttk.Label(saves_frame, text="Ranged Attack:", font=('Arial', 10, 'bold')).grid(row=5, column=0, sticky='e', padx=2, pady=2)
        self.labels['ranged_attack'] = ttk.Label(saves_frame, text="+0", width=5, relief='sunken', font=('Arial', 10, 'bold'))
        self.labels['ranged_attack'].grid(row=5, column=1, padx=2, pady=2)
        
        # Armor Class Section
        ac_frame = ttk.LabelFrame(scrollable_frame, text="Armor Class", padding=10)
        ac_frame.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
        
        # Total AC
        ttk.Label(ac_frame, text="Total AC:", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.labels['ac_total'] = ttk.Label(ac_frame, text="10", width=5, relief='sunken', font=('Arial', 12, 'bold'))
        self.labels['ac_total'].grid(row=0, column=1, padx=2, pady=2)
        
        # AC Components
        ac_components = [
            ('Armor', 'armor_bonus'),
            ('Shield', 'shield_bonus'),
            ('DEX', 'dex_ac'),
            ('Natural', 'natural_armor'),
            ('Deflection', 'deflection_bonus'),
            ('Misc', 'misc_ac_bonus')
        ]
        
        for i, (comp_name, comp_key) in enumerate(ac_components):
            ttk.Label(ac_frame, text=f"{comp_name}:").grid(row=i+1, column=0, sticky='e', padx=2, pady=2)
            
            if comp_key == 'dex_ac':
                # DEX is readonly
                self.labels[comp_key] = ttk.Label(ac_frame, text="+0", width=5, relief='sunken')
                self.labels[comp_key].grid(row=i+1, column=1, padx=2, pady=2)
            else:
                self.entries[comp_key] = ttk.Entry(ac_frame, width=5)
                self.entries[comp_key].grid(row=i+1, column=1, padx=2, pady=2)
                self.entries[comp_key].insert(0, "0")
                self.entries[comp_key].bind('<FocusOut>', lambda e: self.update_all_calculated_fields())
        
        # Touch and Flat-footed AC
        ttk.Label(ac_frame, text="Touch AC:").grid(row=7, column=0, sticky='e', padx=2, pady=2)
        self.labels['touch_ac'] = ttk.Label(ac_frame, text="10", width=5, relief='sunken')
        self.labels['touch_ac'].grid(row=7, column=1, padx=2, pady=2)
        
        ttk.Label(ac_frame, text="Flat-footed:").grid(row=8, column=0, sticky='e', padx=2, pady=2)
        self.labels['flatfooted_ac'] = ttk.Label(ac_frame, text="10", width=5, relief='sunken')
        self.labels['flatfooted_ac'].grid(row=8, column=1, padx=2, pady=2)
        
        # Hit Points Section
        hp_frame = ttk.LabelFrame(scrollable_frame, text="Hit Points", padding=10)
        hp_frame.grid(row=2, column=2, columnspan=2, sticky='ew', padx=5, pady=5)
        
        ttk.Label(hp_frame, text="Max HP:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['max_hp'] = ttk.Entry(hp_frame, width=8)
        self.entries['max_hp'].grid(row=0, column=1, padx=2, pady=2)
        self.entries['max_hp'].insert(0, "0")
        
        ttk.Label(hp_frame, text="Current HP:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['current_hp'] = ttk.Entry(hp_frame, width=8)
        self.entries['current_hp'].grid(row=1, column=1, padx=2, pady=2)
        self.entries['current_hp'].insert(0, "0")
        
        # Combat Section
        combat_frame = ttk.LabelFrame(scrollable_frame, text="Combat", padding=10)
        combat_frame.grid(row=3, column=0, columnspan=4, sticky='ew', padx=5, pady=5)
        
        # Initiative
        ttk.Label(combat_frame, text="Initiative:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.labels['initiative'] = ttk.Label(combat_frame, text="+0", width=5, relief='sunken', font=('Arial', 10, 'bold'))
        self.labels['initiative'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(combat_frame, text="Misc:").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        self.entries['initiative_misc'] = ttk.Entry(combat_frame, width=5)
        self.entries['initiative_misc'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['initiative_misc'].insert(0, "0")
        self.entries['initiative_misc'].bind('<FocusOut>', lambda e: self.update_all_calculated_fields())
        
        # Base Attack Bonus
        ttk.Label(combat_frame, text="Base Attack Bonus:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['bab'] = ttk.Entry(combat_frame, width=5)
        self.entries['bab'].grid(row=1, column=1, padx=2, pady=2)
        self.entries['bab'].insert(0, "0")
        self.entries['bab'].bind('<FocusOut>', lambda e: self.update_all_calculated_fields())
        
        # Spell Resistance
        ttk.Label(combat_frame, text="Spell Resistance:").grid(row=1, column=2, sticky='e', padx=2, pady=2)

        self.entries['spell_resistance'] = ttk.Entry(combat_frame, width=5)
        self.entries['spell_resistance'].grid(row=3, column=1, padx=2, pady=2)
        self.entries['spell_resistance'].insert(0, "0")
        
        # Weapons Section
        weapons_frame = ttk.LabelFrame(scrollable_frame, text="Weapons", padding=10)
        weapons_frame.grid(row=4, column=0, columnspan=4, sticky='ew', padx=5, pady=5)
        
        # Add weapon controls
        add_weapon_frame = ttk.Frame(weapons_frame)
        add_weapon_frame.pack(fill='x', pady=(0, 5))
        
        # Row 0: Name, Type, Size
        ttk.Label(add_weapon_frame, text="Weapon Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['weapon_name'] = ttk.Entry(add_weapon_frame, width=20)
        self.entries['weapon_name'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(add_weapon_frame, text="Type:").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        weapon_types = ['Melee', 'Ranged']
        self.entries['weapon_type'] = ttk.Combobox(add_weapon_frame, width=10, values=weapon_types)
        self.entries['weapon_type'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['weapon_type'].current(0)
        
        ttk.Label(add_weapon_frame, text="Size:").grid(row=0, column=4, sticky='e', padx=2, pady=2)
        weapon_sizes = ['Fine', 'Diminutive', 'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal']
        self.entries['weapon_size'] = ttk.Combobox(add_weapon_frame, width=10, values=weapon_sizes)
        self.entries['weapon_size'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['weapon_size'].current(4)  # Medium
        
        # Row 1: Damage, Critical, Damage Type
        ttk.Label(add_weapon_frame, text="Damage:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['weapon_damage'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_damage'].grid(row=1, column=1, padx=2, pady=2)
        
        ttk.Label(add_weapon_frame, text="Critical:").grid(row=1, column=2, sticky='e', padx=2, pady=2)
        self.entries['weapon_crit'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_crit'].grid(row=1, column=3, padx=2, pady=2)
        self.entries['weapon_crit'].insert(0, "20/x2")
        
        ttk.Label(add_weapon_frame, text="Damage Type:").grid(row=1, column=4, sticky='e', padx=2, pady=2)
        damage_types = ['Slashing', 'Piercing', 'Bludgeoning', 'S/P', 'P/B', 'S/B', 'S/P/B']
        self.entries['weapon_damage_type'] = ttk.Combobox(add_weapon_frame, width=12, values=damage_types)
        self.entries['weapon_damage_type'].grid(row=1, column=5, padx=2, pady=2)
        self.entries['weapon_damage_type'].current(0)
        
        # Row 2: Range, Weight, Enhancement Bonus
        ttk.Label(add_weapon_frame, text="Range:").grid(row=2, column=0, sticky='e', padx=2, pady=2)
        self.entries['weapon_range'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_range'].grid(row=2, column=1, padx=2, pady=2)
        
        ttk.Label(add_weapon_frame, text="Weight (lbs):").grid(row=2, column=2, sticky='e', padx=2, pady=2)
        self.entries['weapon_weight'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_weight'].grid(row=2, column=3, padx=2, pady=2)
        self.entries['weapon_weight'].insert(0, "0")
        
        ttk.Label(add_weapon_frame, text="Enhancement:").grid(row=2, column=4, sticky='e', padx=2, pady=2)
        self.entries['weapon_attack_bonus'] = ttk.Entry(add_weapon_frame, width=5)
        self.entries['weapon_attack_bonus'].grid(row=2, column=5, sticky='w', padx=2, pady=2)
        self.entries['weapon_attack_bonus'].insert(0, "0")
        
        # Row 3: Misc Attack/Damage Bonuses
        ttk.Label(add_weapon_frame, text="Misc Attack:").grid(row=3, column=0, sticky='e', padx=2, pady=2)
        self.entries['weapon_misc_attack'] = ttk.Entry(add_weapon_frame, width=5)
        self.entries['weapon_misc_attack'].grid(row=3, column=1, sticky='w', padx=2, pady=2)
        self.entries['weapon_misc_attack'].insert(0, "0")
        
        ttk.Label(add_weapon_frame, text="Misc Damage:").grid(row=3, column=2, sticky='e', padx=2, pady=2)
        self.entries['weapon_damage_bonus'] = ttk.Entry(add_weapon_frame, width=5)
        self.entries['weapon_damage_bonus'].grid(row=3, column=3, sticky='w', padx=2, pady=2)
        self.entries['weapon_damage_bonus'].insert(0, "0")
        
        # Row 4: Notes
        ttk.Label(add_weapon_frame, text="Notes:").grid(row=4, column=0, sticky='e', padx=2, pady=2)
        self.entries['weapon_notes'] = ttk.Entry(add_weapon_frame, width=60)
        self.entries['weapon_notes'].grid(row=4, column=1, columnspan=5, sticky='ew', padx=2, pady=2)
        
        add_weapon_btn = ttk.Button(add_weapon_frame, text="Add Weapon", command=self.add_weapon)
        add_weapon_btn.grid(row=5, column=0, columnspan=6, pady=5)
        
        # Weapons list
        weapons_list_frame = ttk.Frame(weapons_frame)
        weapons_list_frame.pack(fill='both', expand=True)
        
        weapons_scroll = ttk.Scrollbar(weapons_list_frame)
        weapons_scroll.pack(side='right', fill='y')
        
        columns = ('name', 'type', 'attack', 'damage', 'critical', 'range', 'damage_type', 'size', 'weight', 'notes')
        self.weapons_tree = ttk.Treeview(weapons_list_frame, columns=columns, show='headings',
                                        yscrollcommand=weapons_scroll.set, height=6)
        
        self.weapons_tree.heading('name', text='Weapon')
        self.weapons_tree.heading('type', text='Type')
        self.weapons_tree.heading('attack', text='Attack')
        self.weapons_tree.heading('damage', text='Damage')
        self.weapons_tree.heading('critical', text='Critical')
        self.weapons_tree.heading('range', text='Range')
        self.weapons_tree.heading('damage_type', text='Dmg Type')
        self.weapons_tree.heading('size', text='Size')
        self.weapons_tree.heading('weight', text='Weight')
        self.weapons_tree.heading('notes', text='Notes')
        
        self.weapons_tree.column('name', width=150)
        self.weapons_tree.column('type', width=60)
        self.weapons_tree.column('attack', width=60)
        self.weapons_tree.column('damage', width=80)
        self.weapons_tree.column('critical', width=70)
        self.weapons_tree.column('range', width=60)
        self.weapons_tree.column('damage_type', width=80)
        self.weapons_tree.column('size', width=70)
        self.weapons_tree.column('weight', width=60)
        self.weapons_tree.column('notes', width=150)
        
        self.weapons_tree.pack(side='left', fill='both', expand=True)
        weapons_scroll.config(command=self.weapons_tree.yview)
        
        # Remove weapon button
        remove_weapon_btn = ttk.Button(weapons_frame, text="Remove Selected Weapon", command=self.remove_weapon)
        remove_weapon_btn.pack(pady=5)
    
    def build_skills_tab(self):
        """Build the skills tab"""
        # Create scrollable frame
        canvas = tk.Canvas(self.skills_tab)
        scrollbar = ttk.Scrollbar(self.skills_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        self.bind_mousewheel(canvas)
        
        # Skill points info at top
        points_frame = ttk.Frame(scrollable_frame)
        points_frame.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        
        ttk.Label(points_frame, text="Skill Points Available:", font=('Arial', 11, 'bold')).pack(side='left', padx=5)
        self.labels['skill_points_available'] = ttk.Label(points_frame, text="0", font=('Arial', 11, 'bold'), 
                                                          relief='sunken', width=8)
        self.labels['skill_points_available'].pack(side='left', padx=5)
        
        # Add spent points display
        ttk.Label(points_frame, text="Spent:", font=('Arial', 10)).pack(side='left', padx=(20, 2))
        self.labels['skill_points_spent'] = ttk.Label(points_frame, text="0", font=('Arial', 10), 
                                                      relief='sunken', width=6)
        self.labels['skill_points_spent'].pack(side='left', padx=2)
        
        ttk.Label(points_frame, text="(Max Ranks = Level + 3 for class skills, (Level + 3)/2 for cross-class)", 
                 font=('Arial', 9, 'italic')).pack(side='left', padx=10)
        
        # Skills frame
        skills_frame = ttk.LabelFrame(scrollable_frame, text="Skills", padding=10)
        skills_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        # Headers
        ttk.Label(skills_frame, text="Skill Name", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', padx=2, pady=2)
        ttk.Label(skills_frame, text="Total", font=('Arial', 10, 'bold')).grid(row=0, column=1, padx=2, pady=2)
        ttk.Label(skills_frame, text="Ranks", font=('Arial', 10, 'bold')).grid(row=0, column=2, padx=2, pady=2)
        ttk.Label(skills_frame, text="Ability", font=('Arial', 10, 'bold')).grid(row=0, column=3, padx=2, pady=2)
        ttk.Label(skills_frame, text="Misc", font=('Arial', 10, 'bold')).grid(row=0, column=4, padx=2, pady=2)
        
        # Create skill rows
        skill_list = sorted(self.character.skills.keys())
        
        for i, skill_name in enumerate(skill_list, start=1):
            # Skill name
            ttk.Label(skills_frame, text=skill_name).grid(row=i, column=0, sticky='w', padx=2, pady=1)
            
            # Total (readonly)
            self.labels[f'skill_total_{skill_name}'] = ttk.Label(skills_frame, text="+0", width=5, relief='sunken')
            self.labels[f'skill_total_{skill_name}'].grid(row=i, column=1, padx=2, pady=1)
            
            # Ranks
            self.entries[f'skill_ranks_{skill_name}'] = ttk.Entry(skills_frame, width=5)
            self.entries[f'skill_ranks_{skill_name}'].grid(row=i, column=2, padx=2, pady=1)
            self.entries[f'skill_ranks_{skill_name}'].insert(0, "0")
            self.entries[f'skill_ranks_{skill_name}'].bind('<FocusOut>', lambda e, s=skill_name: self.update_skill(s))
            
            # Ability modifier (readonly)
            ability = self.character.skill_abilities[skill_name].upper()
            self.labels[f'skill_ability_{skill_name}'] = ttk.Label(skills_frame, text=f"{ability} +0", width=8, relief='sunken')
            self.labels[f'skill_ability_{skill_name}'].grid(row=i, column=3, padx=2, pady=1)
            
            # Misc
            self.entries[f'skill_misc_{skill_name}'] = ttk.Entry(skills_frame, width=5)
            self.entries[f'skill_misc_{skill_name}'].grid(row=i, column=4, padx=2, pady=1)
            self.entries[f'skill_misc_{skill_name}'].insert(0, "0")
            self.entries[f'skill_misc_{skill_name}'].bind('<FocusOut>', lambda e, s=skill_name: self.update_skill(s))
    
    def get_entry_int(self, key, default=0):
        """Get integer value from entry widget"""
        try:
            value = self.entries[key].get()
            return int(value) if value else default
        except (ValueError, KeyError):
            return default
    
    def update_ability_score(self, ability):
        """Update ability score and all dependent fields"""
        # Update character model
        score = self.get_entry_int(ability, 10)
        temp = self.get_entry_int(f'{ability}_temp', 0)
        
        setattr(self.character, ability, score)
        setattr(self.character, f'{ability[0:3]}_temp_mod', temp)
        
        # Update all calculated fields
        self.update_all_calculated_fields()
        
        # Update inventory if strength changed
        if ability == 'strength':
            self.update_inventory_display()
    
    def update_from_entry(self, field_name):
        """Update a character field from entry widget"""
        value = self.entries[field_name].get()
        try:
            # Try to convert to int
            value = int(value)
        except ValueError:
            pass  # Keep as string
        
        setattr(self.character, field_name, value)
        self.update_all_calculated_fields()
    
    def update_skill(self, skill_name):
        """Update a skill and recalculate totals"""
        # Get previous ranks to calculate the difference
        previous_ranks = self.character.skills.get(skill_name, 0)
        
        ranks = self.get_entry_int(f'skill_ranks_{skill_name}', 0)
        misc = self.get_entry_int(f'skill_misc_{skill_name}', 0)
        
        # Calculate points spent
        points_spent = ranks - previous_ranks
        
        # Check if we have enough skill points
        if points_spent > 0 and self.character.skill_points_available < points_spent:
            messagebox.showwarning(
                "Insufficient Skill Points", 
                f"You only have {self.character.skill_points_available} skill points available.\n"
                f"You need {points_spent} more points."
            )
            # Reset to previous value
            self.set_entry(f'skill_ranks_{skill_name}', str(previous_ranks))
            return
        
        # Update character model
        self.character.skills[skill_name] = ranks
        self.character.skill_misc[skill_name] = misc
        
        # Adjust available skill points
        self.character.skill_points_available -= points_spent
        
        # Update display
        if 'skill_points_available' in self.labels:
            self.labels['skill_points_available'].config(text=str(self.character.skill_points_available))
        
        # Update spent points display
        if 'skill_points_spent' in self.labels:
            total_spent = sum(self.character.skills.values())
            self.labels['skill_points_spent'].config(text=str(total_spent))
        
        self.update_all_calculated_fields()
        self.mark_modified()
    
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
        
        for ability, func in zip(abilities, ability_funcs):
            mod = func()
            mod_str = f"+{mod}" if mod >= 0 else str(mod)
            self.labels[f'{ability}_mod'].config(text=mod_str)
        
        # Update saving throws
        # First update character model with base and misc values
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
        
        # Update AC
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
        
        # Update Skills
        for skill_name in self.character.skills.keys():
            total = self.character.get_skill_total(skill_name)
            total_str = f"+{total}" if total >= 0 else str(total)
            self.labels[f'skill_total_{skill_name}'].config(text=total_str)
            
            # Update ability modifier display for skill
            ability = self.character.skill_abilities[skill_name]
            if ability == 'str':
                ability_mod = self.character.get_str_modifier()
            elif ability == 'dex':
                ability_mod = self.character.get_dex_modifier()
            elif ability == 'con':
                ability_mod = self.character.get_con_modifier()
            elif ability == 'int':
                ability_mod = self.character.get_int_modifier()
            elif ability == 'wis':
                ability_mod = self.character.get_wis_modifier()
            elif ability == 'cha':
                ability_mod = self.character.get_cha_modifier()
            else:
                ability_mod = 0
            
            ability_str = f"{ability.upper()} {'+' if ability_mod >= 0 else ''}{ability_mod}"
            self.labels[f'skill_ability_{skill_name}'].config(text=ability_str)
        
        # Update spell DCs (if spells tab exists)
        if hasattr(self, 'spells_tree'):
            self.update_spell_dcs()
        
        # Update weapons display (attack bonuses depend on BAB and ability scores)
        if hasattr(self, 'weapons_tree'):
            self.refresh_weapons()
    
    def on_class_changed(self):
        """Handle class selection change"""
        self.character.character_class = self.class_var.get()
        self.character.update_class_based_stats()
        
        # Update GUI to reflect new BAB and saves
        self.set_entry('bab', str(self.character.base_attack_bonus))
        self.set_entry('fort_base', str(self.character.fort_base))
        self.set_entry('ref_base', str(self.character.ref_base))
        self.set_entry('will_base', str(self.character.will_base))
        
        # Update spellcasting ability dropdown if it exists
        if hasattr(self, 'spellcasting_ability_var'):
            self.spellcasting_ability_var.set(self.character.spellcasting_ability)
            self.update_spell_dcs()
        
        self.update_all_calculated_fields()
        self.mark_modified()
    
    def update_from_entry(self, field_name):
        """Update character field from entry widget"""
        if field_name == 'level':
            new_level = self.get_entry_int('level', 1)
            if new_level != self.character.level and new_level >= 1:
                self.character.level = new_level
                self.character.update_class_based_stats()
                
                # Update GUI
                self.set_entry('bab', str(self.character.base_attack_bonus))
                self.set_entry('fort_base', str(self.character.fort_base))
                self.set_entry('ref_base', str(self.character.ref_base))
                self.set_entry('will_base', str(self.character.will_base))
                
                self.update_all_calculated_fields()
                self.mark_modified()
        elif field_name == 'experience':
            self.character.experience = self.get_entry_int('experience', 0)
            self.mark_modified()
    
    def show_manage_classes_dialog(self):
        """Show dialog for managing multiple classes"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Manage Classes")
        dialog.geometry("550x450")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Info frame
        info_frame = ttk.LabelFrame(dialog, text="Current Classes", padding=10)
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create a scrollable frame for classes
        canvas = tk.Canvas(info_frame)
        scrollbar = ttk.Scrollbar(info_frame, orient="vertical", command=canvas.yview)
        classes_frame = ttk.Frame(canvas)
        
        classes_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=classes_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Track class level entries
        class_entries = {}
        
        def refresh_classes_display():
            """Refresh the display of all classes"""
            # Clear existing widgets
            for widget in classes_frame.winfo_children():
                widget.destroy()
            class_entries.clear()
            
            # Header
            ttk.Label(classes_frame, text="Class", font=('TkDefaultFont', 9, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky='w')
            ttk.Label(classes_frame, text="Level", font=('TkDefaultFont', 9, 'bold')).grid(row=0, column=1, padx=5, pady=5)
            ttk.Label(classes_frame, text="", font=('TkDefaultFont', 9, 'bold')).grid(row=0, column=2, padx=5, pady=5)
            
            # Display each class
            for idx, class_info in enumerate(self.character.classes):
                class_name = class_info['name']
                class_level = class_info['level']
                
                # Class name label
                ttk.Label(classes_frame, text=class_name).grid(row=idx+1, column=0, padx=5, pady=2, sticky='w')
                
                # Level spinbox
                level_var = tk.IntVar(value=class_level)
                level_spinbox = ttk.Spinbox(classes_frame, from_=1, to=20, textvariable=level_var, width=5)
                level_spinbox.grid(row=idx+1, column=1, padx=5, pady=2)
                
                class_entries[class_name] = level_var
                
                # Update level callback
                def update_level(cn=class_name, lv=level_var):
                    for c in self.character.classes:
                        if c['name'] == cn:
                            c['level'] = lv.get()
                            break
                    self.character.update_class_based_stats()
                    update_total_label()
                
                level_spinbox.config(command=update_level)
                
                # Remove button (only if more than one class)
                if len(self.character.classes) > 1:
                    remove_btn = ttk.Button(classes_frame, text="Remove", 
                                          command=lambda cn=class_name: remove_class(cn))
                    remove_btn.grid(row=idx+1, column=2, padx=5, pady=2)
            
            update_total_label()
        
        def remove_class(class_name):
            """Remove a class"""
            if len(self.character.classes) <= 1:
                messagebox.showwarning("Cannot Remove", "Character must have at least one class!")
                return
            
            self.character.remove_class(class_name)
            self.character.update_class_based_stats()
            refresh_classes_display()
            self.mark_modified()
        
        def add_new_class():
            """Add a new class (including prestige classes)"""
            # Create popup for class selection
            add_dialog = tk.Toplevel(dialog)
            add_dialog.title("Add Class")
            add_dialog.geometry("500x450")
            add_dialog.transient(dialog)
            add_dialog.grab_set()
            
            # Class selection frame
            selection_frame = ttk.LabelFrame(add_dialog, text="Select Class", padding=10)
            selection_frame.pack(fill='x', padx=10, pady=10)
            
            ttk.Label(selection_frame, text="Choose a class to add:").pack(pady=5)
            
            # Get available classes (exclude ones already taken)
            current_classes = [c['name'] for c in self.character.classes]
            available_base_classes = [c for c in sorted(CLASS_DEFINITIONS.keys()) if c not in current_classes]
            available_prestige_classes = [c for c in sorted(get_all_prestige_classes()) if c not in current_classes]
            
            # Combine base and prestige classes with separator
            all_available = []
            if available_base_classes:
                all_available.extend(available_base_classes)
            if available_prestige_classes:
                if all_available:
                    all_available.append("--- PRESTIGE CLASSES ---")
                all_available.extend(available_prestige_classes)
            
            if not all_available or all_available == ["--- PRESTIGE CLASSES ---"]:
                messagebox.showinfo("No Classes Available", "You already have all available classes!")
                add_dialog.destroy()
                return
            
            class_var = tk.StringVar(value=all_available[0])
            class_combo = ttk.Combobox(add_dialog, textvariable=class_var, values=all_available, 
                                      state='readonly', width=30)
            class_combo.pack(pady=5)
            
            # Requirements display
            req_frame = ttk.LabelFrame(add_dialog, text="Requirements", padding=10)
            req_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            req_text = tk.Text(req_frame, height=12, width=55, wrap='word', state='disabled')
            req_scrollbar = ttk.Scrollbar(req_frame, command=req_text.yview)
            req_text.config(yscrollcommand=req_scrollbar.set)
            req_text.pack(side='left', fill='both', expand=True)
            req_scrollbar.pack(side='right', fill='y')
            
            def update_requirements():
                """Update requirements display when class selection changes"""
                selected = class_var.get()
                req_text.config(state='normal')
                req_text.delete(1.0, tk.END)
                
                if selected == "--- PRESTIGE CLASSES ---":
                    req_text.insert(tk.END, "Please select a class.")
                    req_text.config(state='disabled')
                    return
                
                if is_prestige_class(selected):
                    # Show prestige class requirements
                    eligible, requirements = self.character.check_prestige_requirements(selected)
                    
                    prestige_info = PRESTIGE_CLASS_DEFINITIONS[selected]
                    req_text.insert(tk.END, f"Prestige Class: {selected}\n\n", 'bold')
                    req_text.insert(tk.END, f"{prestige_info['description']}\n\n")
                    
                    if eligible:
                        req_text.insert(tk.END, "✓ You meet the basic requirements!\n\n", 'success')
                    else:
                        req_text.insert(tk.END, "⚠ Requirements not fully verified:\n\n", 'warning')
                    
                    req_text.insert(tk.END, "Requirements:\n")
                    for req in requirements:
                        req_text.insert(tk.END, f"  • {req}\n")
                    
                    # Configure tags
                    req_text.tag_config('bold', font=('TkDefaultFont', 9, 'bold'))
                    req_text.tag_config('success', foreground='green', font=('TkDefaultFont', 9, 'bold'))
                    req_text.tag_config('warning', foreground='orange', font=('TkDefaultFont', 9, 'bold'))
                else:
                    # Base class - no special requirements
                    req_text.insert(tk.END, f"Base Class: {selected}\n\n")
                    req_text.insert(tk.END, "No special requirements.")
                
                req_text.config(state='disabled')
            
            class_combo.bind('<<ComboboxSelected>>', lambda e: update_requirements())
            update_requirements()  # Initial display
            
            # Buttons
            button_frame = ttk.Frame(add_dialog)
            button_frame.pack(fill='x', padx=10, pady=10)
            
            def confirm_add():
                selected_class = class_var.get()
                
                if selected_class == "--- PRESTIGE CLASSES ---":
                    messagebox.showwarning("Invalid Selection", "Please select an actual class.")
                    return
                
                # Warn if adding prestige class with unmet requirements
                if is_prestige_class(selected_class):
                    eligible, requirements = self.character.check_prestige_requirements(selected_class)
                    if not eligible:
                        response = messagebox.askyesno(
                            "Requirements Check",
                            f"Some requirements for {selected_class} may not be fully met.\n\n"
                            "Do you want to add this prestige class anyway?",
                            icon='warning'
                        )
                        if not response:
                            return
                
                self.character.add_class(selected_class, 1)
                self.character.update_class_based_stats()
                refresh_classes_display()
                self.mark_modified()
                add_dialog.destroy()
            
            ttk.Button(button_frame, text="Add Class", command=confirm_add).pack(side='left', padx=5)
            ttk.Button(button_frame, text="Cancel", command=add_dialog.destroy).pack(side='right', padx=5)
        
        # Total level display
        total_frame = ttk.Frame(dialog)
        total_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(total_frame, text="Total Level:", font=('TkDefaultFont', 10, 'bold')).pack(side='left', padx=5)
        total_label = ttk.Label(total_frame, text="1", font=('TkDefaultFont', 10, 'bold'))
        total_label.pack(side='left', padx=5)
        
        def update_total_label():
            total = self.character.get_total_level()
            total_label.config(text=str(total))
        
        # Buttons frame
        button_frame = ttk.Frame(dialog)
        button_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(button_frame, text="Add Class", command=add_new_class).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Close", command=lambda: self.close_manage_classes_dialog(dialog)).pack(side='right', padx=5)
        
        # Initial display
        refresh_classes_display()
    
    def close_manage_classes_dialog(self, dialog):
        """Close the manage classes dialog and update display"""
        # Update the main display
        self.update_class_display()
        self.populate_fields_from_character()
        dialog.destroy()
    
    def update_class_display(self):
        """Update the class display label to show all classes"""
        class_text = " / ".join([f"{c['name']} {c['level']}" for c in self.character.classes])
        self.class_display.config(text=class_text)
    
    def show_level_up_dialog(self):
        """Show dialog for leveling up character"""
        import random
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Level Up!")
        dialog.geometry("450x400")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Class selection for multiclass
        class_select_frame = ttk.LabelFrame(dialog, text="Select Class to Level", padding=10)
        class_select_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(class_select_frame, text="Level up which class?").pack(anchor='w')
        
        class_options = [f"{c['name']} (currently level {c['level']})" for c in self.character.classes]
        class_var = tk.StringVar(value=class_options[0])
        class_combo = ttk.Combobox(class_select_frame, textvariable=class_var, values=class_options, state='readonly', width=30)
        class_combo.pack(pady=5, fill='x')
        
        # Get selected class info
        def get_selected_class_name():
            selection = class_var.get()
            return selection.split(' (')[0]  # Extract class name before parenthesis
        
        def update_class_info():
            selected_class = get_selected_class_name()
            class_info = CLASS_DEFINITIONS[selected_class]
            hit_die = class_info['hit_die']
            
            current_level = self.character.get_class_level(selected_class)
            
            info_text = f"Current Level: {self.character.get_total_level()}\n"
            info_text += f"New Total Level: {self.character.get_total_level() + 1}\n"
            info_text += f"{selected_class} Level: {current_level} → {current_level + 1}\n"
            info_text += f"Hit Die: d{hit_die}"
            
            info_label.config(text=info_text)
            
            hp_instructions.config(text=f"Roll 1d{hit_die} for HP (or use average: {(hit_die // 2) + 1})")
            hp_entry.delete(0, tk.END)
            hp_entry.insert(0, str((hit_die // 2) + 1))
            roll_button.config(text=f"Roll d{hit_die}", 
                             command=lambda: hp_entry.delete(0, tk.END) or hp_entry.insert(0, str(random.randint(1, hit_die))))
        
        class_combo.bind('<<ComboboxSelected>>', lambda e: update_class_info())
        
        # Info frame
        info_frame = ttk.LabelFrame(dialog, text="Level Up Information", padding=10)
        info_frame.pack(fill='x', padx=10, pady=10)
        
        info_label = ttk.Label(info_frame, text="", justify='left')
        info_label.pack(anchor='w')
        
        # HP Roll frame
        hp_frame = ttk.LabelFrame(dialog, text="Hit Points", padding=10)
        hp_frame.pack(fill='x', padx=10, pady=10)
        
        hp_instructions = ttk.Label(hp_frame, text="")
        hp_instructions.pack(anchor='w')
        
        hp_roll_frame = ttk.Frame(hp_frame)
        hp_roll_frame.pack(fill='x', pady=5)
        
        ttk.Label(hp_roll_frame, text="HP Roll:").grid(row=0, column=0, sticky='e', padx=5)
        hp_entry = ttk.Entry(hp_roll_frame, width=10)
        hp_entry.grid(row=0, column=1, sticky='w', padx=5)
        
        roll_button = ttk.Button(hp_roll_frame, text="Roll", command=lambda: None)
        roll_button.grid(row=0, column=2, padx=5)
        
        con_mod = self.character.get_con_modifier()
        con_mod_str = f"+{con_mod}" if con_mod >= 0 else str(con_mod)
        ttk.Label(hp_frame, text=f"CON Modifier: {con_mod_str} (added automatically)").pack(anchor='w')
        
        # Initialize display
        update_class_info()
        
        # Preview frame
        preview_frame = ttk.LabelFrame(dialog, text="Level Up Preview", padding=10)
        preview_frame.pack(fill='x', padx=10, pady=10)
        
        preview_text = tk.Text(preview_frame, height=6, width=50, state='disabled')
        preview_text.pack(fill='both', expand=True)
        
        def update_preview():
            try:
                hp_roll = int(hp_entry.get())
            except:
                selected_class = get_selected_class_name()
                class_info = CLASS_DEFINITIONS[selected_class]
                hit_die = class_info['hit_die']
                hp_roll = (hit_die // 2) + 1
            
            selected_class = get_selected_class_name()
            class_info = CLASS_DEFINITIONS[selected_class]
            
            # Calculate preview
            hp_gain = max(1, hp_roll + con_mod)
            new_total_level = self.character.get_total_level() + 1
            
            skill_points = class_info['skill_points'] + self.character.get_int_modifier()
            skill_points = max(1, skill_points)
            
            preview_text.config(state='normal')
            preview_text.delete(1.0, tk.END)
            preview_text.insert(tk.END, f"Class: {selected_class}\n")
            preview_text.insert(tk.END, f"HP Gained: +{hp_gain}\n")
            preview_text.insert(tk.END, f"New Max HP: {self.character.max_hp + hp_gain}\n")
            preview_text.insert(tk.END, f"Total Level: {new_total_level}\n")
            preview_text.insert(tk.END, f"Skill Points: +{skill_points}\n")
            preview_text.config(state='disabled')
        
        hp_entry.bind('<KeyRelease>', lambda e: update_preview())
        update_preview()
        
        # Buttons
        button_frame = ttk.Frame(dialog)
        button_frame.pack(fill='x', padx=10, pady=10)
        
        def do_level_up():
            try:
                hp_roll = int(hp_entry.get())
            except:
                selected_class = get_selected_class_name()
                class_info = CLASS_DEFINITIONS[selected_class]
                hit_die = class_info['hit_die']
                hp_roll = (hit_die // 2) + 1
            
            selected_class = get_selected_class_name()
            
            # Level up the selected class
            for class_entry in self.character.classes:
                if class_entry['name'] == selected_class:
                    class_entry['level'] += 1
                    break
            
            # Update total level and stats
            self.character.update_class_based_stats()
            
            # Add HP
            con_mod = self.character.get_con_modifier()
            hp_gain = max(1, hp_roll + con_mod)
            
            # Get class info for skill points
            class_info = CLASS_DEFINITIONS[selected_class]
            hit_die = class_info['hit_die']
            
            # Store HP roll
            self.character.hit_dice.append({'class': selected_class, 'roll': hp_roll, 'con_mod': con_mod})
            self.character.max_hp += hp_gain
            self.character.current_hp += hp_gain
            
            # Add skill points
            skill_points = class_info['skill_points'] + self.character.get_int_modifier()
            skill_points = max(1, skill_points)
            self.character.skill_points_available += skill_points
            
            # Update XP requirement
            new_level = self.character.get_total_level()
            self.character.level = new_level
            self.character.update_xp_for_epic_level()  # Use epic XP calculation if needed
            
            # Update GUI
            self.update_class_display()
            self.set_entry('level', str(self.character.level))
            self.set_entry('max_hp', str(self.character.max_hp))
            self.set_entry('current_hp', str(self.character.current_hp))
            self.set_entry('bab', str(self.character.base_attack_bonus))
            self.set_entry('fort_base', str(self.character.fort_base))
            self.set_entry('ref_base', str(self.character.ref_base))
            self.set_entry('will_base', str(self.character.will_base))
            self.labels['next_level_xp'].config(text=str(self.character.next_level_xp))
            
            # Update skill points label if it exists
            if 'skill_points_available' in self.labels:
                self.labels['skill_points_available'].config(text=str(self.character.skill_points_available))
            
            self.update_all_calculated_fields()
            self.mark_modified()
            
            # Build level up message
            level_up_msg = f"Congratulations! {selected_class} level increased!\n\n"
            level_up_msg += f"Total Level: {new_level}\n"
            level_up_msg += f"HP gained: +{hp_gain}\n"
            level_up_msg += f"Skill points: +{skill_points}\n"
            level_up_msg += f"BAB: +{self.character.base_attack_bonus}\n"
            level_up_msg += f"Saves - Fort: +{self.character.fort_base}, Ref: +{self.character.ref_base}, Will: +{self.character.will_base}\n"
            
            # Add epic level notifications
            if self.character.is_epic_level():
                epic_info = self.character.get_epic_info()
                level_up_msg += f"\n🌟 EPIC LEVEL {epic_info['epic_level']}! 🌟\n"
                
                # Check if gained epic feat this level
                if new_level == 21:
                    level_up_msg += "\n✨ You've reached EPIC LEVEL!\n"
                    level_up_msg += "• You can now select your first Epic Feat!\n"
                    level_up_msg += "• Visit the Feats tab to choose Epic Feats\n"
                elif (new_level - 21) % 2 == 0:  # Epic feat at 21, then every 2 levels
                    level_up_msg += f"\n✨ Epic Feat available!\n"
                    level_up_msg += f"• You can select a new Epic Feat (Total: {epic_info['epic_feats']})\n"
                    level_up_msg += "• Visit the Feats tab to choose Epic Feats\n"
                
                # Check if gained ability increase
                if (new_level - 20) % 4 == 0 and new_level > 20:  # Every 4 levels starting at 24
                    level_up_msg += f"\n📈 Ability Score Increase!\n"
                    level_up_msg += "• You can increase any ability score by +1\n"
                    level_up_msg += "• Edit your ability scores on the Main tab\n"
            elif new_level == 20:
                level_up_msg += "\n⚠️ One more level until EPIC LEVEL!\n"
                level_up_msg += "At level 21, you'll gain access to Epic Feats!\n"
            
            messagebox.showinfo("Level Up!", level_up_msg)
            dialog.destroy()
        
        ttk.Button(button_frame, text="Level Up!", command=do_level_up).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side='left', padx=5)
    
    def build_inventory_tab(self):
        """Build the inventory tab"""
        # Create main container
        main_container = ttk.Frame(self.inventory_tab)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Top frame for carrying capacity info
        capacity_frame = ttk.LabelFrame(main_container, text="Carrying Capacity", padding=10)
        capacity_frame.pack(fill='x', padx=5, pady=5)
        
        # Carrying capacity display
        cap_info_frame = ttk.Frame(capacity_frame)
        cap_info_frame.pack(fill='x')
        
        ttk.Label(cap_info_frame, text="Light Load:", font=('Arial', 9, 'bold')).grid(row=0, column=0, sticky='e', padx=5, pady=2)
        self.labels['light_load'] = ttk.Label(cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['light_load'].grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(cap_info_frame, text="Medium Load:", font=('Arial', 9, 'bold')).grid(row=0, column=2, sticky='e', padx=5, pady=2)
        self.labels['medium_load'] = ttk.Label(cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['medium_load'].grid(row=0, column=3, padx=5, pady=2)
        
        ttk.Label(cap_info_frame, text="Heavy Load:", font=('Arial', 9, 'bold')).grid(row=1, column=0, sticky='e', padx=5, pady=2)
        self.labels['heavy_load'] = ttk.Label(cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['heavy_load'].grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(cap_info_frame, text="Maximum:", font=('Arial', 9, 'bold')).grid(row=1, column=2, sticky='e', padx=5, pady=2)
        self.labels['max_load'] = ttk.Label(cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['max_load'].grid(row=1, column=3, padx=5, pady=2)
        
        # Current weight and encumbrance
        current_frame = ttk.Frame(capacity_frame)
        current_frame.pack(fill='x', pady=(10, 0))
        
        ttk.Label(current_frame, text="Total Weight Carried:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='e', padx=5, pady=2)
        self.labels['total_weight'] = ttk.Label(current_frame, text="0 lbs", relief='sunken', width=12, font=('Arial', 10, 'bold'))
        self.labels['total_weight'].grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(current_frame, text="Current Load:", font=('Arial', 10, 'bold')).grid(row=0, column=2, sticky='e', padx=5, pady=2)
        self.labels['current_load'] = ttk.Label(current_frame, text="Light", relief='sunken', width=12, font=('Arial', 10, 'bold'))
        self.labels['current_load'].grid(row=0, column=3, padx=5, pady=2)
        
        # Encumbrance penalties
        penalty_frame = ttk.LabelFrame(main_container, text="Encumbrance Penalties", padding=10)
        penalty_frame.pack(fill='x', padx=5, pady=5)
        
        pen_info_frame = ttk.Frame(penalty_frame)
        pen_info_frame.pack(fill='x')
        
        ttk.Label(pen_info_frame, text="Max DEX Bonus:", font=('Arial', 9)).grid(row=0, column=0, sticky='e', padx=5, pady=2)
        self.labels['enc_max_dex'] = ttk.Label(pen_info_frame, text="None", relief='sunken', width=10)
        self.labels['enc_max_dex'].grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(pen_info_frame, text="Check Penalty:", font=('Arial', 9)).grid(row=0, column=2, sticky='e', padx=5, pady=2)
        self.labels['enc_check_penalty'] = ttk.Label(pen_info_frame, text="0", relief='sunken', width=10)
        self.labels['enc_check_penalty'].grid(row=0, column=3, padx=5, pady=2)
        
        ttk.Label(pen_info_frame, text="Speed Reduction:", font=('Arial', 9)).grid(row=0, column=4, sticky='e', padx=5, pady=2)
        self.labels['enc_speed'] = ttk.Label(pen_info_frame, text="0 ft", relief='sunken', width=10)
        self.labels['enc_speed'].grid(row=0, column=5, padx=5, pady=2)
        
        # Inventory list frame
        inventory_frame = ttk.LabelFrame(main_container, text="Inventory", padding=10)
        inventory_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Add item controls
        add_frame = ttk.Frame(inventory_frame)
        add_frame.pack(fill='x', pady=(0, 5))
        
        ttk.Label(add_frame, text="Item Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['item_name'] = ttk.Entry(add_frame, width=20)
        self.entries['item_name'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Weight (lbs):").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        self.entries['item_weight'] = ttk.Entry(add_frame, width=8)
        self.entries['item_weight'].grid(row=0, column=3, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Quantity:").grid(row=0, column=4, sticky='e', padx=2, pady=2)
        self.entries['item_quantity'] = ttk.Entry(add_frame, width=8)
        self.entries['item_quantity'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['item_quantity'].insert(0, "1")
        
        ttk.Label(add_frame, text="Notes:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['item_notes'] = ttk.Entry(add_frame, width=40)
        self.entries['item_notes'].grid(row=1, column=1, columnspan=3, padx=2, pady=2, sticky='ew')
        
        add_btn = ttk.Button(add_frame, text="Add Item", command=self.add_inventory_item)
        add_btn.grid(row=1, column=4, columnspan=2, padx=2, pady=2)
        
        # Inventory list with scrollbar
        list_frame = ttk.Frame(inventory_frame)
        list_frame.pack(fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Create treeview for inventory
        columns = ('name', 'weight', 'quantity', 'total_weight', 'notes')
        self.inventory_tree = ttk.Treeview(list_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        
        self.inventory_tree.heading('name', text='Item Name')
        self.inventory_tree.heading('weight', text='Weight (ea)')
        self.inventory_tree.heading('quantity', text='Qty')
        self.inventory_tree.heading('total_weight', text='Total Weight')
        self.inventory_tree.heading('notes', text='Notes')
        
        self.inventory_tree.column('name', width=200)
        self.inventory_tree.column('weight', width=80)
        self.inventory_tree.column('quantity', width=60)
        self.inventory_tree.column('total_weight', width=100)
        self.inventory_tree.column('notes', width=250)
        
        self.inventory_tree.pack(fill='both', expand=True)
        scrollbar.config(command=self.inventory_tree.yview)
        
        # Remove button
        remove_frame = ttk.Frame(inventory_frame)
        remove_frame.pack(fill='x', pady=(5, 0))
        
        remove_btn = ttk.Button(remove_frame, text="Remove Selected Item", command=self.remove_inventory_item)
        remove_btn.pack(side='left', padx=2)
    
    def add_inventory_item(self):
        """Add an item to the inventory"""
        try:
            name = self.entries['item_name'].get().strip()
            if not name:
                messagebox.showwarning("Missing Name", "Please enter an item name.")
                return
            
            weight_str = self.entries['item_weight'].get().strip()
            weight = float(weight_str) if weight_str else 0.0
            
            quantity_str = self.entries['item_quantity'].get().strip()
            quantity = int(quantity_str) if quantity_str else 1
            
            notes = self.entries['item_notes'].get().strip()
            
            # Add to character
            self.character.add_item(name, weight, quantity, notes)
            
            # Update display
            self.update_inventory_display()
            
            # Clear entry fields
            self.entries['item_name'].delete(0, tk.END)
            self.entries['item_weight'].delete(0, tk.END)
            self.entries['item_quantity'].delete(0, tk.END)
            self.entries['item_quantity'].insert(0, "1")
            self.entries['item_notes'].delete(0, tk.END)
            
        except ValueError as e:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and quantity.")
    
    def remove_inventory_item(self):
        """Remove selected item from inventory"""
        selection = self.inventory_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to remove.")
            return
        
        # Get index of selected item
        item = selection[0]
        index = self.inventory_tree.index(item)
        
        # Remove from character
        self.character.remove_item(index)
        
        # Update display
        self.update_inventory_display()
    
    def update_inventory_display(self):
        """Update the inventory treeview and weight/capacity displays"""
        # Clear treeview
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        
        # Populate treeview
        for item in self.character.inventory:
            name = item['name']
            weight = item['weight']
            quantity = item['quantity']
            total_weight = weight * quantity
            notes = item.get('notes', '')
            
            self.inventory_tree.insert('', 'end', values=(name, f"{weight:.1f}", quantity, f"{total_weight:.1f}", notes))
        
        # Update carrying capacity
        capacity = self.character.get_carrying_capacity()
        self.labels['light_load'].config(text=f"{capacity['light']} lbs")
        self.labels['medium_load'].config(text=f"{capacity['medium']} lbs")
        self.labels['heavy_load'].config(text=f"{capacity['heavy']} lbs")
        self.labels['max_load'].config(text=f"{capacity['max']} lbs")
        
        # Update current weight
        total_weight = self.character.get_total_weight_carried()
        self.labels['total_weight'].config(text=f"{total_weight:.1f} lbs")
        
        # Update current load
        current_load = self.character.get_current_load()
        load_text = current_load.capitalize()
        
        # Color code the load
        if current_load == 'light':
            bg_color = 'green'
        elif current_load == 'medium':
            bg_color = 'yellow'
        elif current_load == 'heavy':
            bg_color = 'orange'
        else:  # overloaded
            bg_color = 'red'
            load_text = 'OVERLOADED!'
        
        self.labels['current_load'].config(text=load_text, background=bg_color)
        
        # Update encumbrance penalties
        penalties = self.character.get_encumbrance_penalties()
        
        max_dex_text = "None" if penalties['max_dex'] is None else str(penalties['max_dex'])
        self.labels['enc_max_dex'].config(text=max_dex_text)
        self.labels['enc_check_penalty'].config(text=str(penalties['check_penalty']))
        self.labels['enc_speed'].config(text=f"{penalties['speed_reduction']} ft")
    
    def build_spells_tab(self):
        """Build the spells tab"""
        # Create main container
        main_container = ttk.Frame(self.spells_tab)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Top frame for spellcasting info
        casting_frame = ttk.LabelFrame(main_container, text="Spellcasting", padding=10)
        casting_frame.pack(fill='x', padx=5, pady=5)
        
        # Spellcasting ability
        ability_frame = ttk.Frame(casting_frame)
        ability_frame.pack(fill='x')
        
        ttk.Label(ability_frame, text="Spellcasting Ability:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        
        self.spellcasting_ability_var = tk.StringVar(value='intelligence')
        ability_options = [
            ('Intelligence', 'intelligence'),
            ('Wisdom', 'wisdom'),
            ('Charisma', 'charisma')
        ]
        
        for i, (label, value) in enumerate(ability_options):
            rb = ttk.Radiobutton(ability_frame, text=label, variable=self.spellcasting_ability_var, 
                                value=value, command=self.update_spellcasting_ability)
            rb.grid(row=0, column=i+1, padx=5, pady=5)
        
        # Spellcasting modifier and DC
        ttk.Label(ability_frame, text="Modifier:", font=('Arial', 10)).grid(row=0, column=4, sticky='e', padx=5, pady=5)
        self.labels['spell_modifier'] = ttk.Label(ability_frame, text="+0", relief='sunken', width=5, font=('Arial', 10, 'bold'))
        self.labels['spell_modifier'].grid(row=0, column=5, padx=5, pady=5)
        
        # Spell slots frame
        slots_frame = ttk.LabelFrame(main_container, text="Spell Slots", padding=10)
        slots_frame.pack(fill='x', padx=5, pady=5)
        
        # Headers
        ttk.Label(slots_frame, text="Level", font=('Arial', 9, 'bold')).grid(row=0, column=0, padx=5, pady=2)
        ttk.Label(slots_frame, text="Save DC", font=('Arial', 9, 'bold')).grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(slots_frame, text="Max Slots", font=('Arial', 9, 'bold')).grid(row=0, column=2, padx=5, pady=2)
        ttk.Label(slots_frame, text="Used", font=('Arial', 9, 'bold')).grid(row=0, column=3, padx=5, pady=2)
        ttk.Label(slots_frame, text="Remaining", font=('Arial', 9, 'bold')).grid(row=0, column=4, padx=5, pady=2)
        
        # Create spell slot rows for levels 0-9
        for level in range(10):
            row = level + 1
            
            # Level label
            level_text = "Cantrips" if level == 0 else f"{level}{'st' if level == 1 else 'nd' if level == 2 else 'rd' if level == 3 else 'th'}"
            ttk.Label(slots_frame, text=level_text, font=('Arial', 9)).grid(row=row, column=0, padx=5, pady=2)
            
            # Save DC (readonly)
            self.labels[f'spell_dc_{level}'] = ttk.Label(slots_frame, text="10", relief='sunken', width=5)
            self.labels[f'spell_dc_{level}'].grid(row=row, column=1, padx=5, pady=2)
            
            # Max slots
            self.entries[f'spell_max_{level}'] = ttk.Entry(slots_frame, width=5)
            self.entries[f'spell_max_{level}'].grid(row=row, column=2, padx=5, pady=2)
            self.entries[f'spell_max_{level}'].insert(0, "0")
            self.entries[f'spell_max_{level}'].bind('<FocusOut>', lambda e, l=level: self.update_spell_slots(l))
            self.entries[f'spell_max_{level}'].bind('<KeyRelease>', lambda e: self.mark_modified())
            
            # Used slots
            self.entries[f'spell_used_{level}'] = ttk.Entry(slots_frame, width=5)
            self.entries[f'spell_used_{level}'].grid(row=row, column=3, padx=5, pady=2)
            self.entries[f'spell_used_{level}'].insert(0, "0")
            self.entries[f'spell_used_{level}'].bind('<FocusOut>', lambda e, l=level: self.update_spell_slots(l))
            self.entries[f'spell_used_{level}'].bind('<KeyRelease>', lambda e: self.mark_modified())
            
            # Remaining (readonly)
            self.labels[f'spell_remaining_{level}'] = ttk.Label(slots_frame, text="0", relief='sunken', width=5, font=('Arial', 9, 'bold'))
            self.labels[f'spell_remaining_{level}'].grid(row=row, column=4, padx=5, pady=2)
        
        # Buttons frame
        buttons_frame = ttk.Frame(slots_frame)
        buttons_frame.grid(row=11, column=0, columnspan=5, pady=10)
        
        # Calculate spell slots button
        calc_btn = ttk.Button(buttons_frame, text="Calculate Spell Slots (from Class/Level)", 
                             command=self.calculate_spell_slots_from_class)
        calc_btn.pack(side='left', padx=5)
        
        # Rest button
        rest_btn = ttk.Button(buttons_frame, text="Long Rest (Reset Used Slots)", command=self.reset_spell_slots)
        rest_btn.pack(side='left', padx=5)
        
        # Spell list frame
        spells_list_frame = ttk.LabelFrame(main_container, text="Spell List", padding=10)
        spells_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Add spell controls
        add_frame = ttk.Frame(spells_list_frame)
        add_frame.pack(fill='x', pady=(0, 5))
        
        ttk.Label(add_frame, text="Spell Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['spell_name'] = ttk.Entry(add_frame, width=25)
        self.entries['spell_name'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Level:").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        self.entries['spell_level'] = ttk.Combobox(add_frame, width=5, values=list(range(10)), state='readonly')
        self.entries['spell_level'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['spell_level'].current(0)
        
        ttk.Label(add_frame, text="School:").grid(row=0, column=4, sticky='e', padx=2, pady=2)
        schools = ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 
                   'Evocation', 'Illusion', 'Necromancy', 'Transmutation', 'Universal']
        self.entries['spell_school'] = ttk.Combobox(add_frame, width=12, values=schools)
        self.entries['spell_school'].grid(row=0, column=5, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Range:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['spell_range'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_range'].grid(row=1, column=1, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Duration:").grid(row=1, column=2, sticky='e', padx=2, pady=2)
        self.entries['spell_duration'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_duration'].grid(row=1, column=3, columnspan=3, sticky='ew', padx=2, pady=2)
        
        ttk.Label(add_frame, text="Components:").grid(row=2, column=0, sticky='e', padx=2, pady=2)
        self.entries['spell_components'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_components'].grid(row=2, column=1, padx=2, pady=2)
        
        ttk.Label(add_frame, text="Casting Time:").grid(row=2, column=2, sticky='e', padx=2, pady=2)
        self.entries['spell_casting_time'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_casting_time'].grid(row=2, column=3, padx=2, pady=2)
        
        # Prepared checkbox
        self.spell_prepared_var = tk.BooleanVar(value=False)
        prep_cb = ttk.Checkbutton(add_frame, text="Prepared", variable=self.spell_prepared_var)
        prep_cb.grid(row=2, column=4, columnspan=2, padx=2, pady=2)
        
        add_spell_btn = ttk.Button(add_frame, text="Add Spell", command=self.add_spell_to_list)
        add_spell_btn.grid(row=3, column=0, columnspan=6, pady=5)
        
        # Spell list with scrollbar
        list_frame = ttk.Frame(spells_list_frame)
        list_frame.pack(fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Create treeview for spells
        columns = ('name', 'level', 'school', 'range', 'duration', 'components', 'prepared')
        self.spells_tree = ttk.Treeview(list_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        
        self.spells_tree.heading('name', text='Spell Name')
        self.spells_tree.heading('level', text='Level')
        self.spells_tree.heading('school', text='School')
        self.spells_tree.heading('range', text='Range')
        self.spells_tree.heading('duration', text='Duration')
        self.spells_tree.heading('components', text='Components')
        self.spells_tree.heading('prepared', text='Prepared')
        
        self.spells_tree.column('name', width=180)
        self.spells_tree.column('level', width=50)
        self.spells_tree.column('school', width=100)
        self.spells_tree.column('range', width=100)
        self.spells_tree.column('duration', width=120)
        self.spells_tree.column('components', width=80)
        self.spells_tree.column('prepared', width=70)
        
        self.spells_tree.pack(fill='both', expand=True)
        scrollbar.config(command=self.spells_tree.yview)
        
        # Bind double-click to toggle prepared status
        self.spells_tree.bind('<Double-1>', self.toggle_spell_prepared)
        
        # Remove button
        remove_frame = ttk.Frame(spells_list_frame)
        remove_frame.pack(fill='x', pady=(5, 0))
        
        remove_spell_btn = ttk.Button(remove_frame, text="Remove Selected Spell", command=self.remove_spell_from_list)
        remove_spell_btn.pack(side='left', padx=2)
        
        filter_frame = ttk.Frame(remove_frame)
        filter_frame.pack(side='right')
        
        ttk.Label(filter_frame, text="Filter by Level:").pack(side='left', padx=2)
        self.spell_filter_var = tk.StringVar(value="All")
        filter_combo = ttk.Combobox(filter_frame, width=8, textvariable=self.spell_filter_var, 
                                    values=["All"] + [str(i) for i in range(10)], state='readonly')
        filter_combo.pack(side='left', padx=2)
        filter_combo.bind('<<ComboboxSelected>>', lambda e: self.update_spell_list_display())
    
    def update_spellcasting_ability(self):
        """Update spellcasting ability and recalculate DCs"""
        self.character.spellcasting_ability = self.spellcasting_ability_var.get()
        self.mark_modified()
        self.update_spell_dcs()
    
    def update_spell_slots(self, level):
        """Update spell slots for a specific level"""
        max_slots = self.get_entry_int(f'spell_max_{level}', 0)
        used_slots = self.get_entry_int(f'spell_used_{level}', 0)
        
        self.character.spell_slots_max[level] = max_slots
        self.character.spell_slots_used[level] = used_slots
        
        remaining = max(0, max_slots - used_slots)
        self.labels[f'spell_remaining_{level}'].config(text=str(remaining))
        
        self.mark_modified()
    
    def calculate_spell_slots_from_class(self):
        """Calculate and set spell slots based on class, level, and ability scores"""
        # Update character's ability scores from GUI first
        self.character.strength = self.get_entry_int('strength', 10)
        self.character.dexterity = self.get_entry_int('dexterity', 10)
        self.character.constitution = self.get_entry_int('constitution', 10)
        self.character.intelligence = self.get_entry_int('intelligence', 10)
        self.character.wisdom = self.get_entry_int('wisdom', 10)
        self.character.charisma = self.get_entry_int('charisma', 10)
        
        # Update spell slots from class
        self.character.update_spell_slots_from_class()
        
        # Update GUI to show new values
        for level in range(10):
            max_slots = self.character.spell_slots_max.get(level, 0)
            self.entries[f'spell_max_{level}'].delete(0, tk.END)
            self.entries[f'spell_max_{level}'].insert(0, str(max_slots))
            self.update_spell_slots(level)
        
        # Show info message
        class_info = self.character.get_class_info()
        if class_info['spellcasting_ability']:
            base_1st = self.character.get_base_spells_per_day(1)
            bonus_1st = self.character.get_bonus_spells(1)
            total_1st = base_1st + bonus_1st if base_1st > 0 else 0
            
            ability_name = self.character.spellcasting_ability.capitalize()
            ability_mod = self.character.get_spellcasting_modifier()
            
            messagebox.showinfo("Spell Slots Calculated", 
                              f"Spell slots updated for {self.character.character_class} level {self.character.level}.\n\n"
                              f"Spellcasting Ability: {ability_name} ({ability_mod:+d})\n"
                              f"Example (1st level): {base_1st} base + {bonus_1st} bonus = {total_1st} total\n\n"
                              f"Bonus spells are granted based on your {ability_name} modifier.")
        else:
            messagebox.showinfo("No Spellcasting", 
                              f"{self.character.character_class} does not have spellcasting abilities.")
        
        self.mark_modified()
    
    def reset_spell_slots(self):
        """Reset all spell slots (long rest)"""
        self.character.reset_spell_slots()
        
        for level in range(10):
            self.entries[f'spell_used_{level}'].delete(0, tk.END)
            self.entries[f'spell_used_{level}'].insert(0, "0")
            self.update_spell_slots(level)
        
        messagebox.showinfo("Long Rest", "All spell slots have been restored!")
    
    def update_spell_dcs(self):
        """Update all spell save DCs"""
        for level in range(10):
            dc = self.character.get_spell_dc(level)
            self.labels[f'spell_dc_{level}'].config(text=str(dc))
        
        # Update spell modifier display
        modifier = self.character.get_spellcasting_modifier()
        mod_str = f"+{modifier}" if modifier >= 0 else str(modifier)
        self.labels['spell_modifier'].config(text=mod_str)
    
    def add_spell_to_list(self):
        """Add a spell to the spell list"""
        name = self.entries['spell_name'].get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter a spell name.")
            return
        
        level = int(self.entries['spell_level'].get())
        school = self.entries['spell_school'].get().strip()
        range_ = self.entries['spell_range'].get().strip()
        duration = self.entries['spell_duration'].get().strip()
        components = self.entries['spell_components'].get().strip()
        casting_time = self.entries['spell_casting_time'].get().strip()
        prepared = self.spell_prepared_var.get()
        
        self.character.add_spell(
            name=name,
            level=level,
            school=school,
            range_=range_,
            duration=duration,
            components=components,
            casting_time=casting_time,
            prepared=prepared
        )
        
        self.update_spell_list_display()
        
        # Clear entry fields
        self.entries['spell_name'].delete(0, tk.END)
        self.entries['spell_school'].delete(0, tk.END)
        self.entries['spell_range'].delete(0, tk.END)
        self.entries['spell_duration'].delete(0, tk.END)
        self.entries['spell_components'].delete(0, tk.END)
        self.entries['spell_casting_time'].delete(0, tk.END)
        self.spell_prepared_var.set(False)
        
        self.mark_modified()
    
    def remove_spell_from_list(self):
        """Remove selected spell from list"""
        selection = self.spells_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a spell to remove.")
            return
        
        item = selection[0]
        index = self.spells_tree.index(item)
        
        # Account for filter
        filter_level = self.spell_filter_var.get()
        if filter_level != "All":
            # Find the actual index in the full spell list
            filtered_spells = [s for s in self.character.spells if str(s['level']) == filter_level]
            spell_to_remove = filtered_spells[index]
            index = self.character.spells.index(spell_to_remove)
        
        self.character.remove_spell(index)
        self.update_spell_list_display()
        self.mark_modified()
    
    def toggle_spell_prepared(self, event):
        """Toggle prepared status of selected spell"""
        selection = self.spells_tree.selection()
        if not selection:
            return
        
        item = selection[0]
        index = self.spells_tree.index(item)
        
        # Account for filter
        filter_level = self.spell_filter_var.get()
        if filter_level != "All":
            filtered_spells = [s for s in self.character.spells if str(s['level']) == filter_level]
            spell = filtered_spells[index]
        else:
            spell = self.character.spells[index]
        
        spell['prepared'] = not spell['prepared']
        self.update_spell_list_display()
        self.mark_modified()
    
    def update_spell_list_display(self):
        """Update the spell list treeview"""
        # Clear treeview
        for item in self.spells_tree.get_children():
            self.spells_tree.delete(item)
        
        # Get filter level
        filter_level = self.spell_filter_var.get()
        
        # Filter and sort spells
        spells_to_show = self.character.spells
        if filter_level != "All":
            spells_to_show = [s for s in spells_to_show if str(s['level']) == filter_level]
        
        # Sort by level, then name
        spells_to_show = sorted(spells_to_show, key=lambda x: (x['level'], x['name']))
        
        # Populate treeview
        for spell in spells_to_show:
            prepared_text = "Yes" if spell.get('prepared', False) else "No"
            self.spells_tree.insert('', 'end', values=(
                spell['name'],
                spell['level'],
                spell.get('school', ''),
                spell.get('range', ''),
                spell.get('duration', ''),
                spell.get('components', ''),
                prepared_text
            ))


    def build_feats_tab(self):
        """Build the feats and special abilities tab"""
        # Create main container with two sections
        main_container = ttk.Frame(self.feats_tab)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create paned window to split feats and abilities
        paned = ttk.PanedWindow(main_container, orient='vertical')
        paned.pack(fill='both', expand=True)
        
        # ===== FEATS SECTION =====
        feats_container = ttk.LabelFrame(paned, text="Feats", padding=10)
        paned.add(feats_container, weight=1)
        
        # Add feat controls
        add_feat_frame = ttk.Frame(feats_container)
        add_feat_frame.pack(fill='x', pady=(0, 5))
        
        ttk.Label(add_feat_frame, text="Feat Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['feat_name'] = ttk.Entry(add_feat_frame, width=25)
        self.entries['feat_name'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(add_feat_frame, text="Type:").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        feat_types = ['General', 'Metamagic', 'Item Creation', 'Combat', 'Skill', 'Special']
        self.entries['feat_type'] = ttk.Combobox(add_feat_frame, width=15, values=feat_types)
        self.entries['feat_type'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['feat_type'].current(0)
        
        ttk.Label(add_feat_frame, text="Prerequisites:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        self.entries['feat_prereq'] = ttk.Entry(add_feat_frame, width=40)
        self.entries['feat_prereq'].grid(row=1, column=1, columnspan=3, sticky='ew', padx=2, pady=2)
        
        ttk.Label(add_feat_frame, text="Benefit:").grid(row=2, column=0, sticky='ne', padx=2, pady=2)
        
        # Text widget for multi-line benefit description
        benefit_frame = ttk.Frame(add_feat_frame)
        benefit_frame.grid(row=2, column=1, columnspan=3, sticky='ew', padx=2, pady=2)
        
        self.feat_benefit_text = tk.Text(benefit_frame, height=3, width=50, wrap='word')
        self.feat_benefit_text.pack(side='left', fill='both', expand=True)
        
        benefit_scroll = ttk.Scrollbar(benefit_frame, command=self.feat_benefit_text.yview)
        benefit_scroll.pack(side='right', fill='y')
        self.feat_benefit_text.config(yscrollcommand=benefit_scroll.set)
        
        add_feat_btn = ttk.Button(add_feat_frame, text="Add Feat", command=self.add_feat)
        add_feat_btn.grid(row=3, column=0, columnspan=4, pady=5)
        
        # Feats list
        feats_list_frame = ttk.Frame(feats_container)
        feats_list_frame.pack(fill='both', expand=True)
        
        feats_scroll = ttk.Scrollbar(feats_list_frame)
        feats_scroll.pack(side='right', fill='y')
        
        columns = ('name', 'type', 'prerequisites', 'benefit')
        self.feats_tree = ttk.Treeview(feats_list_frame, columns=columns, show='headings', 
                                       yscrollcommand=feats_scroll.set, height=8)
        
        self.feats_tree.heading('name', text='Feat Name')
        self.feats_tree.heading('type', text='Type')
        self.feats_tree.heading('prerequisites', text='Prerequisites')
        self.feats_tree.heading('benefit', text='Benefit')
        
        self.feats_tree.column('name', width=180)
        self.feats_tree.column('type', width=120)
        self.feats_tree.column('prerequisites', width=150)
        self.feats_tree.column('benefit', width=300)
        
        self.feats_tree.pack(side='left', fill='both', expand=True)
        feats_scroll.config(command=self.feats_tree.yview)
        
        # Feat action buttons
        feat_btn_frame = ttk.Frame(feats_container)
        feat_btn_frame.pack(fill='x', pady=5)
        
        remove_feat_btn = ttk.Button(feat_btn_frame, text="Remove Selected Feat", command=self.remove_feat)
        remove_feat_btn.pack(side='left', padx=2)
        
        epic_feats_btn = ttk.Button(feat_btn_frame, text="Epic Feats (21+)", command=self.show_epic_feats_dialog)
        epic_feats_btn.pack(side='left', padx=2)
        
        # ===== SPECIAL ABILITIES SECTION =====
        abilities_container = ttk.LabelFrame(paned, text="Special Abilities", padding=10)
        paned.add(abilities_container, weight=1)
        
        # Add ability controls
        add_ability_frame = ttk.Frame(abilities_container)
        add_ability_frame.pack(fill='x', pady=(0, 5))
        
        ttk.Label(add_ability_frame, text="Ability Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['ability_name'] = ttk.Entry(add_ability_frame, width=25)
        self.entries['ability_name'].grid(row=0, column=1, padx=2, pady=2)
        
        ttk.Label(add_ability_frame, text="Source:").grid(row=0, column=2, sticky='e', padx=2, pady=2)
        ability_sources = ['Class', 'Racial', 'Feat', 'Item', 'Spell', 'Other']
        self.entries['ability_source'] = ttk.Combobox(add_ability_frame, width=12, values=ability_sources)
        self.entries['ability_source'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['ability_source'].current(0)
        
        ttk.Label(add_ability_frame, text="Uses/Day:").grid(row=0, column=4, sticky='e', padx=2, pady=2)
        self.entries['ability_uses'] = ttk.Entry(add_ability_frame, width=8)
        self.entries['ability_uses'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['ability_uses'].insert(0, "0")
        
        ttk.Label(add_ability_frame, text="Description:").grid(row=1, column=0, sticky='ne', padx=2, pady=2)
        
        # Text widget for multi-line description
        desc_frame = ttk.Frame(add_ability_frame)
        desc_frame.grid(row=1, column=1, columnspan=5, sticky='ew', padx=2, pady=2)
        
        self.ability_desc_text = tk.Text(desc_frame, height=3, width=60, wrap='word')
        self.ability_desc_text.pack(side='left', fill='both', expand=True)
        
        desc_scroll = ttk.Scrollbar(desc_frame, command=self.ability_desc_text.yview)
        desc_scroll.pack(side='right', fill='y')
        self.ability_desc_text.config(yscrollcommand=desc_scroll.set)
        
        add_ability_btn = ttk.Button(add_ability_frame, text="Add Special Ability", command=self.add_ability)
        add_ability_btn.grid(row=2, column=0, columnspan=6, pady=5)
        
        # Abilities list
        abilities_list_frame = ttk.Frame(abilities_container)
        abilities_list_frame.pack(fill='both', expand=True)
        
        abilities_scroll = ttk.Scrollbar(abilities_list_frame)
        abilities_scroll.pack(side='right', fill='y')
        
        columns = ('name', 'source', 'uses', 'description')
        self.abilities_tree = ttk.Treeview(abilities_list_frame, columns=columns, show='headings',
                                          yscrollcommand=abilities_scroll.set, height=8)
        
        self.abilities_tree.heading('name', text='Ability Name')
        self.abilities_tree.heading('source', text='Source')
        self.abilities_tree.heading('uses', text='Uses (Remaining/Max)')
        self.abilities_tree.heading('description', text='Description')
        
        self.abilities_tree.column('name', width=180)
        self.abilities_tree.column('source', width=100)
        self.abilities_tree.column('uses', width=120)
        self.abilities_tree.column('description', width=350)
        
        self.abilities_tree.pack(side='left', fill='both', expand=True)
        abilities_scroll.config(command=self.abilities_tree.yview)
        
        # Ability action buttons
        ability_btn_frame = ttk.Frame(abilities_container)
        ability_btn_frame.pack(fill='x', pady=5)
        
        use_ability_btn = ttk.Button(ability_btn_frame, text="Use Ability (-1 Use)", command=self.use_ability)
        use_ability_btn.pack(side='left', padx=2)
        
        reset_abilities_btn = ttk.Button(ability_btn_frame, text="Long Rest (Reset All)", command=self.reset_abilities)
        reset_abilities_btn.pack(side='left', padx=2)
        
        remove_ability_btn = ttk.Button(ability_btn_frame, text="Remove Selected Ability", command=self.remove_ability)
        remove_ability_btn.pack(side='left', padx=2)
    
    def add_feat(self):
        """Add a feat to the character"""
        name = self.entries['feat_name'].get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter a feat name.")
            return
        
        feat_type = self.entries['feat_type'].get()
        prereq = self.entries['feat_prereq'].get().strip()
        benefit = self.feat_benefit_text.get('1.0', 'end-1c').strip()
        
        self.character.add_feat(
            name=name,
            feat_type=feat_type,
            prerequisites=prereq,
            benefit=benefit
        )
        
        self.update_feats_display()
        
        # Clear fields
        self.entries['feat_name'].delete(0, tk.END)
        self.entries['feat_prereq'].delete(0, tk.END)
        self.feat_benefit_text.delete('1.0', tk.END)
        
        self.mark_modified()
    
    def remove_feat(self):
        """Remove selected feat"""
        selection = self.feats_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a feat to remove.")
            return
        
        item = selection[0]
        index = self.feats_tree.index(item)
        
        self.character.remove_feat(index)
        self.update_feats_display()
        self.mark_modified()
    
    def show_epic_feats_dialog(self):
        """Show dialog for managing epic feats"""
        # Check if character is epic level
        if not self.character.is_epic_level():
            messagebox.showinfo("Not Epic Level", 
                              "Your character must be level 21 or higher to select epic feats.\n\n"
                              f"Current Level: {self.character.get_total_level()}\n"
                              "Epic levels begin at 21st level.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Epic Feats")
        dialog.geometry("800x600")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Epic level info at top
        info_frame = ttk.LabelFrame(dialog, text="Epic Level Information", padding=10)
        info_frame.pack(fill='x', padx=10, pady=10)
        
        epic_info = self.character.get_epic_info()
        total_level = self.character.get_total_level()
        
        info_text = f"Total Level: {total_level} (Epic Level {epic_info['epic_level']})\n"
        info_text += f"Epic Feats Available: {epic_info['epic_feats']}\n"
        info_text += f"Epic Feats Selected: {len(self.character.epic_feats)}\n"
        info_text += f"Next Epic Feat at Level: {epic_info['next_epic_feat_level']}\n"
        info_text += f"Epic Ability Increases: {epic_info['epic_ability_increases']}\n"
        info_text += f"Next Ability Increase at Level: {epic_info['next_ability_increase_level']}"
        
        info_label = ttk.Label(info_frame, text=info_text, justify='left', font=('Arial', 10))
        info_label.pack(anchor='w')
        
        # Current epic feats
        current_frame = ttk.LabelFrame(dialog, text="Current Epic Feats", padding=10)
        current_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        current_list = tk.Listbox(current_frame, height=6)
        current_list.pack(fill='both', expand=True)
        
        def refresh_current_feats():
            current_list.delete(0, tk.END)
            for feat in self.character.epic_feats:
                current_list.insert(tk.END, feat)
        
        refresh_current_feats()
        
        # Remove epic feat button
        remove_btn = ttk.Button(current_frame, text="Remove Selected Epic Feat",
                               command=lambda: remove_epic_feat())
        remove_btn.pack(pady=5)
        
        def remove_epic_feat():
            selection = current_list.curselection()
            if selection:
                feat_name = current_list.get(selection[0])
                self.character.remove_epic_feat(feat_name)
                refresh_current_feats()
                self.mark_modified()
        
        # Available epic feats
        available_frame = ttk.LabelFrame(dialog, text="Available Epic Feats", padding=10)
        available_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Selection frame
        select_frame = ttk.Frame(available_frame)
        select_frame.pack(fill='x', pady=5)
        
        ttk.Label(select_frame, text="Select Epic Feat:").pack(side='left', padx=5)
        
        epic_feat_var = tk.StringVar()
        all_epic_feats = self.character.get_all_epic_feats_list()
        epic_feat_combo = ttk.Combobox(select_frame, textvariable=epic_feat_var,
                                      values=all_epic_feats, state='readonly', width=40)
        epic_feat_combo.pack(side='left', padx=5, fill='x', expand=True)
        if all_epic_feats:
            epic_feat_combo.current(0)
        
        # Description frame
        desc_frame = ttk.Frame(available_frame)
        desc_frame.pack(fill='both', expand=True)
        
        desc_text = tk.Text(desc_frame, height=10, width=70, wrap='word', state='disabled')
        desc_scroll = ttk.Scrollbar(desc_frame, command=desc_text.yview)
        desc_text.config(yscrollcommand=desc_scroll.set)
        desc_text.pack(side='left', fill='both', expand=True)
        desc_scroll.pack(side='right', fill='y')
        
        def update_description(*args):
            selected = epic_feat_var.get()
            if not selected:
                return
            
            feat_info = EPIC_FEATS.get(selected, {})
            
            desc_text.config(state='normal')
            desc_text.delete('1.0', tk.END)
            
            desc_text.insert(tk.END, f"{selected}\n\n", 'title')
            desc_text.insert(tk.END, f"Type: {feat_info.get('type', 'Epic')}\n\n", 'bold')
            desc_text.insert(tk.END, f"Prerequisites: {feat_info.get('prerequisites', 'None')}\n\n")
            desc_text.insert(tk.END, f"Benefit: {feat_info.get('benefit', '')}\n\n")
            if feat_info.get('special'):
                desc_text.insert(tk.END, f"Special: {feat_info.get('special', '')}\n", 'special')
            
            desc_text.tag_config('title', font=('Arial', 12, 'bold'))
            desc_text.tag_config('bold', font=('Arial', 10, 'bold'))
            desc_text.tag_config('special', font=('Arial', 9, 'italic'))
            
            desc_text.config(state='disabled')
        
        epic_feat_combo.bind('<<ComboboxSelected>>', update_description)
        update_description()
        
        # Add button
        def add_epic_feat():
            selected = epic_feat_var.get()
            if not selected:
                messagebox.showwarning("No Selection", "Please select an epic feat.")
                return
            
            # Check if already have this feat (for feats that can't be taken multiple times)
            if selected in self.character.epic_feats:
                feat_info = EPIC_FEATS.get(selected, {})
                if feat_info.get('special') and 'multiple times' in feat_info['special'].lower():
                    # Can take multiple times
                    pass
                else:
                    messagebox.showwarning("Already Selected",
                                         f"You already have {selected}.\n"
                                         "This feat cannot be taken multiple times.")
                    return
            
            # Check if character has enough epic feats available
            if len(self.character.epic_feats) >= epic_info['epic_feats']:
                messagebox.showwarning("No Epic Feats Available",
                                     f"You have already selected {len(self.character.epic_feats)} epic feats.\n"
                                     f"You can have up to {epic_info['epic_feats']} epic feats at your level.\n"
                                     f"You'll gain another epic feat at level {epic_info['next_epic_feat_level']}.")
                return
            
            self.character.add_epic_feat(selected)
            refresh_current_feats()
            self.mark_modified()
            messagebox.showinfo("Epic Feat Added", f"{selected} has been added to your epic feats!")
        
        add_btn = ttk.Button(available_frame, text="Add Epic Feat", command=add_epic_feat)
        add_btn.pack(pady=5)
        
        # Close button
        close_btn = ttk.Button(dialog, text="Close", command=dialog.destroy)
        close_btn.pack(pady=10)
    
    def add_ability(self):
        """Add a special ability to the character"""
        name = self.entries['ability_name'].get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter an ability name.")
            return
        
        source = self.entries['ability_source'].get()
        description = self.ability_desc_text.get('1.0', 'end-1c').strip()
        
        try:
            uses = int(self.entries['ability_uses'].get())
        except ValueError:
            uses = 0
        
        self.character.add_special_ability(
            name=name,
            source=source,
            description=description,
            uses_per_day=uses
        )
        
        self.update_abilities_display()
        
        # Clear fields
        self.entries['ability_name'].delete(0, tk.END)
        self.entries['ability_uses'].delete(0, tk.END)
        self.entries['ability_uses'].insert(0, "0")
        self.ability_desc_text.delete('1.0', tk.END)
        
        self.mark_modified()
    
    def remove_ability(self):
        """Remove selected special ability"""
        selection = self.abilities_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an ability to remove.")
            return
        
        item = selection[0]
        index = self.abilities_tree.index(item)
        
        self.character.remove_special_ability(index)
        self.update_abilities_display()
        self.mark_modified()
    
    def use_ability(self):
        """Use one charge of selected ability"""
        selection = self.abilities_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an ability to use.")
            return
        
        item = selection[0]
        index = self.abilities_tree.index(item)
        
        if self.character.use_special_ability(index):
            self.update_abilities_display()
            self.mark_modified()
        else:
            messagebox.showinfo("No Uses", "This ability has no remaining uses.")
    
    def reset_abilities(self):
        """Reset all special ability uses (long rest)"""
        self.character.reset_special_abilities()
        self.update_abilities_display()
        self.mark_modified()
        messagebox.showinfo("Long Rest", "All special ability uses have been restored!")
    
    def update_feats_display(self):
        """Update the feats treeview"""
        # Clear treeview
        for item in self.feats_tree.get_children():
            self.feats_tree.delete(item)
        
        # Populate with feats
        for feat in self.character.feats:
            self.feats_tree.insert('', 'end', values=(
                feat['name'],
                feat.get('type', 'General'),
                feat.get('prerequisites', ''),
                feat.get('benefit', '')[:50] + ('...' if len(feat.get('benefit', '')) > 50 else '')
            ))
    
    def update_abilities_display(self):
        """Update the special abilities treeview"""
        # Clear treeview
        for item in self.abilities_tree.get_children():
            self.abilities_tree.delete(item)
        
        # Populate with abilities
        for ability in self.character.special_abilities:
            uses_per_day = ability.get('uses_per_day', 0)
            uses_remaining = ability.get('uses_remaining', 0)
            
            if uses_per_day == 0:
                uses_text = "At-Will"
            else:
                uses_text = f"{uses_remaining}/{uses_per_day}"
            
            desc = ability.get('description', '')
            desc_preview = desc[:60] + ('...' if len(desc) > 60 else '')
            
            self.abilities_tree.insert('', 'end', values=(
                ability['name'],
                ability.get('source', 'Other'),
                uses_text,
                desc_preview
            ))
    
    def build_magic_items_tab(self):
        """Build the magic items tab"""
        main_container = ttk.Frame(self.magic_items_tab)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Title
        title_label = ttk.Label(main_container, text="Magic Items", font=('Arial', 12, 'bold'))
        title_label.pack(pady=5)
        
        # Add magic item controls
        add_item_frame = ttk.LabelFrame(main_container, text="Add Magic Item", padding=10)
        add_item_frame.pack(fill='x', padx=5, pady=5)
        
        # Row 0: Name and Type
        ttk.Label(add_item_frame, text="Item Name:").grid(row=0, column=0, sticky='e', padx=2, pady=2)
        self.entries['magic_item_name'] = ttk.Entry(add_item_frame, width=30)
        self.entries['magic_item_name'].grid(row=0, column=1, columnspan=2, sticky='ew', padx=2, pady=2)
        
        ttk.Label(add_item_frame, text="Type:").grid(row=0, column=3, sticky='e', padx=2, pady=2)
        item_types = ['Weapon', 'Armor', 'Shield', 'Ring', 'Wondrous Item', 'Potion', 'Scroll', 'Wand', 'Rod', 'Staff', 'Other']
        self.entries['magic_item_type'] = ttk.Combobox(add_item_frame, width=15, values=item_types)
        self.entries['magic_item_type'].grid(row=0, column=4, padx=2, pady=2)
        self.entries['magic_item_type'].current(0)
        
        # Row 1: Slot and Caster Level
        ttk.Label(add_item_frame, text="Slot:").grid(row=1, column=0, sticky='e', padx=2, pady=2)
        slots = ['None', 'Head', 'Eyes', 'Neck', 'Shoulders', 'Body', 'Torso', 'Arms', 'Hands', 'Ring', 'Waist', 'Feet']
        self.entries['magic_item_slot'] = ttk.Combobox(add_item_frame, width=12, values=slots)
        self.entries['magic_item_slot'].grid(row=1, column=1, padx=2, pady=2)
        self.entries['magic_item_slot'].current(0)
        
        ttk.Label(add_item_frame, text="Caster Level:").grid(row=1, column=2, sticky='e', padx=2, pady=2)
        self.entries['magic_item_cl'] = ttk.Entry(add_item_frame, width=8)
        self.entries['magic_item_cl'].grid(row=1, column=3, padx=2, pady=2)
        self.entries['magic_item_cl'].insert(0, "1")
        
        ttk.Label(add_item_frame, text="Charges:").grid(row=1, column=4, sticky='e', padx=2, pady=2)
        self.entries['magic_item_charges'] = ttk.Entry(add_item_frame, width=8)
        self.entries['magic_item_charges'].grid(row=1, column=5, padx=2, pady=2)
        self.entries['magic_item_charges'].insert(0, "0")
        
        # Row 2: Properties
        ttk.Label(add_item_frame, text="Properties:").grid(row=2, column=0, sticky='ne', padx=2, pady=2)
        
        properties_frame = ttk.Frame(add_item_frame)
        properties_frame.grid(row=2, column=1, columnspan=5, sticky='ew', padx=2, pady=2)
        
        self.magic_item_properties_text = tk.Text(properties_frame, height=2, width=60, wrap='word')
        self.magic_item_properties_text.pack(side='left', fill='both', expand=True)
        
        properties_scroll = ttk.Scrollbar(properties_frame, command=self.magic_item_properties_text.yview)
        properties_scroll.pack(side='right', fill='y')
        self.magic_item_properties_text.config(yscrollcommand=properties_scroll.set)
        
        # Row 3: Description
        ttk.Label(add_item_frame, text="Description:").grid(row=3, column=0, sticky='ne', padx=2, pady=2)
        
        desc_frame = ttk.Frame(add_item_frame)
        desc_frame.grid(row=3, column=1, columnspan=5, sticky='ew', padx=2, pady=2)
        
        self.magic_item_desc_text = tk.Text(desc_frame, height=3, width=60, wrap='word')
        self.magic_item_desc_text.pack(side='left', fill='both', expand=True)
        
        desc_scroll = ttk.Scrollbar(desc_frame, command=self.magic_item_desc_text.yview)
        desc_scroll.pack(side='right', fill='y')
        self.magic_item_desc_text.config(yscrollcommand=desc_scroll.set)
        
        # Add button
        add_item_btn = ttk.Button(add_item_frame, text="Add Magic Item", command=self.add_magic_item)
        add_item_btn.grid(row=4, column=0, columnspan=6, pady=5)
        
        # Magic Items list
        list_frame = ttk.LabelFrame(main_container, text="Magic Items List", padding=10)
        list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        items_list_frame = ttk.Frame(list_frame)
        items_list_frame.pack(fill='both', expand=True)
        
        items_scroll = ttk.Scrollbar(items_list_frame)
        items_scroll.pack(side='right', fill='y')
        
        columns = ('name', 'type', 'slot', 'cl', 'charges', 'properties', 'description')
        self.magic_items_tree = ttk.Treeview(items_list_frame, columns=columns, show='headings',
                                             yscrollcommand=items_scroll.set, height=15)
        
        self.magic_items_tree.heading('name', text='Item Name')
        self.magic_items_tree.heading('type', text='Type')
        self.magic_items_tree.heading('slot', text='Slot')
        self.magic_items_tree.heading('cl', text='CL')
        self.magic_items_tree.heading('charges', text='Charges')
        self.magic_items_tree.heading('properties', text='Properties')
        self.magic_items_tree.heading('description', text='Description')
        
        self.magic_items_tree.column('name', width=180)
        self.magic_items_tree.column('type', width=120)
        self.magic_items_tree.column('slot', width=100)
        self.magic_items_tree.column('cl', width=50)
        self.magic_items_tree.column('charges', width=80)
        self.magic_items_tree.column('properties', width=200)
        self.magic_items_tree.column('description', width=250)
        
        self.magic_items_tree.pack(side='left', fill='both', expand=True)
        items_scroll.config(command=self.magic_items_tree.yview)
        
        # Buttons
        btn_frame = ttk.Frame(list_frame)
        btn_frame.pack(fill='x', pady=5)
        
        use_charge_btn = ttk.Button(btn_frame, text="Use Charge (-1)", command=self.use_magic_item_charge)
        use_charge_btn.pack(side='left', padx=2)
        
        recharge_btn = ttk.Button(btn_frame, text="Recharge", command=self.recharge_magic_item)
        recharge_btn.pack(side='left', padx=2)
        
        remove_item_btn = ttk.Button(btn_frame, text="Remove Selected Item", command=self.remove_magic_item)
        remove_item_btn.pack(side='left', padx=2)
    
    def add_magic_item(self):
        """Add a magic item to the character"""
        name = self.entries['magic_item_name'].get().strip()
        if not name:
            messagebox.showwarning("Missing Information", "Please enter an item name.")
            return
        
        try:
            caster_level = int(self.entries['magic_item_cl'].get())
            charges = int(self.entries['magic_item_charges'].get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Caster Level and Charges must be numbers.")
            return
        
        properties = self.magic_item_properties_text.get('1.0', 'end-1c').strip()
        description = self.magic_item_desc_text.get('1.0', 'end-1c').strip()
        
        magic_item = {
            'name': name,
            'type': self.entries['magic_item_type'].get(),
            'slot': self.entries['magic_item_slot'].get(),
            'caster_level': caster_level,
            'description': description,
            'properties': properties,
            'charges': charges,
            'max_charges': charges
        }
        
        self.character.magic_items.append(magic_item)
        self.refresh_magic_items()
        
        # Clear inputs
        self.entries['magic_item_name'].delete(0, 'end')
        self.entries['magic_item_cl'].delete(0, 'end')
        self.entries['magic_item_cl'].insert(0, "1")
        self.entries['magic_item_charges'].delete(0, 'end')
        self.entries['magic_item_charges'].insert(0, "0")
        self.magic_item_properties_text.delete('1.0', 'end')
        self.magic_item_desc_text.delete('1.0', 'end')
    
    def remove_magic_item(self):
        """Remove the selected magic item"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a magic item to remove.")
            return
        
        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][0]
        
        # Find and remove the item
        for i, magic_item in enumerate(self.character.magic_items):
            if magic_item['name'] == item_name:
                del self.character.magic_items[i]
                break
        
        self.refresh_magic_items()
    
    def use_magic_item_charge(self):
        """Use one charge from a magic item"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a magic item.")
            return
        
        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][0]
        
        # Find and update the item
        for magic_item in self.character.magic_items:
            if magic_item['name'] == item_name:
                if magic_item['charges'] > 0:
                    magic_item['charges'] -= 1
                    self.refresh_magic_items()
                else:
                    messagebox.showinfo("No Charges", "This item has no charges remaining.")
                break
    
    def recharge_magic_item(self):
        """Recharge a magic item to full"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a magic item.")
            return
        
        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][0]
        
        # Find and update the item
        for magic_item in self.character.magic_items:
            if magic_item['name'] == item_name:
                magic_item['charges'] = magic_item['max_charges']
                self.refresh_magic_items()
                break
    
    def refresh_magic_items(self):
        """Refresh the magic items display"""
        # Clear tree
        for item in self.magic_items_tree.get_children():
            self.magic_items_tree.delete(item)
        
        # Repopulate
        for magic_item in self.character.magic_items:
            # Truncate long text for display
            properties = magic_item.get('properties', '')
            if len(properties) > 50:
                properties = properties[:47] + '...'
            
            description = magic_item.get('description', '')
            if len(description) > 50:
                description = description[:47] + '...'
            
            charges_text = f"{magic_item.get('charges', 0)}/{magic_item.get('max_charges', 0)}"
            
            self.magic_items_tree.insert('', 'end', values=(
                magic_item['name'],
                magic_item.get('type', 'Other'),
                magic_item.get('slot', 'None'),
                magic_item.get('caster_level', 1),
                charges_text,
                properties,
                description
            ))
    
    def add_weapon(self):
        """Add a weapon to the character"""
        name = self.entries['weapon_name'].get().strip()
        if not name:
            messagebox.showwarning("Missing Information", "Please enter a weapon name.")
            return
        
        try:
            attack_bonus = int(self.entries['weapon_attack_bonus'].get())
            misc_attack = int(self.entries['weapon_misc_attack'].get())
            damage_bonus = int(self.entries['weapon_damage_bonus'].get())
            weight = float(self.entries['weapon_weight'].get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Attack bonuses, damage bonus, and weight must be numbers.")
            return
        
        weapon = {
            'name': name,
            'type': self.entries['weapon_type'].get().lower(),
            'damage': self.entries['weapon_damage'].get().strip(),
            'critical': self.entries['weapon_crit'].get().strip(),
            'range': self.entries['weapon_range'].get().strip(),
            'damage_type': self.entries['weapon_damage_type'].get(),
            'size': self.entries['weapon_size'].get(),
            'weight': weight,
            'attack_bonus': attack_bonus,
            'misc_attack': misc_attack,
            'damage_bonus': damage_bonus,
            'notes': self.entries['weapon_notes'].get().strip()
        }
        
        self.character.weapons.append(weapon)
        self.refresh_weapons()
        
        # Clear inputs
        self.entries['weapon_name'].delete(0, 'end')
        self.entries['weapon_damage'].delete(0, 'end')
        self.entries['weapon_range'].delete(0, 'end')
        self.entries['weapon_crit'].delete(0, 'end')
        self.entries['weapon_crit'].insert(0, "20/x2")
        self.entries['weapon_weight'].delete(0, 'end')
        self.entries['weapon_weight'].insert(0, "0")
        self.entries['weapon_attack_bonus'].delete(0, 'end')
        self.entries['weapon_attack_bonus'].insert(0, "0")
        self.entries['weapon_misc_attack'].delete(0, 'end')
        self.entries['weapon_misc_attack'].insert(0, "0")
        self.entries['weapon_damage_bonus'].delete(0, 'end')
        self.entries['weapon_damage_bonus'].insert(0, "0")
        self.entries['weapon_notes'].delete(0, 'end')
        self.entries['weapon_size'].current(4)  # Reset to Medium
        self.entries['weapon_damage_type'].current(0)  # Reset to Slashing
    
    def remove_weapon(self):
        """Remove the selected weapon"""
        selection = self.weapons_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a weapon to remove.")
            return
        
        item = self.weapons_tree.item(selection[0])
        weapon_name = item['values'][0]
        
        # Find and remove the weapon
        for i, weapon in enumerate(self.character.weapons):
            if weapon['name'] == weapon_name:
                del self.character.weapons[i]
                break
        
        self.refresh_weapons()
    
    def refresh_weapons(self):
        """Refresh the weapons display"""
        # Clear tree
        for item in self.weapons_tree.get_children():
            self.weapons_tree.delete(item)
        
        # Get BAB and ability modifiers
        bab = self.character.base_attack_bonus
        str_mod = self.character.get_str_modifier()
        dex_mod = self.character.get_dex_modifier()
        
        # Repopulate
        for weapon in self.character.weapons:
            weapon_type = weapon.get('type', 'melee')
            
            # Calculate total attack bonus (BAB + ability + enhancement + misc)
            if weapon_type == 'melee':
                total_attack = bab + str_mod + weapon.get('attack_bonus', 0) + weapon.get('misc_attack', 0)
                ability_mod = str_mod
            else:  # ranged
                total_attack = bab + dex_mod + weapon.get('attack_bonus', 0) + weapon.get('misc_attack', 0)
                ability_mod = dex_mod
            
            attack_text = f"+{total_attack}" if total_attack >= 0 else str(total_attack)
            
            # Calculate total damage (base + ability + enhancement + misc)
            base_damage = weapon.get('damage', '')
            damage_bonus = weapon.get('damage_bonus', 0)
            enhancement = weapon.get('attack_bonus', 0)  # Enhancement bonus applies to damage too
            
            # For melee weapons, add STR mod to damage; for ranged, typically don't (except for composite bows, etc.)
            if weapon_type == 'melee':
                total_damage_bonus = ability_mod + enhancement + damage_bonus
            else:
                total_damage_bonus = enhancement + damage_bonus
            
            if base_damage:
                if total_damage_bonus >= 0:
                    damage_text = f"{base_damage}+{total_damage_bonus}"
                else:
                    damage_text = f"{base_damage}{total_damage_bonus}"
            else:
                damage_text = ""
            
            # Truncate notes if too long
            notes = weapon.get('notes', '')
            if len(notes) > 30:
                notes = notes[:27] + '...'
            
            weight = weapon.get('weight', 0)
            weight_text = f"{weight}" if weight else ""
            
            self.weapons_tree.insert('', 'end', values=(
                weapon['name'],
                weapon_type.capitalize(),
                attack_text,
                damage_text,
                weapon.get('critical', '20/x2'),
                weapon.get('range', ''),
                weapon.get('damage_type', ''),
                weapon.get('size', ''),
                weight_text,
                notes
            ))


def main():
    """Main entry point"""
    root = tk.Tk()
    app = CharacterSheetGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
