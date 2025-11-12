"""
Feats Tab
"""

import tkinter as tk
from tkinter import ttk, messagebox
from Epic_levels.epic_levels import EPIC_FEATS
from .base_tab import BaseTab


class FeatsTab(BaseTab):
    """Feats management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        """Build the feats and special abilities tab"""
        # Create main container with two sections
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)

        # Create paned window to split feats and abilities
        paned = ttk.PanedWindow(main_container, orient='vertical')
        paned.pack(fill='both', expand=True)

        # ===== FEATS SECTION =====
        feats_container = ttk.LabelFrame(paned, text="Feats", padding=10)
        # Give more space to feats section
        paned.add(feats_container, weight=3)

        # Add feat controls
        add_feat_frame = ttk.Frame(feats_container)
        add_feat_frame.pack(fill='x', pady=(0, 5))

        ttk.Label(
            add_feat_frame,
            text="Feat Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['feat_name'] = ttk.Entry(add_feat_frame, width=25)
        self.entries['feat_name'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            add_feat_frame,
            text="Type:").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        feat_types = [
            'General',
            'Metamagic',
            'Item Creation',
            'Combat',
            'Skill',
            'Special']
        self.entries['feat_type'] = ttk.Combobox(
            add_feat_frame, width=15, values=feat_types)
        self.entries['feat_type'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['feat_type'].current(0)

        ttk.Label(
            add_feat_frame,
            text="Prerequisites:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['feat_prereq'] = ttk.Entry(add_feat_frame, width=40)
        self.entries['feat_prereq'].grid(
            row=1, column=1, columnspan=3, sticky='ew', padx=2, pady=2)

        ttk.Label(
            add_feat_frame,
            text="Benefit:").grid(
            row=2,
            column=0,
            sticky='ne',
            padx=2,
            pady=2)

        # Text widget for multi-line benefit description
        benefit_frame = ttk.Frame(add_feat_frame)
        benefit_frame.grid(
            row=2,
            column=1,
            columnspan=3,
            sticky='ew',
            padx=2,
            pady=2)

        self.feat_benefit_text = tk.Text(
            benefit_frame, height=3, width=50, wrap='word')
        self.feat_benefit_text.pack(side='left', fill='both', expand=True)

        benefit_scroll = ttk.Scrollbar(
            benefit_frame, command=self.feat_benefit_text.yview)
        benefit_scroll.pack(side='right', fill='y')
        self.feat_benefit_text.config(yscrollcommand=benefit_scroll.set)

        add_feat_btn = ttk.Button(
            add_feat_frame,
            text="Add Feat",
            command=self.add_feat)
        add_feat_btn.grid(row=3, column=0, columnspan=4, pady=5)

        # Feats list
        feats_list_frame = ttk.Frame(feats_container)
        feats_list_frame.pack(fill='both', expand=True)

        feats_scroll = ttk.Scrollbar(feats_list_frame)
        feats_scroll.pack(side='right', fill='y')

        columns = ('name', 'type', 'prerequisites', 'benefit')
        self.feats_tree = ttk.Treeview(
            feats_list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=feats_scroll.set,
            height=6)

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

        remove_feat_btn = ttk.Button(
            feat_btn_frame,
            text="Remove Selected Feat",
            command=self.remove_feat)
        remove_feat_btn.pack(side='left', padx=2)

        epic_feats_btn = ttk.Button(
            feat_btn_frame,
            text="Epic Feats",
            command=self.show_epic_feats_dialog)
        epic_feats_btn.pack(side='left', padx=2)

        # ===== SPECIAL ABILITIES SECTION =====
        abilities_container = ttk.LabelFrame(
            paned, text="Special Abilities", padding=10)
        # Less space for abilities section
        paned.add(abilities_container, weight=2)

        # Add ability controls
        add_ability_frame = ttk.Frame(abilities_container)
        add_ability_frame.pack(fill='x', pady=(0, 5))

        ttk.Label(
            add_ability_frame,
            text="Ability Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['ability_name'] = ttk.Entry(add_ability_frame, width=25)
        self.entries['ability_name'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            add_ability_frame,
            text="Source:").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        ability_sources = ['Class', 'Racial', 'Feat', 'Item', 'Spell', 'Other']
        self.entries['ability_source'] = ttk.Combobox(
            add_ability_frame, width=12, values=ability_sources)
        self.entries['ability_source'].grid(row=0, column=3, padx=2, pady=2)
        self.entries['ability_source'].current(0)

        ttk.Label(add_ability_frame, text="Uses/Day:").grid(row=0,
                                                            column=4, sticky='e', padx=2, pady=2)
        self.entries['ability_uses'] = ttk.Entry(add_ability_frame, width=8)
        self.entries['ability_uses'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['ability_uses'].insert(0, "0")

        ttk.Label(
            add_ability_frame,
            text="Description:").grid(
            row=1,
            column=0,
            sticky='ne',
            padx=2,
            pady=2)

        # Text widget for multi-line description
        desc_frame = ttk.Frame(add_ability_frame)
        desc_frame.grid(
            row=1,
            column=1,
            columnspan=5,
            sticky='ew',
            padx=2,
            pady=2)

        self.ability_desc_text = tk.Text(
            desc_frame, height=3, width=60, wrap='word')
        self.ability_desc_text.pack(side='left', fill='both', expand=True)

        desc_scroll = ttk.Scrollbar(
            desc_frame, command=self.ability_desc_text.yview)
        desc_scroll.pack(side='right', fill='y')
        self.ability_desc_text.config(yscrollcommand=desc_scroll.set)

        add_ability_btn = ttk.Button(
            add_ability_frame,
            text="Add Special Ability",
            command=self.add_ability)
        add_ability_btn.grid(row=2, column=0, columnspan=6, pady=5)

        # Abilities list
        abilities_list_frame = ttk.Frame(abilities_container)
        abilities_list_frame.pack(fill='both', expand=True)

        abilities_scroll = ttk.Scrollbar(abilities_list_frame)
        abilities_scroll.pack(side='right', fill='y')

        columns = ('name', 'source', 'uses', 'description')
        self.abilities_tree = ttk.Treeview(
            abilities_list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=abilities_scroll.set,
            height=8)

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

        use_ability_btn = ttk.Button(
            ability_btn_frame,
            text="Use Ability (-1 Use)",
            command=self.use_ability)
        use_ability_btn.pack(side='left', padx=2)

        reset_abilities_btn = ttk.Button(
            ability_btn_frame,
            text="Long Rest (Reset All)",
            command=self.reset_abilities)
        reset_abilities_btn.pack(side='left', padx=2)

        remove_ability_btn = ttk.Button(
            ability_btn_frame,
            text="Remove Selected Ability",
            command=self.remove_ability)
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
            messagebox.showwarning(
                "No Selection",
                "Please select a feat to remove.")
            return

        item = selection[0]
        index = self.feats_tree.index(item)

        self.character.remove_feat(index)
        self.update_feats_display()
        self.mark_modified()

    def show_epic_feats_dialog(self):
        """Show dialog for managing epic feats"""
        # Removed level restriction - individual feat prerequisites will
        # determine eligibility

        dialog = tk.Toplevel(self.root)
        dialog.title("Epic Feats")
        dialog.geometry("800x600")
        dialog.transient(self.root)
        dialog.grab_set()

        # Epic level info at top
        info_frame = ttk.LabelFrame(
            dialog, text="Character Information", padding=10)
        info_frame.pack(fill='x', padx=10, pady=10)

        total_level = self.character.get_total_level()

        # Simplified info display - no feat count tracking
        info_text = f"Total Level: {total_level}\n"
        info_text += f"Epic Feats Selected: {len(self.character.epic_feats)}\n\n"
        info_text += "Epic feats are available to any character who meets the individual feat prerequisites.\n"
        info_text += "Prerequisites may include minimum level, ability scores, BAB, skills, or other feats."

        info_label = ttk.Label(
            info_frame,
            text=info_text,
            justify='left',
            font=(
                'Arial',
                10))
        info_label.pack(anchor='w')

        # Current epic feats
        current_frame = ttk.LabelFrame(
            dialog, text="Current Epic Feats", padding=10)
        current_frame.pack(fill='both', expand=True, padx=10, pady=5)

        current_list = tk.Listbox(current_frame, height=6)
        current_list.pack(fill='both', expand=True)

    def refresh_current_feats():
        current_list.delete(0, tk.END)
        for feat in self.character.epic_feats:
            current_list.insert(tk.END, feat)

        refresh_current_feats()

        # Remove epic feat button
        remove_btn = ttk.Button(
            current_frame,
            text="Remove Selected Epic Feat",
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
        available_frame = ttk.LabelFrame(
            dialog, text="Available Epic Feats", padding=10)
        available_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Selection frame
        select_frame = ttk.Frame(available_frame)
        select_frame.pack(fill='x', pady=5)

        ttk.Label(
            select_frame,
            text="Select Epic Feat:").pack(
            side='left',
            padx=5)

        epic_feat_var = tk.StringVar()
        all_epic_feats = self.character.get_all_epic_feats_list()
        epic_feat_combo = ttk.Combobox(
            select_frame,
            textvariable=epic_feat_var,
            values=all_epic_feats,
            state='readonly',
            width=40)
        epic_feat_combo.pack(side='left', padx=5, fill='x', expand=True)
        if all_epic_feats:
            epic_feat_combo.current(0)

        # Description frame
        desc_frame = ttk.Frame(available_frame)
        desc_frame.pack(fill='both', expand=True)

        desc_text = tk.Text(
            desc_frame,
            height=10,
            width=70,
            wrap='word',
            state='disabled')
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
        desc_text.insert(
            tk.END,
            f"Type: {
                feat_info.get(
                    'type',
                    'Epic')}\n\n",
            'bold')
        desc_text.insert(
            tk.END,
            f"Prerequisites: {
                feat_info.get(
                    'prerequisites',
                    'None')}\n\n")
        desc_text.insert(
            tk.END, f"Benefit: {
                feat_info.get(
                    'benefit', '')}\n\n")
        if feat_info.get('special'):
            desc_text.insert(
                tk.END,
                f"Special: {
                    feat_info.get(
                        'special',
                        '')}\n",
                'special')

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

        # Check if already have this feat (for feats that can't be taken
        # multiple times)
        if selected in self.character.epic_feats:
            feat_info = EPIC_FEATS.get(selected, {})
            if feat_info.get(
                    'special') and 'multiple times' in feat_info['special'].lower():
                # Can take multiple times
                pass
            else:
                messagebox.showwarning("Already Selected",
                                       f"You already have {selected}.\n"
                                       "This feat cannot be taken multiple times.")
                return

        # No feat count restriction - only individual feat prerequisites matter
        self.character.add_epic_feat(selected)
        refresh_current_feats()
        self.mark_modified()
        messagebox.showinfo("Epic Feat Added",
                            f"{selected} has been added to your epic feats!")

        add_btn = ttk.Button(
            available_frame,
            text="Add Epic Feat",
            command=add_epic_feat)
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
            messagebox.showwarning(
                "No Selection",
                "Please select an ability to remove.")
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
            messagebox.showwarning(
                "No Selection",
                "Please select an ability to use.")
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
        messagebox.showinfo(
            "Long Rest",
            "All special ability uses have been restored!")

    def update_feats_display(self):
        """Update the feats treeview"""
        # Clear treeview
        for item in self.feats_tree.get_children():
            self.feats_tree.delete(item)

        # Populate with feats
        for feat in self.character.feats:
            self.feats_tree.insert(
                '', 'end', values=(
                    feat['name'], feat.get(
                        'type', 'General'), feat.get(
                        'prerequisites', ''), feat.get(
                        'benefit', '')[
                            :50] + (
                                '...' if len(
                                    feat.get(
                                        'benefit', '')) > 50 else '')))

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
