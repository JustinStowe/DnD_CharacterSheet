"""
Setup script for building executable with cx_Freeze
Usage: python setup.py build
"""
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter"],
    "excludes": [],
    "include_files": []  # Add any data files here if needed
}

setup(
    name="DnD Character Sheet",
    version="1.0",
    description="D&D 3rd Edition Character Sheet",
    options={"build_exe": build_exe_options},
    executables=[Executable(
        "character_sheet_gui.py",
        base="Win32GUI",  # Use "Win32GUI" for no console window
        target_name="DnD_CharacterSheet.exe"
    )]
)
