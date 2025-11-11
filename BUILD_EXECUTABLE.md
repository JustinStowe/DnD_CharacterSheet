# Building an Executable

## Method 1: PyInstaller (Recommended)

### Quick Build

Simply double-click `build_executable.bat` - this will:
1. Install PyInstaller (if needed)
2. Build the executable
3. Place it in the `dist` folder

### Manual Build

```bash
# Install PyInstaller
pip install pyinstaller

# Build single executable file
pyinstaller --onefile --windowed --name "DnD_CharacterSheet" character_sheet_gui.py
```

The executable will be in the `dist` folder. You can move it anywhere and double-click to run!

### Build Options

**Basic (smallest file, but slower startup):**
```bash
pyinstaller --onefile --windowed character_sheet_gui.py
```

**With folder (larger, but faster startup):**
```bash
pyinstaller --windowed character_sheet_gui.py
```

**With custom icon:**
```bash
pyinstaller --onefile --windowed --icon=icon.ico character_sheet_gui.py
```

### Add an Icon (Optional)

1. Find or create a `.ico` file for your application
2. Save it as `icon.ico` in the project folder
3. Run the build with `--icon=icon.ico` option

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
