@echo off
echo Building D^&D Character Sheet executable...
echo.

REM Install PyInstaller if not already installed
python -m pip install pyinstaller

REM Build the executable (without icon - you can add one later)
python -m PyInstaller --onefile --windowed --name "DnD_CharacterSheet" character_sheet_gui.py

echo.
echo Build complete! Check the 'dist' folder for your executable.
echo.
pause
