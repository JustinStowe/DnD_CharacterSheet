import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable, Dict, Any, List

from inventory_parts import helpers as inv_helpers


def show_manage_contents_dialog(
    root: tk.Tk,
    current_item: Dict[str, Any],
    staged_contents: List[Dict[str, Any]],
    on_modified: Callable[[], None] = None,
    on_update_indicator: Callable[[], None] = None,
    on_close: Callable[[], None] = None,
):
    """Display a Manage Contents dialog which edits staged_contents (list reference).

    - staged_contents is modified in-place; on_close commit logic is expected to call back and copy.
    - on_modified() is called whenever a change is made.
    - on_update_indicator() is called to update staged indicator.
    """
    dlg = tk.Toplevel(root)
    dlg.title('Manage Contents')
    dlg.transient(root)
    try:
        dlg.grab_set()
    except Exception:
        pass

    cf = ttk.Frame(dlg, padding=10)
    cf.pack(fill='both', expand=True)

    content_tree = ttk.Treeview(cf, columns=('name', 'weight', 'quantity', 'notes', 'manage'), show='headings')
    for h, w in [('name', 150), ('weight', 80), ('quantity', 60), ('notes', 200), ('manage', 80)]:
        content_tree.heading(h, text=h.title())
        content_tree.column(h, width=w)
    content_tree.pack(fill='both', expand=True)

    def refresh_tree():
        for it in content_tree.get_children():
            content_tree.delete(it)
        for c in staged_contents:
            mv = 'Manage' if c.get('is_container') else ''
            name_val = (f"📦 {c['name']}" if c.get('is_container') else c.get('name', ''))
            content_tree.insert('', 'end', values=(name_val, f"{c.get('weight',0):.1f}", c.get('quantity',1), c.get('notes',''), mv))

    refresh_tree()

    # Layout
    addf = ttk.Frame(cf)
    addf.pack(fill='x', pady=(5,0))
    ttk.Label(addf, text='Name:').grid(row=0, column=0, padx=2)
    ttk.Label(addf, text='Weight (lbs):').grid(row=0, column=1, padx=2)
    ttk.Label(addf, text='Qty:').grid(row=0, column=2, padx=2)
    ttk.Label(addf, text='Notes:').grid(row=0, column=3, padx=2)
    ttk.Label(addf, text='Is Container').grid(row=0, column=4, padx=2)
    ttk.Label(addf, text='Capacity (lbs):').grid(row=0, column=5, padx=2)
    ttk.Label(addf, text='Count contents?').grid(row=0, column=6, padx=2)

    name_c = ttk.Entry(addf, width=20); name_c.grid(row=1, column=0, padx=2)
    weight_c = ttk.Entry(addf, width=8); weight_c.grid(row=1, column=1, padx=2)
    q_c = ttk.Entry(addf, width=8); q_c.grid(row=1, column=2, padx=2); q_c.insert(0, '1')
    notes_c = ttk.Entry(addf, width=30); notes_c.grid(row=1, column=3, padx=2)
    is_container_c_var = tk.BooleanVar(value=False)
    is_container_c_cb = ttk.Checkbutton(addf, text='Is Container', variable=is_container_c_var); is_container_c_cb.grid(row=1, column=4, padx=2)
    capacity_c = ttk.Entry(addf, width=8); capacity_c.grid(row=1, column=5, padx=2)
    count_c_var = tk.BooleanVar(value=True); count_c_cb = ttk.Checkbutton(addf, text='', variable=count_c_var); count_c_cb.grid(row=1, column=6, padx=2)

    def update_indicator_and_refresh():
        if on_update_indicator:
            try:
                on_update_indicator()
            except Exception:
                pass
        refresh_tree()

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
        try:
            cap_val = float(capacity_c.get().strip() or 0)
        except Exception:
            cap_val = 0.0
        item = {
            'name': nm,
            'weight': wt,
            'quantity': q,
            'notes': nt,
            'is_container': bool(is_container_c_var.get()) or (cap_val > 0),
            'capacity_lbs': cap_val,
            'count_contents_toward_carry': bool(count_c_var.get()),
            'contents': []
        }
        ok = inv_helpers.add_content_to_container({'is_container': True, 'capacity_lbs': current_item.get('capacity_lbs', 0), 'contents': staged_contents}, item)
        if not ok:
            messagebox.showwarning('Capacity Exceeded', 'Cannot add item: exceeds container capacity.', parent=dlg)
            return
        try:
            if on_modified:
                on_modified()
        except Exception:
            pass
        update_indicator_and_refresh()
        name_c.delete(0, tk.END); weight_c.delete(0, tk.END); q_c.delete(0, tk.END); q_c.insert(0, '1'); notes_c.delete(0, tk.END); capacity_c.delete(0, tk.END); is_container_c_var.set(False); count_c_var.set(True)

    def remove_content_item():
        sel = content_tree.selection()
        if not sel:
            return
        idx = content_tree.index(sel[0])
        content_tree.delete(sel[0])
        removed = inv_helpers.remove_content_from_container({'is_container': True, 'contents': staged_contents}, idx)
        if removed:
            try:
                if on_modified:
                    on_modified()
            except Exception:
                pass
        update_indicator_and_refresh()

    def edit_content_item(_evt=None):
        sel = content_tree.selection()
        if not sel:
            return
        idx = content_tree.index(sel[0])
        c = staged_contents[idx]
        ed = tk.Toplevel(dlg); ed.transient(dlg)
        try: ed.grab_set();
        except Exception: pass
        ef = ttk.Frame(ed, padding=10); ef.pack(fill='both', expand=True)
        ttk.Label(ef, text='Name:').grid(row=0, column=0)
        ne = ttk.Entry(ef, width=30); ne.grid(row=0, column=1); ne.insert(0, c.get('name', ''))
        ttk.Label(ef, text='Weight:').grid(row=1, column=0)
        we = ttk.Entry(ef, width=12); we.grid(row=1, column=1); we.insert(0, str(c.get('weight', 0)))
        ttk.Label(ef, text='Qty:').grid(row=2, column=0)
        qe = ttk.Entry(ef, width=8); qe.grid(row=2, column=1); qe.insert(0, str(c.get('quantity', 1)))
        ttk.Label(ef, text='Notes:').grid(row=3, column=0)
        notee = ttk.Entry(ef, width=30); notee.grid(row=3, column=1); notee.insert(0, c.get('notes', ''))
        ttk.Label(ef, text='Is Container').grid(row=4, column=0)
        is_container_ed_var = tk.BooleanVar(value=c.get('is_container', False))
        is_container_ed_cb = ttk.Checkbutton(ef, text='Is Container', variable=is_container_ed_var)
        is_container_ed_cb.grid(row=4, column=1)
        ttk.Label(ef, text='Capacity (lbs):').grid(row=4, column=2)
        cap_ed = ttk.Entry(ef, width=12); cap_ed.grid(row=4, column=3); cap_ed.insert(0, str(c.get('capacity_lbs', 0)))
        count_ed_var = tk.BooleanVar(value=c.get('count_contents_toward_carry', True))
        count_ed_cb = ttk.Checkbutton(ef, text='Count contents towards carry', variable=count_ed_var)
        count_ed_cb.grid(row=5, column=0, columnspan=2)

        def save_edit():
            try:
                nn = ne.get().strip()
                nw = float(we.get().strip() or 0)
                nq = int(qe.get().strip() or 1)
            except Exception:
                messagebox.showerror('Invalid Input', 'Please provide valid numbers for weight and quantity.', parent=ed)
                return
            # Validate parent capacity for this child edit
            cap = current_item.get('capacity_lbs', 0) or 0
            existing = sum(c0.get('weight',0)*c0.get('quantity',1) for i0,c0 in enumerate(staged_contents) if i0 != idx)
            if cap > 0 and (existing + (nw * nq)) > cap:
                messagebox.showwarning('Capacity Exceeded', 'Cannot set description: exceeds container capacity.', parent=ed)
                return
            try:
                updated_cap = float(cap_ed.get().strip() or 0)
            except Exception:
                updated_cap = 0.0
            new = {
                'name': nn,
                'weight': nw,
                'quantity': nq,
                'notes': notee.get().strip(),
                'is_container': bool(is_container_ed_var.get()) or (updated_cap > 0),
                'capacity_lbs': updated_cap,
                'count_contents_toward_carry': bool(count_ed_var.get()),
                'contents': c.get('contents', []).copy() if c.get('contents') else []
            }
            ok = inv_helpers.edit_content_in_container({'is_container': True, 'contents': staged_contents, 'capacity_lbs': current_item.get('capacity_lbs', 0)}, idx, new)
            if not ok:
                messagebox.showwarning('Capacity Exceeded', 'Cannot set values: exceeds container capacity.', parent=ed)
                return
            try:
                if on_modified:
                    on_modified()
            except Exception:
                pass
            update_indicator_and_refresh()
            ed.destroy()

        ttk.Button(ef, text='Save', command=save_edit).grid(row=6, column=0)
        ttk.Button(ef, text='Cancel', command=ed.destroy).grid(row=6, column=1)
        try:
            root.wait_window(ed)
        except Exception:
            pass

    content_tree.bind('<Double-1>', edit_content_item)

    def _on_content_click(evt):
        try:
            col = content_tree.identify_column(evt.x)
            row = content_tree.identify_row(evt.y)
            if not row:
                return
            idx = content_tree.index(row)
            if col == f"#{len(content_tree['columns'])}":
                child = staged_contents[idx]
                if child.get('is_container'):
                    # Recurse into nested manage for this child
                    show_manage_contents_dialog(root, child, child['contents'], on_modified=on_modified, on_update_indicator=on_update_indicator)
        except Exception:
            pass

    content_tree.bind('<ButtonRelease-1>', _on_content_click)

    # Add/Remove buttons
    add_btn = ttk.Button(addf, text='Add', command=add_content_item)
    add_btn.grid(row=1, column=7, padx=2)
    remove_btn = ttk.Button(addf, text='Remove', command=remove_content_item)
    remove_btn.grid(row=1, column=8, padx=2)

    def close_dlg():
        try:
            if on_close:
                on_close()
        except Exception:
            pass
        dlg.destroy()
    btnf = ttk.Frame(cf); btnf.pack(fill='x', pady=6)
    close_btn = ttk.Button(btnf, text='Close', command=close_dlg)
    close_btn.pack(side='left')

    try:
        root.wait_window(dlg)
    except Exception:
        pass
    # Return dialog references for tests
    # expose widget references for test harnesses to avoid scanning children in tests
    widgets = {
        'name': name_c,
        'weight': weight_c,
        'quantity': q_c,
        'notes': notes_c,
        'is_container': is_container_c_cb,
        'capacity': capacity_c,
        'count_contents': count_c_cb,
        'add_button': add_btn,
        'remove_button': remove_btn,
        'close_button': close_btn,
    }
    return {'dlg': dlg, 'addf': addf, 'tree': content_tree, 'widgets': widgets}
        
