"""
Magic Items Tab (clean)
This module provides a clean, single-definition implementation of MagicItemsTab.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab
from dialogs.magic_item_dialog import MagicItemDialog


class MagicItemsTab(BaseTab):
    """Manage magic items cleanly"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        main = ttk.Frame(self.parent)
        main.pack(fill='both', expand=True, padx=5, pady=5)

        ttk.Label(main, text='Magic Items', font=('TkDefaultFont', 12, 'bold')).pack(pady=5)
        list_frame = ttk.LabelFrame(main, text='Magic Items List')
        list_frame.pack(fill='both', expand=True, padx=5, pady=5)

        frame = ttk.Frame(list_frame)
        frame.pack(fill='both', expand=True)
        scroll = ttk.Scrollbar(frame)
        scroll.pack(side='right', fill='y')

        cols = ('equipped', 'name', 'type', 'slot', 'bonuses', 'charges', 'properties')
        self.magic_items_tree = ttk.Treeview(frame, columns=cols, show='headings', yscrollcommand=scroll.set)
        for name, width in [('equipped', 70), ('name', 180), ('type', 100), ('slot', 100), ('bonuses', 200), ('charges', 80), ('properties', 300)]:
            self.magic_items_tree.heading(name, text=name.title())
            self.magic_items_tree.column(name, width=width)
        self.magic_items_tree.pack(side='left', fill='both', expand=True)
        scroll.config(command=self.magic_items_tree.yview)

        self.magic_items_tree.bind('<Double-Button-1>', self.show_magic_item_details)
        self.magic_items_tree.bind('<Button-1>', self.on_magic_item_click)

        btns = ttk.Frame(list_frame)
        btns.pack(fill='x')
        ttk.Button(btns, text='Create New Item', command=self.show_create_magic_item_dialog).pack(side='left', padx=4)
        ttk.Button(btns, text='Use Charge (-1)', command=self.use_magic_item_charge).pack(side='left', padx=4)
        ttk.Button(btns, text='Recharge', command=self.recharge_magic_item).pack(side='left', padx=4)
        ttk.Button(btns, text='Remove Selected', command=self.remove_magic_item).pack(side='left', padx=4)

    def _post_item_change_update(self):
        self.refresh_magic_items()
        self.mark_modified()
        if hasattr(self.gui, 'update_all_calculated_fields'):
            self.gui.update_all_calculated_fields()

    def _open_magic_item_dialog(self, magic_item=None, item_index=None):
        """Open the dialog UI for creating or editing a magic item.
        We use the modal dialog implemented in `dialogs.magic_item_dialog`.
        """
        def _on_save(mi, idx=None):
            if idx is None:
                self.character.magic_items.append(mi)
            else:
                self.character.magic_items[idx] = mi
            self._post_item_change_update()

        MagicItemDialog(self.root, self.character, magic_item, item_index, _on_save, self.gui)

    def show_create_magic_item_dialog(self):
        self._open_magic_item_dialog()

    def update(self):
        self.refresh_magic_items()

    def on_magic_item_click(self, event):
        region = self.magic_items_tree.identify_region(event.x, event.y)
        if region != 'cell':
            return
        column = self.magic_items_tree.identify_column(event.x)
        if column != '#1':
            return
        row = self.magic_items_tree.identify_row(event.y)
        if not row:
            return
        item = self.magic_items_tree.item(row)
        name = item['values'][1]
        for mi in self.character.magic_items:
            if mi['name'] == name:
                mi['equipped'] = not mi.get('equipped', False)
                self._post_item_change_update()
                break

    def remove_magic_item(self):
        sel = self.magic_items_tree.selection()
        if not sel:
            messagebox.showwarning('No Selection', 'Please select a magic item to remove.')
            return
        item = self.magic_items_tree.item(sel[0])
        name = item['values'][1]
        for i, mi in enumerate(self.character.magic_items):
            if mi['name'] == name:
                del self.character.magic_items[i]
                break
        self._post_item_change_update()

    def use_magic_item_charge(self):
        sel = self.magic_items_tree.selection()
        if not sel:
            messagebox.showwarning('No Selection', 'Please select a magic item.')
            return
        item = self.magic_items_tree.item(sel[0])
        name = item['values'][1]
        for mi in self.character.magic_items:
            if mi['name'] == name:
                if mi.get('charges', 0) > 0:
                    mi['charges'] -= 1
                    self._post_item_change_update()
                else:
                    messagebox.showinfo('No Charges', 'This item has no charges remaining.')
                break

    def recharge_magic_item(self):
        sel = self.magic_items_tree.selection()
        if not sel:
            messagebox.showwarning('No Selection', 'Please select a magic item.')
            return
        item = self.magic_items_tree.item(sel[0])
        name = item['values'][1]
        for mi in self.character.magic_items:
            if mi['name'] == name:
                mi['charges'] = mi.get('max_charges', 0)
                self._post_item_change_update()
                break

    def show_magic_item_details(self, event=None):
        sel = self.magic_items_tree.selection()
        if not sel:
            return
        item = self.magic_items_tree.item(sel[0])
        name = item['values'][1]
        for idx, mi in enumerate(self.character.magic_items):
            if mi['name'] == name:
                self._open_magic_item_dialog(mi, idx)
                break

    def refresh_magic_items(self):
        self.magic_items_tree.delete(*self.magic_items_tree.get_children())
        for mi in self.character.magic_items:
            eq = '✓' if mi.get('equipped', False) else ''
            bonuses = ''
            if mi.get('bonuses'):
                b = ', '.join([f"{bb['type']} {'+' if bb['value'] >= 0 else ''}{bb['value']}" for bb in mi['bonuses'][:3]])
            props = mi.get('properties', '').replace('\n', ' | ')
            if len(props) > 80:
                props = props[:77] + '...'
            charges = f"{mi.get('charges', 0)}/{mi.get('max_charges', 0)}" if mi.get('max_charges', 0) > 0 else ''
            self.magic_items_tree.insert('', 'end', values=(eq, mi['name'], mi.get('type', 'Other'), mi.get('slot', 'None'), bonuses, charges, props))
