@echo off
echo Building D^&D Character Sheet executable...
echo.

REM Install PyInstaller if not already installed
python -m pip install pyinstaller

REM Convert PNG icon to ICO if needed
if not exist DnD_icon.ico (
    echo Converting icon...
    python convert_icon.py
    echo.
)

REM Build the executable with icon
python -m PyInstaller --onefile --windowed --icon=DnD_icon.ico --name "DnD_CharacterSheet" character_sheet_gui.py

echo.
echo Build complete! Check the 'dist' folder for your executable.
echo.
pause
