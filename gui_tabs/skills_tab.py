"""
Skills Tab - Handles skill management only
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .base_tab import BaseTab


class SkillsTab(BaseTab):
    """Skills management tab"""

    def __init__(self, parent, gui):
        super().__init__(parent, gui)

    def build(self):
        """Build the skills tab"""
        # Create scrollable frame
        canvas = tk.Canvas(self.parent)
        scrollbar = ttk.Scrollbar(
            self.parent,
            orient="vertical",
            command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel scrolling
        self.bind_mousewheel(canvas)

        # Skill points info at top
        points_frame = ttk.Frame(scrollable_frame)
        points_frame.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        ttk.Label(
            points_frame,
            text="Skill Points Available:",
            font=(
                'Arial',
                11,
                'bold')).pack(
            side='left',
            padx=5)
        self.labels['skill_points_available'] = ttk.Label(
            points_frame, text="0", font=(
                'Arial', 11, 'bold'), relief='sunken', width=8)
        self.labels['skill_points_available'].pack(side='left', padx=5)

        # Add spent points display
        ttk.Label(
            points_frame,
            text="Spent:",
            font=(
                'Arial',
                10)).pack(
            side='left',
            padx=(
                20,
                5))
        self.labels['skill_points_spent'] = ttk.Label(
            points_frame, text="0", font=(
                'Arial', 10), relief='sunken', width=6)
        self.labels['skill_points_spent'].pack(side='left', padx=2)

        ttk.Label(
            points_frame,
            text="(Max Ranks = Level + 3 for class skills, (Level + 3)/2 for cross-class)",
            font=(
                'Arial',
                9,
                'italic')).pack(
            side='left',
            padx=10)

        # Skills frame
        skills_frame = ttk.LabelFrame(
            scrollable_frame, text="Skills", padding=10)
        skills_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        # Headers
        ttk.Label(
            skills_frame,
            text="Skill Name",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=0,
            sticky='w',
            padx=2,
            pady=2)
        ttk.Label(
            skills_frame,
            text="Total",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=1,
            padx=2,
            pady=2)
        ttk.Label(
            skills_frame,
            text="Ranks",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=2,
            padx=2,
            pady=2)
        ttk.Label(
            skills_frame,
            text="Ability",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=3,
            padx=2,
            pady=2)
        ttk.Label(
            skills_frame,
            text="Misc",
            font=(
                'Arial',
                10,
                'bold')).grid(
            row=0,
            column=4,
            padx=2,
            pady=2)

        # Create skill rows
        skill_list = sorted(self.character.skills.keys())

        for i, skill_name in enumerate(skill_list, start=1):
            # Skill name
            ttk.Label(
                skills_frame,
                text=skill_name).grid(
                row=i,
                column=0,
                sticky='w',
                padx=2,
                pady=1)

            # Total (readonly)
            self.labels[f'skill_total_{skill_name}'] = ttk.Label(
                skills_frame, text="+0", width=5, relief='sunken')
            self.labels[f'skill_total_{skill_name}'].grid(
                row=i, column=1, padx=2, pady=1)

            # Ranks
            self.entries[f'skill_ranks_{skill_name}'] = ttk.Entry(
                skills_frame, width=5)
            self.entries[f'skill_ranks_{skill_name}'].grid(
                row=i, column=2, padx=2, pady=1)
            self.entries[f'skill_ranks_{skill_name}'].insert(0, "0")
            self.entries[f'skill_ranks_{skill_name}'].bind(
                '<FocusOut>', lambda e, s=skill_name: self.update_skill(s))

            # Ability modifier (readonly)
            ability = self.character.skill_abilities[skill_name].upper()
            self.labels[f'skill_ability_{skill_name}'] = ttk.Label(
                skills_frame, text=f"{ability} +0", width=8, relief='sunken')
            self.labels[f'skill_ability_{skill_name}'].grid(
                row=i, column=3, padx=2, pady=1)

            # Misc
            self.entries[f'skill_misc_{skill_name}'] = ttk.Entry(
                skills_frame, width=5)
            self.entries[f'skill_misc_{skill_name}'].grid(
                row=i, column=4, padx=2, pady=1)
            self.entries[f'skill_misc_{skill_name}'].insert(0, "0")
            self.entries[f'skill_misc_{skill_name}'].bind(
                '<FocusOut>', lambda e, s=skill_name: self.update_skill(s))

    def update_skill(self, skill_name):
        """Update a skill and recalculate totals"""
        # Get previous ranks to calculate the difference
        previous_ranks = self.character.skills.get(skill_name, 0)

        ranks = self.get_entry_int(f'skill_ranks_{skill_name}', 0)
        misc = self.get_entry_int(f'skill_misc_{skill_name}', 0)

        # Calculate points spent
        points_spent = ranks - previous_ranks

        # Check if we have enough skill points
        if points_spent > 0 and self.character.skill_points_available < points_spent:
            messagebox.showwarning(
                "Insufficient Skill Points",
                f"You only have {self.character.skill_points_available} skill points available.\n"
                f"You need {points_spent} more points."
            )
            # Reset to previous value
            self.set_entry(f'skill_ranks_{skill_name}', str(previous_ranks))
            return

        # Update character model
        self.character.skills[skill_name] = ranks
        self.character.skill_misc[skill_name] = misc

        # Adjust available skill points
        self.character.skill_points_available -= points_spent

        # Update display
        if 'skill_points_available' in self.labels:
            self.labels['skill_points_available'].config(
                text=str(self.character.skill_points_available))

        # Update spent points display
        if 'skill_points_spent' in self.labels:
            total_spent = sum(self.character.skills.values())
            self.labels['skill_points_spent'].config(text=str(total_spent))

        # Update the skill total display
        total = self.character.get_skill_total(skill_name)
        total_str = f"+{total}" if total >= 0 else str(total)
        self.labels[f'skill_total_{skill_name}'].config(text=total_str)

        self.mark_modified()

    def refresh_skills_display(self):
        """Refresh all skill displays (called from other tabs when abilities change)"""
        for skill_name in self.character.skills.keys():
            # Update total
            total = self.character.get_skill_total(skill_name)
            total_str = f"+{total}" if total >= 0 else str(total)
            if f'skill_total_{skill_name}' in self.labels:
                self.labels[f'skill_total_{skill_name}'].config(text=total_str)

            # Update ability modifier display for skill
            ability = self.character.skill_abilities[skill_name]
            if ability == 'str':
                ability_mod = self.character.get_str_modifier()
            elif ability == 'dex':
                ability_mod = self.character.get_dex_modifier()
            elif ability == 'con':
                ability_mod = self.character.get_con_modifier()
            elif ability == 'int':
                ability_mod = self.character.get_int_modifier()
            elif ability == 'wis':
                ability_mod = self.character.get_wis_modifier()
            elif ability == 'cha':
                ability_mod = self.character.get_cha_modifier()
            else:
                ability_mod = 0

            ability_str = f"{ability.upper()} {'+' if ability_mod >= 0 else ''}{ability_mod}"
            if f'skill_ability_{skill_name}' in self.labels:
                self.labels[f'skill_ability_{skill_name}'].config(text=ability_str)

        # Update skill points display
        if 'skill_points_available' in self.labels:
            self.labels['skill_points_available'].config(
                text=str(self.character.skill_points_available))
        if 'skill_points_spent' in self.labels:
            total_spent = sum(self.character.skills.values())
            self.labels['skill_points_spent'].config(text=str(total_spent))
