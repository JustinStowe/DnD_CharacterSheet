# D&D 3rd Edition Character Sheet

An interactive character sheet application for Dungeons & Dragons 3rd Edition that automatically updates all derived statistics when you change base values.

## Features

- **Class-based character system**: Choose from 11 D&D 3e core classes with automatic stat adjustments
  - Fighter, Barbarian, Ranger, Paladin (martial classes)
  - Cleric, Druid (Wisdom-based casters)
  - Wizard (Intelligence-based caster)
  - Sorcerer, Bard (Charisma-based casters)
  - Monk, Rogue (skill specialists)
- **Character advancement**: Level up with automatic BAB, save, HP, and skill point calculations
- **Auto-calculating stats**: Change your stat score and watch your saves update automatically
- **Complete character tracking**:
  - All six ability scores (STR, DEX, CON, INT, WIS, CHA)
  - Saving throws (Fortitude, Reflex, Will) - auto-calculated from class
  - Base Attack Bonus - auto-calculated from class and level
  - Armor Class (including touch and flat-footed)
  - Combat stats (Initiative, Attack bonuses)
  - All D&D 3e skills with proper ability modifiers
  - **Automatic skill point tracking** - points deducted as you allocate ranks
  - Experience points and level tracking
  - **Weapon statistics** - complete D&D 3e weapon details with auto-calculated attack/damage
  - **Inventory tracking with weight and carrying capacity**
  - **Spell tracking with spell slots and prepared spells**
  - **Magic item tracking** - slots, properties, and charge management
  - **Feat and special ability tracking**
- **Spellcasting support**: Automatic spellcasting ability assignment based on class
  - Clerics, Druids, Paladins, Rangers use Wisdom
  - Wizards use Intelligence
  - Sorcerers and Bards use Charisma
  - Spell DCs calculated automatically from the correct ability
- **Temporary modifiers**: Track temporary ability score changes
- **Encumbrance system**: Automatic carrying capacity calculations based on Strength
- **Feats & Abilities**: Track feats, racial abilities, class features, and daily use abilities
- **Save/Load characters**: Save your character to a file and load it later
- **Easy-to-use GUI**: Clean tabbed interface built with tkinter

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

1. **Class Selection**: Choose your character class from the dropdown menu
   - Automatically sets BAB progression, save progressions, hit die, and spellcasting ability
   - Changes to class immediately update BAB and base saves
2. **Level & Experience**: Track your character's progression
   - XP tracking with next level threshold display
   - **Level Up Button**: Opens dialog to advance your character
     - Roll or use average for HP gain
     - Automatically updates BAB, saves, and grants skill points
     - Preview shows all changes before confirming
3. **Ability Scores**: Enter your ability scores (STR, DEX, CON, INT, WIS, CHA)
   - The modifier is calculated automatically
   - Use "Temp" fields for temporary bonuses/penalties
4. **Saving Throws**: Base saves auto-calculate from class and level
   - Ability modifiers are added automatically
   - Add misc bonuses from feats, items, etc.
5. **Armor Class**: Enter armor, shield, and other AC bonuses
   - DEX modifier is applied automatically
   - Touch AC and Flat-footed AC are calculated for you
6. **Combat**: Base Attack Bonus auto-calculates from class and level
   - Melee attack (BAB + STR) is calculated automatically
   - Ranged attack (BAB + DEX) is calculated automatically

#### Skills Tab

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

#### Inventory Tab

- Track all your equipment
  - Add items with weight and quantity
  - Carrying capacity auto-calculates based on STR
  - Color-coded load indicator (Light/Medium/Heavy/Overloaded)
  - Shows encumbrance penalties (Max DEX, Check Penalty, Speed Reduction)

#### Spells Tab

- **Spellcasting Ability**: Automatically set based on class
  - Can be manually changed if needed
  - Spell save DCs auto-calculate for each spell level based on correct ability
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
- Add spells with full details (school, range, duration, components, etc.)
- Mark spells as prepared (for prepared casters like Clerics and Wizards)
- Filter spell list by level
- Long Rest button to reset used spell slots
- Double-click a spell to toggle prepared status

#### Feats & Abilities Tab

- **Feats Section**: Add feats with name, type, prerequisites, and benefit
  - Types: General, Metamagic, Item Creation, Combat, Skill, Special
  - Full text descriptions for benefits
- **Special Abilities Section**: Track class features, racial abilities, etc.
  - Track uses per day (or mark as at-will with 0)
  - Use ability button to decrement remaining uses
  - Long Rest button to restore all daily abilities

#### Magic Items Tab

- **Add Magic Items**: Track all magical equipment
  - Item name, type (Weapon, Armor, Ring, Wondrous Item, Potion, Scroll, Wand, Rod, Staff, etc.)
  - Slot assignment (Head, Eyes, Neck, Shoulders, Body, Arms, Hands, Ring, Waist, Feet, or None)
  - Caster level for determining spell effects
  - Properties and full description
  - Charge tracking for items with limited uses (wands, potions, etc.)
- **Charge Management**:
  - Use Charge button to decrement charges
  - Recharge button to restore to maximum
  - Displays current/max charges for each item
- Remove items from inventory as needed

#### Weapons (Main Tab)

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

#### Save/Load

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

## License

Free to use for personal D&D games!

## Future Enhancements

Possible additions:

- Multiple characters (character manager)
- Character advancement/leveling
- Export to PDF
- Character portrait/image support
- Dice roller integration
- Combat tracker
