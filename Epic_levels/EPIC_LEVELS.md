# Epic Level Handbook Implementation

## Overview

Complete implementation of D&D 3rd Edition Epic Level Handbook rules for characters level 21 and above.

## Files Created/Modified

### New Files

1. **epic_levels.py** - Core epic level logic

   - 53 epic feats with full descriptions
   - Epic BAB progression formulas
   - Epic save progression formulas
   - Epic feat and ability increase progression
   - Epic XP calculation
   - Helper functions for all epic level mechanics

2. **test_epic_levels.py** - Comprehensive test suite
   - Tests for epic level detection
   - BAB progression validation
   - Save progression validation
   - Epic feat progression
   - Multiclass epic characters
   - Epic feat management
   - XP progression

### Modified Files

1. **character.py**

   - Added epic level imports
   - Updated `get_base_attack_bonus_from_class()` to include epic BAB
   - Updated `get_base_save_from_class()` to include epic saves
   - Added epic feat tracking (list)
   - Added epic ability increase tracking (dictionary)
   - Added epic level helper methods:
     - `is_epic_level()`
     - `get_epic_info()`
     - `get_max_skill_ranks()`
     - `get_epic_feats_available()`
     - `add_epic_feat()`
     - `remove_epic_feat()`
     - `check_epic_feat_requirements()`
     - `get_all_epic_feats_list()`
     - `apply_epic_ability_increase()`
     - `update_xp_for_epic_level()`
   - Updated `to_dict()` and `from_dict()` for save/load support

2. **character_sheet_gui.py**

   - Added epic level imports
   - Added "Epic Feats (21+)" button to Feats tab
   - Implemented `show_epic_feats_dialog()`:
     - Shows epic level information
     - Lists current epic feats
     - Allows adding new epic feats from dropdown
     - Shows full feat descriptions with prerequisites
     - Validates feat limits based on level
     - Checks for duplicate feats (unless allowed)
   - Updated `show_level_up_dialog()`:
     - Shows epic level notifications
     - Alerts when gaining epic feats
     - Alerts when gaining ability increases
     - Shows "one more level until epic" at level 20
   - Updated XP calculation to use `update_xp_for_epic_level()`

3. **README.md**
   - Added epic level support to Features section
   - Listed all epic level mechanics
   - Documented 53 epic feats
   - Added Epic Feats usage documentation in Feats & Abilities Tab section
   - Highlighted full Epic Level Handbook support

## Epic Level Features

### 1. Epic BAB Progression (Level 21+)

- **Full BAB Classes** (Fighter, Barbarian, Ranger, Paladin): +1 per level
  - Level 21: +21, Level 25: +25, Level 30: +30
- **Medium BAB Classes** (Cleric, Druid, Monk, Rogue, Bard): +1 every 2 levels
  - Level 20: +15, Level 22: +16, Level 30: +20
- **Poor BAB Classes** (Wizard, Sorcerer): +1 every 2 levels
  - Level 20: +10, Level 22: +11, Level 30: +15

### 2. Epic Save Progression (Level 21+)

- **Good Saves**: +1 every 2 epic levels
  - Level 20: +12, Level 22: +13, Level 30: +17
- **Poor Saves**: +1 every 3 epic levels
  - Level 20: +6, Level 22: +7, Level 30: +10

### 3. Epic Feats (53 Total)

Gained at level 21, then every 2 levels (23, 25, 27, 29...)

**Combat Epic Feats:**

- Epic Weapon Focus (+2 attack, stacks with Weapon Focus)
- Epic Weapon Specialization (+4 damage, stacks with Weapon Specialization)
- Epic Prowess (+1 to all attacks, can take multiple times)
- Devastating Critical (instant death on crit)
- Overwhelming Critical (extra damage on crit)
- Improved Combat Reflexes (unlimited AoOs)
- Improved Whirlwind Attack
- Blinding Speed (haste effect)
- Epic Dodge (auto-avoid one attack per round)

**Defensive Epic Feats:**

- Epic Toughness (+30 HP, can take multiple times)
- Epic Fortitude/Reflexes/Will (+4 to saves, can take multiple times)
- Armor Skin (+1 natural armor, can take multiple times up to +10)
- Damage Reduction (gain DR 3/—, can take multiple times)
- Fast Healing (gain fast healing 3, can take multiple times)
- Perfect Health (immune to disease)

**Ability Score Epic Feats:**

- Great Strength/Dexterity/Constitution/Intelligence/Wisdom/Charisma (+1 to ability, can take multiple times)

**Spellcasting Epic Feats:**

- Epic Spellcasting (cast epic spells)
- Epic Spell Focus (+1 DC for school)
- Epic Spell Penetration (+2 to overcome SR)
- Improved Spell Capacity (gain 10th-13th level spell slots)
- Epic Skill Focus (+10 to skill, stacks with Skill Focus)
- Improved Combat Casting (no AoO when casting)
- Spell Opportunity (cast quickened spell as AoO)
- Spell Knowledge (learn extra spell)
- Permanent Emanation (make emanation spell permanent)
- Spontaneous Spell (cast prepared spell spontaneously)
- Spell Stowaway (catch and store spells)
- Tenacious Magic (requires two dispels to remove)

**Special Epic Feats:**

- Epic Speed (+30 ft movement, can take multiple times)
- Epic Reputation (+4 to Charisma skills)
- Epic Endurance (+10 Concentration, sleep in armor)
- Combat Insight (add Wisdom to melee attacks)
- Uncanny Accuracy (ignore concealment)
- Infinite Deflection (deflect unlimited ranged attacks)
- Instant Reload (reload crossbow as free action)
- Legendary Commander/Rider/Tracker
- Polyglot (speak all languages)

**Class-Specific Epic Feats:**

- Great Smiting (add Cha to smite damage)
- Improved Aura of Courage (immunity to fear)
- Improved Ki Strike (+1 to ki strike DR penetration)
- Improved Sneak Attack (+1d6 sneak attack)
- Improved Stunning Fist (+2 DC)
- Swarm of Arrows (fire at all in 30 ft area)

### 4. Epic Ability Score Increases

- Gained every 4 levels after 20th: Level 24, 28, 32, 36, 40
- +1 to any ability score of choice
- Works like normal ability increases but at epic levels

### 5. Epic XP Progression

- Level 21: 41,000 XP total
- Level 22: 63,000 XP total
- Level 25: 161,000 XP total
- Level 30: 306,000 XP total
- Formula: Previous total + (current level × 1000)

### 6. Multiclass Epic Support

- All epic progressions work correctly with multiclass characters
- Example: Fighter 15/Wizard 10 (Total 25, Epic 5)
  - BAB: 20 (15 from Fighter + 5 from Wizard)
  - Epic Feats: 3 (at levels 21, 23, 25)
  - Works with base classes and prestige classes

## Usage

### Reaching Epic Level

1. Level your character to 20th level normally
2. At level 21, you'll see "EPIC LEVEL!" notification
3. Epic feat button becomes available on Feats tab
4. Continue leveling with epic progressions

### Selecting Epic Feats

1. Open the Feats & Abilities tab
2. Click "Epic Feats (21+)" button
3. View your current epic feats and available feat slots
4. Select an epic feat from the dropdown
5. Read the description, prerequisites, and benefits
6. Click "Add Epic Feat" to add it
7. Some feats can be taken multiple times (noted in Special field)

### Epic Ability Increases

1. When you reach level 24 (or 28, 32, etc.)
2. Level up dialog shows "Ability Score Increase!" notification
3. Manually increase any ability score by +1 on the Main tab
4. System tracks epic ability increases separately

### Saving Epic Characters

- Epic feats and ability increases are saved with character
- Load saved epic characters to continue progression
- All epic calculations automatic on load

## Testing

Run the test suite to verify all epic level features:

```bash
python test_epic_levels.py
```

All tests pass, validating:

- Epic level detection
- BAB progression (all three types)
- Save progression (good and poor)
- Epic feat progression
- Multiclass epic characters
- Epic feat management
- XP progression

## Technical Implementation

### Epic Level Detection

```python
def is_epic_level(total_level):
    return total_level >= 21
```

### Epic Feat Progression

```python
def get_epic_feat_progression(total_level):
    if total_level < 21:
        return 0
    return 1 + (total_level - 21) // 2
```

### Epic BAB Calculation

- Calculate normal BAB up to level 20
- Add epic bonus for levels beyond 20
- Full: +1 per epic level
- Medium/Poor: +1 per 2 epic levels

### Epic Save Calculation

- Calculate normal save up to level 20
- Add epic bonus for levels beyond 20
- Good: +1 per 2 epic levels
- Poor: +1 per 3 epic levels

## Future Enhancements (Optional)

- Epic prestige classes (Epic Infiltrator, etc.)
- Epic spells implementation
- Automatic prerequisite checking for epic feats
- Epic magic items
- Epic monsters/challenges

## Conclusion

Full Epic Level Handbook support is now integrated into the D&D 3e Character Sheet application. Characters can progress beyond 20th level with proper epic BAB, saves, feats, and ability increases, following official D&D 3e epic level rules.
