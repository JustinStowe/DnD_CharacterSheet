"""
Startup Dialog for D&D 3e Character Sheet
Encapsulates the startup choice UI logic.
"""
import tkinter as tk
from tkinter import ttk, filedialog


class StartupDialog:
    """Dialog for choosing between creating a new character or loading an existing one"""
    
    def __init__(self):
        """Initialize the startup dialog"""
        # Create a temporary root window for the dialog
        self.temp_root = tk.Tk()
        self.temp_root.withdraw()
        
        self.dialog = tk.Toplevel(self.temp_root)
        self.dialog.title("D&D 3e Character Sheet")
        self.dialog.geometry("400x200")
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f"+{x}+{y}")
        
        self.choice = {'action': None, 'file': None}
        
        self._build_ui()
        
        # Set up window close protocol
        self.dialog.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _build_ui(self):
        """Build the UI for the startup dialog"""
        # Title
        ttk.Label(
            self.dialog,
            text="D&D 3rd Edition Character Sheet",
            font=('TkDefaultFont', 16, 'bold')
        ).pack(pady=20)
        
        ttk.Label(
            self.dialog,
            text="What would you like to do?",
            font=('TkDefaultFont', 12)
        ).pack(pady=10)
        
        # Button frame
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(pady=20)
        
        # New Character button
        ttk.Button(
            button_frame,
            text="Create New Character",
            command=self._new_character,
            width=25
        ).pack(side='left', padx=10)
        
        # Load Character button
        ttk.Button(
            button_frame,
            text="Load Existing Character",
            command=self._load_character,
            width=25
        ).pack(side='left', padx=10)
    
    def _new_character(self):
        """Handle new character selection"""
        self.choice['action'] = 'new'
        self.dialog.destroy()
        self.temp_root.quit()
    
    def _load_character(self):
        """Handle load character selection"""
        filename = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("Character Files", "*.json"), ("All Files", "*.*")],
            title="Load Character"
        )
        if filename:
            self.choice['action'] = 'load'
            self.choice['file'] = filename
            self.dialog.destroy()
            self.temp_root.quit()
    
    def _on_close(self):
        """Handle window close event"""
        self.choice['action'] = None
        self.dialog.destroy()
        self.temp_root.quit()
    
    def show(self):
        """Show the dialog and return the user's choice"""
        # Run the dialog
        self.temp_root.mainloop()
        
        # Store choice before destroying
        result = self.choice.copy()
        
        # Properly destroy everything
        try:
            self.dialog.destroy()
        except:
            pass
        self.temp_root.destroy()
        
        return result
