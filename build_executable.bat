@echo off
echo Building D&D Character Sheet executable...
echo.

REM Install PyInstaller if not already installed
pip install pyinstaller

REM Build the executable
pyinstaller --onefile --windowed --name "DnD_CharacterSheet" --icon=icon.ico character_sheet_gui.py

echo.
echo Build complete! Check the 'dist' folder for your executable.
echo.
pause
