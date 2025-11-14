"""
Main Tab
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab
from character import CLASS_DEFINITIONS
from prestige_classes.prestige_classes import (
    PRESTIGE_CLASS_DEFINITIONS,
    get_all_prestige_classes,
    is_prestige_class
)


class MainTab(BaseTab):
    """Main management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        """Build the main character sheet tab"""
        # Create scrollable frame
        canvas = tk.Canvas(self.parent)
        scrollbar = ttk.Scrollbar(
            self.parent,
            orient="vertical",
            command=canvas.yview)
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
        basic_frame = ttk.LabelFrame(
            scrollable_frame,
            text="Basic Information",
            padding=10)
        basic_frame.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky='ew',
            padx=5,
            pady=5)

        self.entries['name'] = self.create_labeled_entry(
            basic_frame, "Name:", 0, 0, width=20)
        self.entries['player'] = self.create_labeled_entry(
            basic_frame, "Player:", 0, 2, width=20)

        # Class display and management
        ttk.Label(
            basic_frame,
            text="Class:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)

        # Show classes (for display purposes - actual management done through
        # dialog)
        self.class_display = ttk.Label(
            basic_frame,
            text="Fighter 1",
            relief='sunken',
            anchor='w',
            width=25)
        self.class_display.grid(
            row=1,
            column=1,
            columnspan=2,
            sticky='ew',
            padx=2,
            pady=2)

        # Manage Classes button
        self.manage_classes_button = ttk.Button(
            basic_frame,
            text="Manage Classes",
            command=self.show_manage_classes_dialog)
        self.manage_classes_button.grid(row=1, column=3, padx=5, pady=2)

        self.entries['level'] = self.create_labeled_entry(
            basic_frame, "Total Level:", 1, 4, width=5)

        # Level Up button
        self.level_up_button = ttk.Button(
            basic_frame,
            text="Level Up",
            command=self.show_level_up_dialog)
        self.level_up_button.grid(row=1, column=6, padx=5, pady=2)

        # XP tracking
        ttk.Label(
            basic_frame,
            text="XP:").grid(
            row=2,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['experience'] = ttk.Entry(basic_frame, width=10)
        self.entries['experience'].grid(
            row=2, column=1, sticky='w', padx=2, pady=2)
        self.entries['experience'].insert(0, "0")
        self.entries['experience'].bind(
            '<FocusOut>', lambda e: self.gui.update_from_entry('experience'))
        self.entries['experience'].bind(
            '<KeyRelease>', lambda e: self.mark_modified())

        ttk.Label(
            basic_frame,
            text="Next Level:").grid(
            row=2,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['next_level_xp'] = ttk.Label(basic_frame, text="1000")
        self.labels['next_level_xp'].grid(
            row=2, column=3, sticky='w', padx=2, pady=2)

        self.entries['race'] = self.create_labeled_entry(
            basic_frame, "Race:", 3, 0, width=15)
        self.entries['alignment'] = self.create_labeled_entry(
            basic_frame, "Alignment:", 3, 2, width=15)
        
        # Additional character details
        self.entries['deity'] = self.create_labeled_entry(
            basic_frame, "Deity:", 4, 0, width=15)
        self.entries['gender'] = self.create_labeled_entry(
            basic_frame, "Gender:", 4, 2, width=15)
        
        self.entries['height'] = self.create_labeled_entry(
            basic_frame, "Height:", 5, 0, width=15)
        self.entries['weight'] = self.create_labeled_entry(
            basic_frame, "Weight:", 5, 2, width=15)
        
        self.entries['hair_color'] = self.create_labeled_entry(
            basic_frame, "Hair Color:", 6, 0, width=15)
        self.entries['eye_color'] = self.create_labeled_entry(
            basic_frame, "Eye Color:", 6, 2, width=15)

        # Bind update events for basic info
        for key in ['name', 'player', 'race', 'alignment', 'deity', 'gender', 'height', 'weight', 'hair_color', 'eye_color']:
            self.entries[key].bind(
                '<KeyRelease>', lambda e: self.mark_modified())

        # Bind update events for level (affects many things)
        self.entries['level'].bind('<FocusOut>',
                                   lambda e: self.gui.update_from_entry('level'))

        # Ability Scores Section
        ability_frame = ttk.LabelFrame(
            scrollable_frame, text="Ability Scores", padding=10)
        ability_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky='ew',
            padx=5,
            pady=5)

        abilities = [
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma']
        ability_labels = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

        for i, (ability, label) in enumerate(zip(abilities, ability_labels)):
            # Score entry
            score_label = ttk.Label(ability_frame, text=f"{label} Score:")
            score_label.grid(row=i, column=0, sticky='e', padx=2, pady=2)

            self.entries[ability] = ttk.Entry(ability_frame, width=5)
            self.entries[ability].grid(row=i, column=1, padx=2, pady=2)
            self.entries[ability].insert(0, "10")
            self.entries[ability].bind(
                '<FocusOut>',
                lambda e,
                a=ability: self.update_ability_score(a))
            self.entries[ability].bind(
                '<KeyRelease>', lambda e: self.mark_modified())

            # Modifier (readonly)
            mod_label = ttk.Label(ability_frame, text="Mod:")
            mod_label.grid(row=i, column=2, sticky='e', padx=2, pady=2)

            self.labels[f'{ability}_mod'] = ttk.Label(
                ability_frame, text="+0", width=5, relief='sunken')
            self.labels[f'{ability}_mod'].grid(row=i, column=3, padx=2, pady=2)

            # Temp modifier
            temp_label = ttk.Label(ability_frame, text="Temp:")
            temp_label.grid(row=i, column=4, sticky='e', padx=2, pady=2)

            self.entries[f'{ability}_temp'] = ttk.Entry(ability_frame, width=5)
            self.entries[f'{ability}_temp'].grid(row=i, column=5, padx=2, pady=2)
            self.entries[f'{ability}_temp'].insert(0, "0")
            self.entries[f'{ability}_temp'].bind(
                '<FocusOut>', lambda e, a=ability: self.update_ability_score(a))
            self.entries[f'{ability}_temp'].bind(
                '<KeyRelease>', lambda e: self.mark_modified())

        # Saving Throws Section
        saves_frame = ttk.LabelFrame(
            scrollable_frame,
            text="Saving Throws",
            padding=10)
        saves_frame.grid(
            row=1,
            column=2,
            columnspan=2,
            sticky='ew',
            padx=5,
            pady=5)

        saves = [
            ('Fortitude', 'fort', 'CON'),
            ('Reflex', 'ref', 'DEX'),
            ('Will', 'will', 'WIS')
        ]

        for i, (save_name, save_key, ability) in enumerate(saves):
            ttk.Label(
                saves_frame,
                text=f"{save_name}:",
                font=(
                    'Arial',
                    10,
                    'bold')).grid(
                row=i,
                column=0,
                sticky='e',
                padx=2,
                pady=2)

            # Total (readonly)
            self.labels[f'{save_key}_total'] = ttk.Label(
                saves_frame, text="+0", width=5, relief='sunken', font=('Arial', 10, 'bold'))
            self.labels[f'{save_key}_total'].grid(
                row=i, column=1, padx=2, pady=2)

            # Base
            ttk.Label(
                saves_frame,
                text="Base:").grid(
                row=i,
                column=2,
                sticky='e',
                padx=2,
                pady=2)
            self.entries[f'{save_key}_base'] = ttk.Entry(saves_frame, width=5)
            self.entries[f'{save_key}_base'].grid(
                row=i, column=3, padx=2, pady=2)
            self.entries[f'{save_key}_base'].insert(0, "0")
            self.entries[f'{save_key}_base'].bind(
                '<FocusOut>', lambda e: self.gui.update_all_calculated_fields())

            # Ability mod (readonly)
            ttk.Label(
                saves_frame,
                text=f"{ability}:").grid(
                row=i,
                column=4,
                sticky='e',
                padx=2,
                pady=2)
            self.labels[f'{save_key}_ability'] = ttk.Label(
                saves_frame, text="+0", width=5, relief='sunken')
            self.labels[f'{save_key}_ability'].grid(
                row=i, column=5, padx=2, pady=2)

            # Misc
            ttk.Label(
                saves_frame,
                text="Misc:").grid(
                row=i,
                column=6,
                sticky='e',
                padx=2,
                pady=2)
            self.entries[f'{save_key}_misc'] = ttk.Entry(saves_frame, width=5)
            self.entries[f'{save_key}_misc'].grid(
                row=i, column=7, padx=2, pady=2)
            self.entries[f'{save_key}_misc'].insert(0, "0")
            self.entries[f'{save_key}_misc'].bind(
                '<FocusOut>', lambda e: self.gui.update_all_calculated_fields())
            
            # Magic bonus label (initially empty)
            magic_label_key = f'{save_key}_magic'
            self.labels[magic_label_key] = ttk.Label(
                saves_frame, text="", foreground='blue', font=('Arial', 10, 'bold'))
            self.labels[magic_label_key].grid(row=i, column=8, sticky='w', padx=2)
        
        # Initialize save magic bonuses display (will show when items are equipped)
        self.update_save_components(0)

        # Add attack bonuses to saves frame
        ttk.Label(saves_frame, text="").grid(row=3, column=0, pady=5)  # Spacer

        ttk.Label(
            saves_frame,
            text="Melee Attack:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=4,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['melee_attack'] = ttk.Label(
            saves_frame,
            text="+0",
            width=5,
            relief='sunken',
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['melee_attack'].grid(row=4, column=1, padx=2, pady=2)

        ttk.Label(
            saves_frame,
            text="Ranged Attack:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=5,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['ranged_attack'] = ttk.Label(
            saves_frame,
            text="+0",
            width=5,
            relief='sunken',
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['ranged_attack'].grid(row=5, column=1, padx=2, pady=2)

        # Armor Class Section
        ac_frame = ttk.LabelFrame(
            scrollable_frame,
            text="Armor Class",
            padding=10)
        ac_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='ew',
            padx=5,
            pady=5)

        # Total AC
        ttk.Label(
            ac_frame,
            text="Total AC:",
            font=(
                'Arial',
                12,
                'bold')).grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['ac_total'] = ttk.Label(
            ac_frame, text="10", width=5, relief='sunken', font=(
                'Arial', 12, 'bold'))
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
            ttk.Label(
                ac_frame,
                text=f"{comp_name}:").grid(
                row=i + 1,
                column=0,
                sticky='e',
                padx=2,
                pady=2)

            if comp_key == 'dex_ac':
                # DEX is readonly
                self.labels[comp_key] = ttk.Label(
                    ac_frame, text="+0", width=5, relief='sunken')
                self.labels[comp_key].grid(row=i + 1, column=1, padx=2, pady=2)
            else:
                self.entries[comp_key] = ttk.Entry(ac_frame, width=5)
                self.entries[comp_key].grid(
                    row=i + 1, column=1, padx=2, pady=2)
                self.entries[comp_key].insert(0, "0")
                self.entries[comp_key].bind(
                    '<FocusOut>', lambda e: self.gui.update_all_calculated_fields())
            
            # Add label to show magic item bonus for ALL components
            magic_label_key = f'{comp_key}_magic'
            self.labels[magic_label_key] = ttk.Label(
                ac_frame, text="", foreground='blue', font=('Arial', 10, 'bold'))
            self.labels[magic_label_key].grid(row=i + 1, column=2, sticky='w', padx=2)
        
        # Initialize magic bonuses display (will show when items are equipped)
        self.update_ac_components(0, 0, 0, 0)

        # Touch and Flat-footed AC
        ttk.Label(
            ac_frame,
            text="Touch AC:").grid(
            row=7,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['touch_ac'] = ttk.Label(
            ac_frame, text="10", width=5, relief='sunken')
        self.labels['touch_ac'].grid(row=7, column=1, padx=2, pady=2)

        ttk.Label(ac_frame, text="Flat-footed:").grid(row=8,
                                                      column=0, sticky='e', padx=2, pady=2)
        self.labels['flatfooted_ac'] = ttk.Label(
            ac_frame, text="10", width=5, relief='sunken')
        self.labels['flatfooted_ac'].grid(row=8, column=1, padx=2, pady=2)

        # Hit Points Section
        hp_frame = ttk.LabelFrame(
            scrollable_frame,
            text="Hit Points",
            padding=10)
        hp_frame.grid(
            row=2,
            column=2,
            columnspan=2,
            sticky='ew',
            padx=5,
            pady=5)

        ttk.Label(
            hp_frame,
            text="Max HP:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['max_hp'] = ttk.Entry(hp_frame, width=8)
        self.entries['max_hp'].grid(row=0, column=1, padx=2, pady=2)
        self.entries['max_hp'].insert(0, "0")

        ttk.Label(
            hp_frame,
            text="Current HP:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['current_hp'] = ttk.Entry(hp_frame, width=8)
        self.entries['current_hp'].grid(row=1, column=1, padx=2, pady=2)
        self.entries['current_hp'].insert(0, "0")

        # Combat Section
        combat_frame = ttk.LabelFrame(
            scrollable_frame, text="Combat", padding=10)
        combat_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky='ew',
            padx=5,
            pady=5)

        # Initiative
        ttk.Label(
            combat_frame,
            text="Initiative:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.labels['initiative'] = ttk.Label(
            combat_frame,
            text="+0",
            width=5,
            relief='sunken',
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['initiative'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            combat_frame,
            text="Misc:").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['initiative_misc'] = ttk.Entry(combat_frame, width=5)
        self.entries['initiative_misc'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['initiative_misc'].insert(0, "0")
        self.entries['initiative_misc'].bind(
            '<FocusOut>', lambda e: self.gui.update_all_calculated_fields())

        # Base Attack Bonus
        ttk.Label(
            combat_frame,
            text="Base Attack Bonus:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['bab'] = ttk.Entry(combat_frame, width=5)
        self.entries['bab'].grid(row=1, column=1, padx=2, pady=2)
        self.entries['bab'].insert(0, "0")
        self.entries['bab'].bind('<FocusOut>',
                                 lambda e: self.gui.update_all_calculated_fields())

        # Spell Resistance
        ttk.Label(
            combat_frame,
            text="Spell Resistance:").grid(
            row=2,
            column=0,
            sticky='e',
            padx=2,
            pady=2)

        self.entries['spell_resistance'] = ttk.Entry(combat_frame, width=5)
        self.entries['spell_resistance'].grid(row=2, column=1, padx=2, pady=2)
        self.entries['spell_resistance'].insert(0, "0")

        # Weapons Section
        weapons_frame = ttk.LabelFrame(
            scrollable_frame, text="Weapons", padding=10)
        weapons_frame.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky='ew',
            padx=5,
            pady=5)

        # Add weapon controls
        add_weapon_frame = ttk.Frame(weapons_frame)
        add_weapon_frame.pack(fill='x', pady=(0, 5))

        # Row 0: Name, Type, Size
        ttk.Label(
            add_weapon_frame,
            text="Weapon Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_name'] = ttk.Entry(add_weapon_frame, width=20)
        self.entries['weapon_name'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            add_weapon_frame,
            text="Type:").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        weapon_types = ['Melee', 'Ranged']
        self.entries['weapon_type'] = ttk.Combobox(
            add_weapon_frame, width=10, values=weapon_types)
        self.entries['weapon_type'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['weapon_type'].current(0)

        ttk.Label(
            add_weapon_frame,
            text="Size:").grid(
            row=0,
            column=4,
            sticky='e',
            padx=2,
            pady=2)
        weapon_sizes = [
            'Fine',
            'Diminutive',
            'Tiny',
            'Small',
            'Medium',
            'Large',
            'Huge',
            'Gargantuan',
            'Colossal']
        self.entries['weapon_size'] = ttk.Combobox(
            add_weapon_frame, width=10, values=weapon_sizes)
        self.entries['weapon_size'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['weapon_size'].current(4)  # Medium

        # Row 1: Damage, Critical, Damage Type
        ttk.Label(
            add_weapon_frame,
            text="Damage:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_damage'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_damage'].grid(row=1, column=1, padx=2, pady=2)

        ttk.Label(
            add_weapon_frame,
            text="Critical:").grid(
            row=1,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_crit'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_crit'].grid(row=1, column=3, padx=2, pady=2)
        self.entries['weapon_crit'].insert(0, "20/x2")

        ttk.Label(
            add_weapon_frame,
            text="Damage Type:").grid(
            row=1,
            column=4,
            sticky='e',
            padx=2,
            pady=2)
        damage_types = [
            'Slashing',
            'Piercing',
            'Bludgeoning',
            'S/P',
            'P/B',
            'S/B',
            'S/P/B']
        self.entries['weapon_damage_type'] = ttk.Combobox(
            add_weapon_frame, width=12, values=damage_types)
        self.entries['weapon_damage_type'].grid(
            row=1, column=5, padx=2, pady=2)
        self.entries['weapon_damage_type'].current(0)

        # Row 2: Range, Weight, Enhancement Bonus
        ttk.Label(
            add_weapon_frame,
            text="Range:").grid(
            row=2,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_range'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_range'].grid(row=2, column=1, padx=2, pady=2)

        ttk.Label(
            add_weapon_frame,
            text="Weight (lbs):").grid(
            row=2,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_weight'] = ttk.Entry(add_weapon_frame, width=10)
        self.entries['weapon_weight'].grid(row=2, column=3, padx=2, pady=2)
        self.entries['weapon_weight'].insert(0, "0")

        ttk.Label(
            add_weapon_frame,
            text="Enhancement:").grid(
            row=2,
            column=4,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_attack_bonus'] = ttk.Entry(
            add_weapon_frame, width=5)
        self.entries['weapon_attack_bonus'].grid(
            row=2, column=5, sticky='w', padx=2, pady=2)
        self.entries['weapon_attack_bonus'].insert(0, "0")

        # Row 3: Misc Attack/Damage Bonuses
        ttk.Label(
            add_weapon_frame,
            text="Misc Attack:").grid(
            row=3,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_misc_attack'] = ttk.Entry(
            add_weapon_frame, width=5)
        self.entries['weapon_misc_attack'].grid(
            row=3, column=1, sticky='w', padx=2, pady=2)
        self.entries['weapon_misc_attack'].insert(0, "0")

        ttk.Label(
            add_weapon_frame,
            text="Misc Damage:").grid(
            row=3,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_damage_bonus'] = ttk.Entry(
            add_weapon_frame, width=5)
        self.entries['weapon_damage_bonus'].grid(
            row=3, column=3, sticky='w', padx=2, pady=2)
        self.entries['weapon_damage_bonus'].insert(0, "0")

        # Row 4: Notes
        ttk.Label(
            add_weapon_frame,
            text="Notes:").grid(
            row=4,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['weapon_notes'] = ttk.Entry(add_weapon_frame, width=60)
        self.entries['weapon_notes'].grid(
            row=4, column=1, columnspan=5, sticky='ew', padx=2, pady=2)

        add_weapon_btn = ttk.Button(
            add_weapon_frame,
            text="Add Weapon",
            command=self.add_weapon)
        add_weapon_btn.grid(row=5, column=0, columnspan=6, pady=5)

        # Weapons list
        weapons_list_frame = ttk.Frame(weapons_frame)
        weapons_list_frame.pack(fill='both', expand=True)

        weapons_scroll = ttk.Scrollbar(weapons_list_frame)
        weapons_scroll.pack(side='right', fill='y')

        columns = (
            'name',
            'type',
            'attack',
            'damage',
            'critical',
            'range',
            'damage_type',
            'size',
            'weight',
            'notes')
        self.weapons_tree = ttk.Treeview(
            weapons_list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=weapons_scroll.set,
            height=6)

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
        
        # Bind double-click to show weapon details
        self.weapons_tree.bind('<Double-Button-1>', self.show_weapon_details)

        # Remove weapon button
        remove_weapon_btn = ttk.Button(
            weapons_frame,
            text="Remove Selected Weapon",
            command=self.remove_weapon)
        remove_weapon_btn.pack(pady=5)

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
        scrollbar = ttk.Scrollbar(
            info_frame,
            orient="vertical",
            command=canvas.yview)
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
            ttk.Label(
                classes_frame,
                text="Class",
                font=(
                    'TkDefaultFont',
                    9,
                    'bold')).grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
                sticky='w')
            ttk.Label(
                classes_frame,
                text="Level",
                font=(
                    'TkDefaultFont',
                    9,
                    'bold')).grid(
                row=0,
                column=1,
                padx=5,
                pady=5)
            ttk.Label(
                classes_frame,
                text="",
                font=(
                    'TkDefaultFont',
                    9,
                    'bold')).grid(
                row=0,
                column=2,
                padx=5,
                pady=5)

            # Display each class
            for idx, class_info in enumerate(self.character.classes):
                class_name = class_info['name']
                class_level = class_info['level']

                # Class name label
                ttk.Label(
                    classes_frame,
                    text=class_name).grid(
                    row=idx + 1,
                    column=0,
                    padx=5,
                    pady=2,
                    sticky='w')

                # Level spinbox
                level_var = tk.IntVar(value=class_level)
                level_spinbox = ttk.Spinbox(
                    classes_frame,
                    from_=1,
                    to=20,
                    textvariable=level_var,
                    width=5)
                level_spinbox.grid(row=idx + 1, column=1, padx=5, pady=2)

                class_entries[class_name] = level_var

                # Update level callback
                def update_level(cn=class_name, lv=level_var):
                    for c in self.character.classes:
                        if c['name'] == cn:
                            c['level'] = lv.get()
                            break
                    self.character.update_class_based_stats()
                    update_total_label()
                    self.update_class_display()
                    # Refresh all GUI fields to reflect updated HP, saves, etc.
                    self.gui.populate_fields_from_character()
                    self.gui.update_all_calculated_fields()
                    if hasattr(self.gui, 'spells_tab'):
                        self.gui.spells_tab.update()
                    # Refresh skills display to show updated skill points
                    if hasattr(self.gui, 'skills_tab') and hasattr(self.gui.skills_tab, 'refresh_skills_display'):
                        self.gui.skills_tab.refresh_skills_display()
                    self.mark_modified()

                level_spinbox.config(command=update_level)

                # Remove button (only if more than one class)
                if len(self.character.classes) > 1:
                    remove_btn = ttk.Button(
                        classes_frame,
                        text="Remove",
                        command=lambda cn=class_name: remove_class(cn))
                    remove_btn.grid(row=idx + 1, column=2, padx=5, pady=2)

            update_total_label()

        def remove_class(class_name):
            """Remove a class"""
            if len(self.character.classes) <= 1:
                messagebox.showwarning("Cannot Remove",
                                       "Character must have at least one class!")
                return

            self.character.remove_class(class_name)
            self.character.update_class_based_stats()
            refresh_classes_display()
            self.update_class_display()
            # Refresh all GUI fields to reflect updated HP, saves, etc.
            self.gui.populate_fields_from_character()
            self.gui.update_all_calculated_fields()
            if hasattr(self.gui, 'spells_tab'):
                self.gui.spells_tab.update()
            # Refresh skills display to show updated skill points
            if hasattr(self.gui, 'skills_tab') and hasattr(self.gui.skills_tab, 'refresh_skills_display'):
                self.gui.skills_tab.refresh_skills_display()
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
            selection_frame = ttk.LabelFrame(
                add_dialog, text="Select Class", padding=10)
            selection_frame.pack(fill='x', padx=10, pady=10)

            ttk.Label(selection_frame, text="Choose a class to add:").pack(pady=5)

            # Get available classes (exclude ones already taken)
            current_classes = [c['name'] for c in self.character.classes]
            available_base_classes = [c for c in sorted(
                CLASS_DEFINITIONS.keys()) if c not in current_classes]
            available_prestige_classes = [c for c in sorted(
                get_all_prestige_classes()) if c not in current_classes]

            # Combine base and prestige classes with separator
            all_available = []
            if available_base_classes:
                all_available.extend(available_base_classes)
            if available_prestige_classes:
                if all_available:
                    all_available.append("--- PRESTIGE CLASSES ---")
                all_available.extend(available_prestige_classes)

            if not all_available or all_available == ["--- PRESTIGE CLASSES ---"]:
                messagebox.showinfo(
                    "No Classes Available",
                    "You already have all available classes!")
                add_dialog.destroy()
                return

            class_var = tk.StringVar(value=all_available[0])
            class_combo = ttk.Combobox(
                selection_frame,
                textvariable=class_var,
                values=all_available,
                state='readonly',
                width=30)
            class_combo.pack(pady=5)

            # Requirements display
            req_frame = ttk.LabelFrame(add_dialog, text="Requirements", padding=10)
            req_frame.pack(fill='both', expand=True, padx=10, pady=10)

            req_text = tk.Text(
                req_frame,
                height=12,
                width=55,
                wrap='word',
                state='disabled')
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
                    eligible, requirements = self.character.check_prestige_requirements(
                        selected)

                    prestige_info = PRESTIGE_CLASS_DEFINITIONS[selected]
                    req_text.insert(tk.END, f"Prestige Class: {selected}\n\n", 'bold')
                    req_text.insert(tk.END, f"{prestige_info['description']}\n\n")

                    if eligible:
                        req_text.insert(
                            tk.END,
                            "✓ You meet the basic requirements!\n\n",
                            'success')
                    else:
                        req_text.insert(
                            tk.END,
                            "⚠ Requirements not fully verified:\n\n",
                            'warning')

                    req_text.insert(tk.END, "Requirements:\n")
                    for req in requirements:
                        req_text.insert(tk.END, f"  • {req}\n")

                    # Configure tags
                    req_text.tag_config('bold', font=('TkDefaultFont', 9, 'bold'))
                    req_text.tag_config(
                        'success', foreground='green', font=(
                            'TkDefaultFont', 9, 'bold'))
                    req_text.tag_config(
                        'warning', foreground='orange', font=(
                            'TkDefaultFont', 9, 'bold'))
                else:
                    # Base class - no special requirements
                    req_text.insert(tk.END, f"Base Class: {selected}\n\n")
                    req_text.insert(tk.END, "No special requirements.")

                req_text.config(state='disabled')

            class_combo.bind(
                '<<ComboboxSelected>>',
                lambda e: update_requirements())
            update_requirements()  # Initial display

            # Buttons
            button_frame = ttk.Frame(add_dialog)
            button_frame.pack(fill='x', padx=10, pady=10)

            def confirm_add():
                selected_class = class_var.get()

                if selected_class == "--- PRESTIGE CLASSES ---":
                    messagebox.showwarning(
                        "Invalid Selection",
                        "Please select an actual class.")
                    return

                # Warn if adding prestige class with unmet requirements
                if is_prestige_class(selected_class):
                    eligible, requirements = self.character.check_prestige_requirements(
                        selected_class)
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
                self.update_class_display()
                # Refresh all GUI fields to reflect updated HP, saves, etc.
                self.gui.populate_fields_from_character()
                self.gui.update_all_calculated_fields()
                if hasattr(self.gui, 'spells_tab'):
                    self.gui.spells_tab.update()
                # Refresh skills display to show updated skill points
                if hasattr(self.gui, 'skills_tab') and hasattr(self.gui.skills_tab, 'refresh_skills_display'):
                    self.gui.skills_tab.refresh_skills_display()
                self.mark_modified()
                add_dialog.destroy()

            ttk.Button(
                button_frame,
                text="Add Class",
                command=confirm_add).pack(
                side='left',
                padx=5)
            ttk.Button(
                button_frame,
                text="Cancel",
                command=add_dialog.destroy).pack(
                side='right',
                padx=5)

        # Total level display
        total_frame = ttk.Frame(dialog)
        total_frame.pack(fill='x', padx=10, pady=5)

        ttk.Label(
            total_frame,
            text="Total Level:",
            font=(
                'TkDefaultFont',
                10,
                'bold')).pack(
            side='left',
            padx=5)
        total_label = ttk.Label(
            total_frame, text="1", font=(
                'TkDefaultFont', 10, 'bold'))
        total_label.pack(side='left', padx=5)

        def update_total_label():
            total = self.character.get_total_level()
            total_label.config(text=str(total))

        # Buttons frame
        button_frame = ttk.Frame(dialog)
        button_frame.pack(fill='x', padx=10, pady=10)

        def close_dialog():
            """Close dialog and update all displays"""
            self.update_class_display()
            self.gui.update_all_calculated_fields()
            # Update spells tab to recalculate spell slots
            if hasattr(self.gui, 'spells_tab'):
                self.gui.spells_tab.update()
            dialog.destroy()

        ttk.Button(
            button_frame,
            text="Add Class",
            command=add_new_class).pack(
            side='left',
            padx=5)
        ttk.Button(
            button_frame,
            text="Close",
            command=close_dialog).pack(
            side='right',
            padx=5)

        # Initial display
        refresh_classes_display()

    def update_ability_score(self, ability):
        """Update ability score and all dependent fields"""
        # Update character model
        score = self.get_entry_int(ability, 10)
        temp = self.get_entry_int(f'{ability}_temp', 0)

        setattr(self.character, ability, score)
        setattr(self.character, f'{ability[0:3]}_temp_mod', temp)

        # Update all calculated fields
        self.gui.update_all_calculated_fields()

        # Update inventory if strength changed
        if ability == 'strength':
            self.gui.update_inventory_display()

    def show_level_up_dialog(self):
        """Show dialog for leveling up character"""
        import random

        dialog = tk.Toplevel(self.root)
        dialog.title("Level Up!")
        dialog.geometry("550x600")  # Increased size to show all content
        dialog.transient(self.root)
        dialog.grab_set()

        # Class selection for multiclass
        class_select_frame = ttk.LabelFrame(
            dialog, text="Select Class to Level", padding=10)
        class_select_frame.pack(fill='x', padx=10, pady=10)

        ttk.Label(
            class_select_frame,
            text="Level up which class?").pack(
            anchor='w')

        class_options = [
            f"{c['name']} (currently level {c['level']})" for c in self.character.classes]
        class_var = tk.StringVar(value=class_options[0])
        class_combo = ttk.Combobox(
            class_select_frame,
            textvariable=class_var,
            values=class_options,
            state='readonly',
            width=30)
        class_combo.pack(pady=5, fill='x')

        # Get selected class info
        def get_selected_class_name():
            selection = class_var.get()
            # Extract class name before parenthesis
            return selection.split(' (')[0]

        def update_class_info():
            selected_class = get_selected_class_name()
            class_info = CLASS_DEFINITIONS[selected_class]
            hit_die = class_info['hit_die']

            current_level = self.character.get_class_level(selected_class)

            info_text = f"Current Level: {self.character.get_total_level()}\n"
            info_text += f"New Total Level: {
                self.character.get_total_level() + 1}\n"
            info_text += f"{selected_class} Level: {current_level} → {current_level + 1}\n"
            info_text += f"Hit Die: d{hit_die}"

            info_label.config(text=info_text)

            hp_instructions.config(
                text=f"Roll 1d{hit_die} for HP (or use average: {(hit_die // 2) + 1})")
            hp_entry.delete(0, tk.END)
            hp_entry.insert(0, str((hit_die // 2) + 1))
            roll_button.config(
                text=f"Roll d{hit_die}", command=lambda: hp_entry.delete(
                    0, tk.END) or hp_entry.insert(
                    0, str(
                        random.randint(
                            1, hit_die))))

        class_combo.bind('<<ComboboxSelected>>', lambda e: update_class_info())

        # Info frame
        info_frame = ttk.LabelFrame(
            dialog, text="Level Up Information", padding=10)
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

        ttk.Label(
            hp_roll_frame,
            text="HP Roll:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=5)
        hp_entry = ttk.Entry(hp_roll_frame, width=10)
        hp_entry.grid(row=0, column=1, sticky='w', padx=5)

        roll_button = ttk.Button(
            hp_roll_frame,
            text="Roll",
            command=lambda: None)
        roll_button.grid(row=0, column=2, padx=5)

        con_mod = self.character.get_con_modifier()
        con_mod_str = f"+{con_mod}" if con_mod >= 0 else str(con_mod)
        ttk.Label(
            hp_frame,
            text=f"CON Modifier: {con_mod_str} (added automatically)").pack(
            anchor='w')

        # Initialize display
        update_class_info()

        # Preview frame
        preview_frame = ttk.LabelFrame(
            dialog, text="Level Up Preview", padding=10)
        preview_frame.pack(fill='both', expand=True, padx=10, pady=10)

        preview_text = tk.Text(
            preview_frame,
            height=8,
            width=50,
            wrap='word',
            state='disabled')
        preview_scrollbar = ttk.Scrollbar(
            preview_frame, command=preview_text.yview)
        preview_text.config(yscrollcommand=preview_scrollbar.set)
        preview_text.pack(side='left', fill='both', expand=True)
        preview_scrollbar.pack(side='right', fill='y')

        def update_preview():
            try:
                hp_roll = int(hp_entry.get())
            except BaseException:
                selected_class = get_selected_class_name()
                class_info = CLASS_DEFINITIONS[selected_class]
                hit_die = class_info['hit_die']
                hp_roll = (hit_die // 2) + 1
            
            selected_class = get_selected_class_name()
            class_info = CLASS_DEFINITIONS[selected_class]

            # Calculate preview
            hp_gain = max(1, hp_roll + con_mod)
            new_total_level = self.character.get_total_level() + 1

            skill_points = class_info['skill_points'] + \
                self.character.get_int_modifier()
            skill_points = max(1, skill_points)

            preview_text.config(state='normal')
            preview_text.delete(1.0, tk.END)
            preview_text.insert(tk.END, f"Class: {selected_class}\n")
            preview_text.insert(tk.END, f"HP Gained: +{hp_gain}\n")
            preview_text.insert(
                tk.END, f"New Max HP: {
                    self.character.max_hp + hp_gain}\n")
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
            except BaseException:
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
            self.character.hit_dice.append(
                {'class': selected_class, 'roll': hp_roll, 'con_mod': con_mod})
            self.character.max_hp += hp_gain
            self.character.current_hp += hp_gain

            # Add skill points
            skill_points = class_info['skill_points'] + \
                self.character.get_int_modifier()
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
            self.labels['next_level_xp'].config(
                text=str(self.character.next_level_xp))

            # Update skill points label if it exists
            if 'skill_points_available' in self.labels:
                self.labels['skill_points_available'].config(
                    text=str(self.character.skill_points_available))

            self.gui.update_all_calculated_fields()
            self.mark_modified()

            # Build level up message
            level_up_msg = f"Congratulations! {selected_class} level increased!\n\n"
            level_up_msg += f"Total Level: {new_level}\n"
            level_up_msg += f"HP gained: +{hp_gain}\n"
            level_up_msg += f"Skill points: +{skill_points}\n"
            level_up_msg += f"BAB: +{self.character.base_attack_bonus}\n"
            level_up_msg += f"Saves - Fort: +{
                self.character.fort_base}, Ref: +{
                self.character.ref_base}, Will: +{
                self.character.will_base}\n"

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
                    level_up_msg += f"• You can select a new Epic Feat (Total: {
                        epic_info['epic_feats']})\n"
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

        ttk.Button(
            button_frame,
            text="Level Up!",
            command=do_level_up).pack(
            side='left',
            padx=5)
        ttk.Button(
            button_frame,
            text="Cancel",
            command=dialog.destroy).pack(
            side='left',
            padx=5)

    def update_class_display(self):
        """Update the class display label to show all classes"""
        class_text = " / ".join(
            [f"{c['name']} {c['level']}" for c in self.character.classes])
        self.class_display.config(text=class_text)

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

        self.gui.update_all_calculated_fields()
        self.mark_modified()

    def add_weapon(self):
        """Add a weapon to the character"""
        name = self.entries['weapon_name'].get().strip()
        if not name:
            messagebox.showwarning(
                "Missing Information",
                "Please enter a weapon name.")
            return

        try:
            attack_bonus = int(self.entries['weapon_attack_bonus'].get())
            misc_attack = int(self.entries['weapon_misc_attack'].get())
            damage_bonus = int(self.entries['weapon_damage_bonus'].get())
            weight = float(self.entries['weapon_weight'].get())
        except ValueError:
            messagebox.showwarning(
                "Invalid Input",
                "Attack bonuses, damage bonus, and weight must be numbers.")
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

    def show_weapon_details(self, event=None):
        """Show detailed information about a weapon in an editable dialog"""
        selection = self.weapons_tree.selection()
        if not selection:
            return

        item = self.weapons_tree.item(selection[0])
        weapon_name = item['values'][0]

        # Find the weapon and its index
        weapon = None
        weapon_index = None
        for idx, w in enumerate(self.character.weapons):
            if w['name'] == weapon_name:
                weapon = w
                weapon_index = idx
                break

        if not weapon or weapon_index is None:
            return

        # Create detail dialog
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Edit Weapon: {weapon['name']}")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()

        # Main frame
        main_frame = ttk.Frame(dialog, padding=10)
        main_frame.pack(fill='both', expand=True)

        # Title
        ttk.Label(main_frame, text="Edit Weapon", font=('TkDefaultFont', 14, 'bold')).pack(pady=10)

        # Basic info frame
        basic_frame = ttk.LabelFrame(main_frame, text="Weapon Information", padding=10)
        basic_frame.pack(fill='x', pady=5)

        # Name
        ttk.Label(basic_frame, text="Name:").grid(row=0, column=0, sticky='e', padx=5, pady=3)
        name_var = tk.StringVar(value=weapon['name'])
        ttk.Entry(basic_frame, textvariable=name_var, width=40).grid(row=0, column=1, columnspan=3, sticky='ew', padx=5, pady=3)

        # Type and Attack
        ttk.Label(basic_frame, text="Type:").grid(row=1, column=0, sticky='e', padx=5, pady=3)
        weapon_types = ['Melee', 'Ranged', 'Both']
        type_var = tk.StringVar(value=weapon.get('type', 'Melee'))
        ttk.Combobox(basic_frame, textvariable=type_var, values=weapon_types, width=12).grid(row=1, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text="Attack Bonus:").grid(row=1, column=2, sticky='e', padx=5, pady=3)
        attack_var = tk.IntVar(value=weapon.get('attack_bonus', 0))
        ttk.Spinbox(basic_frame, from_=-5, to=20, textvariable=attack_var, width=8).grid(row=1, column=3, sticky='w', padx=5, pady=3)

        # Damage and Critical
        ttk.Label(basic_frame, text="Damage:").grid(row=2, column=0, sticky='e', padx=5, pady=3)
        damage_var = tk.StringVar(value=weapon.get('damage', '1d8'))
        ttk.Entry(basic_frame, textvariable=damage_var, width=15).grid(row=2, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text="Critical:").grid(row=2, column=2, sticky='e', padx=5, pady=3)
        critical_var = tk.StringVar(value=weapon.get('critical', '20/x2'))
        ttk.Entry(basic_frame, textvariable=critical_var, width=15).grid(row=2, column=3, sticky='w', padx=5, pady=3)

        # Range and Damage Type
        ttk.Label(basic_frame, text="Range:").grid(row=3, column=0, sticky='e', padx=5, pady=3)
        range_var = tk.StringVar(value=weapon.get('range', '-'))
        ttk.Entry(basic_frame, textvariable=range_var, width=15).grid(row=3, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text="Damage Type:").grid(row=3, column=2, sticky='e', padx=5, pady=3)
        damage_types = ['Slashing', 'Piercing', 'Bludgeoning', 'S/P', 'P/B', 'S/B', 'S/P/B']
        damage_type_var = tk.StringVar(value=weapon.get('damage_type', 'Slashing'))
        ttk.Combobox(basic_frame, textvariable=damage_type_var, values=damage_types, width=12).grid(row=3, column=3, sticky='w', padx=5, pady=3)

        # Size and Weight
        ttk.Label(basic_frame, text="Size:").grid(row=4, column=0, sticky='e', padx=5, pady=3)
        sizes = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal']
        size_var = tk.StringVar(value=weapon.get('size', 'Medium'))
        ttk.Combobox(basic_frame, textvariable=size_var, values=sizes, width=12).grid(row=4, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text="Weight:").grid(row=4, column=2, sticky='e', padx=5, pady=3)
        weight_var = tk.StringVar(value=weapon.get('weight', ''))
        ttk.Entry(basic_frame, textvariable=weight_var, width=15).grid(row=4, column=3, sticky='w', padx=5, pady=3)

        # Notes frame
        notes_frame = ttk.LabelFrame(main_frame, text="Notes", padding=10)
        notes_frame.pack(fill='both', expand=True, pady=5)

        notes_text = tk.Text(notes_frame, height=8, width=60, wrap='word')
        notes_scroll = ttk.Scrollbar(notes_frame, command=notes_text.yview)
        notes_text.config(yscrollcommand=notes_scroll.set)
        notes_text.insert('1.0', weapon.get('notes', ''))
        notes_text.pack(side='left', fill='both', expand=True)
        notes_scroll.pack(side='right', fill='y')

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        def save_changes():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning("Missing Name", "Please enter a weapon name.", parent=dialog)
                return

            # Update weapon
            self.character.weapons[weapon_index] = {
                'name': name,
                'type': type_var.get(),
                'attack_bonus': attack_var.get(),
                'damage': damage_var.get(),
                'critical': critical_var.get(),
                'range': range_var.get(),
                'damage_type': damage_type_var.get(),
                'size': size_var.get(),
                'weight': weight_var.get(),
                'notes': notes_text.get('1.0', 'end-1c').strip()
            }

            self.refresh_weapons()
            self.mark_modified()
            dialog.destroy()

        ttk.Button(btn_frame, text="Save", command=save_changes, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy, width=15).pack(side='left', padx=5)

    def remove_weapon(self):
        """Remove the selected weapon"""
        selection = self.weapons_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a weapon to remove.")
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
                total_attack = bab + str_mod + \
                    weapon.get('attack_bonus', 0) + weapon.get('misc_attack', 0)
                ability_mod = str_mod
            else:  # ranged
                total_attack = bab + dex_mod + \
                    weapon.get('attack_bonus', 0) + weapon.get('misc_attack', 0)
                ability_mod = dex_mod

            attack_text = f"+{total_attack}" if total_attack >= 0 else str(
                total_attack)

            # Calculate total damage (base + ability + enhancement + misc)
            base_damage = weapon.get('damage', '')
            damage_bonus = weapon.get('damage_bonus', 0)
            # Enhancement bonus applies to damage too
            enhancement = weapon.get('attack_bonus', 0)

            # For melee weapons, add STR mod to damage; for ranged, typically don't
            # (except for composite bows, etc.)
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
    
    def update_ac_components(self, magic_armor, magic_shield, magic_natural, magic_deflection):
        """Update AC component displays to show magic item bonuses"""
        # Update the magic bonus labels to show what's being added from equipment
        bonus_mapping = {
            'armor_bonus_magic': magic_armor,
            'shield_bonus_magic': magic_shield,
            'natural_armor_magic': magic_natural,
            'deflection_bonus_magic': magic_deflection
        }
        
        for label_key, bonus_value in bonus_mapping.items():
            if label_key in self.labels:
                if bonus_value > 0:
                    self.labels[label_key].config(text=f"+{bonus_value} (magic)", foreground='blue')
                else:
                    self.labels[label_key].config(text="")
    
    def update_save_components(self, magic_resistance):
        """Update saving throw displays to show magic item bonuses"""
        # Update magic bonus labels for all three saves
        for save_key in ['fort', 'ref', 'will']:
            label_key = f'{save_key}_magic'
            if label_key in self.labels:
                if magic_resistance > 0:
                    self.labels[label_key].config(text=f"+{magic_resistance} (magic)", foreground='blue')
                else:
                    self.labels[label_key].config(text="")
