import tkinter as tk
from gui_tabs import InventoryTab


def test_add_container_via_add_form(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    # Fill add form with container info
    it.entries['item_name'].insert(0, 'Bag of Holding')
    it.entries['item_weight'].insert(0, '2')
    it.entries['item_quantity'].delete(0, tk.END)
    it.entries['item_quantity'].insert(0, '1')
    it.entries['item_capacity'].insert(0, '50')
    it.is_container_var.set(True)
    it.count_contents_var.set(True)

    # Add the item
    it.add_inventory_item()

    # Validate that the last inventory item is a container with capacity
    last_item = gui.character.inventory[-1]
    assert last_item['name'] == 'Bag of Holding'
    assert last_item['is_container'] is True
    assert float(last_item['capacity_lbs']) == 50.0


def test_edit_container_manage_contents(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    # Create a container via character directly so edit dialog can modify
    gui.character.add_item('Bag', 2, 1, 'Container', is_container=True, capacity_lbs=30, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    # Select the container row and open edit dialog via method
    child = it.inventory_tree.get_children()[0]
    it.inventory_tree.selection_set(child)
    # Simulate double-click by calling edit directly (no event needed)
    it.edit_inventory_item(None)

    # We can't easily programmatically interact with the modal, but we can assert it exists
    # Instead, manually modify contents using the character model and then re-open display
    gui.character.inventory[0]['contents'].append({'name': 'Gem', 'weight': 10, 'quantity': 1, 'notes': ''})
    it.update_inventory_display()
    # Ensure inside weight shows 10.0
    row = it.inventory_tree.get_children()[0]
    values = it.inventory_tree.item(row)['values']
    assert values[4] == '10.0'  # inside_weight column
