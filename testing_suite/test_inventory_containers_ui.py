import tkinter as tk
from tkinter import ttk
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
    # Ensure inside weight/capacity shows '10.0/30.0'
    row = it.inventory_tree.get_children()[0]
    values = it.inventory_tree.item(row)['values']
    assert values[4] == '10.0/30.0'  # inside/capacity column


def test_capacity_validation_prevents_add(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Small Bag', 1, 1, 'Container', is_container=True, capacity_lbs=10, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()
    container = gui.character.inventory[-1]

    # Try to add a heavy item exceeding capacity
    ok = it.add_content_to_container(container, {'name': 'Rock', 'weight': 12, 'quantity': 1, 'notes': ''})
    assert not ok
    assert len(container['contents']) == 0

    # Add smaller item then try to add item exceeding remaining capacity
    ok = it.add_content_to_container(container, {'name': 'Apple', 'weight': 1, 'quantity': 1, 'notes': ''})
    assert ok
    ok = it.add_content_to_container(container, {'name': 'Anvil', 'weight': 10, 'quantity': 1, 'notes': ''})
    assert not ok


def test_edit_content_via_helper_updates_ui(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Medium Bag', 1, 1, 'Container', is_container=True, capacity_lbs=20, count_contents_toward_carry=True, contents=[{'name':'Stone','weight':5,'quantity':1,'notes':''}])
    it.update_inventory_display()

    container = gui.character.inventory[-1]
    # edit content weight from 5 to 10
    ok = it.edit_content_in_container(container, 0, {'name':'Stone','weight':10,'quantity':1,'notes':''})
    assert ok
    it.update_inventory_display()
    row = it.inventory_tree.get_children()[0]
    values = it.inventory_tree.item(row)['values']
    # inside/capacity should be 10.0/20.0
    assert values[4] == '10.0/20.0'


def test_contents_persist_after_save_and_load(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    # Create a container and add contents via the helper
    gui.character.add_item('Water Bag', 2, 1, 'Container', is_container=True, capacity_lbs=50, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    container = gui.character.inventory[-1]
    before_weight = gui.character.get_total_weight_carried()
    ok = it.add_content_to_container(container, {'name': 'Waterskin', 'weight': 2, 'quantity': 3, 'notes': ''})
    assert ok
    it.update_inventory_display()
    after_weight = gui.character.get_total_weight_carried()
    # Waterskin weight is 2 * 3 = 6 lbs, so after_weight should be at least 6 greater than before_weight
    assert after_weight - before_weight == 6

    # Ensure contents are present
    assert len(container['contents']) == 1
    assert container['contents'][0]['name'] == 'Waterskin'
    assert container['contents'][0]['quantity'] == 3

    # Simulate save/load via to_dict/from_dict
    data = gui.character.to_dict()
    new_char = Character()
    new_char.from_dict(data)
    # Find container in new character
    new_container = new_char.inventory[-1]
    assert new_container.get('is_container') is True
    assert len(new_container.get('contents', [])) == 1
    assert new_container['contents'][0]['name'] == 'Waterskin'
    assert new_container['contents'][0]['quantity'] == 3


def test_staged_indicator_shows_and_clears_on_cancel(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Little Bag', 1, 1, 'Container', is_container=True, capacity_lbs=20, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    # Open edit dialog for the container
    row = it.inventory_tree.get_children()[0]
    it.inventory_tree.selection_set(row)
    it.edit_inventory_item(None)

    # Initially no staged changes
    assert it._last_edit_dialog_staged_label_var.get() == ''

    # Simulate staged change by appending to staged_contents and updating the indicator
    it._last_edit_dialog_staged_contents.append({'name': 'Apple', 'weight': 1, 'quantity': 1, 'notes': ''})
    it._update_last_edit_dialog_indicator()
    assert it._last_edit_dialog_staged_label_var.get() == '* Staged Changes'

    # Cancel the edit dialog which should clear staged changes
    it._last_edit_dialog_cancel_fn()
    # After cancel, the staged label variable should be cleared or no longer set
    assert it._last_edit_dialog_staged_label_var is None or it._last_edit_dialog_staged_label_var.get() == ''
    # Ensure the character's container did not gain the staged item
    assert len(gui.character.inventory[0]['contents']) == 0


def test_staged_indicator_shows_and_commits_on_save(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Little Bag', 1, 1, 'Container', is_container=True, capacity_lbs=20, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    # Open edit dialog for the container
    row = it.inventory_tree.get_children()[0]
    it.inventory_tree.selection_set(row)
    it.edit_inventory_item(None)

    # Simulate staged change
    it._last_edit_dialog_staged_contents.append({'name': 'Apple', 'weight': 1, 'quantity': 1, 'notes': ''})
    it._update_last_edit_dialog_indicator()
    assert it._last_edit_dialog_staged_label_var.get() == '* Staged Changes'

    # Invoke Save which should commit the staged contents and clear the staged indicator
    it._last_edit_dialog_save_fn()
    assert it._last_edit_dialog_staged_label_var is None or it._last_edit_dialog_staged_label_var.get() == ''
    # Ensure the character's container now contains the staged item
    assert len(gui.character.inventory[0]['contents']) == 1
    assert gui.character.inventory[0]['contents'][0]['name'] == 'Apple'


def test_manage_add_controls_have_headers(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Little Bag', 1, 1, 'Container', is_container=True, capacity_lbs=20, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    # Open edit dialog for the container
    row = it.inventory_tree.get_children()[0]
    it.inventory_tree.selection_set(row)
    it.edit_inventory_item(None)

    # Invoke the Manage Contents button to open the manage dialog
    assert hasattr(it, '_last_manage_button')
    # To avoid blocking due to wait_window in headless tests, patch root.wait_window temporarily
    old_wait = getattr(it.root, 'wait_window', None)
    it.root.wait_window = lambda d: None
    try:
        it._last_manage_button.invoke()
    finally:
        # restore wait_window
        if old_wait is not None:
            it.root.wait_window = old_wait

    # Now inspect the addf frame's children and check for header labels
    assert hasattr(it, '_last_manage_addf') and it._last_manage_addf is not None
    texts = [c.cget('text') for c in it._last_manage_addf.winfo_children() if isinstance(c, tk.Label) or isinstance(c, ttk.Label)]
    assert 'Name:' in texts
    assert 'Weight (lbs):' in texts
    assert 'Qty:' in texts
    assert 'Notes:' in texts
    # close the manage dialog if left open
    if hasattr(it, '_last_manage_dlg') and it._last_manage_dlg is not None:
        try:
            it._last_manage_dlg.destroy()
        except Exception:
            pass
    # Ensure content items created use same schema as top-level inventory items
    container = gui.character.inventory[0]
    assert len(container['contents']) == 0
    ok = it.add_content_to_container(container, {'name': 'Sack', 'weight': 1, 'quantity': 1, 'notes': ''})
    assert ok
    c = container['contents'][0]
    # Content item should mirror top-level item schema
    assert 'name' in c
    assert 'weight' in c
    assert 'quantity' in c
    assert 'notes' in c


def test_ui_add_content_creates_full_schema(dummy_gui):
    from character import Character
    gui = dummy_gui
    gui.character = Character()
    frame = tk.Frame(gui.root)
    it = InventoryTab(frame, gui)
    it.build()

    gui.character.add_item('Little Bag', 1, 1, 'Container', is_container=True, capacity_lbs=20, count_contents_toward_carry=True, contents=[])
    it.update_inventory_display()

    # Open edit dialog for the container
    row = it.inventory_tree.get_children()[0]
    it.inventory_tree.selection_set(row)
    it.edit_inventory_item(None)

    # Avoid wait_window blocking
    old_wait = getattr(it.root, 'wait_window', None)
    it.root.wait_window = lambda d: None
    try:
        it._last_manage_button.invoke()
    finally:
        if old_wait is not None:
            it.root.wait_window = old_wait

    addf = it._last_manage_addf
    # Fill the add inputs (identify entries by grid column)
    for c in addf.winfo_children():
        info = c.grid_info()
        if info and info.get('row') == 1:
            col = int(info.get('column'))
            if col == 0 and isinstance(c, ttk.Entry):
                c.delete(0, tk.END); c.insert(0, 'Lantern')
            elif col == 1 and isinstance(c, ttk.Entry):
                c.delete(0, tk.END); c.insert(0, '2')
            elif col == 2 and isinstance(c, ttk.Entry):
                c.delete(0, tk.END); c.insert(0, '1')
            elif col == 3 and isinstance(c, ttk.Entry):
                c.delete(0, tk.END); c.insert(0, 'A bamboo lantern')

    # Find the Add button and click it
    add_btn = None
    for c in addf.winfo_children():
        if isinstance(c, ttk.Button) and c.cget('text') == 'Add':
            add_btn = c
            break
    assert add_btn is not None
    add_btn.invoke()

    # Commit staged contents by clicking the Close button in the manage dialog
    # Find Close button by searching widget tree recursively
    def find_button(widget, text):
        for child in widget.winfo_children():
            try:
                if isinstance(child, ttk.Button) and child.cget('text') == text:
                    return child
            except Exception:
                pass
            res = find_button(child, text)
            if res:
                return res
        return None
    dlg = it._last_manage_dlg
    assert dlg is not None
    close_btn = find_button(dlg, 'Close')
    assert close_btn is not None
    close_btn.invoke()

    # Ensure content was created with normalized schema
    container = gui.character.inventory[0]
    assert len(container['contents']) == 1
    c = container['contents'][0]
    assert 'is_container' in c
    assert 'capacity_lbs' in c
    assert 'count_contents_toward_carry' in c
    assert 'contents' in c
    # Clean up
    if hasattr(it, '_last_manage_dlg') and it._last_manage_dlg is not None:
        try:
            it._last_manage_dlg.destroy()
        except Exception:
            pass
    assert 'is_container' in c
    assert 'capacity_lbs' in c
    assert 'count_contents_toward_carry' in c
    assert 'contents' in c
