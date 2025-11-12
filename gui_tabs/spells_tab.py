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

        # Spell list frame
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

        # Spell list with scrollbar
        list_frame = ttk.Frame(spells_list_frame)
        list_frame.pack(fill='both', expand=True)

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')

        # Create treeview for spells
        columns = (
            'name',
            'level',
            'school',
            'range',
            'duration',
            'components',
            'prepared')
        self.spells_tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=scrollbar.set)

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

        remove_spell_btn = ttk.Button(
            remove_frame,
            text="Remove Selected Spell",
            command=self.remove_spell_from_list)
        remove_spell_btn.pack(side='left', padx=2)

        filter_frame = ttk.Frame(remove_frame)
        filter_frame.pack(side='right')

        ttk.Label(
            filter_frame,
            text="Filter by Level:").pack(
            side='left',
            padx=2)
        self.spell_filter_var = tk.StringVar(value="All")
        filter_combo = ttk.Combobox(filter_frame,
                                    width=8,
                                    textvariable=self.spell_filter_var,
                                    values=["All"] + [str(i) for i in range(10)],
                                    state='readonly')
        filter_combo.pack(side='left', padx=2)
        filter_combo.bind('<<ComboboxSelected>>',
                          lambda e: self.update_spell_list_display())

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
        selection = self.spells_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a spell to remove.")
            return

        item = selection[0]
        index = self.spells_tree.index(item)

        # Account for filter
        filter_level = self.spell_filter_var.get()
        if filter_level != "All":
            # Find the actual index in the full spell list
            filtered_spells = [
                s for s in self.character.spells if str(
                    s['level']) == filter_level]
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
            filtered_spells = [
                s for s in self.character.spells if str(
                    s['level']) == filter_level]
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
            spells_to_show = [
                s for s in spells_to_show if str(
                    s['level']) == filter_level]

        # Sort by level, then name
        spells_to_show = sorted(
            spells_to_show, key=lambda x: (
                x['level'], x['name']))

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
