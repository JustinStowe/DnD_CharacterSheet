# Building an Executable

## Method 1: PyInstaller (Recommended)

### Quick Build

Simply double-click `build_executable.bat` - this will:

1. Install PyInstaller (if needed)
2. Convert the icon (DnD_icon.png → DnD_icon.ico) if needed
3. Build the executable with the D&D icon
4. Place it in the `dist` folder

### Manual Build

```bash
# Install PyInstaller
pip install pyinstaller

# Install Pillow for icon conversion (if needed)
pip install pillow

# Convert icon (only needed once)
python convert_icon.py

# Build single executable file with icon
pyinstaller --onefile --windowed --icon=DnD_icon.ico --name "DnD_CharacterSheet" character_sheet_gui.py
```

The executable will be in the `dist` folder with the D&D icon. You can move it anywhere and double-click to run!

### Build Options

**Basic (smallest file, but slower startup):**

```bash
pyinstaller --onefile --windowed character_sheet_gui.py
```

**With folder (larger, but faster startup):**

```bash
pyinstaller --windowed character_sheet_gui.py
```

**With custom icon (already configured):**

```bash
pyinstaller --onefile --windowed --icon=DnD_icon.ico character_sheet_gui.py
```

### Icon Information

The project includes:

- `DnD_icon.png` - Source icon image
- `DnD_icon.ico` - Windows icon file (auto-generated)
- `convert_icon.py` - Script to convert PNG to ICO format

The icon is automatically applied when using `build_executable.bat`.
If you want to use a different icon, replace `DnD_icon.jpg` and delete `DnD_icon.ico`, then rebuild.

## Method 2: Auto-py-to-exe (GUI Tool)

For a graphical interface to configure your build:

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

Then:

1. Select `character_sheet_gui.py` as the script
2. Choose "One File"
3. Choose "Window Based" (no console)
4. Click "Convert .py to .exe"

## Method 3: cx_Freeze

```bash
pip install cx_Freeze

# Create setup.py (see below)
python setup.py build
```

## Distribution

After building:

- The `.exe` file in the `dist` folder is standalone
- No Python installation needed on other computers
- Just double-click to run!
- You can copy it anywhere or share it

## Troubleshooting

**Antivirus warnings:** Some antivirus software flags PyInstaller executables as suspicious. This is a false positive - you can add an exception.

**File not found errors:** Make sure sample JSON files are in the same directory as the executable, or use PyInstaller's `--add-data` option.

**Large file size:** The executable includes the entire Python runtime (~10-50 MB). This is normal.

## Notes

- First run may be slow as Windows scans the new executable
- The executable works on the same OS it was built on (Windows exe works on Windows)
- For cross-platform distribution, build on each platform separately
