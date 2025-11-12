"""
Base Tab Class
Contains shared functionality for all character sheet tabs
"""

import tkinter as tk
from tkinter import ttk


class BaseTab:
    """Base class for all character sheet tabs"""

    def __init__(self, parent, gui):
        """
        Initialize base tab

        Args:
            parent: The parent frame widget
            gui: Reference to the main CharacterSheetGUI instance
        """
        self.parent = parent
        self.gui = gui
        self.character = gui.character
        self.root = gui.root
        self.entries = gui.entries
        self.labels = gui.labels

    def mark_modified(self):
        """Mark the character as modified"""
        self.gui.mark_modified()

    def create_labeled_entry(
            self,
            parent,
            label_text,
            row,
            col,
            width=10,
            state='normal'):
        """Create a labeled entry widget"""
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, sticky='e', padx=5, pady=2)

        entry = ttk.Entry(parent, width=width, state=state)
        entry.grid(row=row, column=col + 1, sticky='w', padx=5, pady=2)

        return entry

    def create_labeled_readonly(self, parent, label_text, row, col, width=10):
        """Create a labeled read-only entry widget"""
        return self.create_labeled_entry(
            parent, label_text, row, col, width, state='readonly')

    def bind_mousewheel(self, canvas):
        """
        Bind mouse wheel scrolling to canvas using enter/leave events

        Args:
            canvas: The canvas widget to bind scrolling to
        """
        def on_mousewheel(event):
            try:
                # Only scroll if canvas still exists
                if canvas.winfo_exists():
                    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            except tk.TclError:
                # Canvas has been destroyed, ignore the event
                pass

        def bind_wheel(event):
            try:
                if canvas.winfo_exists():
                    canvas.bind_all("<MouseWheel>", on_mousewheel)
            except tk.TclError:
                pass

        def unbind_wheel(event):
            try:
                if canvas.winfo_exists():
                    canvas.unbind_all("<MouseWheel>")
            except tk.TclError:
                pass

        # Bind on mouse enter, unbind on mouse leave
        canvas.bind('<Enter>', bind_wheel)
        canvas.bind('<Leave>', unbind_wheel)

    def get_entry_int(self, key, default=0):
        """Get integer value from entry widget"""
        try:
            return int(self.entries[key].get())
        except (ValueError, KeyError):
            return default

    def set_entry(self, key, value):
        """Set value in entry widget"""
        if key in self.entries:
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, str(value))

    def build(self):
        """Build the tab UI - must be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement build() method")
