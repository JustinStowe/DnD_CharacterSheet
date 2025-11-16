"""
Inventory Tab - Character inventory, carrying capacity, and encumbrance
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab


class InventoryTab(BaseTab):
    """Inventory management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)
        self.inventory_tree = None
        # Helper methods: not strictly required for UI but useful for programmatic tests
        
    def add_content_to_container(self, container_item, content_item):
        """Add a content item to a container, validating capacity. Returns True if added, False otherwise."""
        if not container_item.get('is_container'):
            return False
        cap = container_item.get('capacity_lbs', 0) or 0
        if cap > 0:
            current = sum([c.get('weight', 0) * c.get('quantity', 1) for c in container_item.get('contents', [])])
            new_total = current + (content_item.get('weight', 0) * content_item.get('quantity', 1))
            if new_total > cap:
                return False
        # normalize the content item schema so nested items are consistent
        normalized = self._normalize_item_schema(content_item)
        container_item.setdefault('contents', []).append(normalized)
        return True

    def edit_content_in_container(self, container_item, index, new_content):
        """Edit content in container at index; validate capacity. Returns True on success."""
        if not container_item.get('is_container'):
            return False
        contents = container_item.get('contents', [])
        if not (0 <= index < len(contents)):
            return False
        cap = container_item.get('capacity_lbs', 0) or 0
        if cap > 0:
            existing = sum([c.get('weight', 0) * c.get('quantity', 1) for i, c in enumerate(contents) if i != index])
            new_total = existing + (new_content.get('weight', 0) * new_content.get('quantity', 1))
            if new_total > cap:
                return False
        contents[index] = self._normalize_item_schema(new_content)
        return True

    def remove_content_from_container(self, container_item, index):
        """Remove content at index from container. Returns True if removed."""
        contents = container_item.get('contents', [])
        if not (0 <= index < len(contents)):
            return False
        contents.pop(index)
        return True

    def _normalize_item_schema(self, item):
        """Ensure an item dict uses the full item schema used for top-level inventory items.
        This makes contents items more consistent with top-level items.
        """
        return {
            'name': item.get('name', ''),
            'weight': item.get('weight', 0.0),
            'quantity': item.get('quantity', 1),
            'notes': item.get('notes', ''),
            'is_container': bool(item.get('is_container', False)),
            'capacity_lbs': float(item.get('capacity_lbs', 0.0) or 0.0),
            'count_contents_toward_carry': bool(item.get('count_contents_toward_carry', True)),
            'contents': item.get('contents', []).copy() if item.get('contents') else []
        }

    def build(self):
        """Build the inventory tab"""
        # Create main container
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill='both', expand=True, padx=5, pady=5)

        # Top frame for carrying capacity info
        capacity_frame = ttk.LabelFrame(
            main_container, text="Carrying Capacity", padding=10)
        capacity_frame.pack(fill='x', padx=5, pady=5)

        # Carrying capacity display
        cap_info_frame = ttk.Frame(capacity_frame)
        cap_info_frame.pack(fill='x')

        ttk.Label(
            cap_info_frame,
            text="Light Load:",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['light_load'] = ttk.Label(
            cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['light_load'].grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(
            cap_info_frame,
            text="Medium Load:",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=0,
            column=2,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['medium_load'] = ttk.Label(
            cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['medium_load'].grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(
            cap_info_frame,
            text="Heavy Load:",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=1,
            column=0,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['heavy_load'] = ttk.Label(
            cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['heavy_load'].grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(
            cap_info_frame,
            text="Maximum:",
            font=(
                'Arial',
                9,
                'bold')).grid(
            row=1,
            column=2,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['max_load'] = ttk.Label(
            cap_info_frame, text="0 lbs", relief='sunken', width=10)
        self.labels['max_load'].grid(row=1, column=3, padx=5, pady=2)

        # Current weight and encumbrance
        current_frame = ttk.Frame(capacity_frame)
        current_frame.pack(fill='x', pady=(10, 0))

        ttk.Label(
            current_frame,
            text="Total Weight Carried:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['total_weight'] = ttk.Label(
            current_frame,
            text="0 lbs",
            relief='sunken',
            width=12,
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['total_weight'].grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(
            current_frame,
            text="Current Load:",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=2,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['current_load'] = ttk.Label(
            current_frame,
            text="Light",
            relief='sunken',
            width=12,
            font=(
                'Arial',
                10,
                'bold'))
        self.labels['current_load'].grid(row=0, column=3, padx=5, pady=2)

        # Encumbrance penalties
        penalty_frame = ttk.LabelFrame(
            main_container,
            text="Encumbrance Penalties",
            padding=10)
        penalty_frame.pack(fill='x', padx=5, pady=5)

        pen_info_frame = ttk.Frame(penalty_frame)
        pen_info_frame.pack(fill='x')

        ttk.Label(
            pen_info_frame,
            text="Max DEX Bonus:",
            font=(
                'Arial',
                9)).grid(
            row=0,
            column=0,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['enc_max_dex'] = ttk.Label(
            pen_info_frame, text="None", relief='sunken', width=10)
        self.labels['enc_max_dex'].grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(
            pen_info_frame,
            text="Check Penalty:",
            font=(
                'Arial',
                9)).grid(
            row=0,
            column=2,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['enc_check_penalty'] = ttk.Label(
            pen_info_frame, text="0", relief='sunken', width=10)
        self.labels['enc_check_penalty'].grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(
            pen_info_frame,
            text="Speed Reduction:",
            font=(
                'Arial',
                9)).grid(
            row=0,
            column=4,
            sticky='e',
            padx=5,
            pady=2)
        self.labels['enc_speed'] = ttk.Label(
            pen_info_frame, text="0 ft", relief='sunken', width=10)
        self.labels['enc_speed'].grid(row=0, column=5, padx=5, pady=2)

        # Currency section
        currency_frame = ttk.LabelFrame(
            main_container, text="Currency", padding=10)
        currency_frame.pack(fill='x', padx=5, pady=5)

        curr_grid = ttk.Frame(currency_frame)
        curr_grid.pack(fill='x')

        # Platinum
        ttk.Label(
            curr_grid,
            text="Platinum (pp):",
            font=('Arial', 9, 'bold')).grid(
            row=0, column=0, sticky='e', padx=5, pady=2)
        self.entries['currency_platinum'] = ttk.Entry(curr_grid, width=12)
        self.entries['currency_platinum'].grid(row=0, column=1, padx=5, pady=2)
        self.entries['currency_platinum'].insert(0, "0")
        self.entries['currency_platinum'].bind(
            '<KeyRelease>', lambda e: self.update_currency_total())

        # Gold
        ttk.Label(
            curr_grid,
            text="Gold (gp):",
            font=('Arial', 9, 'bold')).grid(
            row=0, column=2, sticky='e', padx=5, pady=2)
        self.entries['currency_gold'] = ttk.Entry(curr_grid, width=12)
        self.entries['currency_gold'].grid(row=0, column=3, padx=5, pady=2)
        self.entries['currency_gold'].insert(0, "0")
        self.entries['currency_gold'].bind(
            '<KeyRelease>', lambda e: self.update_currency_total())

        # Silver
        ttk.Label(
            curr_grid,
            text="Silver (sp):",
            font=('Arial', 9, 'bold')).grid(
            row=1, column=0, sticky='e', padx=5, pady=2)
        self.entries['currency_silver'] = ttk.Entry(curr_grid, width=12)
        self.entries['currency_silver'].grid(row=1, column=1, padx=5, pady=2)
        self.entries['currency_silver'].insert(0, "0")
        self.entries['currency_silver'].bind(
            '<KeyRelease>', lambda e: self.update_currency_total())

        # Copper
        ttk.Label(
            curr_grid,
            text="Copper (cp):",
            font=('Arial', 9, 'bold')).grid(
            row=1, column=2, sticky='e', padx=5, pady=2)
        self.entries['currency_copper'] = ttk.Entry(curr_grid, width=12)
        self.entries['currency_copper'].grid(row=1, column=3, padx=5, pady=2)
        self.entries['currency_copper'].insert(0, "0")
        self.entries['currency_copper'].bind(
            '<KeyRelease>', lambda e: self.update_currency_total())

        # Total value in gold
        ttk.Label(
            curr_grid,
            text="Total Value:",
            font=('Arial', 10, 'bold')).grid(
            row=2, column=0, sticky='e', padx=5, pady=(10, 2))
        self.labels['currency_total'] = ttk.Label(
            curr_grid,
            text="0 gp",
            relief='sunken',
            width=15,
            font=('Arial', 10, 'bold'))
        self.labels['currency_total'].grid(
            row=2, column=1, columnspan=3, sticky='w', padx=5, pady=(10, 2))

        # Inventory list frame
        inventory_frame = ttk.LabelFrame(
            main_container, text="Inventory", padding=10)
        inventory_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Add item controls
        add_frame = ttk.Frame(inventory_frame)
        add_frame.pack(fill='x', pady=(0, 5))

        ttk.Label(
            add_frame,
            text="Item Name:").grid(
            row=0,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['item_name'] = ttk.Entry(add_frame, width=20)
        self.entries['item_name'].grid(row=0, column=1, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Weight (lbs):").grid(
            row=0,
            column=2,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['item_weight'] = ttk.Entry(add_frame, width=8)
        self.entries['item_weight'].grid(row=0, column=3, padx=2, pady=2)

        ttk.Label(
            add_frame,
            text="Quantity:").grid(
            row=0,
            column=4,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['item_quantity'] = ttk.Entry(add_frame, width=8)
        self.entries['item_quantity'].grid(row=0, column=5, padx=2, pady=2)
        self.entries['item_quantity'].insert(0, "1")

        ttk.Label(
            add_frame,
            text="Notes:").grid(
            row=1,
            column=0,
            sticky='e',
            padx=2,
            pady=2)
        self.entries['item_notes'] = ttk.Entry(add_frame, width=40)
        self.entries['item_notes'].grid(
            row=1, column=1, columnspan=3, padx=2, pady=2, sticky='ew')

        # Container options
        self.is_container_var = tk.BooleanVar(value=False)
        self.entries['item_is_container'] = ttk.Checkbutton(add_frame, text='Is Container', variable=self.is_container_var)
        self.entries['item_is_container'].grid(row=0, column=6, padx=4)

        ttk.Label(add_frame, text="Capacity (lbs):").grid(row=1, column=4, sticky='e', padx=2)
        self.entries['item_capacity'] = ttk.Entry(add_frame, width=12)
        self.entries['item_capacity'].grid(row=1, column=5, padx=2, pady=2)

        self.count_contents_var = tk.BooleanVar(value=True)
        self.entries['item_count_contents'] = ttk.Checkbutton(add_frame, text='Count contents towards carry', variable=self.count_contents_var)
        self.entries['item_count_contents'].grid(row=1, column=6, padx=4)

        add_btn = ttk.Button(
            add_frame,
            text="Add Item",
            command=self.add_inventory_item)
        # Move the Add Item button to the right of the container checkboxes (column 7)
        # Place the Add button to the right of both container checkboxes and align vertically
        add_btn.grid(row=0, column=7, rowspan=2, columnspan=1, padx=2, pady=2)

        # Inventory list with scrollbar
        list_frame = ttk.Frame(inventory_frame)
        list_frame.pack(fill='both', expand=True)

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')

        # Create treeview for inventory
        columns = ('name', 'weight', 'quantity', 'total_weight', 'inside_cap', 'counted', 'notes')
        self.inventory_tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=scrollbar.set)

        self.inventory_tree.heading('name', text='Item Name')
        self.inventory_tree.heading('weight', text='Weight (ea)')
        self.inventory_tree.heading('quantity', text='Qty')
        self.inventory_tree.heading('total_weight', text='Total Weight')
        self.inventory_tree.heading('inside_cap', text='Inside/Capacity')
        self.inventory_tree.heading('counted', text='Counted?')
        self.inventory_tree.heading('notes', text='Notes')

        self.inventory_tree.column('name', width=200)
        self.inventory_tree.column('weight', width=80)
        self.inventory_tree.column('quantity', width=60)
        self.inventory_tree.column('total_weight', width=100)
        self.inventory_tree.column('inside_cap', width=120)
        self.inventory_tree.column('counted', width=60)
        self.inventory_tree.column('notes', width=250)

        self.inventory_tree.pack(fill='both', expand=True)
        scrollbar.config(command=self.inventory_tree.yview)

        # Bind double-click to edit item
        self.inventory_tree.bind('<Double-1>', self.edit_inventory_item)

        # Remove button
        remove_frame = ttk.Frame(inventory_frame)
        remove_frame.pack(fill='x', pady=(5, 0))

        remove_btn = ttk.Button(
            remove_frame,
            text="Remove Selected Item",
            command=self.remove_inventory_item)
        remove_btn.pack(side='left', padx=2)

    def add_inventory_item(self):
        """Add an item to the inventory"""
        try:
            name = self.entries['item_name'].get().strip()
            if not name:
                messagebox.showwarning(
                    "Missing Name", "Please enter an item name.")
                return

            weight_str = self.entries['item_weight'].get().strip()
            weight = float(weight_str) if weight_str else 0.0

            quantity_str = self.entries['item_quantity'].get().strip()
            quantity = int(quantity_str) if quantity_str else 1

            notes = self.entries['item_notes'].get().strip()

            # Add to character
            is_container = bool(self.is_container_var.get())
            capacity = 0.0
            try:
                capacity_str = self.entries['item_capacity'].get().strip()
                capacity = float(capacity_str) if capacity_str else 0.0
            except Exception:
                capacity = 0.0
            count_contents = bool(self.count_contents_var.get())
            self.character.add_item(name, weight, quantity, notes, is_container=is_container, capacity_lbs=capacity, count_contents_toward_carry=count_contents, contents=[])

            # Update display
            self.update_inventory_display()

            # Clear entry fields
            self.entries['item_name'].delete(0, tk.END)
            self.entries['item_weight'].delete(0, tk.END)
            self.entries['item_quantity'].delete(0, tk.END)
            self.entries['item_quantity'].insert(0, "1")
            self.entries['item_notes'].delete(0, tk.END)
            # Reset container fields
            self.is_container_var.set(False)
            self.entries['item_capacity'].delete(0, tk.END)
            self.count_contents_var.set(True)

            self.mark_modified()

        except ValueError as e:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers for weight and quantity.")

    def remove_inventory_item(self):
        """Remove selected item from inventory"""
        selection = self.inventory_tree.selection()
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select an item to remove.")
            return

        # Get index of selected item
        item = selection[0]
        index = self.inventory_tree.index(item)

        # Remove from character
        self.character.remove_item(index)

        # Update display
        self.update_inventory_display()
        self.mark_modified()

    def edit_inventory_item(self, event):
        """Edit selected item from inventory (double-click handler)"""
        selection = self.inventory_tree.selection()
        if not selection:
            return

        # Get index of selected item
        item = selection[0]
        index = self.inventory_tree.index(item)
        
        # Get current item data
        current_item = self.character.inventory[index]
        
        # Create local staged edits workspace for this edit dialog
        original_contents = current_item.get('contents', []).copy()
        staged_contents = original_contents.copy()

        # Create edit dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Item")
        dialog.geometry("450x250")
        dialog.transient(self.root)
        try:
            dialog.grab_set()
        except Exception:
            # In unit tests or headless environments, fall back to a non-modal dialog
            dialog = tk.Toplevel(self.root)
        
        # Create form
        form_frame = ttk.Frame(dialog, padding=20)
        form_frame.pack(fill='both', expand=True)
        
        ttk.Label(form_frame, text="Item Name:").grid(
            row=0, column=0, sticky='e', padx=5, pady=5)
        name_entry = ttk.Entry(form_frame, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        name_entry.insert(0, current_item['name'])
        
        ttk.Label(form_frame, text="Weight (lbs):").grid(
            row=1, column=0, sticky='e', padx=5, pady=5)
        weight_entry = ttk.Entry(form_frame, width=15)
        weight_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        weight_entry.insert(0, str(current_item['weight']))
        
        ttk.Label(form_frame, text="Quantity:").grid(
            row=2, column=0, sticky='e', padx=5, pady=5)
        quantity_entry = ttk.Entry(form_frame, width=15)
        quantity_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        quantity_entry.insert(0, str(current_item['quantity']))
        
        ttk.Label(form_frame, text="Notes:").grid(
            row=3, column=0, sticky='e', padx=5, pady=5)
        notes_entry = ttk.Entry(form_frame, width=30)
        notes_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
        notes_entry.insert(0, current_item.get('notes', ''))

        # Container options
        is_container_var = tk.BooleanVar(value=current_item.get('is_container', False))
        is_container_cb = ttk.Checkbutton(form_frame, text='Is Container', variable=is_container_var)
        is_container_cb.grid(row=0, column=2, padx=5)

        ttk.Label(form_frame, text='Capacity (lbs):').grid(row=1, column=2, sticky='e', padx=5)
        capacity_entry = ttk.Entry(form_frame, width=12)
        capacity_entry.grid(row=1, column=3, padx=5)
        capacity_entry.insert(0, str(current_item.get('capacity_lbs', '')))

        count_contents_var = tk.BooleanVar(value=current_item.get('count_contents_toward_carry', True))
        count_contents_cb = ttk.Checkbutton(form_frame, text='Count contents towards carry', variable=count_contents_var)
        count_contents_cb.grid(row=2, column=2, columnspan=2, padx=5)

        # UI indicator for staged changes (appear when staged_contents differs from original_contents)
        staged_changes_var = tk.StringVar(value='')
        staged_label = ttk.Label(form_frame, textvariable=staged_changes_var, foreground='orange')
        staged_label.grid(row=3, column=3, padx=5, sticky='w')

        # Expose references to the staged / original contents and label var so tests can interact
        self._last_edit_dialog_staged_contents = staged_contents
        self._last_edit_dialog_original_contents = original_contents
        self._last_edit_dialog_staged_label_var = staged_changes_var

        def update_staged_indicator():
            try:
                self._update_last_edit_dialog_indicator()
            except Exception:
                pass

        def manage_contents():
            # Open a small dialog to manage contents
            contents = staged_contents
            # Use a temp container wrapper so add/edit/remove act on staged_contents
            temp_container = {
                'is_container': True,
                'capacity_lbs': current_item.get('capacity_lbs', 0),
                'count_contents_toward_carry': current_item.get('count_contents_toward_carry', True),
                'contents': staged_contents
            }
            dlg = tk.Toplevel(self.root)
            dlg.title('Manage Contents')
            dlg.transient(self.root)
            try:
                dlg.grab_set()
            except Exception:
                # In headless environments or where grabs are not permitted, proceed without modal grab
                pass
            try:
                self._last_manage_dlg = dlg
            except Exception:
                pass

            cf = ttk.Frame(dlg, padding=10)
            cf.pack(fill='both', expand=True)

            content_tree = ttk.Treeview(cf, columns=('name', 'weight', 'quantity', 'notes'), show='headings')
            for h, w in [('name', 150), ('weight', 80), ('quantity', 60), ('notes', 200)]:
                content_tree.heading(h, text=h.title())
                content_tree.column(h, width=w)
            content_tree.pack(fill='both', expand=True)

            for c in contents:
                content_tree.insert('', 'end', values=(c.get('name', ''), f"{c.get('weight',0):.1f}", c.get('quantity',1), c.get('notes','')))

            # Add content controls
            addf = ttk.Frame(cf)
            addf.pack(fill='x', pady=(5,0))
            try:
                # expose addf so tests can inspect the add controls
                self._last_manage_addf = addf
            except Exception:
                pass
            # Column headers for the add content controls
            ttk.Label(addf, text='Name:').grid(row=0, column=0, padx=2)
            ttk.Label(addf, text='Weight (lbs):').grid(row=0, column=1, padx=2)
            ttk.Label(addf, text='Qty:').grid(row=0, column=2, padx=2)
            ttk.Label(addf, text='Notes:').grid(row=0, column=3, padx=2)
            name_c = ttk.Entry(addf, width=20)
            name_c.grid(row=1, column=0, padx=2)
            weight_c = ttk.Entry(addf, width=8)
            weight_c.grid(row=1, column=1, padx=2)
            q_c = ttk.Entry(addf, width=8)
            q_c.insert(0, '1')
            q_c.grid(row=1, column=2, padx=2)
            notes_c = ttk.Entry(addf, width=30)
            notes_c.grid(row=1, column=3, padx=2)

            def add_content_item():
                nm = name_c.get().strip()
                try:
                    wt = float(weight_c.get()) if weight_c.get() else 0.0
                except Exception:
                    wt = 0.0
                try:
                    q = int(q_c.get()) if q_c.get() else 1
                except Exception:
                    q = 1
                nt = notes_c.get().strip()
                # Create content item with the same schema as inventory items
                item = {
                    'name': nm,
                    'weight': wt,
                    'quantity': q,
                    'notes': nt,
                    # Defaults so item inside a container mirrors top-level item schema
                    'is_container': False,
                    'capacity_lbs': 0.0,
                    'count_contents_toward_carry': True,
                    'contents': []
                }
                ok = self.add_content_to_container(temp_container, item)
                if not ok:
                    messagebox.showwarning('Capacity Exceeded', 'Cannot add item: exceeds container capacity.', parent=dlg)
                    return
                # Refresh tree
                content_tree.insert('', 'end', values=(nm, f"{wt:.1f}", q, nt))
                name_c.delete(0, tk.END)
                weight_c.delete(0, tk.END)
                q_c.delete(0, tk.END)
                q_c.insert(0, '1')
                notes_c.delete(0, tk.END)
                # Mark character modified so it's clear something changed
                try:
                    self.mark_modified()
                except Exception:
                    pass
                try:
                    update_staged_indicator()
                except Exception:
                    pass

            def remove_content_item():
                sel = content_tree.selection()
                if not sel:
                    return
                idx = content_tree.index(sel[0])
                content_tree.delete(sel[0])
                removed = self.remove_content_from_container(temp_container, idx)
                if removed:
                    try:
                        self.mark_modified()
                    except Exception:
                        pass
                    try:
                        update_staged_indicator()
                    except Exception:
                        pass

            def edit_content_item(_evt=None):
                sel = content_tree.selection()
                if not sel:
                    return
                idx = content_tree.index(sel[0])
                c = contents[idx]
                # open small edit dialog
                ed = tk.Toplevel(dlg)
                ed.transient(dlg)
                ed.grab_set()
                ef = ttk.Frame(ed, padding=10)
                ef.pack(fill='both', expand=True)
                ttk.Label(ef, text='Name:').grid(row=0, column=0)
                ne = ttk.Entry(ef, width=30)
                ne.grid(row=0, column=1)
                ne.insert(0, c.get('name', ''))
                ttk.Label(ef, text='Weight:').grid(row=1, column=0)
                we = ttk.Entry(ef, width=12)
                we.grid(row=1, column=1)
                we.insert(0, str(c.get('weight', 0)))
                ttk.Label(ef, text='Qty:').grid(row=2, column=0)
                qe = ttk.Entry(ef, width=8)
                qe.grid(row=2, column=1)
                qe.insert(0, str(c.get('quantity', 1)))
                ttk.Label(ef, text='Notes:').grid(row=3, column=0)
                notee = ttk.Entry(ef, width=30)
                notee.grid(row=3, column=1)
                notee.insert(0, c.get('notes', ''))

                def save_edit():
                    try:
                        nn = ne.get().strip()
                        nw = float(we.get().strip() or 0)
                        nq = int(qe.get().strip() or 1)
                    except Exception:
                        messagebox.showerror('Invalid Input', 'Please provide valid numbers for weight and quantity.', parent=ed)
                        return
                    # Validate capacity
                    cap = current_item.get('capacity_lbs', 0) or 0
                    if cap > 0:
                        existing = sum([c0.get('weight',0)*c0.get('quantity',1) for i0,c0 in enumerate(contents) if i0 != idx])
                        if existing + (nw * nq) > cap:
                            messagebox.showwarning('Capacity Exceeded', 'Cannot set description: exceeds container capacity.', parent=ed)
                            return
                        # Preserve any existing metadata on the content if present (for nested containers)
                        new = {
                            'name': nn,
                            'weight': nw,
                            'quantity': nq,
                            'notes': notee.get().strip(),
                            'is_container': c.get('is_container', False),
                            'capacity_lbs': c.get('capacity_lbs', 0.0),
                            'count_contents_toward_carry': c.get('count_contents_toward_carry', True),
                            'contents': c.get('contents', []).copy() if c.get('contents') else []
                        }
                    ok = self.edit_content_in_container(temp_container, idx, new)
                    if not ok:
                        messagebox.showwarning('Capacity Exceeded', 'Cannot set values: exceeds container capacity.', parent=ed)
                        return
                    # update tree entry
                    content_tree.item(sel[0], values=(new.get('name',''), f"{new.get('weight',0):.1f}", new.get('quantity',1), new.get('notes','')))
                    try:
                        self.mark_modified()
                    except Exception:
                        pass
                    try:
                        update_staged_indicator()
                    except Exception:
                        pass
                    ed.destroy()

                ttk.Button(ef, text='Save', command=save_edit).grid(row=4, column=0)
                ttk.Button(ef, text='Cancel', command=ed.destroy).grid(row=4, column=1)
                self.root.wait_window(ed)

            ttk.Button(addf, text='Add', command=add_content_item).grid(row=1, column=4, padx=2)
            ttk.Button(addf, text='Remove', command=remove_content_item).grid(row=1, column=5, padx=2)
            # Bind double-click to edit
            content_tree.bind('<Double-1>', edit_content_item)

            def close_dlg():
                # Commit staged contents into the current_item when closing the Manage Contents dialog
                current_item['contents'] = staged_contents.copy()
                try:
                    self.update_inventory_display()
                except Exception:
                    pass
                try:
                    self.mark_modified()
                except Exception:
                    pass
                try:
                    self._last_manage_addf = None
                    self._last_manage_dlg = None
                except Exception:
                    pass
                dlg.destroy()

            btnf = ttk.Frame(cf)
            btnf.pack(fill='x', pady=6)
            ttk.Button(btnf, text='Close', command=close_dlg).pack(side='left')
            self.root.wait_window(dlg)
            # Do NOT save contents back here - they are staged until the main dialog is saved

        if current_item.get('is_container'):
            manage_btn = ttk.Button(form_frame, text='Manage Contents', command=manage_contents)
            manage_btn.grid(row=3, column=2, padx=5, pady=5)
            try:
                self._last_manage_button = manage_btn
            except Exception:
                pass
            update_staged_indicator()
        else:
            try:
                staged_label.grid_remove()
            except Exception:
                pass
        
        form_frame.columnconfigure(1, weight=1)
        
        def save_changes():
            try:
                name = name_entry.get().strip()
                if not name:
                    messagebox.showwarning(
                        "Missing Name", 
                        "Please enter an item name.",
                        parent=dialog)
                    return
                
                weight_str = weight_entry.get().strip()
                weight = float(weight_str) if weight_str else 0.0
                
                quantity_str = quantity_entry.get().strip()
                quantity = int(quantity_str) if quantity_str else 1
                
                notes = notes_entry.get().strip()
                
                # Update the item in character's inventory
                new_item = {
                    'name': name,
                    'weight': weight,
                    'quantity': quantity,
                    'notes': notes
                }
                if is_container_var.get():
                    new_item['is_container'] = True
                    try:
                        new_item['capacity_lbs'] = float(capacity_entry.get().strip() or 0)
                    except Exception:
                        new_item['capacity_lbs'] = 0.0
                    new_item['count_contents_toward_carry'] = bool(count_contents_var.get())
                    # Commit staged contents to be saved when the main dialog's Save is clicked
                    new_item['contents'] = staged_contents.copy()

                self.character.inventory[index] = new_item
                
                # Update display
                self.update_inventory_display()
                self.mark_modified()
                
                # Clear staged indicator when final save occurs
                try:
                    update_staged_indicator()
                except Exception:
                    pass
                # Clear local last-edit dialog diagnostics
                try:
                    self._last_edit_dialog_staged_contents = None
                    self._last_edit_dialog_original_contents = None
                    self._last_edit_dialog_staged_label_var = None
                except Exception:
                    pass
                dialog.destroy()
                
            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter valid numbers for weight and quantity.",
                    parent=dialog)
        
        # Buttons
        button_frame = ttk.Frame(dialog)
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        ttk.Button(
            button_frame,
            text="Save",
            command=save_changes).pack(side='left', padx=5)
        def cancel_and_revert():
            # Revert any staged changes if the user cancels the edit dialog
            current_item['contents'] = original_contents.copy()
            try:
                self.update_inventory_display()
            except Exception:
                pass
            # Clear staged indicator on cancel
            try:
                update_staged_indicator()
            except Exception:
                pass
            # Clear local last-edit dialog diagnostics on cancel
            try:
                self._last_edit_dialog_staged_contents = None
                self._last_edit_dialog_original_contents = None
                self._last_edit_dialog_staged_label_var = None
            except Exception:
                pass
            dialog.destroy()
        ttk.Button(
            button_frame,
            text="Cancel",
            command=cancel_and_revert).pack(side='left', padx=5)
        dialog.protocol('WM_DELETE_WINDOW', cancel_and_revert)
        
        # Focus on name entry
        name_entry.focus()
        name_entry.select_range(0, tk.END)
        # Expose callbacks for integration tests
        try:
            self._last_edit_dialog_save_fn = save_changes
            self._last_edit_dialog_cancel_fn = cancel_and_revert
        except Exception:
            try:
                self._last_edit_dialog_save_fn = None
                self._last_edit_dialog_cancel_fn = None
            except Exception:
                pass

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
            inside_weight = ''
            capacity = ''
            counted = ''
            if item.get('is_container'):
                # calculate contents weight
                contents_weight = 0
                for c in item.get('contents', []):
                    contents_weight += c.get('weight', 0) * c.get('quantity', 1)
                inside_weight = f"{contents_weight:.1f}"
                capacity = f"{item.get('capacity_lbs', 0):.1f}"
                counted = 'Yes' if item.get('count_contents_toward_carry', True) else 'No'
            notes = item.get('notes', '')

            inside_cap_display = f"{inside_weight}/{capacity}" if inside_weight or capacity else ''
            self.inventory_tree.insert(
                '', 'end', values=(
                    name, f"{weight:.1f}", quantity, f"{total_weight:.1f}", inside_cap_display, counted, notes))

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

        max_dex_text = "None" if penalties['max_dex'] is None else str(
            penalties['max_dex'])
        self.labels['enc_max_dex'].config(text=max_dex_text)
        self.labels['enc_check_penalty'].config(
            text=str(penalties['check_penalty']))
        self.labels['enc_speed'].config(
            text=f"{penalties['speed_reduction']} ft")

    def _update_last_edit_dialog_indicator(self):
        """Helper to update the staged indicator label on the last opened edit dialog."""
        try:
            sc = getattr(self, '_last_edit_dialog_staged_contents', None)
            oc = getattr(self, '_last_edit_dialog_original_contents', None)
            var = getattr(self, '_last_edit_dialog_staged_label_var', None)
            if var is None:
                return
            if sc != oc:
                var.set('* Staged Changes')
            else:
                var.set('')
        except Exception:
            # Best-effort: ignore if data/vars aren't set
            pass

    def update_currency_total(self):
        """Calculate and display total currency value in gold pieces"""
        try:
            # Get currency values, default to 0 if empty or invalid
            pp = float(self.entries['currency_platinum'].get() or 0)
            gp = float(self.entries['currency_gold'].get() or 0)
            sp = float(self.entries['currency_silver'].get() or 0)
            cp = float(self.entries['currency_copper'].get() or 0)
            
            # Convert to gold pieces
            # 1 pp = 10 gp, 10 sp = 1 gp, 100 cp = 1 gp
            total_gp = (pp * 10) + gp + (sp / 10) + (cp / 100)
            
            self.labels['currency_total'].config(text=f"{total_gp:.2f} gp")
            
            # Update character's currency
            self.character.currency['platinum'] = int(pp)
            self.character.currency['gold'] = int(gp)
            self.character.currency['silver'] = int(sp)
            self.character.currency['copper'] = int(cp)
            
            self.mark_modified()
        except ValueError:
            # If there's an error in conversion, just ignore it
            pass

    def load_currency(self):
        """Load currency values from character into UI"""
        currency = self.character.currency
        self.entries['currency_platinum'].delete(0, tk.END)
        self.entries['currency_platinum'].insert(0, str(currency.get('platinum', 0)))
        
        self.entries['currency_gold'].delete(0, tk.END)
        self.entries['currency_gold'].insert(0, str(currency.get('gold', 0)))
        
        self.entries['currency_silver'].delete(0, tk.END)
        self.entries['currency_silver'].insert(0, str(currency.get('silver', 0)))
        
        self.entries['currency_copper'].delete(0, tk.END)
        self.entries['currency_copper'].insert(0, str(currency.get('copper', 0)))
        
        self.update_currency_total()
