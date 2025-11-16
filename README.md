<!-- PROJECT SHIELDS -->
<!-- Using placeholder shields - update links if you use CI / badges -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# D&D 3rd Edition Character Sheet

An interactive character sheet application that automatically updates derived stats and supports epic levels, prestige classes, spells, and more.

     - View total character level

- Automatically sets BAB progression, save progressions, hit die, and spellcasting ability
- **Multiclass BAB & Saves**: Stack correctly according to D&D 3e rules
  - Fighter 5: BAB +5, Fort +4, Ref +1, Will +1
  - Wizard 3: BAB +1, Fort +1, Ref +1, Will +3
  - Duelist 2: BAB +2, Fort +0, Ref +3, Will +0
  - Combined Fighter 5/Wizard 3/Duelist 2: BAB +8, Fort +5, Ref +5, Will +4

2. **Level & Experience**: Track your character's progression
   - XP tracking with next level threshold display
   - **Level Up Button**: Opens dialog to advance your character
     - Choose which class to level (for multiclass characters)
     - Roll or use average for HP gain (based on selected class's hit die)
     - Automatically updates BAB, saves, and grants skill points
     - Preview shows all changes before confirming
3. **Ability Scores**: Enter your ability scores (STR, DEX, CON, INT, WIS, CHA)
   - The modifier is calculated automatically
   - Use "Temp" fields for temporary bonuses/penalties
4. **Saving Throws**: Base saves auto-calculate from class and level
   - For multiclass characters, saves stack from all classes
   - Ability modifiers are added automatically
   - Add misc bonuses from feats, items, etc.
5. **Armor Class**: Enter armor, shield, and other AC bonuses
   - DEX modifier is applied automatically
   - Touch AC and Flat-footed AC are calculated for you
6. **Combat**: Base Attack Bonus auto-calculates from class and level
   - For multiclass characters, BAB stacks from all classes
   - Melee attack (BAB + STR) is calculated automatically
   - Ranged attack (BAB + DEX) is calculated automatically

### Skills Tab

- **Skill Points**: Display shows available unspent skill points
  - First level: (Class skill points + INT mod) × 4
  - Each additional level: Class skill points + INT mod (minimum 1)
  - **Automatic Point Tracking**: When you assign ranks to a skill, points are automatically deducted
  - **Spent Points Display**: Shows total skill points spent
  - **Validation**: Prevents spending more points than available

### Inventory Tab

- Track all your equipment
  - Add items with weight, quantity, and notes
  - Add containers: check "Is Container" and specify a capacity (lbs)
    - Container items include a combined "Inside / Capacity" column to show the total weight of the contents and the capacity
    - Use the "Manage Contents" dialog to add, edit, or remove items stored inside a container
    - Toggle whether a container's contents count toward the character's carried weight ("Count Contents Toward Carry")
    - Capacity validation prevents adding items that would exceed a container's capacity
  - **Double-click to edit items** - modify name, weight, quantity, or notes
  - Carrying capacity auto-calculates based on STR
  - Color-coded load indicator (Light/Medium/Heavy/Overloaded)
  - Shows encumbrance penalties (Max DEX, Check Penalty, Speed Reduction)

### Spells Tab

- **Spellcasting Ability**: Automatically set based on class
  - Can be manually changed if needed
  - Spell save DCs auto-calculate for each spell level based on correct ability
  - Range Definitions: Close: 25 ft + 5 ft/2 levels; Medium: 100 ft + 10 ft/level; Long: 400 ft + 40 ft/level
  - Updates automatically as character level changes
- **Spell Level Organization**: Spells organized in sub-tabs by spell level (0-9), sortable and searchable

### Feats & Abilities

- **Feats Section**: Add feats with name, type, prerequisites, and benefit
  - Types: General, Metamagic, Item Creation, Combat, Skill, Special
  - Full text descriptions for benefits
- **Epic Feats Button** (Level 21+): Access epic feats for epic level characters; the progressions and checks are applied automatically

### Magic Items Tab

- **Create Magic Items**: Comprehensive item creation dialog
  - Name, type, slot, caster level, and charge tracking
  - **Abilities per Item**: Items can have multiple named abilities (name, cost, description). Using a charge prompts selection and deducts the correct cost.
  - Stat bonuses, properties, description field
  - Set max charges and manage usage/ recharge

### Weapons (Main Tab)

- Comprehensive weapon tracking and calculation of attack & damage; supports weapon properties, critical ranges, and special notes

### Save/Load

Use File menu or keyboard shortcuts (Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+Shift+S). Characters are stored as JSON files for easy sharing.

### Examples

- For examples, see `sample_character.json`, `sorcerer_sample.json`, and `cleric_sample.json` in the repository.

## Developer Notes & Project Structure

- `character.py` is the top-level Character class; project logic is split into `character_parts/` manager modules (e.g., `feats`, `spells`, `equipment`, `leveling`, `ac`, `saves`).
- UI code: `gui_tabs/` contains tabs; `dialogs/` contains modals like `MagicItemDialog` and `ManageContents`.
- Inventory container schema: inventory items may include keys: `is_container`, `capacity_lbs`, `count_contents_toward_carry`, and `contents` (list of items).
- Magic items store an `abilities` list with objects containing `name`, `cost`, and `description`.
- Programmatic helpers for containers are available: `add_content_to_container`, `edit_content_in_container`, `remove_content_from_container` in `gui_tabs/inventory_tab.py`.

## Testing

- Run the full test suite using pytest:

```bash
python -m pytest -q
```

- GUI tests include `dummy_gui` in `testing_suite/conftest.py` for headless CI-friendly tests.
- Add unit tests for managers in `testing_suite/` and UI integration tests using the dummy GUI or a real Tk root if available.

## Contributing

See the `Contributing` section toward the bottom for authoring guidelines and a PR checklist.

## What's New (summary)

- Inventory Containers: Bags and containers with internal contents, capacity validation, and an optional toggle to count contents toward carried weight.
- Magic Item Abilities: Magic items can include multiple named abilities with charge cost and descriptions; using charges prompts ability selection and decrements charges based on ability cost.
- Manager refactor: The `Character` class delegates to per-concern managers for better modularity.
- Headless GUI testing: Added a `dummy_gui` fixture for consistent, headless GUI tests.

## Available Files & Notable Paths

- `character_sheet_gui.py`: Main GUI application
- `character.py`: Character model and delegations to managers
- `gui_tabs/`: Tabbed GUI code
- `dialogs/`: Dialog modals
- `character_parts/`: Manager modules (equipment, feats, spells, leveling, ac, saves, etc.)
- `testing_suite/`: Unit and UI tests, including `conftest.py` for headless testing

## Supported Classes (core 11)

| Class     | Hit Die | BAB    | Fort | Ref  | Will | Skill Points | Spellcasting |
| --------- | ------- | ------ | ---- | ---- | ---- | ------------ | ------------ |
| Fighter   | d10     | Full   | Good | Poor | Poor | 2 + INT      | None         |
| Barbarian | d12     | Full   | Good | Poor | Poor | 4 + INT      | None         |
| Ranger    | d8      | Full   | Good | Good | Poor | 6 + INT      | Wisdom       |
| Paladin   | d10     | Full   | Good | Poor | Poor | 2 + INT      | Wisdom       |
| Cleric    | d8      | Medium | Good | Poor | Good | 2 + INT      | Wisdom       |
| Druid     | d8      | Medium | Good | Poor | Good | 4 + INT      | Wisdom       |
| Monk      | d8      | Medium | Good | Good | Good | 4 + INT      | None         |
| Rogue     | d6      | Medium | Poor | Good | Poor | 8 + INT      | None         |
| Bard      | d6      | Medium | Poor | Good | Good | 6 + INT      | Charisma     |
| Wizard    | d4      | Poor   | Poor | Poor | Good | 2 + INT      | Intelligence |
| Sorcerer  | d4      | Poor   | Poor | Poor | Good | 2 + INT      | Charisma     |

## Available Prestige Classes

### Core DMG (12 classes)

1. Arcane Archer
2. Arcane Trickster
3. Assassin
4. Blackguard
5. Dragon Disciple
6. Duelist
7. Dwarven Defender
8. Eldritch Knight
9. Horizon Walker
10. Loremaster
11. Mystic Theurge
12. Shadowdancer

### Magic of Faerûn (19 classes)

1. Harper Scout
2. Spellsword
3. Red Wizard
4. Guild Thief
5. Shadow Adept
6. Arcane Devotee
7. Divine Champion
8. Divine Disciple
9. Harper Priest
10. Runecaster
11. Silverstar
12. Hospitaler
13. Incantatrix
14. Acolyte of the Ego
15. Acolyte of the Skin
16. Shaaryan Hunter
17. Monk of the Long Death
18. Zhentarim Soldier
19. Zhentarim Spy

### Tome and Blood (12 classes)

1. Abjurer
2. Alienist
3. Bladesinger
4. Blood Magus
5. Candle Caster
6. Geomancer
7. Master Transmogrifist
8. Pale Master
9. Ruathar
10. Seeker of the Song
11. Void Disciple
12. Waverider

### Sword and Fist (14 classes)

1. Cavalier
2. Darkwood Stalker
3. Drunken Master
4. Exotic Weapon Master
5. Frenzied Berserker
6. Gladiator
7. Ironguard
8. Kensai
9. Monk of the Enabled Hand
10. Ravager
11. Reaping Mauler
12. Stonelord
13. War Chanter
14. Wildrunner

### Song and Silence (14 classes)

1. Battle Dancer
2. Fochlucan Lyrist
3. Harper Agent
4. Lyric Thaumaturge
5. Master of Masks
6. Metalsmith
7. Nameless One
8. Justiciar
9. Master Specialist
10. Virtuoso
11. Vigilante
12. Fortune's Friend
13. Thief-Acrobat
14. Night Singer

## Save/Load

Use File menu or keyboard shortcuts:

- Ctrl+N - New character
- Ctrl+O - Open/Load character
- Ctrl+S - Save character
- Ctrl+Shift+S - Save As

Characters are stored in JSON for easy sharing.

<!-- Contributing details are below. -->

## License

Free to use for personal D&D games.

## Acknowledgments

- Borrowed README layout from the `Best-README-Template` for structure and clarity.
- Project design follows D&D 3E rules and community conventions.

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/JustinStowe/DnD_CharacterSheet.svg?style=for-the-badge
[contributors-url]: https://github.com/JustinStowe/DnD_CharacterSheet/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JustinStowe/DnD_CharacterSheet.svg?style=for-the-badge
[forks-url]: https://github.com/JustinStowe/DnD_CharacterSheet/network/members
[stars-shield]: https://img.shields.io/github/stars/JustinStowe/DnD_CharacterSheet.svg?style=for-the-badge
[stars-url]: https://github.com/JustinStowe/DnD_CharacterSheet/stargazers
[issues-shield]: https://img.shields.io/github/issues/JustinStowe/DnD_CharacterSheet.svg?style=for-the-badge
[issues-url]: https://github.com/JustinStowe/DnD_CharacterSheet/issues
[license-shield]: https://img.shields.io/github/license/JustinStowe/DnD_CharacterSheet.svg?style=for-the-badge
[license-url]: https://github.com/JustinStowe/DnD_CharacterSheet/blob/development/LICENSE.txt

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. No additional packages need to be installed - uses only Python standard library!

## Usage

### Running from Python

```bash
python character_sheet_gui.py
```

### Creating a Standalone Executable

Want to double-click to run without Python installed? See [BUILD_EXECUTABLE.md](BUILD_EXECUTABLE.md) for detailed instructions.

**Quick method:**

1. Double-click `build_executable.bat` (Windows)
2. Find the executable in the `dist` folder
3. Double-click to run!

### How to Use

#### Main Tab

1. **Class & Multiclass Management**:
   - Display shows all current classes and levels (e.g., "Fighter 5 / Wizard 3 / Duelist 2")
   - **Manage Classes Button**: Opens dialog to manage multiple classes
     - Add base classes or prestige classes to your character
     - **Prestige Class Requirements**: Automatically checks and displays prerequisites
       - Race, alignment, BAB requirements
       - Skill rank requirements
       - Feat and spellcasting requirements
       - Warning if requirements aren't fully met
     - Adjust levels in each class independently
     - Remove classes (must have at least one)
     - View total character level
   - Automatically sets BAB progression, save progressions, hit die, and spellcasting ability
   - **Multiclass BAB & Saves**: Stack correctly according to D&D 3e rules
     - Fighter 5: BAB +5, Fort +4, Ref +1, Will +1
     - Wizard 3: BAB +1, Fort +1, Ref +1, Will +3
     - Duelist 2: BAB +2, Fort +0, Ref +3, Will +0
     - Combined Fighter 5/Wizard 3/Duelist 2: BAB +8, Fort +5, Ref +5, Will +4
2. **Level & Experience**: Track your character's progression
   - XP tracking with next level threshold display
   - **Level Up Button**: Opens dialog to advance your character
     - Choose which class to level (for multiclass characters)
     - Roll or use average for HP gain (based on selected class's hit die)
     - Automatically updates BAB, saves, and grants skill points
     - Preview shows all changes before confirming
3. **Ability Scores**: Enter your ability scores (STR, DEX, CON, INT, WIS, CHA)
   - The modifier is calculated automatically
   - Use "Temp" fields for temporary bonuses/penalties
4. **Saving Throws**: Base saves auto-calculate from class and level
   - For multiclass characters, saves stack from all classes
   - Ability modifiers are added automatically
   - Add misc bonuses from feats, items, etc.
5. **Armor Class**: Enter armor, shield, and other AC bonuses
   - DEX modifier is applied automatically
   - Touch AC and Flat-footed AC are calculated for you
6. **Combat**: Base Attack Bonus auto-calculates from class and level
   - For multiclass characters, BAB stacks from all classes
   - Melee attack (BAB + STR) is calculated automatically
   - Ranged attack (BAB + DEX) is calculated automatically

### Skills Tab

- **Skill Points**: Display shows available unspent skill points
  - First level: (Class skill points + INT mod) × 4
  - Each additional level: Class skill points + INT mod (minimum 1)
  - **Automatic Point Tracking**: When you assign ranks to a skill, points are automatically deducted
  - **Spent Points Display**: Shows total skill points spent
  - **Validation**: Prevents spending more points than available
- Enter ranks in each skill
  - The appropriate ability modifier is added automatically
  - Total skill bonus is always up-to-date
  - Points are deducted from available pool as you allocate them
  - Reducing ranks refunds points back to available pool

### Inventory Tab

- Track all your equipment
  - Add items with weight, quantity, and notes
  - Add containers: check "Is Container" and specify a capacity (lbs)
    - Container items include a combined "Inside / Capacity" column to show the total weight of the contents and the capacity
    - Use the "Manage Contents" dialog to add, edit, or remove items stored inside a container
    - Toggle whether a container's contents count toward the character's carried weight ("Count Contents Toward Carry")
    - Capacity validation prevents adding items that would exceed a container's capacity
  - **Double-click to edit items** - modify name, weight, quantity, or notes
  - Carrying capacity auto-calculates based on STR
  - Color-coded load indicator (Light/Medium/Heavy/Overloaded)
  - Shows encumbrance penalties (Max DEX, Check Penalty, Speed Reduction)

### Spells Tab

- **Spellcasting Ability**: Automatically set based on class
  - Can be manually changed if needed
  - Spell save DCs auto-calculate for each spell level based on correct ability
- **Range Definitions**: Shows calculated spell ranges based on caster level
  - Close: 25 ft + 5 ft/2 levels
  - Medium: 100 ft + 10 ft/level
  - Long: 400 ft + 40 ft/level
  - Updates automatically as character level changes
- **Spell Level Organization**: Spells organized in sub-tabs by spell level
  - Separate tabs for each spell level: 0 (Cantrips), 1st through 9th
  - Easily navigate between spell levels
  - Each tab shows only spells of that level
  - Cleaner organization for characters with many spells
  - **Scrollable interface** for managing large spell lists
- **Automatic Spell Slots Calculation**:
  - Click "Calculate Spell Slots (from Class/Level)" button
  - Automatically sets spell slots per day based on:
    - Your class (Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Wizard)
    - Your character level
    - Base spells per day from class progression table
    - Bonus spells based on spellcasting ability modifier
  - Example: Level 5 Cleric with WIS 16 (+3)
    - 1st level: 3 base + 1 bonus = 4 total
    - 2nd level: 2 base + 1 bonus = 3 total
    - 3rd level: 1 base + 1 bonus = 2 total
- Track spell slots (max, used, remaining) for levels 0-9
- **Add Spells**: Enter complete spell information
  - Name, level, school, casting time, range, duration, components
  - **Description field** for full spell text and notes
  - Mark spells as prepared (for prepared casters like Clerics and Wizards)
- **Spell List Display**: Shows all important spell information
  - Columns: Name, School, Casting Time, Range, Duration, Components, Prepared, Cast
  - Sorted alphabetically within each spell level
- **Cast Spell Button**: Each spell has a [Cast] button for quick casting
  - Click to automatically use one spell slot of that level
  - Shows confirmation with spell name and remaining slots
  - Warns if no spell slots remaining for that level
  - Integrates with spell slot tracking system
- **Detailed Spell View**: Double-click any spell to view/edit full details
  - Opens dialog with all spell information
  - Edit any field including the full description
  - Scrollable description area for long spell text
  - Change spell level, toggle prepared status
  - Save changes or cancel
- Long Rest button to reset used spell slots

#### Feats & Abilities Tab

- **Feats Section**: Add feats with name, type, prerequisites, and benefit
  - Types: General, Metamagic, Item Creation, Combat, Skill, Special
  - Full text descriptions for benefits
- **Epic Feats Button** (Level 21+): Access epic feats for epic level characters
  - **Epic Feat Selection**: Choose from 53 epic feats
    - Epic Prowess (+1 to all attacks)
    - Epic Toughness (+30 HP, can take multiple times)
    - Epic Weapon Focus/Specialization (enhanced weapon bonuses)
    - Great Strength/Dexterity/etc. (+1 to ability scores)
    - Epic Spellcasting (cast epic spells)
    - Improved Combat Reflexes, Epic Dodge, and many more!
  - **Feat Progression**: Gain epic feats at 21st level, then every 2 levels (23, 25, 27...)
  - **Full Descriptions**: Each epic feat shows prerequisites, benefits, and special notes
  - **Prerequisite Validation**: System checks BAB, ability scores, and other requirements
  - **Multiple Selection**: Some epic feats can be taken multiple times (e.g., Epic Toughness, Great Strength)
  - **Epic Level Info**: Shows current epic level, feats available, and next milestone levels
  - Button only available when character reaches level 21 (epic level)
- **Special Abilities Section**: Track class features, racial abilities, etc.
  - Track uses per day (or mark as at-will with 0)
  - Use ability button to decrement remaining uses
  - Long Rest button to restore all daily abilities

### Magic Items Tab

- **Create Magic Items**: Powerful dialog-based item creation system
  - **Create New Item Button**: Opens comprehensive magic item creation dialog
  - **Basic Information**: Name, type, slot, caster level, and charge tracking
  - **Abilities**: Items can define multiple named abilities (name, cost, description) that consume charges when used
  - **Stat Bonuses System**: Add multiple bonuses that affect character stats when equipped
    - **Bonus Types Available**:
      - **Armor Class**: Armor, Shield, Natural Armor, Deflection
      - **Saving Throws**: Resistance (All Saves), Fort Save, Ref Save, Will Save
      - **Combat**: Attack Bonus, Damage Bonus
      - **Ability Scores**: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
      - **Other**: Spell Resistance, Initiative, Skill Bonus (All), Speed Bonus
    - Add unlimited bonuses to a single item
    - Each bonus has a type and value (can be negative for penalties)
    - Example: Vest of the Archmagi with Armor +8, Resistance +5, Spell Resistance +2
  - **Special Properties**: Text field for abilities like "Recall up to lvl 9 spell (3/day)"
  - **Description**: Full item description and lore
- **Equipment System**:
  - **Equipped Status**: Click the "Equipped" column (shows ✓) to toggle equipment
  - **Automatic Stat Application**: When equipped, bonuses immediately apply to character
    - Armor bonus: Added to AC
    - Resistance bonus: Added to all three saves (Fort, Ref, Will)
    - Individual save bonuses: Added to specific saves
    - Shield/Natural Armor/Deflection: Added to appropriate AC components
    - All other bonuses: Applied to relevant stats
  - **Bonus Stacking Rules**: D&D 3e standard - bonuses of same type don't stack (highest applies)
  - **Real-Time Updates**: Character stats recalculate instantly when toggling equipment
- **Magic Item Display**:
  - Tree view shows: Equipped status, Name, Type, Slot, Bonus summary, Charges, Properties
  - Bonus column shows first 3 bonuses (e.g., "Armor +8, Resistance +5, Spell Resistance +2")
  - **Double-click item**: Opens detailed view with complete information
    - All bonuses listed in blue
    - Full properties and description with scrolling
    - Current equipped status
- **Charge Management**:
  - Set max charges when creating item
  - Use Charge (-1) button to decrement charges
  - If the item has multiple abilities, the UI asks which ability to use and decrements charges by that ability's cost
  - Recharge button to restore to maximum
  - Displays current/max charges (only shows if item has charges)
- **Item Management**:
  - Remove Selected button to delete items
  - Items persist when saving/loading character
  - Equipment bonuses automatically reapply when loading character

**Example Magic Item Creation**:

Creating "Vest of the Archmagi":

1. Click "Create New Item"
2. Name: "Vest of the Archmagi", Type: "armor", Slot: "Body"
3. Add bonuses:
   - Armor: +8
   - Resistance (All Saves): +5
   - Overcome Spell Resistance: +2
4. Properties: "Recall up to lvl 9 spell (3/day)\nExpend spell slot: Heal (5 x spell lvl)"
5. Click "Create Item"
6. Click the Equipped column to equip it
7. Character immediately gains: +8 AC, +5 to all saves, +2 spell penetration

### Weapons (Main Tab)

- **Comprehensive Weapon Tracking**: Located in Combat section of Main tab
  - **Basic Stats**: Name, Type (Melee/Ranged), Damage dice, Critical range/multiplier
  - **Physical Properties**: Size (Fine to Colossal), Weight, Range
  - **Damage Type**: Slashing, Piercing, Bludgeoning, or combinations (S/P, P/B, etc.)
  - **Bonuses**: Enhancement bonus (+1, +2, etc.), Misc attack/damage modifiers
  - **Notes**: Special properties, abilities, or restrictions
- **Auto-Calculated Attack & Damage**:
  - Melee weapons: BAB + STR modifier + enhancement + misc bonuses
  - Ranged weapons: BAB + DEX modifier + enhancement + misc bonuses
  - Damage display includes ability modifiers (STR for melee) and all bonuses
  - Updates automatically when ability scores or BAB changes
- **Weapon Display**: Shows all weapons with complete statistics at a glance

### Save/Load

Use File menu or keyboard shortcuts:

- **Ctrl+N** - New character
- **Ctrl+O** - Open/Load character
- **Ctrl+S** - Save character
- **Ctrl+Shift+S** - Save As
- Characters saved as JSON files for easy sharing

### Example

#### Class and Leveling Example

Create a new Fighter:

1. Select "Fighter" from the class dropdown
   - BAB automatically set to +1 (full progression)
   - Fort save set to +2 (good), Ref/Will set to +0 (poor)
   - Spellcasting ability: None
   - Hit die: d10
2. Click "Level Up" button at level 1 to advance to level 2
   - Roll d10 for HP (or use average: 6)
   - CON modifier added automatically
   - BAB increases to +2
   - Fort increases to +3
   - Skill points granted based on Fighter class (2) + INT modifier

Switch to Wizard:

1. Change class dropdown to "Wizard"
   - BAB recalculates to +0 (poor progression)
   - Fort/Ref set to +0 (poor), Will set to +2 (good)
   - Spellcasting ability automatically changes to Intelligence
   - All spell DCs now use INT modifier instead of WIS/CHA

#### Ability Score Example

If you set your Wisdom to 14:

- WIS modifier automatically shows +2
- Will save automatically updates (base + 2 + misc)
- All Wisdom-based skills (Heal, Listen, Sense Motive, Spot, Survival) update
- If you're a Cleric, all spell DCs update to use WIS modifier

If you increase Wisdom to 16:

- WIS modifier changes to +3
- Will save increases by 1
- All Wisdom-based skills increase by 1
- Cleric spell DCs increase by 1

#### Inventory Example

If you have STR 14 (carrying capacity: Light 58 lbs, Medium 116 lbs, Heavy 175 lbs):

- Add a longsword (4 lbs), chain shirt (25 lbs), backpack with gear (20 lbs)
- Total weight: 49 lbs - shows "Light" load (green)
- No encumbrance penalties

If you increase to STR 16:

- Light load capacity increases to 76 lbs
- Medium load to 153 lbs
- Heavy load to 230 lbs
- Your existing 49 lbs is still a light load

#### Skills Example

**Automatic Skill Point Tracking:**

Create a Level 1 Rogue with INT 14 (+2):

1. Rogue class grants 8 skill points per level
2. At 1st level: (8 + 2) × 4 = 40 skill points available
3. Assign ranks to skills:
   - Add 4 ranks to Hide → Points available: 40 - 4 = 36
   - Add 4 ranks to Move Silently → Points available: 36 - 4 = 32
   - Add 4 ranks to Search → Points available: 32 - 4 = 28
   - Try to add 30 ranks to Disable Device → Warning! Only 28 points available
4. Spent display shows: 12 points spent, 28 available

**Modifying Ranks:**

- Reduce Hide from 4 to 3 ranks → Points refunded: 28 + 1 = 29 available
- Increase Search from 4 to 5 ranks → Points deducted: 29 - 1 = 28 available
- All totals update automatically based on ability modifiers

**Level Up:**

- Click "Level Up" to advance to level 2
- Gain 8 + 2 = 10 more skill points
- Points available: 28 + 10 = 38 available
- Can now distribute more ranks (max rank = level + 3 = 5 for class skills)

#### Spellcasting Example

**Spell Slots Calculation:**

Create a Level 5 Wizard with INT 18 (+4):

1. Select "Wizard" class → spellcasting ability auto-set to Intelligence
2. Set level to 5 and INT to 18
3. Click "Calculate Spell Slots (from Class/Level)" button
4. Spell slots automatically calculated:
   - 0-level (cantrips): 4 (no bonus for cantrips)
   - 1st level: 3 base + 1 bonus = 4 total
   - 2nd level: 2 base + 1 bonus = 3 total
   - 3rd level: 1 base + 1 bonus = 2 total
5. Spell DCs auto-update:
   - 1st level DC = 15 (10 + 1 + 4)
   - 2nd level DC = 16 (10 + 2 + 4)
   - 3rd level DC = 17 (10 + 3 + 4)

**Different Casters:**

Create a Level 4 Sorcerer with CHA 17 (+3):

- Class automatically sets spellcasting ability to Charisma
- Click "Calculate Spell Slots" → automatically sets:
  - 0-level: 6 cantrips (Sorcerers get more)
  - 1st level: 6 spells per day
  - 2nd level: 3 base + 1 bonus = 4 total
- Spell DCs: 1st = 14, 2nd = 15

Create a Level 3 Cleric with WIS 16 (+3):

- Class automatically sets spellcasting ability to Wisdom
- Click "Calculate Spell Slots" → automatically sets:
  - 0-level: 4 orisons
  - 1st level: 2 base + 1 bonus = 3 total
  - 2nd level: 1 base + 1 bonus = 2 total
- Add "Cure Light Wounds" and "Bless", mark as prepared
- Clerics prepare spells, so check "Prepared" for spells you want ready
- Spell DCs: 1st = 14, 2nd = 15

Create a Cleric with WIS 16:

- Class automatically sets spellcasting ability to Wisdom
- 1st level spell DC = 14 (10 + 1 + 3)
- Add "Cure Light Wounds" and "Bless", mark as prepared
- Set 1st level slots to 3, track usage as you cast

## File Structure

- `character_sheet_gui.py` - Main GUI application
- `character.py` - Character data model with class definitions and calculations
- `sample_character.json` - Example Fighter character (level 5 Dwarf)
- `wizard_sample.json` - Example Wizard character (level 5 Elf, INT-based caster)
- `cleric_sample.json` - Example Cleric character (level 3 Human, WIS-based caster)
- `sorcerer_sample.json` - Example Sorcerer character (level 4 Half-Elf, CHA-based caster)
- `README.md` - This file

## Developer Notes & Project Structure

- The `Character` model has been refactored to delegate behavior to per-concern managers in `character_parts/` (e.g., `equipment.py`, `feats.py`, `spells.py`, `ac.py`, `saves.py`, `leveling.py`). This helps keep the code modular and easier to maintain.
- UI and dialogs live in `gui_tabs/` and `dialogs/` respectively. New features such as the `Manage Contents` dialog and the `MagicItemDialog` ability editor are implemented in these directories.
- Inventory containers are represented by the following fields on an inventory item: `is_container`, `capacity_lbs`, `count_contents_toward_carry`, and `contents` (a list of item dicts). Magic items store an `abilities` list on each item where every ability contains `name`, `cost`, and `description` keys.
  - Programmatic helper methods: `add_content_to_container(container_item, content_item)`, `edit_content_in_container(container_item, index, new_content)`, and `remove_content_from_container(container_item, index)` are implemented to help manipulate container contents.

## Testing

- The repository uses `pytest` and includes both unit and GUI tests in `testing_suite/`.
- GUI tests use a `dummy_gui` fixture that patches tkinter when running in headless CI environments. The fixture is defined in `testing_suite/conftest.py` and provides predictable UI objects and a `DummyCharacter` for fast, deterministic tests.
- Run the full test suite with:

```bash
python -m pytest -q
```

If you want to run only the unit tests (excluding GUI/UI test markers), use `-k` to filter test names or paths.

## Supported Classes

All 11 D&D 3e core classes are supported with accurate progressions:

| Class     | Hit Die | BAB    | Fort | Ref  | Will | Skill Points | Spellcasting |
| --------- | ------- | ------ | ---- | ---- | ---- | ------------ | ------------ |
| Fighter   | d10     | Full   | Good | Poor | Poor | 2 + INT      | None         |
| Barbarian | d12     | Full   | Good | Poor | Poor | 4 + INT      | None         |
| Ranger    | d8      | Full   | Good | Good | Poor | 6 + INT      | Wisdom       |
| Paladin   | d10     | Full   | Good | Poor | Poor | 2 + INT      | Wisdom       |
| Cleric    | d8      | Medium | Good | Poor | Good | 2 + INT      | Wisdom       |
| Druid     | d8      | Medium | Good | Poor | Good | 4 + INT      | Wisdom       |
| Monk      | d8      | Medium | Good | Good | Good | 4 + INT      | None         |
| Rogue     | d6      | Medium | Poor | Good | Poor | 8 + INT      | None         |
| Bard      | d6      | Medium | Poor | Good | Good | 6 + INT      | Charisma     |
| Wizard    | d4      | Poor   | Poor | Poor | Good | 2 + INT      | Intelligence |
| Sorcerer  | d4      | Poor   | Poor | Poor | Good | 2 + INT      | Charisma     |

**BAB Progressions:**

- Full: BAB = Level (e.g., Level 5 = +5 BAB)
- Medium: BAB = Level × 3/4 (e.g., Level 5 = +3 BAB)
- Poor: BAB = Level / 2 (e.g., Level 5 = +2 BAB)

**Save Progressions:**

- Good: 2 + Level/2 (e.g., Level 5 = +4)
- Poor: Level/3 (e.g., Level 5 = +1)

## D&D 3e Rules Implemented

- **Character Advancement**: Level-up system with HP rolling, automatic BAB/save increases, skill point grants
- **Class Progressions**: Accurate BAB and saving throw progressions for all 11 core classes
- **Spell Progression Tables**: Complete spells per day tables for all spellcasting classes
  - Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Wizard
  - Automatic calculation based on class and level
- **Bonus Spells**: Automatically calculated based on spellcasting ability modifier
  - Formula: 1 + ((modifier - spell_level) / 4) for each spell level
  - Requires ability score of at least 10 + spell level to cast
  - Example: WIS 16 (+3) grants +1 bonus 1st & 2nd level spell
- Ability modifier calculation: (Score - 10) / 2
- Saving throws: Base + Ability Mod + Misc
- AC: 10 + Armor + Shield + DEX + Natural + Deflection + Misc
- Touch AC: 10 + DEX + Deflection + Misc
- Flat-footed AC: 10 + Armor + Shield + Natural + Deflection + Misc
- Skills: Ranks + Ability Mod + Misc
- **Skill Points**: (Class base + INT mod) × 4 at 1st level, (Class base + INT mod) per level thereafter
- Attack bonuses: BAB + Ability Mod (STR for melee, DEX for ranged)
- Initiative: DEX mod + Misc
- **Carrying Capacity**: Based on D&D 3e carrying capacity table
  - Light Load: up to STR-based limit (no penalties)
  - Medium Load: up to 2x light load (Max DEX +3, -3 check penalty, -10 ft speed)
  - Heavy Load: up to 3x light load (Max DEX +1, -6 check penalty, -10 ft speed)
  - Overloaded: Cannot move
- **Encumbrance Penalties**: Automatically applied based on current weight vs capacity
- **Spell Save DC**: 10 + Spell Level + Spellcasting Ability Modifier
- **Spell Slots**: Track max slots, used slots, and remaining slots for each spell level (0-9)
- **Multiclass BAB**: Sum of BAB from all classes based on their progressions
  - Full BAB (Fighter, Barbarian, Paladin, Ranger): Level × 1
  - Medium BAB (Cleric, Druid, Monk, Rogue): Level × 0.75
  - Poor BAB (Wizard, Sorcerer, Bard): Level × 0.5
  - Example: Fighter 5 (BAB +5) / Rogue 3 (BAB +2) = Total BAB +7
- **Multiclass Saves**: Sum of base saves from all classes based on their progressions
  - Good save: 2 + (Level × 0.5)
  - Poor save: 0 + (Level × 0.33)
  - Example: Cleric 4 (Fort +4, Ref +1, Will +4) / Fighter 2 (Fort +3, Ref +0, Will +0) = Fort +7, Ref +1, Will +4

## Multiclass Examples

### Fighter 5 / Wizard 3 (Eldritch Knight concept)

- **Total Level**: 8
- **BAB**: +6 (Fighter: +5, Wizard: +1)
- **Saves**: Fort +5 (Fighter: +4, Wizard: +1), Ref +2 (Fighter: +1, Wizard: +1), Will +4 (Fighter: +1, Wizard: +3)
- **HP**: Fighter d10 × 5 + Wizard d4 × 3 + CON mod × 8
- **Skills**: Fighter 2/level × 5 + Wizard 2/level × 3 (plus INT mod)

### Ranger 7 / Druid 2 (Nature specialist)

- **Total Level**: 9
- **BAB**: +8 (Both full BAB: Ranger +7, Druid +1)
- **Saves**: Fort +9 (Ranger: +5, Druid: +4), Ref +5 (Ranger: +5, Druid: +0), Will +4 (Ranger: +2, Druid: +2)
- **Spellcasting**: Both classes grant spells (WIS-based)

### Rogue 3 / Fighter 2 / Monk 1 (Jack of all trades)

- **Total Level**: 6
- **BAB**: +4 (Fighter: +2, Rogue: +2, Monk: +0)
- **Saves**: Fort +4 (Fighter: +3, Rogue: +1, Monk: +0), Ref +6 (Fighter: +0, Rogue: +3, Monk: +3), Will +2 (Fighter: +0, Rogue: +1, Monk: +1)
- **Special**: Mix of Fighter feats, Rogue sneak attack, and Monk abilities

## Prestige Class Examples

### Fighter 7 / Duelist 3 (Master Fencer)

- **Total Level**: 10
- **BAB**: +10 (Both full BAB: Fighter +7, Duelist +3)
- **Saves**: Fort +6 (Fighter: +5, Duelist: +1), Ref +5 (Fighter: +2, Duelist: +3), Will +3 (Fighter: +2, Duelist: +1)
- **Requirements Met**: BAB +6, Dodge, Mobility, Weapon Finesse, Perform 3 ranks, Tumble 5 ranks
- **HP**: Fighter d10 × 7 + Duelist d10 × 3 + CON mod × 10

### Wizard 5 / Fighter 2 / Eldritch Knight 3 (Battlemage)

- **Total Level**: 10
- **BAB**: +7 (Fighter: +2, Wizard: +2, Eldritch Knight: +3)
- **Saves**: Fort +7 (Fighter: +3, Wizard: +1, Eldritch Knight: +3), Ref +3, Will +7
- **Requirements Met**: Martial weapon proficiency, 3rd-level arcane spells
- **Spellcasting**: Continues as Wizard (advances with Eldritch Knight levels)

### Rogue 5 / Wizard 3 / Arcane Trickster 2 (Sneaky Mage)

- **Total Level**: 10
- **BAB**: +5 (Rogue: +3, Wizard: +1, Arcane Trickster: +1)
- **Saves**: Fort +3, Ref +10 (Rogue: +4, Wizard: +1, Arcane Trickster: +3), Will +6
- **Requirements Met**: Nonlawful alignment, sneak attack +2d6, mage hand, 3rd-level arcane spells
- **Special**: Combines sneak attack with spellcasting, ranged legerdemain

### Cleric 3 / Wizard 3 / Mystic Theurge 4 (Divine & Arcane Master)

- **Total Level**: 10
- **BAB**: +5 (Cleric: +2, Wizard: +1, Mystic Theurge: +2)
- **Saves**: Fort +6, Ref +3, Will +13 (All good progressions)
- **Requirements Met**: Knowledge (arcana) 6, Knowledge (religion) 6, 2nd-level divine & arcane spells
- **Spellcasting**: Advances BOTH divine and arcane casting with Mystic Theurge levels

## Available Prestige Classes

### Core DMG (12 classes)

1. **Arcane Archer**: Elf/half-elf archer-mage (requires BAB +6, arcane spells)
2. **Arcane Trickster**: Rogue-wizard hybrid (requires sneak attack, 3rd-level arcane)
3. **Assassin**: Evil death dealer (requires evil alignment, Hide 8, Move Silently 8)
4. **Blackguard**: Dark warrior (requires evil alignment, BAB +6, evil outsider contact)
5. **Dragon Disciple**: Sorcerer with dragon powers (requires sorcerer 5+)
6. **Duelist**: Finesse fighter (requires BAB +6, Dodge, Mobility, Weapon Finesse)
7. **Dwarven Defender**: Defensive dwarf warrior (requires dwarf, lawful, BAB +7)
8. **Eldritch Knight**: Warrior-mage (requires martial weapons, 3rd-level arcane)
9. **Horizon Walker**: Terrain master (requires Knowledge (geography) 8)
10. **Loremaster**: Knowledge seeker (requires 10 ranks in 3 Knowledge skills, metamagic feats)
11. **Mystic Theurge**: Dual caster (requires 2nd-level divine AND arcane spells)
12. **Shadowdancer**: Shadow manipulator (requires Hide 10, Move Silently 8, Perform (dance) 5)

### Magic of Faerûn (19 classes)

13. **Harper Scout**: Secret agent for balance
14. **Spellsword**: Weapon-channeling spellcaster
15. **Red Wizard**: Thayan school specialist
16. **Guild Thief**: Professional criminal network member
17. **Shadow Adept**: Shadow Weave spellcaster
18. **Arcane Devotee**: Divine caster of magic deities
19. **Divine Champion**: Deity's chosen warrior
20. **Divine Disciple**: Faith-empowered cleric
21. **Harper Priest**: Divine Harper agent
22. **Runecaster**: Dwarven rune priest
23. **Silverstar**: Selûne's holy warrior
24. **Hospitaler**: Divine healer
25. **Incantatrix**: Female metamagic specialist
26. **Acolyte of the Ego**: Psionic self-enhancer
27. **Acolyte of the Skin**: Demon-skin warrior
28. **Shaaryan Hunter**: Grasslands tracker
29. **Monk of the Long Death**: Death-studying monk
30. **Zhentarim Soldier**: Elite mercenary
31. **Zhentarim Spy**: Covert intelligence agent

### Tome and Blood (12 classes)

32. **Abjurer**: Protective magic specialist
33. **Alienist**: Far Realm summoner
34. **Bladesinger**: Elven warrior-mage
35. **Blood Magus**: Life-force powered caster
36. **Candle Caster**: Magical candle crafter
37. **Geomancer**: Terrain-based divine caster
38. **Master Transmogrifist**: Shapeshifting master
39. **Pale Master**: Undeath-embracing necromancer
40. **Ruathar**: Elven divine cavalry
41. **Seeker of the Song**: Primal song mage
42. **Void Disciple**: Oblivion priest
43. **Waverider**: Water magic sailor

### Sword and Fist (14 classes)

44. **Cavalier**: Elite mounted warrior
45. **Darkwood Stalker**: Elven forest defender
46. **Drunken Master**: Unpredictable monk
47. **Exotic Weapon Master**: Exotic weapon specialist
48. **Frenzied Berserker**: Supernatural rage warrior
49. **Gladiator**: Arena combatant
50. **Ironguard**: Dwarven tough defender
51. **Kensai**: Single-weapon master
52. **Monk of the Enabled Hand**: Healing monk
53. **Ravager**: Destructive barbarian
54. **Reaping Mauler**: Grappling specialist
55. **Stonelord**: Earth-bonded dwarf warrior
56. **War Chanter**: Battlefield song leader
57. **Wildrunner**: Tireless elven runner

### Song and Silence (14 classes)

58. **Battle Dancer**: Combat dancing bard
59. **Fochlucan Lyrist**: Druid-bard hybrid
60. **Harper Agent**: Elite secret agent
61. **Lyric Thaumaturge**: Music-spell combiner
62. **Master of Masks**: Magical disguise master
63. **Metalsmith**: Superior craftsmaster
64. **Nameless One**: Identity-erased rogue
65. **Justiciar**: Lawful enforcer
66. **Master Specialist**: Ultimate school wizard
67. **Virtuoso**: Multi-performance master
68. **Vigilante**: Urban justice warrior
69. **Fortune's Friend**: Luck-blessed rogue
70. **Thief-Acrobat**: Athletic rogue

**Total: 70 prestige classes from 5 sourcebooks**

## License

Free to use for personal D&D games!

## Future Enhancements

Possible additions:

- Multiple characters (character manager)
- Character advancement/leveling improvements
- Export to PDF
- Character portrait/image support
- Dice roller integration
- Combat tracker

## Contributing

Thanks for considering contributing! Below are guidelines and conventions to help contributors get set up and make high-quality changes.

### Branches & Workflow

- Create a feature branch off `development` following the format `feature/<short-description>` or `fix/<short-description>`.
- Keep changes logically grouped and create one PR per set of related changes.
- Write commit messages that explain the intent and include the related ticket/issue number if you have one.

### Code Layout & Manager Pattern

- The `Character` model delegates domain-specific logic to manager modules in `character_parts/`. Each manager should live in a module named after its concern and provide a concise public API. Examples:
  - `character_parts/equipment.py` → `EquipmentManager`
  - `character_parts/spells.py` → `SpellManager`
  - `character_parts/feats.py` → `FeatManager`
- When adding a new manager:
  - Create a file in `character_parts/` that contains the manager class and unit tests that exercise the manager's logic.
  - Update `character.py` to instantiate and delegate to the manager (preserve the public `Character` API where practical).
  - Keep logic inside a manager that is cohesive and limited to a single concern.

### UI: Tabs & Dialogs

- UI code lives in `gui_tabs/` and dialogs in `dialogs/`.
- Dialogs should be implemented as classes using `tk.Toplevel` or a consistent dialog base, avoid tight coupling to the root and prefer dependency injection for testability.
- For new UI changes:
  - Create or modify a tab under `gui_tabs/` and the dialog in `dialogs/`.
  - Add unit tests to `testing_suite/` that exercise logic where possible and UI tests that use the `dummy_gui` fixture for headless validation.

### Tests

- Run unit and UI tests using `pytest`:

```bash
python -m pytest -q
```

- The test suite includes `testing_suite/conftest.py`, which provides a `dummy_gui` fixture used to run GUI tests headlessly in CI environments.
- Add unit tests for new manager logic under `testing_suite/` and UI tests that exercise key flows for tabs and dialogs.
- Aim for a good mix of unit and integration tests: use unit tests for logic in managers and integration/UI tests for dialog + tab behavior.

### Style & Quality

- The project targets Python 3.14; use modern Python constructs (type hints, f-strings, dataclasses where appropriate).
- Keep code modular and testable; avoid large monolithic functions or classes.
- When updating existing behavior, add tests to prevent regressions.

### Release & Changelog

- If your change affects user-visible behavior, add an entry to `CHANGELOG.md` (create one if it doesn't exist) describing the change and the rationale.

### PR Checklist

- Include tests for new functionality or bug fixes.
- Update the README if adding a user-facing feature.
- Ensure CI passes before marking PR as ready for review.
