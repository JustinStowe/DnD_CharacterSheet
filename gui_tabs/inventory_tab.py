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

        add_btn = ttk.Button(
            add_frame,
            text="Add Item",
            command=self.add_inventory_item)
        add_btn.grid(row=1, column=4, columnspan=2, padx=2, pady=2)

        # Inventory list with scrollbar
        list_frame = ttk.Frame(inventory_frame)
        list_frame.pack(fill='both', expand=True)

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')

        # Create treeview for inventory
        columns = ('name', 'weight', 'quantity', 'total_weight', 'notes')
        self.inventory_tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show='headings',
            yscrollcommand=scrollbar.set)

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
            self.character.add_item(name, weight, quantity, notes)

            # Update display
            self.update_inventory_display()

            # Clear entry fields
            self.entries['item_name'].delete(0, tk.END)
            self.entries['item_weight'].delete(0, tk.END)
            self.entries['item_quantity'].delete(0, tk.END)
            self.entries['item_quantity'].insert(0, "1")
            self.entries['item_notes'].delete(0, tk.END)

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
        
        # Create edit dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Item")
        dialog.geometry("450x250")
        dialog.transient(self.root)
        dialog.grab_set()
        
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
                self.character.inventory[index] = {
                    'name': name,
                    'weight': weight,
                    'quantity': quantity,
                    'notes': notes
                }
                
                # Update display
                self.update_inventory_display()
                self.mark_modified()
                
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
        ttk.Button(
            button_frame,
            text="Cancel",
            command=dialog.destroy).pack(side='left', padx=5)
        
        # Focus on name entry
        name_entry.focus()
        name_entry.select_range(0, tk.END)

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

            self.inventory_tree.insert(
                '', 'end', values=(
                    name, f"{
                        weight:.1f}", quantity, f"{
                        total_weight:.1f}", notes))

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
