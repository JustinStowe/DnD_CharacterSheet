"""
Spells Tab
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab


class SpellsTab(BaseTab):
    """Spells management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        """Build the spells tab"""
        # Create main container
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)

        # Top frame for spellcasting info
        casting_frame = ttk.LabelFrame(
            main_container, text="Spellcasting", padding=10)
        casting_frame.pack(fill='x', padx=5, pady=5)

        # Spellcasting ability
        ability_frame = ttk.Frame(casting_frame)
        ability_frame.pack(fill='x')

        ttk.Label(
            ability_frame,
            text="Spellcasting Ability:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=5)

        self.spellcasting_ability_var = tk.StringVar(value='intelligence')
        ability_options = [
            ('Intelligence', 'intelligence'),
            ('Wisdom', 'wisdom'),
            ('Charisma', 'charisma')
        ]

        for i, (label, value) in enumerate(ability_options):
            rb = ttk.Radiobutton(
                ability_frame,
                text=label,
                variable=self.spellcasting_ability_var,
                value=value,
                command=self.update_spellcasting_ability)
            rb.grid(row=0, column=i + 1, padx=5, pady=5)

        # Spellcasting modifier and DC
        ttk.Label(
            ability_frame,
            text="Modifier:",
            font=(
                'Arial',
                10)).grid(
            row=0,
            column=4,
            sticky='e',
            padx=5,
            pady=5)
        self.labels['spell_modifier'] = ttk.Label(
            ability_frame,
            text="+0",
            relief='sunken',
            width=5,
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['spell_modifier'].grid(row=0, column=5, padx=5, pady=5)

        # Spell slots frame
        slots_frame = ttk.LabelFrame(
            main_container, text="Spell Slots", padding=10)
        slots_frame.pack(fill='x', padx=5, pady=5)

        # Headers
        ttk.Label(
            slots_frame,
            text="Level",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=0,
            padx=5,
            pady=2)
        ttk.Label(
            slots_frame,
            text="Save DC",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=1,
            padx=5,
            pady=2)
        ttk.Label(
            slots_frame,
            text="Max Slots",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=2,
            padx=5,
            pady=2)
        ttk.Label(
            slots_frame,
            text="Used",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=3,
            padx=5,
            pady=2)
        ttk.Label(
            slots_frame,
            text="Remaining",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=4,
            padx=5,
            pady=2)

        # Create spell slot rows for levels 0-9
        for level in range(10):
            row = level + 1

            # Level label
            level_text = "Cantrips" if level == 0 else f"{level}{
                'st' if level == 1 else 'nd' if level == 2 else 'rd' if level == 3 else 'th'}"
            ttk.Label(
                slots_frame,
                text=level_text,
                font=(
                    'Arial',
                    9)).grid(
                row=row,
                column=0,
                padx=5,
                pady=2)

            # Save DC (readonly)
            self.labels[f'spell_dc_{level}'] = ttk.Label(
                slots_frame, text="10", relief='sunken', width=5)
            self.labels[f'spell_dc_{level}'].grid(
                row=row, column=1, padx=5, pady=2)

            # Max slots
            self.entries[f'spell_max_{level}'] = ttk.Entry(slots_frame, width=5)
            self.entries[f'spell_max_{level}'].grid(
                row=row, column=2, padx=5, pady=2)
            self.entries[f'spell_max_{level}'].insert(0, "0")
            self.entries[f'spell_max_{level}'].bind(
                '<FocusOut>', lambda e, l=level: self.update_spell_slots(l))
            self.entries[f'spell_max_{level}'].bind(
                '<KeyRelease>', lambda e: self.mark_modified())

            # Used slots
            self.entries[f'spell_used_{level}'] = ttk.Entry(slots_frame, width=5)
            self.entries[f'spell_used_{level}'].grid(
                row=row, column=3, padx=5, pady=2)
            self.entries[f'spell_used_{level}'].insert(0, "0")
            self.entries[f'spell_used_{level}'].bind(
                '<FocusOut>', lambda e, l=level: self.update_spell_slots(l))
            self.entries[f'spell_used_{level}'].bind(
                '<KeyRelease>', lambda e: self.mark_modified())

            # Remaining (readonly)
            self.labels[f'spell_remaining_{level}'] = ttk.Label(
                slots_frame, text="0", relief='sunken', width=5, font=('Arial', 9, 'bold'))
            self.labels[f'spell_remaining_{level}'].grid(
                row=row, column=4, padx=5, pady=2)

        # Buttons frame
        buttons_frame = ttk.Frame(slots_frame)
        buttons_frame.grid(row=11, column=0, columnspan=5, pady=10)

        # Calculate spell slots button
        calc_btn = ttk.Button(buttons_frame,
                              text="Calculate Spell Slots (from Class/Level)",
                              command=self.calculate_spell_slots_from_class)
        calc_btn.pack(side='left', padx=5)

        # Rest button
        rest_btn = ttk.Button(
            buttons_frame,
            text="Long Rest (Reset Used Slots)",
            command=self.reset_spell_slots)
        rest_btn.pack(side='left', padx=5)

        # Spell list frame with sub-tabs for each spell level
        spells_list_frame = ttk.LabelFrame(
            main_container, text="Spell List", padding=10)
        spells_list_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Add spell controls
        add_frame = ttk.Frame(spells_list_frame)
        add_frame.pack(fill='x', pady=(0, 5))

        ttk.Label(
            add_frame,
            text="Spell Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_name'] = ttk.Entry(add_frame, width=25)
        self.entries['spell_name'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Level:").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_level'] = ttk.Combobox(
            add_frame, width=5, values=list(
                range(10)), state='readonly')
        self.entries['spell_level'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['spell_level'].current(0)

        ttk.Label(
            add_frame,
            text="School:").grid(
            row=0,
            column=4,
            sticky='e',
            padx=2,
            pady=2)
        schools = [
            'Abjuration',
            'Conjuration',
            'Divination',
            'Enchantment',
            'Evocation',
            'Illusion',
            'Necromancy',
            'Transmutation',
            'Universal']
        self.entries['spell_school'] = ttk.Combobox(
            add_frame, width=12, values=schools)
        self.entries['spell_school'].grid(row=0, column=5, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Range:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_range'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_range'].grid(row=1, column=1, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Duration:").grid(
            row=1,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_duration'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_duration'].grid(
            row=1, column=3, columnspan=3, sticky='ew', padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Components:").grid(
            row=2,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_components'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_components'].grid(row=2, column=1, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Casting Time:").grid(
            row=2,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['spell_casting_time'] = ttk.Entry(add_frame, width=15)
        self.entries['spell_casting_time'].grid(
            row=2, column=3, padx=2, pady=2)

        # Prepared checkbox
        self.spell_prepared_var = tk.BooleanVar(value=False)
        prep_cb = ttk.Checkbutton(
            add_frame,
            text="Prepared",
            variable=self.spell_prepared_var)
        prep_cb.grid(row=2, column=4, columnspan=2, padx=2, pady=2)

        add_spell_btn = ttk.Button(
            add_frame,
            text="Add Spell",
            command=self.add_spell_to_list)
        add_spell_btn.grid(row=3, column=0, columnspan=6, pady=5)

        # Create notebook for spell level tabs
        self.spell_level_notebook = ttk.Notebook(spells_list_frame)
        self.spell_level_notebook.pack(fill='both', expand=True)
        
        # Create a tab for each spell level (0-9)
        self.spell_level_frames = {}
        self.spell_level_trees = {}
        
        spell_level_names = [
            "0 (Cantrips)",
            "1st Level",
            "2nd Level",
            "3rd Level",
            "4th Level",
            "5th Level",
            "6th Level",
            "7th Level",
            "8th Level",
            "9th Level"
        ]
        
        # Define columns for the treeview
        columns = (
            'name',
            'school',
            'range',
            'duration',
            'components',
            'prepared',
            'cast')
        
        for level in range(10):
            # Create frame for this spell level
            level_frame = ttk.Frame(self.spell_level_notebook)
            self.spell_level_notebook.add(level_frame, text=spell_level_names[level])
            self.spell_level_frames[level] = level_frame
            
            # Create treeview for this level
            tree_frame = ttk.Frame(level_frame)
            tree_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            scrollbar = ttk.Scrollbar(tree_frame)
            scrollbar.pack(side='right', fill='y')
            
            tree = ttk.Treeview(
                tree_frame,
                columns=columns,
                show='headings',
                yscrollcommand=scrollbar.set)
            
            tree.heading('name', text='Spell Name')
            tree.heading('school', text='School')
            tree.heading('range', text='Range')
            tree.heading('duration', text='Duration')
            tree.heading('components', text='Components')
            tree.heading('prepared', text='Prepared')
            tree.heading('cast', text='Cast')
            
            tree.column('name', width=200)
            tree.column('school', width=100)
            tree.column('range', width=100)
            tree.column('duration', width=150)
            tree.column('components', width=100)
            tree.column('prepared', width=80)
            tree.column('cast', width=60)
            
            tree.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=tree.yview)
            
            # Bind events
            tree.bind('<Double-1>', self.on_spell_double_click)
            tree.bind('<Delete>', self.delete_spell)
            tree.bind('<Button-1>', self.on_spell_click)
            
            self.spell_level_trees[level] = tree
        
        # Keep reference to main tree (level 0) for backward compatibility
        self.spells_tree = self.spell_level_trees[0]

        # Remove button frame (applies to all tabs)
        remove_frame = ttk.Frame(spells_list_frame)
        remove_frame.pack(fill='x', pady=(5, 0))

        remove_spell_btn = ttk.Button(
            remove_frame,
            text="Remove Selected Spell",
            command=self.remove_spell_from_list)
        remove_spell_btn.pack(side='left', padx=2)

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
            messagebox.showinfo(
                "No Spellcasting", f"{
                    self.character.character_class} does not have spellcasting abilities.")

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
        # Get currently active tab (spell level)
        current_tab_index = self.spell_level_notebook.index(
            self.spell_level_notebook.select())
        current_tree = self.spell_level_trees[current_tab_index]
        
        selection = current_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a spell to remove.")
            return

        item = selection[0]
        index = current_tree.index(item)

        # Find the spell in this level's list
        level_spells = [
            s for s in self.character.spells if s['level'] == current_tab_index]
        if index < len(level_spells):
            spell_to_remove = level_spells[index]
            # Find actual index in full spell list
            actual_index = self.character.spells.index(spell_to_remove)
            self.character.remove_spell(actual_index)
            self.update_spell_list_display()
            self.mark_modified()

    def toggle_spell_prepared(self, event):
        """Toggle prepared status of selected spell"""
        # Get which tree was clicked
        widget = event.widget
        
        # Find which level tree this is
        spell_level = None
        for level, tree in self.spell_level_trees.items():
            if tree == widget:
                spell_level = level
                break
        
        if spell_level is None:
            return
        
        selection = widget.selection()
        if not selection:
            return

        item = selection[0]
        index = widget.index(item)

        # Find the spell in this level's list
        level_spells = [
            s for s in self.character.spells if s['level'] == spell_level]
        if index < len(level_spells):
            spell = level_spells[index]
            spell['prepared'] = not spell['prepared']
            self.update_spell_list_display()
            self.mark_modified()
    
    def delete_spell(self, event):
        """Handle delete key press to remove spell"""
        self.remove_spell_from_list()

    def on_spell_click(self, event):
        """Handle single click on spell - check if Cast button was clicked"""
        # Get which tree was clicked
        tree = event.widget
        
        # Find which level tree this is
        spell_level = None
        for level, t in self.spell_level_trees.items():
            if t == tree:
                spell_level = level
                break
        
        if spell_level is None:
            return
        
        # Get the region clicked
        region = tree.identify_region(event.x, event.y)
        if region != "cell":
            return
        
        # Get column clicked
        column = tree.identify_column(event.x)
        
        # Column #7 is the Cast column (0-indexed as #6, but Tkinter uses 1-indexed)
        if column == '#7':  # Cast column
            # Get the item clicked
            item = tree.identify_row(event.y)
            if item:
                self.cast_spell(tree, item, spell_level)
    
    def on_spell_double_click(self, event):
        """Handle double-click on spell - toggle prepared status"""
        # Get which tree was clicked
        tree = event.widget
        
        # Find which level tree this is
        spell_level = None
        for level, t in self.spell_level_trees.items():
            if t == tree:
                spell_level = level
                break
        
        if spell_level is None:
            return
        
        # Get column clicked
        column = tree.identify_column(event.x)
        
        # Don't toggle prepared if clicking on Cast column
        if column == '#7':  # Cast column
            return
        
        # Otherwise, toggle prepared status
        self.toggle_spell_prepared(event)
    
    def cast_spell(self, tree, item, spell_level):
        """Cast a spell - increment used spell slots for that level"""
        # Check if there are available spell slots
        max_slots = self.character.spell_slots_max.get(spell_level, 0)
        used_slots = self.character.spell_slots_used.get(spell_level, 0)
        remaining = max_slots - used_slots
        
        if remaining <= 0:
            messagebox.showwarning(
                "No Spell Slots",
                f"You have no spell slots remaining for level {spell_level} spells.\n\n"
                f"Used: {used_slots}/{max_slots}")
            return
        
        # Get spell name for confirmation
        values = tree.item(item, 'values')
        spell_name = values[0] if values else "spell"
        
        # Increment used spell slots
        self.character.spell_slots_used[spell_level] = used_slots + 1
        
        # Update the GUI entry
        self.entries[f'spell_used_{spell_level}'].delete(0, tk.END)
        self.entries[f'spell_used_{spell_level}'].insert(0, str(used_slots + 1))
        
        # Update remaining label
        self.update_spell_slots(spell_level)
        
        # Show confirmation
        new_remaining = remaining - 1
        messagebox.showinfo(
            "Spell Cast",
            f"Cast: {spell_name}\n\n"
            f"Level {spell_level} Slots Remaining: {new_remaining}/{max_slots}")
        
        self.mark_modified()

    def update_spell_list_display(self):
        """Update all spell list treeviews"""
        # Clear all treeviews
        for tree in self.spell_level_trees.values():
            for item in tree.get_children():
                tree.delete(item)

        # Sort spells by name within each level
        spells_by_level = {}
        for level in range(10):
            spells_by_level[level] = []
        
        for spell in self.character.spells:
            level = spell.get('level', 0)
            if 0 <= level <= 9:
                spells_by_level[level].append(spell)
        
        # Populate each level's treeview
        for level in range(10):
            tree = self.spell_level_trees[level]
            level_spells = sorted(spells_by_level[level], key=lambda x: x['name'])
            
            for spell in level_spells:
                prepared_text = "Yes" if spell.get('prepared', False) else "No"
                tree.insert('', 'end', values=(
                    spell['name'],
                    spell.get('school', ''),
                    spell.get('range', ''),
                    spell.get('duration', ''),
                    spell.get('components', ''),
                    prepared_text,
                    '[Cast]'
                ))
