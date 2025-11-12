"""
Magic Items Tab
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab


class MagicItemsTab(BaseTab):
    """Magic Items management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        """Build the magic items tab"""
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)

        # Title
        title_label = ttk.Label(
            main_container, text="Magic Items", font=(
                'Arial', 12, 'bold'))
        title_label.pack(pady=5)

        # Info label
        info_label = ttk.Label(
            main_container,
            text="Click 'Equipped' column to toggle equipment status. Double-click item for details.",
            font=(
                'Arial',
                9,
                'italic'))
        info_label.pack(pady=2)

        # Magic Items list
        list_frame = ttk.LabelFrame(
            main_container,
            text="Magic Items List",
            padding=10)
        list_frame.pack(fill='both', expand=True, padx=5, pady=5)

        items_list_frame = ttk.Frame(list_frame)
        items_list_frame.pack(fill='both', expand=True)

        items_scroll = ttk.Scrollbar(items_list_frame)
        items_scroll.pack(side='right', fill='y')

        columns = (
            'equipped',
            'name',
            'type',
            'slot',
            'bonuses',
            'charges',
            'properties')
        self.magic_items_tree = ttk.Treeview(
            items_list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=items_scroll.set,
            height=15)

        self.magic_items_tree.heading('equipped', text='Equipped')
        self.magic_items_tree.heading('name', text='Item Name')
        self.magic_items_tree.heading('type', text='Type')
        self.magic_items_tree.heading('slot', text='Slot')
        self.magic_items_tree.heading('bonuses', text='Bonuses')
        self.magic_items_tree.heading('charges', text='Charges')
        self.magic_items_tree.heading('properties', text='Properties')

        self.magic_items_tree.column('equipped', width=70)
        self.magic_items_tree.column('name', width=180)
        self.magic_items_tree.column('type', width=100)
        self.magic_items_tree.column('slot', width=100)
        self.magic_items_tree.column('bonuses', width=200)
        self.magic_items_tree.column('charges', width=80)
        self.magic_items_tree.column('properties', width=300)

        self.magic_items_tree.pack(side='left', fill='both', expand=True)
        items_scroll.config(command=self.magic_items_tree.yview)

        # Bind double-click to show details
        self.magic_items_tree.bind(
            '<Double-Button-1>',
            self.show_magic_item_details)
        # Bind single-click to toggle equipped
        self.magic_items_tree.bind('<Button-1>', self.on_magic_item_click)

        # Buttons
        btn_frame = ttk.Frame(list_frame)
        btn_frame.pack(fill='x', pady=5)

        add_item_btn = ttk.Button(
            btn_frame,
            text="Create New Item",
            command=self.show_create_magic_item_dialog)
        add_item_btn.pack(side='left', padx=2)

        use_charge_btn = ttk.Button(
            btn_frame,
            text="Use Charge (-1)",
            command=self.use_magic_item_charge)
        use_charge_btn.pack(side='left', padx=2)

        recharge_btn = ttk.Button(
            btn_frame,
            text="Recharge",
            command=self.recharge_magic_item)
        recharge_btn.pack(side='left', padx=2)

        remove_item_btn = ttk.Button(
            btn_frame,
            text="Remove Selected",
            command=self.remove_magic_item)
        remove_item_btn.pack(side='left', padx=2)

    def show_create_magic_item_dialog(self):
        """Show dialog to create a new magic item with bonuses"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create Magic Item")
        dialog.geometry("700x650")
        dialog.transient(self.root)
        dialog.grab_set()

        # Scrollable content
        canvas = tk.Canvas(dialog)
        scrollbar = ttk.Scrollbar(
            dialog, orient="vertical", command=canvas.yview)
        content_frame = ttk.Frame(canvas)

        content_frame.bind(
            "<Configure>", lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Title
        ttk.Label(
            content_frame,
            text="Create Magic Item",
            font=(
                'TkDefaultFont',
                14,
                'bold')).pack(
            pady=10)

        # Basic Info Frame
        basic_frame = ttk.LabelFrame(
            content_frame, text="Basic Information", padding=10)
        basic_frame.pack(fill='x', padx=20, pady=5)

        ttk.Label(
            basic_frame,
            text="Item Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=3)
        name_var = tk.StringVar()
        ttk.Entry(
            basic_frame,
            textvariable=name_var,
            width=40).grid(
            row=0,
            column=1,
            columnspan=3,
            sticky='ew',
            padx=5,
            pady=3)

        ttk.Label(
            basic_frame,
            text="Type:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=5,
            pady=3)
        item_types = [
            'Weapon',
            'Armor',
            'Shield',
            'Ring',
            'Wondrous Item',
            'Potion',
            'Scroll',
            'Wand',
            'Rod',
            'Staff',
            'Other']
        type_var = tk.StringVar(value='Wondrous Item')
        ttk.Combobox(
            basic_frame,
            textvariable=type_var,
            values=item_types,
            width=15).grid(
            row=1,
            column=1,
            sticky='w',
            padx=5,
            pady=3)

        ttk.Label(
            basic_frame,
            text="Slot:").grid(
            row=1,
            column=2,
            sticky='e',
            padx=5,
            pady=3)
        slots = [
            'None',
            'Head',
            'Eyes',
            'Neck',
            'Shoulders',
            'Body',
            'Torso',
            'Arms',
            'Hands',
            'Ring',
            'Waist',
            'Feet']
        slot_var = tk.StringVar(value='None')
        ttk.Combobox(
            basic_frame,
            textvariable=slot_var,
            values=slots,
            width=12).grid(
            row=1,
            column=3,
            sticky='w',
            padx=5,
            pady=3)

        ttk.Label(
            basic_frame,
            text="Caster Level:").grid(
            row=2,
            column=0,
            sticky='e',
            padx=5,
            pady=3)
        cl_var = tk.IntVar(value=1)
        ttk.Spinbox(
            basic_frame,
            from_=1,
            to=40,
            textvariable=cl_var,
            width=8).grid(
            row=2,
            column=1,
            sticky='w',
            padx=5,
            pady=3)

        ttk.Label(
            basic_frame,
            text="Charges:").grid(
            row=2,
            column=2,
            sticky='e',
            padx=5,
            pady=3)
        charges_var = tk.IntVar(value=0)
        ttk.Spinbox(
            basic_frame,
            from_=0,
            to=100,
            textvariable=charges_var,
            width=8).grid(
            row=2,
            column=3,
            sticky='w',
            padx=5,
            pady=3)

        # Bonuses Frame
        bonuses_frame = ttk.LabelFrame(
            content_frame,
            text="Bonuses (Affects Character Stats When Equipped)",
            padding=10)
        bonuses_frame.pack(fill='both', expand=True, padx=20, pady=5)

        bonus_list = []  # List to track bonuses

        # Bonus types available
        bonus_types = [
            'Armor',
            'Shield',
            'Natural Armor',
            'Deflection',
            'Resistance (All Saves)',
            'Fort Save',
            'Ref Save',
            'Will Save',
            'Attack Bonus',
            'Damage Bonus',
            'Strength',
            'Dexterity',
            'Constitution',
            'Intelligence',
            'Wisdom',
            'Charisma',
            'Spell Resistance',
            'Initiative',
            'Skill Bonus (All)',
            'Speed Bonus']

        # Bonuses list display
        bonus_tree_frame = ttk.Frame(bonuses_frame)
        bonus_tree_frame.pack(fill='both', expand=True)

        bonus_tree = ttk.Treeview(
            bonus_tree_frame,
            columns=(
                'type',
                'value'),
            show='headings',
            height=6)
        bonus_tree.heading('type', text='Bonus Type')
        bonus_tree.heading('value', text='Value')
        bonus_tree.column('type', width=250)
        bonus_tree.column('value', width=100)
        bonus_tree.pack(side='left', fill='both', expand=True)

        bonus_scroll = ttk.Scrollbar(
            bonus_tree_frame, command=bonus_tree.yview)
        bonus_scroll.pack(side='right', fill='y')
        bonus_tree.config(yscrollcommand=bonus_scroll.set)

        # Add bonus controls
        add_bonus_frame = ttk.Frame(bonuses_frame)
        add_bonus_frame.pack(fill='x', pady=5)

        ttk.Label(add_bonus_frame, text="Type:").pack(side='left', padx=2)
        bonus_type_var = tk.StringVar(value=bonus_types[0])
        ttk.Combobox(
            add_bonus_frame,
            textvariable=bonus_type_var,
            values=bonus_types,
            width=20).pack(
            side='left',
            padx=2)

        ttk.Label(add_bonus_frame, text="Value:").pack(side='left', padx=2)
        bonus_value_var = tk.IntVar(value=1)
        ttk.Spinbox(
            add_bonus_frame,
            from_=-10,
            to=20,
            textvariable=bonus_value_var,
            width=8).pack(
            side='left',
            padx=2)

    def add_bonus():
        bonus_type = bonus_type_var.get()
        bonus_value = bonus_value_var.get()
        bonus_list.append({'type': bonus_type, 'value': bonus_value})
        bonus_tree.insert(
            '',
            'end',
            values=(
                bonus_type,
                f"+{bonus_value}" if bonus_value >= 0 else str(bonus_value)))

    def remove_bonus():
        selection = bonus_tree.selection()
        if selection:
            index = bonus_tree.index(selection[0])
            del bonus_list[index]
            bonus_tree.delete(selection[0])

        ttk.Button(
            add_bonus_frame,
            text="Add Bonus",
            command=add_bonus).pack(
            side='left',
            padx=2)
        ttk.Button(
            add_bonus_frame,
            text="Remove Selected",
            command=remove_bonus).pack(
            side='left',
            padx=2)

        # Properties Frame
        prop_frame = ttk.LabelFrame(
            content_frame,
            text="Special Properties/Abilities",
            padding=10)
        prop_frame.pack(fill='x', padx=20, pady=5)

        prop_text = tk.Text(prop_frame, height=4, width=60, wrap='word')
        prop_scroll = ttk.Scrollbar(prop_frame, command=prop_text.yview)
        prop_text.config(yscrollcommand=prop_scroll.set)
        prop_text.pack(side='left', fill='both', expand=True)
        prop_scroll.pack(side='right', fill='y')

        # Description Frame
        desc_frame = ttk.LabelFrame(
            content_frame, text="Description", padding=10)
        desc_frame.pack(fill='x', padx=20, pady=5)

        desc_text = tk.Text(desc_frame, height=3, width=60, wrap='word')
        desc_scroll = ttk.Scrollbar(desc_frame, command=desc_text.yview)
        desc_text.config(yscrollcommand=desc_scroll.set)
        desc_text.pack(side='left', fill='both', expand=True)
        desc_scroll.pack(side='right', fill='y')

        # Buttons
        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(pady=10)

    def create_item():
        name = name_var.get().strip()
        if not name:
            messagebox.showwarning(
                "Missing Name",
                "Please enter an item name.",
                parent=dialog)
            return

        magic_item = {
            'name': name,
            'type': type_var.get(),
            'slot': slot_var.get(),
            'caster_level': cl_var.get(),
            'charges': charges_var.get(),
            'max_charges': charges_var.get(),
            'properties': prop_text.get('1.0', 'end-1c').strip(),
            'description': desc_text.get('1.0', 'end-1c').strip(),
            'bonuses': bonus_list.copy(),
            'equipped': False
        }

        self.character.magic_items.append(magic_item)
        self.refresh_magic_items()
        self.update_all_calculated_fields()  # Update stats in case item affects them
        dialog.destroy()

        ttk.Button(
            btn_frame,
            text="Create Item",
            command=create_item,
            width=15).pack(
            side='left',
            padx=5)
        ttk.Button(
            btn_frame,
            text="Cancel",
            command=dialog.destroy,
            width=15).pack(
            side='left',
            padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.bind_mousewheel(canvas)

    def on_magic_item_click(self, event):
        """Handle clicks on magic item tree - toggle equipped status if clicking equipped column"""
        region = self.magic_items_tree.identify_region(event.x, event.y)
        if region == "cell":
            column = self.magic_items_tree.identify_column(event.x)
        if column == '#1':  # Equipped column
            row_id = self.magic_items_tree.identify_row(event.y)
        if row_id:
            item = self.magic_items_tree.item(row_id)
            item_name = item['values'][1]  # Name is second column now

        # Toggle equipped status
        for magic_item in self.character.magic_items:
            if magic_item['name'] == item_name:
                magic_item['equipped'] = not magic_item.get('equipped', False)
                self.refresh_magic_items()
                self.update_all_calculated_fields()  # Recalculate stats

                break

    def remove_magic_item(self):
        """Remove the selected magic item"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a magic item to remove.")
            return

        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][1]  # Name is second column now

        # Find and remove the item
        for i, magic_item in enumerate(self.character.magic_items):
            if magic_item['name'] == item_name:
                del self.character.magic_items[i]
                break

        self.refresh_magic_items()
        self.update_all_calculated_fields()  # Recalculate stats

    def use_magic_item_charge(self):
        """Use one charge from a magic item"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection", "Please select a magic item.")
            return

        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][1]  # Name is second column now

        # Find and update the item
        for magic_item in self.character.magic_items:
            if magic_item['name'] == item_name:
                if magic_item['charges'] > 0:
                    magic_item['charges'] -= 1
                    self.refresh_magic_items()
                else:
                    messagebox.showinfo(
                        "No Charges", "This item has no charges remaining.")
                    break

    def recharge_magic_item(self):
        """Recharge a magic item to full"""
        selection = self.magic_items_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a magic item.")
            return

        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][1]  # Name is second column now

        # Find and update the item
        for magic_item in self.character.magic_items:
            if magic_item['name'] == item_name:
                magic_item['charges'] = magic_item['max_charges']
                self.refresh_magic_items()
                break

    def show_magic_item_details(self, event=None):
        """Show detailed information about a magic item in a dialog"""
        selection = self.magic_items_tree.selection()
        if not selection:
            return

        item = self.magic_items_tree.item(selection[0])
        item_name = item['values'][1]  # Name is second column now

        # Find the full item data
        magic_item = None
        for mi in self.character.magic_items:
            if mi['name'] == item_name:
                magic_item = mi
                break

        if not magic_item:
            return

        # Create detail dialog
        detail_dialog = tk.Toplevel(self.root)
        detail_dialog.title(f"Magic Item: {magic_item['name']}")
        detail_dialog.geometry("600x500")
        detail_dialog.transient(self.root)

        # Create scrollable frame
        canvas = tk.Canvas(detail_dialog)
        scrollbar = ttk.Scrollbar(
            detail_dialog,
            orient="vertical",
            command=canvas.yview)
        content_frame = ttk.Frame(canvas)

        content_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Title
        title_label = ttk.Label(content_frame, text=magic_item['name'],
                                font=('TkDefaultFont', 14, 'bold'))
        title_label.pack(pady=10, padx=20, anchor='w')

        # Basic info frame
        info_frame = ttk.LabelFrame(
            content_frame,
            text="Basic Information",
            padding=10)
        info_frame.pack(fill='x', padx=20, pady=5)

        info_text = f"""Type: {magic_item.get('type', 'Other')}
        Slot: {magic_item.get('slot', 'None')}
        Caster Level: {magic_item.get('caster_level', 1)}
        Charges: {magic_item.get('charges', 0)}/{magic_item.get('max_charges', 0)}
        Equipped: {'Yes' if magic_item.get('equipped', False) else 'No'}"""

        ttk.Label(info_frame, text=info_text, justify='left').pack(anchor='w')

        # Bonuses frame
        if magic_item.get('bonuses'):
            bonus_frame = ttk.LabelFrame(
                content_frame,
                text="Bonuses (Active When Equipped)",
                padding=10)
            bonus_frame.pack(fill='x', padx=20, pady=5)

            for bonus in magic_item['bonuses']:
                bonus_text = f"{
                    bonus['type']}: {
                    '+' if bonus['value'] >= 0 else ''}{
                    bonus['value']}"
                ttk.Label(
                    bonus_frame,
                    text=bonus_text,
                    foreground='blue').pack(
                    anchor='w',
            pady=2)

        # Properties frame
        if magic_item.get('properties'):
            prop_frame = ttk.LabelFrame(
                content_frame,
                text="Special Properties",
                padding=10)
            prop_frame.pack(fill='both', expand=True, padx=20, pady=5)

            prop_text = tk.Text(prop_frame, height=10, width=60, wrap='word')
            prop_scrollbar = ttk.Scrollbar(prop_frame, command=prop_text.yview)
            prop_text.config(yscrollcommand=prop_scrollbar.set)

            prop_text.insert('1.0', magic_item['properties'])
            prop_text.config(state='disabled')

            prop_text.pack(side='left', fill='both', expand=True)
            prop_scrollbar.pack(side='right', fill='y')

        # Description frame
        if magic_item.get('description'):
            desc_frame = ttk.LabelFrame(
                content_frame, text="Description", padding=10)
            desc_frame.pack(fill='both', expand=True, padx=20, pady=5)

            desc_text = tk.Text(desc_frame, height=8, width=60, wrap='word')
            desc_scrollbar = ttk.Scrollbar(desc_frame, command=desc_text.yview)
            desc_text.config(yscrollcommand=desc_scrollbar.set)

            desc_text.insert('1.0', magic_item['description'])
            desc_text.config(state='disabled')

            desc_text.pack(side='left', fill='both', expand=True)
            desc_scrollbar.pack(side='right', fill='y')

        # Close button
        ttk.Button(content_frame, text="Close",
                   command=detail_dialog.destroy, width=15).pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel
        self.bind_mousewheel(canvas)

    def refresh_magic_items(self):
        """Refresh the magic items display"""
        # Clear tree
        for item in self.magic_items_tree.get_children():
            self.magic_items_tree.delete(item)

        # Repopulate
        for magic_item in self.character.magic_items:
            # Equipped status
            equipped = '✓' if magic_item.get('equipped', False) else ''

            # Bonuses summary
            bonuses_text = ''
            if magic_item.get('bonuses'):
                bonus_strs = []
                for bonus in magic_item['bonuses'][:3]:  # Show first 3 bonuses
                    value = bonus['value']
                    bonus_strs.append(
                        f"{bonus['type']} {'+' if value >= 0 else ''}{value}")
                bonuses_text = ', '.join(bonus_strs)
                if len(magic_item['bonuses']) > 3:
                    bonuses_text += '...'

            # Properties - convert newlines to separators
            properties = magic_item.get('properties', '')
            properties = properties.replace('\n', ' | ')
            if len(properties) > 80:
                properties = properties[:77] + '...'

            charges_text = f"{
                magic_item.get(
                    'charges',
                    0)}/{
                magic_item.get(
                    'max_charges',
                    0)}" if magic_item.get(
                        'max_charges',
                0) > 0 else ''

        self.magic_items_tree.insert('', 'end', values=(
            equipped,
            magic_item['name'],
            magic_item.get('type', 'Other'),
            magic_item.get('slot', 'None'),
            bonuses_text,
            charges_text,
            properties
        ))