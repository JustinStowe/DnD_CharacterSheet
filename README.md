# D&D 3rd Edition Character Sheet

An interactive character sheet application for Dungeons & Dragons 3rd Edition that automatically updates all derived statistics when you change base values. Includes **full Epic Level Handbook support** for characters level 21+!

## Features

- **Class-based character system**: Choose from 11 D&D 3e core classes with automatic stat adjustments
  - Fighter, Barbarian, Ranger, Paladin (martial classes)
  - Cleric, Druid (Wisdom-based casters)
  - Wizard (Intelligence-based caster)
  - Sorcerer, Bard (Charisma-based casters)
  - Monk, Rogue (skill specialists)
- **Prestige class support**: 70 prestige classes with automatic requirement checking
  - 11 Core DMG prestige classes: Arcane Archer, Arcane Trickster, Assassin, Blackguard, Dragon Disciple, Duelist, Dwarven Defender, Eldritch Knight, Horizon Walker, Loremaster, Mystic Theurge, Shadowdancer
  - 19 Magic of Faerûn prestige classes: Harper Scout, Spellsword, Red Wizard, Guild Thief, Shadow Adept, and 14 more!
  - 12 Tome and Blood prestige classes: Bladesinger, Pale Master, Alienist, Blood Magus, Geomancer, and 7 more!
  - 14 Sword and Fist prestige classes: Cavalier, Kensai, Drunken Master, Frenzied Berserker, and 10 more!
  - 14 Song and Silence prestige classes: Battle Dancer, Master of Masks, Lyric Thaumaturge, Thief-Acrobat, and 10 more!
  - Requirements displayed when adding prestige classes
  - Validates race, alignment, BAB, skills, and other prerequisites
  - Full integration with multiclass system
- **Epic Level Handbook support** (Level 21+): Full implementation of epic level rules
  - **Epic BAB and Saves**: Continues progression beyond 20th level
    - Full BAB: +1 per level
    - Medium BAB: +1 every 2 levels
    - Poor BAB: +1 every 2 levels
    - Good saves: +1 every 2 levels
    - Poor saves: +1 every 3 levels
  - **Epic Feats**: Gain epic feats at 21st level, then every 2 levels
    - 53 epic feats defined with full prerequisites
    - Epic Prowess, Epic Toughness, Epic Weapon Focus/Specialization
    - Great Ability Score increases (Strength, Dexterity, etc.)
    - Epic Spellcasting, Improved Combat Reflexes, and more
    - Epic feat selection dialog with descriptions
  - **Epic Ability Increases**: +1 to any ability score every 4 levels (24, 28, 32...)
  - **Epic XP Progression**: Proper XP requirements for epic levels
  - **Works with multiclass**: All epic progressions work with multiclass characters
- **Multiclass support**: Take levels in multiple classes with proper D&D 3e stacking rules
  - BAB stacks from all classes based on their progressions (including epic levels)
  - Saving throws stack from all classes based on their progressions (including epic levels)
  - Track individual class levels separately
  - Choose which class to level when gaining levels
  - Mix base classes, prestige classes, and epic levels freely
- **Character advancement**: Level up with automatic BAB, save, HP, and skill point calculations
  - Level up dialog shows epic feat and ability increase notifications
  - Automatic detection when reaching epic level (21+)
- **Auto-calculating stats**: Change your stat score and watch your saves update automatically
- **Complete character tracking**:
  - All six ability scores (STR, DEX, CON, INT, WIS, CHA)
  - Saving throws (Fortitude, Reflex, Will) - auto-calculated from class (including epic bonuses)
  - Base Attack Bonus - auto-calculated from class and level
  - Armor Class (including touch and flat-footed)
  - Combat stats (Initiative, Attack bonuses)
  - All D&D 3e skills with proper ability modifiers
  - **Automatic skill point tracking** - points deducted as you allocate ranks
  - Experience points and level tracking
  - **Weapon statistics** - complete D&D 3e weapon details with auto-calculated attack/damage
  - **Inventory tracking with weight and carrying capacity**
  - **Spell tracking with spell slots and prepared spells**
  - **Magic item tracking with equipment bonuses** - create items with stat bonuses that automatically apply when equipped
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

#### Magic Items Tab

- **Create Magic Items**: Powerful dialog-based item creation system
  - **Create New Item Button**: Opens comprehensive magic item creation dialog
  - **Basic Information**: Name, type, slot, caster level, and charge tracking
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
  - Recharge button to restore to maximum
  - Displays current/max charges (only shows if item has charges)
- **Item Management**:
  - Remove Selected button to delete items
  - Items persist when saving/loading character
  - Equipment bonuses automatically reapply when loading character

**Example Magic Item Creation**:

Creating "Vest of the Archmagi":
1. Click "Create New Item"
2. Name: "Vest of the Archmagi", Type: "Wondrous Item", Slot: "Body"
3. Add bonuses:
   - Armor: +8
   - Resistance (All Saves): +5
   - Overcome Spell Resistance: +2
4. Properties: "Recall up to lvl 9 spell (3/day)\nExpend spell slot: Heal (5 x spell lvl)"
5. Click "Create Item"
6. Click the Equipped column to equip it
7. Character immediately gains: +8 AC, +5 to all saves, +2 Spell Resistance

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
