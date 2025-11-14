"""
Feats Tab
"""

import tkinter as tk
from tkinter import ttk, messagebox
from feats import ALL_FEATS, get_all_feats_list, get_feats_by_type
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
            'Special',
            'Epic']
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

        self.feats_tree.column('name', width=250)
        self.feats_tree.column('type', width=100)
        self.feats_tree.column('prerequisites', width=150)
        self.feats_tree.column('benefit', width=300)

        self.feats_tree.pack(side='left', fill='both', expand=True)
        feats_scroll.config(command=self.feats_tree.yview)

        # Bind double-click to show feat details
        self.feats_tree.bind('<Double-Button-1>', self.show_feat_details)

        # Feat action buttons
        feat_btn_frame = ttk.Frame(feats_container)
        feat_btn_frame.pack(fill='x', pady=5)

        remove_feat_btn = ttk.Button(
            feat_btn_frame,
            text="Remove Selected Feat",
            command=self.remove_feat)
        remove_feat_btn.pack(side='left', padx=2)

        browse_feats_btn = ttk.Button(
            feat_btn_frame,
            text="Browse Feats",
            command=self.show_browse_feats_dialog)
        browse_feats_btn.pack(side='left', padx=2)

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

        # Bind double-click to show ability details
        self.abilities_tree.bind('<Double-Button-1>', self.show_ability_details)

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

    def show_feat_details(self, event=None):
        """Show detailed information about a feat in an editable dialog"""
        selection = self.feats_tree.selection()
        if not selection:
            return

        item = self.feats_tree.item(selection[0])
        feat_name = item['values'][0]

        # Ignore separator row
        if '═══' in feat_name:
            return

        # Find the feat and its index
        feat = None
        feat_index = None
        for idx, f in enumerate(self.character.feats):
            if f['name'] == feat_name:
                feat = f
                feat_index = idx
                break

        if not feat or feat_index is None:
            return

        # Create detail dialog
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Edit Feat: {feat['name']}")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()

        # Main frame
        main_frame = ttk.Frame(dialog, padding=10)
        main_frame.pack(fill='both', expand=True)

        # Title
        ttk.Label(main_frame, text="Edit Feat", font=('TkDefaultFont', 14, 'bold')).pack(pady=10)

        # Feat info frame
        info_frame = ttk.LabelFrame(main_frame, text="Feat Information", padding=10)
        info_frame.pack(fill='both', expand=True, pady=5)

        # Name
        ttk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky='e', padx=5, pady=3)
        name_var = tk.StringVar(value=feat['name'])
        ttk.Entry(info_frame, textvariable=name_var, width=40).grid(row=0, column=1, columnspan=3, sticky='ew', padx=5, pady=3)

        # Type
        ttk.Label(info_frame, text="Type:").grid(row=1, column=0, sticky='e', padx=5, pady=3)
        feat_types = ['General', 'Metamagic', 'Item Creation', 'Combat', 'Skill', 'Special']
        type_var = tk.StringVar(value=feat.get('type', 'General'))
        ttk.Combobox(info_frame, textvariable=type_var, values=feat_types, width=20).grid(row=1, column=1, sticky='w', padx=5, pady=3)

        # Prerequisites
        ttk.Label(info_frame, text="Prerequisites:").grid(row=2, column=0, sticky='e', padx=5, pady=3)
        prereq_var = tk.StringVar(value=feat.get('prerequisites', ''))
        ttk.Entry(info_frame, textvariable=prereq_var, width=40).grid(row=2, column=1, columnspan=3, sticky='ew', padx=5, pady=3)

        # Benefit
        ttk.Label(info_frame, text="Benefit:").grid(row=3, column=0, sticky='ne', padx=5, pady=3)
        benefit_frame = ttk.Frame(info_frame)
        benefit_frame.grid(row=3, column=1, columnspan=3, sticky='ew', padx=5, pady=3)
        
        benefit_text = tk.Text(benefit_frame, height=10, width=50, wrap='word')
        benefit_scroll = ttk.Scrollbar(benefit_frame, command=benefit_text.yview)
        benefit_text.config(yscrollcommand=benefit_scroll.set)
        benefit_text.insert('1.0', feat.get('benefit', ''))
        benefit_text.pack(side='left', fill='both', expand=True)
        benefit_scroll.pack(side='right', fill='y')

        info_frame.columnconfigure(1, weight=1)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        def save_changes():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning("Missing Name", "Please enter a feat name.", parent=dialog)
                return

            # Update feat
            self.character.feats[feat_index] = {
                'name': name,
                'type': type_var.get(),
                'prerequisites': prereq_var.get().strip(),
                'benefit': benefit_text.get('1.0', 'end-1c').strip(),
                'description': ''  # Keep for compatibility
            }

            self.update_feats_display()
            self.mark_modified()
            dialog.destroy()

        ttk.Button(btn_frame, text="Save", command=save_changes, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy, width=15).pack(side='left', padx=5)

    def show_ability_details(self, event=None):
        """Show detailed information about a special ability in an editable dialog"""
        selection = self.abilities_tree.selection()
        if not selection:
            return

        item = self.abilities_tree.item(selection[0])
        ability_name = item['values'][0]

        # Find the ability and its index
        ability = None
        ability_index = None
        for idx, a in enumerate(self.character.special_abilities):
            if a['name'] == ability_name:
                ability = a
                ability_index = idx
                break

        if not ability or ability_index is None:
            return

        # Create detail dialog
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Edit Special Ability: {ability['name']}")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()

        # Main frame
        main_frame = ttk.Frame(dialog, padding=10)
        main_frame.pack(fill='both', expand=True)

        # Title
        ttk.Label(main_frame, text="Edit Special Ability", font=('TkDefaultFont', 14, 'bold')).pack(pady=10)

        # Ability info frame
        info_frame = ttk.LabelFrame(main_frame, text="Ability Information", padding=10)
        info_frame.pack(fill='both', expand=True, pady=5)

        # Name
        ttk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky='e', padx=5, pady=3)
        name_var = tk.StringVar(value=ability['name'])
        ttk.Entry(info_frame, textvariable=name_var, width=40).grid(row=0, column=1, columnspan=3, sticky='ew', padx=5, pady=3)

        # Source
        ttk.Label(info_frame, text="Source:").grid(row=1, column=0, sticky='e', padx=5, pady=3)
        ability_sources = ['Class', 'Racial', 'Feat', 'Item', 'Spell', 'Other']
        source_var = tk.StringVar(value=ability.get('source', 'Class'))
        ttk.Combobox(info_frame, textvariable=source_var, values=ability_sources, width=20).grid(row=1, column=1, sticky='w', padx=5, pady=3)

        # Uses per day
        ttk.Label(info_frame, text="Uses/Day:").grid(row=1, column=2, sticky='e', padx=5, pady=3)
        uses_var = tk.IntVar(value=ability.get('uses_per_day', 0))
        ttk.Spinbox(info_frame, from_=0, to=100, textvariable=uses_var, width=10).grid(row=1, column=3, sticky='w', padx=5, pady=3)

        # Uses remaining
        ttk.Label(info_frame, text="Uses Remaining:").grid(row=2, column=0, sticky='e', padx=5, pady=3)
        remaining_var = tk.IntVar(value=ability.get('uses_remaining', 0))
        ttk.Spinbox(info_frame, from_=0, to=100, textvariable=remaining_var, width=10).grid(row=2, column=1, sticky='w', padx=5, pady=3)

        # Description
        ttk.Label(info_frame, text="Description:").grid(row=3, column=0, sticky='ne', padx=5, pady=3)
        desc_frame = ttk.Frame(info_frame)
        desc_frame.grid(row=3, column=1, columnspan=3, sticky='ew', padx=5, pady=3)
        
        desc_text = tk.Text(desc_frame, height=12, width=50, wrap='word')
        desc_scroll = ttk.Scrollbar(desc_frame, command=desc_text.yview)
        desc_text.config(yscrollcommand=desc_scroll.set)
        desc_text.insert('1.0', ability.get('description', ''))
        desc_text.pack(side='left', fill='both', expand=True)
        desc_scroll.pack(side='right', fill='y')

        info_frame.columnconfigure(1, weight=1)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        def save_changes():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning("Missing Name", "Please enter an ability name.", parent=dialog)
                return

            # Update ability
            self.character.special_abilities[ability_index] = {
                'name': name,
                'source': source_var.get(),
                'uses_per_day': uses_var.get(),
                'uses_remaining': remaining_var.get(),
                'description': desc_text.get('1.0', 'end-1c').strip()
            }

            self.update_abilities_display()
            self.mark_modified()
            dialog.destroy()

        ttk.Button(btn_frame, text="Save", command=save_changes, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy, width=15).pack(side='left', padx=5)

    def remove_feat(self):
        """Remove selected feat"""
        selection = self.feats_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a feat to remove.")
            return

        item = self.feats_tree.item(selection[0])
        feat_name = item['values'][0]

        # Ignore separator row
        if '═══' in feat_name:
            return

        # Find the feat index by name
        feat_index = None
        for idx, f in enumerate(self.character.feats):
            if f['name'] == feat_name:
                feat_index = idx
                break

        if feat_index is not None:
            self.character.remove_feat(feat_index)
            self.update_feats_display()
            self.mark_modified()

    def show_browse_feats_dialog(self, default_filter='All'):
        """Show dialog to browse and add feats from sourcebooks"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Browse Feats")
        dialog.geometry("800x700")
        dialog.transient(self.root)
        dialog.grab_set()

        # Main frame
        main_frame = ttk.Frame(dialog, padding=10)
        main_frame.pack(fill='both', expand=True)

        # Title
        ttk.Label(main_frame, text="Feat Library", font=('TkDefaultFont', 14, 'bold')).pack(pady=10)

        # Filter frame
        filter_frame = ttk.LabelFrame(main_frame, text="Filter", padding=10)
        filter_frame.pack(fill='x', pady=5)

        ttk.Label(filter_frame, text="Feat Type:").pack(side='left', padx=5)
        
        feat_types = ['All', 'General', 'Combat', 'Metamagic', 'Item Creation', 'Special', 'Epic']
        type_var = tk.StringVar(value=default_filter)
        type_combo = ttk.Combobox(filter_frame, textvariable=type_var, values=feat_types, state='readonly', width=20)
        type_combo.pack(side='left', padx=5)

        # Search frame
        search_frame = ttk.Frame(filter_frame)
        search_frame.pack(side='left', fill='x', expand=True, padx=10)
        
        ttk.Label(search_frame, text="Search:").pack(side='left', padx=5)
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, width=30)
        search_entry.pack(side='left', fill='x', expand=True)

        # Feat list frame
        list_frame = ttk.LabelFrame(main_frame, text="Available Feats", padding=10)
        list_frame.pack(fill='both', expand=True, pady=5)

        # Create listbox with scrollbar
        list_scroll = ttk.Scrollbar(list_frame)
        list_scroll.pack(side='right', fill='y')

        feat_listbox = tk.Listbox(list_frame, yscrollcommand=list_scroll.set, height=15)
        feat_listbox.pack(side='left', fill='both', expand=True)
        list_scroll.config(command=feat_listbox.yview)

        # Details frame
        details_frame = ttk.LabelFrame(main_frame, text="Feat Details", padding=10)
        details_frame.pack(fill='both', expand=True, pady=5)

        details_text = tk.Text(details_frame, height=10, width=70, wrap='word', state='disabled')
        details_scroll = ttk.Scrollbar(details_frame, command=details_text.yview)
        details_text.config(yscrollcommand=details_scroll.set)
        details_text.pack(side='left', fill='both', expand=True)
        details_scroll.pack(side='right', fill='y')

        def update_feat_list():
            """Update the listbox based on filters"""
            feat_listbox.delete(0, tk.END)
            
            selected_type = type_var.get()
            search_term = search_var.get().lower()

            # Get feats based on type filter
            if selected_type == 'All':
                feats_to_show = ALL_FEATS
            else:
                feats_to_show = get_feats_by_type(selected_type)

            # Apply search filter
            for feat_name in sorted(feats_to_show.keys()):
                if search_term in feat_name.lower():
                    feat_listbox.insert(tk.END, feat_name)

        def update_details(event=None):
            """Update details display when a feat is selected"""
            selection = feat_listbox.curselection()
            if not selection:
                return

            feat_name = feat_listbox.get(selection[0])
            feat_info = ALL_FEATS.get(feat_name, {})

            details_text.config(state='normal')
            details_text.delete('1.0', tk.END)

            details_text.insert(tk.END, f"{feat_name}\n\n", 'title')
            details_text.insert(tk.END, f"Type: {feat_info.get('type', 'General')}\n\n", 'bold')
            details_text.insert(tk.END, f"Prerequisites: {feat_info.get('prerequisites', 'None')}\n\n")
            details_text.insert(tk.END, f"Benefit: {feat_info.get('benefit', '')}\n")
            
            if feat_info.get('special'):
                details_text.insert(tk.END, f"\nSpecial: {feat_info.get('special', '')}\n", 'italic')

            details_text.tag_config('title', font=('Arial', 12, 'bold'))
            details_text.tag_config('bold', font=('Arial', 10, 'bold'))
            details_text.tag_config('italic', font=('Arial', 9, 'italic'))

            details_text.config(state='disabled')

        # Bind events
        type_combo.bind('<<ComboboxSelected>>', lambda e: update_feat_list())
        search_var.trace('w', lambda *args: update_feat_list())
        feat_listbox.bind('<<ListboxSelect>>', update_details)
        feat_listbox.bind('<Double-Button-1>', lambda e: add_selected_feat())

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        def add_selected_feat():
            selection = feat_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a feat to add.", parent=dialog)
                return

            feat_name = feat_listbox.get(selection[0])
            
            # Check if already have this feat
            if any(f['name'] == feat_name for f in self.character.feats):
                response = messagebox.askyesno(
                    "Duplicate Feat",
                    f"You already have {feat_name}.\nSome feats can be taken multiple times. Add anyway?",
                    parent=dialog)
                if not response:
                    return

            # Add feat
            feat_info = ALL_FEATS.get(feat_name, {})
            self.character.add_feat(
                name=feat_name,
                feat_type=feat_info.get('type', 'General'),
                prerequisites=feat_info.get('prerequisites', ''),
                benefit=feat_info.get('benefit', '')
            )

            self.update_feats_display()
            self.mark_modified()
            messagebox.showinfo("Feat Added", f"{feat_name} has been added to your feats!", parent=dialog)
            dialog.destroy()

        ttk.Button(btn_frame, text="Add Feat", command=add_selected_feat, width=20).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy, width=20).pack(side='left', padx=5)

        # Initial population
        update_feat_list()
        if feat_listbox.size() > 0:
            feat_listbox.selection_set(0)
            update_details()

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
        """Update the feats treeview - shows regular feats and epic feats with separator"""
        # Clear treeview
        for item in self.feats_tree.get_children():
            self.feats_tree.delete(item)

        # Migrate old epic_feats format if needed
        if hasattr(self.character, 'epic_feats') and self.character.epic_feats:
            # Convert old epic_feats list to new format and add to feats
            for epic_feat_name in self.character.epic_feats:
                # Check if already in feats list
                if not any(f['name'] == epic_feat_name for f in self.character.feats):
                    # Get epic feat info from ALL_FEATS
                    feat_info = ALL_FEATS.get(epic_feat_name, {})
                    self.character.feats.append({
                        'name': epic_feat_name,
                        'type': 'Epic',
                        'prerequisites': feat_info.get('prerequisites', ''),
                        'benefit': feat_info.get('benefit', ''),
                        'description': ''
                    })
            # Clear old epic_feats list
            self.character.epic_feats = []

        # Separate regular and epic feats
        regular_feats = [f for f in self.character.feats if f.get('type', 'General') != 'Epic']
        epic_feats = [f for f in self.character.feats if f.get('type', 'General') == 'Epic']

        # Populate with regular feats
        for feat in regular_feats:
            benefit_preview = feat.get('benefit', '')[:50]
            if len(feat.get('benefit', '')) > 50:
                benefit_preview += '...'
            
            self.feats_tree.insert(
                '', 'end', values=(
                    feat['name'], 
                    feat.get('type', 'General'), 
                    feat.get('prerequisites', ''), 
                    benefit_preview))

        # Add separator if there are epic feats
        if epic_feats:
            # Insert separator row
            separator_id = self.feats_tree.insert(
                '', 'end', values=(
                    '═══════════════ EPIC FEATS ═══════════════',
                    '', '', ''), tags=('separator',))
            # Configure separator appearance
            self.feats_tree.tag_configure('separator', background='#e0e0e0', font=('TkDefaultFont', 9, 'bold'))

            # Populate with epic feats
            for feat in epic_feats:
                benefit_preview = feat.get('benefit', '')[:50]
                if len(feat.get('benefit', '')) > 50:
                    benefit_preview += '...'
                
                self.feats_tree.insert(
                    '', 'end', values=(
                        feat['name'], 
                        feat.get('type', 'Epic'), 
                        feat.get('prerequisites', ''), 
                        benefit_preview))

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
