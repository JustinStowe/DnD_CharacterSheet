"""
Character Creation Dialog for D&D 3e Character Sheet
Encapsulates the character creation UI logic.
"""
import tkinter as tk
from tkinter import ttk, messagebox


class CharacterCreationDialog:
    """Dialog for creating a new D&D 3e character"""
    
    def __init__(self, parent, character_class, class_definitions, bind_mousewheel_func=None):
        """
        Initialize the character creation dialog.
        
        Args:
            parent: Parent window
            character_class: The Character class to instantiate
            class_definitions: Dictionary of class definitions
            bind_mousewheel_func: Optional function to bind mousewheel to canvas
        """
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Create New Character")
        self.dialog.minsize(400, 400)
        self.dialog.geometry("500x600")
        self.dialog.resizable(True, True)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.character_class = character_class
        self.class_definitions = class_definitions
        self.bind_mousewheel_func = bind_mousewheel_func
        self.result = {'created': False, 'character': None}
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the UI for character creation"""
        # Create scrollable frame
        canvas = tk.Canvas(self.dialog)
        scrollbar = ttk.Scrollbar(self.dialog, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Title
        ttk.Label(scrollable_frame, text="Create New Character", 
                 font=('TkDefaultFont', 14, 'bold')).pack(pady=10)
        
        # Name
        name_frame = ttk.Frame(scrollable_frame)
        name_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(name_frame, text="Character Name:", width=20).pack(side="left")
        self.name_var = tk.StringVar(value="")
        self.name_entry = ttk.Entry(name_frame, textvariable=self.name_var, width=30)
        self.name_entry.pack(side="left", fill="x", expand=True)
        
        # Player Name
        player_frame = ttk.Frame(scrollable_frame)
        player_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(player_frame, text="Player Name:", width=20).pack(side="left")
        self.player_var = tk.StringVar(value="")
        ttk.Entry(player_frame, textvariable=self.player_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Race
        race_frame = ttk.Frame(scrollable_frame)
        race_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(race_frame, text="Race:", width=20).pack(side="left")
        races = ["Human", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling"]
        self.race_var = tk.StringVar(value="Human")
        ttk.Combobox(race_frame, textvariable=self.race_var, values=races, width=28).pack(side="left")
        
        # Class
        class_frame = ttk.Frame(scrollable_frame)
        class_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(class_frame, text="Starting Class:", width=20).pack(side="left")
        class_names = sorted(self.class_definitions.keys())
        self.class_var = tk.StringVar(value="Fighter")
        ttk.Combobox(class_frame, textvariable=self.class_var, values=class_names, width=28).pack(side="left")
        
        # Alignment
        align_frame = ttk.Frame(scrollable_frame)
        align_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(align_frame, text="Alignment:", width=20).pack(side="left")
        alignments = ["Lawful Good", "Neutral Good", "Chaotic Good",
                     "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                     "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
        self.align_var = tk.StringVar(value="True Neutral")
        ttk.Combobox(align_frame, textvariable=self.align_var, values=alignments, width=28).pack(side="left")
        
        # Deity
        deity_frame = ttk.Frame(scrollable_frame)
        deity_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(deity_frame, text="Deity:", width=20).pack(side="left")
        self.deity_var = tk.StringVar(value="")
        ttk.Entry(deity_frame, textvariable=self.deity_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Gender
        gender_frame = ttk.Frame(scrollable_frame)
        gender_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(gender_frame, text="Gender:", width=20).pack(side="left")
        self.gender_var = tk.StringVar(value="")
        ttk.Entry(gender_frame, textvariable=self.gender_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Height
        height_frame = ttk.Frame(scrollable_frame)
        height_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(height_frame, text="Height:", width=20).pack(side="left")
        self.height_var = tk.StringVar(value="")
        ttk.Entry(height_frame, textvariable=self.height_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Weight
        weight_frame = ttk.Frame(scrollable_frame)
        weight_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(weight_frame, text="Weight:", width=20).pack(side="left")
        self.weight_var = tk.StringVar(value="")
        ttk.Entry(weight_frame, textvariable=self.weight_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Hair Color
        hair_frame = ttk.Frame(scrollable_frame)
        hair_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(hair_frame, text="Hair Color:", width=20).pack(side="left")
        self.hair_var = tk.StringVar(value="")
        ttk.Entry(hair_frame, textvariable=self.hair_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Eye Color
        eye_frame = ttk.Frame(scrollable_frame)
        eye_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(eye_frame, text="Eye Color:", width=20).pack(side="left")
        self.eye_var = tk.StringVar(value="")
        ttk.Entry(eye_frame, textvariable=self.eye_var, width=30).pack(side="left", fill="x", expand=True)
        
        # Ability Scores Section
        ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', padx=20, pady=10)
        ttk.Label(scrollable_frame, text="Ability Scores", 
                 font=('TkDefaultFont', 12, 'bold')).pack(pady=5)
        
        self.ability_vars = {}
        ABILITY_SCORE_MAX = 30  # Configurable upper limit for ability scores
        for ability in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(fill="x", padx=20, pady=3)
            ttk.Label(frame, text=f"{ability}:", width=20).pack(side="left")
            var = tk.IntVar(value=10)
            self.ability_vars[ability.lower()] = var
            spinbox = ttk.Spinbox(frame, from_=3, to=ABILITY_SCORE_MAX, textvariable=var, width=10)
            spinbox.pack(side="left")
            ttk.Label(frame, text="(Modifier: ", width=12).pack(side="left")
            mod_label = ttk.Label(frame, text="+0)", width=5)
            mod_label.pack(side="left")
            
            # Update modifier display when ability score changes
            def update_mod(label=mod_label, v=var):
                score = v.get()
                mod = (score - 10) // 2
                label.config(text=f"{'+' if mod >= 0 else ''}{mod})")
            var.trace_add('write', lambda *args, l=mod_label, v=var: update_mod(l, v))
        
        # Buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Create Character", command=self._create_character, width=20).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancel", command=self._cancel, width=20).pack(side="left", padx=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel if function provided
        if self.bind_mousewheel_func:
            self.bind_mousewheel_func(canvas)
    
    def _create_character(self):
        """Create the character with the entered data"""
        if not self.name_var.get():
            messagebox.showwarning("Missing Information", "Please enter a character name.", parent=self.dialog)
            self.name_entry.focus()
            return
        
        # Create the character
        character = self.character_class()
        character.name = self.name_var.get()
        character.player = self.player_var.get()
        character.race = self.race_var.get()
        character.alignment = self.align_var.get()
        character.deity = self.deity_var.get()
        character.gender = self.gender_var.get()
        character.height = self.height_var.get()
        character.weight = self.weight_var.get()
        character.hair_color = self.hair_var.get()
        character.eye_color = self.eye_var.get()
        
        # Set ability scores
        character.strength = self.ability_vars['strength'].get()
        character.dexterity = self.ability_vars['dexterity'].get()
        character.constitution = self.ability_vars['constitution'].get()
        character.intelligence = self.ability_vars['intelligence'].get()
        character.wisdom = self.ability_vars['wisdom'].get()
        character.charisma = self.ability_vars['charisma'].get()
        
        # Set starting class
        starting_class = self.class_var.get()
        character.classes = [{'name': starting_class, 'level': 1}]
        character.character_class = starting_class
        character.level = 1
        
        # Initialize hit points based on class
        class_info = self.class_definitions.get(starting_class, self.class_definitions['Fighter'])
        hit_die = class_info.get('hit_die', 10)
        # First level gets max HP + Con modifier, minimum 1
        con_mod = character.get_con_modifier()
        character.max_hp = max(1, hit_die + con_mod)
        character.current_hp = character.max_hp
        character.hit_dice = [hit_die]
        
        # Calculate initial stats
        character.update_class_based_stats()
        
        self.result['created'] = True
        self.result['character'] = character
        self.dialog.destroy()
    
    def _cancel(self):
        """Cancel character creation"""
        self.dialog.destroy()
    
    def show(self):
        """Show the dialog and wait for result"""
        self.dialog.wait_window()
        return self.result
