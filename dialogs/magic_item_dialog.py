"""
Magic Item Dialog
Dialog for creating or editing a magic item; separated into a dialog
so that the UI logic is modular and reusable.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class MagicItemDialog:
    """Modal dialog for editing/creating a magic item"""

    def __init__(self, parent, character, magic_item=None, item_index=None, on_save=None, gui=None):
        self.parent = parent
        self.character = character
        self.magic_item = magic_item
        self.item_index = item_index
        self.on_save = on_save
        self.gui = gui

        self.defaults = magic_item.copy() if magic_item else {
            'name': '',
            'type': 'Wondrous Item',
            'slot': 'None',
            'caster_level': 1,
            'charges': 0,
            'max_charges': 0,
            'properties': '',
            'description': '',
            'bonuses': [],
            'abilities': [],
            'equipped': False
        }

        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title('Edit Magic Item' if magic_item else 'Create Magic Item')
        self.dialog.geometry('800x700')
        self.dialog.transient(self.parent)
        self.dialog.grab_set()

        self._build_ui()

    def _build_ui(self):
        canvas = tk.Canvas(self.dialog)
        scrollbar = ttk.Scrollbar(self.dialog, orient='vertical', command=canvas.yview)
        content_frame = ttk.Frame(canvas)
        content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=content_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        ttk.Label(content_frame, text='Edit Magic Item' if self.magic_item else 'Create Magic Item', font=('TkDefaultFont', 14, 'bold')).pack(pady=10)

        basic_frame = ttk.LabelFrame(content_frame, text='Basic Information', padding=10)
        basic_frame.pack(fill='x', padx=20, pady=5)

        ttk.Label(basic_frame, text='Item Name:').grid(row=0, column=0, sticky='e', padx=5, pady=3)
        self.name_var = tk.StringVar(value=self.defaults.get('name', ''))
        ttk.Entry(basic_frame, textvariable=self.name_var, width=40).grid(row=0, column=1, columnspan=3, sticky='ew', padx=5, pady=3)

        ttk.Label(basic_frame, text='Type:').grid(row=1, column=0, sticky='e', padx=5, pady=3)
        item_types = ['Weapon', 'Armor', 'Shield', 'Ring', 'Wondrous Item', 'Potion', 'Scroll', 'Wand', 'Rod', 'Staff', 'Other']
        self.type_var = tk.StringVar(value=self.defaults.get('type', 'Wondrous Item'))
        ttk.Combobox(basic_frame, textvariable=self.type_var, values=item_types, width=15).grid(row=1, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text='Slot:').grid(row=1, column=2, sticky='e', padx=5, pady=3)
        slots = ['None', 'Head', 'Eyes', 'Neck', 'Shoulders', 'Body', 'Torso', 'Arms', 'Hands', 'Ring', 'Waist', 'Feet']
        self.slot_var = tk.StringVar(value=self.defaults.get('slot', 'None'))
        ttk.Combobox(basic_frame, textvariable=self.slot_var, values=slots, width=12).grid(row=1, column=3, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text='Caster Level:').grid(row=2, column=0, sticky='e', padx=5, pady=3)
        self.cl_var = tk.IntVar(value=self.defaults.get('caster_level', 1))
        ttk.Spinbox(basic_frame, from_=1, to=40, textvariable=self.cl_var, width=8).grid(row=2, column=1, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text='Max Charges:').grid(row=2, column=2, sticky='e', padx=5, pady=3)
        self.max_charges_var = tk.IntVar(value=self.defaults.get('max_charges', 0))
        ttk.Spinbox(basic_frame, from_=0, to=100, textvariable=self.max_charges_var, width=8).grid(row=2, column=3, sticky='w', padx=5, pady=3)

        ttk.Label(basic_frame, text='Current Charges:').grid(row=3, column=0, sticky='e', padx=5, pady=3)
        self.charges_var = tk.IntVar(value=self.defaults.get('charges', 0))
        ttk.Spinbox(basic_frame, from_=0, to=100, textvariable=self.charges_var, width=8).grid(row=3, column=1, sticky='w', padx=5, pady=3)

        self.equipped_var = tk.BooleanVar(value=self.defaults.get('equipped', False))
        ttk.Checkbutton(basic_frame, text='Equipped', variable=self.equipped_var).grid(row=3, column=2, columnspan=2, sticky='w', padx=5, pady=3)

        bonuses_frame = ttk.LabelFrame(content_frame, text='Bonuses (Active When Equipped)', padding=10)
        bonuses_frame.pack(fill='both', expand=True, padx=20, pady=5)
        self.bonus_list = self.defaults.get('bonuses', []).copy()

        bonus_tree_frame = ttk.Frame(bonuses_frame)
        bonus_tree_frame.pack(fill='both', expand=True)
        self.bonus_tree = ttk.Treeview(bonus_tree_frame, columns=('type', 'value'), show='headings', height=6)
        self.bonus_tree.heading('type', text='Bonus Type')
        self.bonus_tree.heading('value', text='Value')
        self.bonus_tree.column('type', width=250)
        self.bonus_tree.column('value', width=100)
        self.bonus_tree.pack(side='left', fill='both', expand=True)

        bonus_scroll = ttk.Scrollbar(bonus_tree_frame, command=self.bonus_tree.yview)
        bonus_scroll.pack(side='right', fill='y')
        self.bonus_tree.config(yscrollcommand=bonus_scroll.set)

        for b in self.bonus_list:
            self.bonus_tree.insert('', 'end', values=(b['type'], f"+{b['value']}" if b['value'] >= 0 else str(b['value'])))

        add_bonus_frame = ttk.Frame(bonuses_frame)
        add_bonus_frame.pack(fill='x', pady=5)
        bonus_types = [
            'Armor', 'Shield', 'Natural Armor', 'Deflection', 'Resistance (All Saves)', 'Fort Save', 'Ref Save', 'Will Save', 'Attack Bonus', 'Damage Bonus',
            'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'Spell Resistance', 'Initiative', 'Skill Bonus (All)', 'Speed Bonus'
        ]
        ttk.Label(add_bonus_frame, text='Type:').pack(side='left', padx=2)
        self.bonus_type_var = tk.StringVar(value=bonus_types[0])
        ttk.Combobox(add_bonus_frame, textvariable=self.bonus_type_var, values=bonus_types, width=20).pack(side='left', padx=2)
        ttk.Label(add_bonus_frame, text='Value:').pack(side='left', padx=2)
        self.bonus_value_var = tk.IntVar(value=1)
        ttk.Spinbox(add_bonus_frame, from_=-10, to=20, textvariable=self.bonus_value_var, width=8).pack(side='left', padx=2)

        def add_bonus():
            bt = self.bonus_type_var.get()
            bv = self.bonus_value_var.get()
            self.bonus_list.append({'type': bt, 'value': bv})
            self.bonus_tree.insert('', 'end', values=(bt, f"+{bv}" if bv >= 0 else str(bv)))

        def remove_bonus():
            selection = self.bonus_tree.selection()
            if selection:
                index = self.bonus_tree.index(selection[0])
                del self.bonus_list[index]
                self.bonus_tree.delete(selection[0])

        ttk.Button(add_bonus_frame, text='Add Bonus', command=add_bonus).pack(side='left', padx=2)
        ttk.Button(add_bonus_frame, text='Remove Selected', command=remove_bonus).pack(side='left', padx=2)

        # Abilities (for items like staves that have multiple abilities costing charges)
        abilities_frame = ttk.LabelFrame(content_frame, text='Abilities (Charges)', padding=10)
        abilities_frame.pack(fill='both', expand=True, padx=20, pady=5)

        self.ability_list = self.defaults.get('abilities', []).copy()
        ability_tree_frame = ttk.Frame(abilities_frame)
        ability_tree_frame.pack(fill='both', expand=True)
        self.ability_tree = ttk.Treeview(ability_tree_frame, columns=('name', 'cost'), show='headings', height=6)
        self.ability_tree.heading('name', text='Ability Name')
        self.ability_tree.heading('cost', text='Cost (Charges)')
        self.ability_tree.column('name', width=300)
        self.ability_tree.column('cost', width=120)
        self.ability_tree.pack(side='left', fill='both', expand=True)

        ability_scroll = ttk.Scrollbar(ability_tree_frame, command=self.ability_tree.yview)
        ability_scroll.pack(side='right', fill='y')
        self.ability_tree.config(yscrollcommand=ability_scroll.set)

        for a in self.ability_list:
            self.ability_tree.insert('', 'end', values=(a.get('name', ''), a.get('cost', 1)))

        add_ability_frame = ttk.Frame(abilities_frame)
        add_ability_frame.pack(fill='x', pady=5)
        ttk.Label(add_ability_frame, text='Ability:').pack(side='left', padx=2)
        self.ability_name_var = tk.StringVar(value='')
        ttk.Entry(add_ability_frame, textvariable=self.ability_name_var, width=30).pack(side='left', padx=2)
        ttk.Label(add_ability_frame, text='Cost:').pack(side='left', padx=2)
        self.ability_cost_var = tk.IntVar(value=1)
        ttk.Spinbox(add_ability_frame, from_=1, to=10, textvariable=self.ability_cost_var, width=5).pack(side='left', padx=2)

        def add_ability():
            name = self.ability_name_var.get().strip()
            cost = int(self.ability_cost_var.get())
            if not name:
                messagebox.showwarning('Missing Name', 'Please enter an ability name.', parent=self.dialog)
                return
            a = {'name': name, 'cost': cost, 'description': ''}
            self.ability_list.append(a)
            self.ability_tree.insert('', 'end', values=(a['name'], a['cost']))
            self.ability_name_var.set('')
            self.ability_cost_var.set(1)

        def remove_ability():
            selection = self.ability_tree.selection()
            if selection:
                index = self.ability_tree.index(selection[0])
                del self.ability_list[index]
                self.ability_tree.delete(selection[0])

        ttk.Button(add_ability_frame, text='Add Ability', command=add_ability).pack(side='left', padx=2)
        ttk.Button(add_ability_frame, text='Remove Selected', command=remove_ability).pack(side='left', padx=2)

        prop_frame = ttk.LabelFrame(content_frame, text='Special Properties/Abilities', padding=10)
        prop_frame.pack(fill='x', padx=20, pady=5)
        self.prop_text = tk.Text(prop_frame, height=4, width=60, wrap='word')
        prop_scroll = ttk.Scrollbar(prop_frame, command=self.prop_text.yview)
        self.prop_text.config(yscrollcommand=prop_scroll.set)
        self.prop_text.insert('1.0', self.defaults.get('properties', ''))
        self.prop_text.pack(side='left', fill='both', expand=True)
        prop_scroll.pack(side='right', fill='y')

        desc_frame = ttk.LabelFrame(content_frame, text='Description', padding=10)
        desc_frame.pack(fill='x', padx=20, pady=5)
        self.desc_text = tk.Text(desc_frame, height=3, width=60, wrap='word')
        desc_scroll = ttk.Scrollbar(desc_frame, command=self.desc_text.yview)
        self.desc_text.config(yscrollcommand=desc_scroll.set)
        self.desc_text.insert('1.0', self.defaults.get('description', ''))
        self.desc_text.pack(side='left', fill='both', expand=True)
        desc_scroll.pack(side='right', fill='y')

        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(pady=10)

        def save_changes():
            name = self.name_var.get().strip()
            if not name:
                messagebox.showwarning('Missing Name', 'Please enter an item name.', parent=self.dialog)
                return
            mi = {
                'name': name,
                'type': self.type_var.get(),
                'slot': self.slot_var.get(),
                'caster_level': self.cl_var.get(),
                'charges': self.charges_var.get(),
                'max_charges': self.max_charges_var.get(),
                'properties': self.prop_text.get('1.0', 'end-1c').strip(),
                'description': self.desc_text.get('1.0', 'end-1c').strip(),
                'bonuses': self.bonus_list.copy(),
                'abilities': self.ability_list.copy(),
                'equipped': self.equipped_var.get()
            }
            # call the save callback if provided, otherwise write to character
            if self.on_save:
                self.on_save(mi, self.item_index)
            else:
                if self.item_index is None:
                    self.character.magic_items.append(mi)
                else:
                    self.character.magic_items[self.item_index] = mi
                if self.gui:
                    if hasattr(self.gui, 'mark_modified'):
                        self.gui.mark_modified()
                    if hasattr(self.gui, 'update_all_calculated_fields'):
                        self.gui.update_all_calculated_fields()
                    if hasattr(self.gui, 'update_ac_display'):
                        self.gui.update_ac_display()
                    if hasattr(self.gui, 'update_saves_display'):
                        self.gui.update_saves_display()
            self.dialog.destroy()

        ttk.Button(btn_frame, text='Save', command=save_changes, width=15).pack(side='left', padx=5)
        ttk.Button(btn_frame, text='Cancel', command=self.dialog.destroy, width=15).pack(side='left', padx=5)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Add mouse wheel scrolling to the dialog canvas
        def _on_mousewheel(event):
            try:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
            except tk.TclError:
                pass
        canvas.bind('<MouseWheel>', _on_mousewheel)