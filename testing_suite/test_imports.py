"""
Verify all imports work correctly after reorganization
"""
print("Testing imports after directory reorganization...")
print("=" * 70)

# Test prestige classes
try:
    from prestige_classes import (
        PRESTIGE_CLASS_DEFINITIONS,
        get_all_prestige_classes,
        is_prestige_class
    )
    classes = get_all_prestige_classes()
    print(f"✓ Prestige classes: {len(classes)} classes loaded")
    print(f"  Sample: {list(classes)[:3]}")
except Exception as e:
    print(f"✗ Prestige classes FAILED: {e}")

# Test epic levels
try:
    from Epic_levels import (
        EPIC_FEATS,
        is_epic_level,
        get_all_epic_feats
    )
    feats = get_all_epic_feats()
    print(f"✓ Epic levels: {len(feats)} epic feats loaded")
    print(f"  Sample: {list(feats)[:3]}")
except Exception as e:
    print(f"✗ Epic levels FAILED: {e}")

# Test character module
try:
    from character import Character, CLASS_DEFINITIONS
    c = Character()
    c.name = "Test Character"
    c.race = "Human"
    c.add_class("Fighter", 5)
    print(f"✓ Character module: Working correctly")
    print(f"  Character: {c.name} ({c.race}) - {c.get_class_string()}")
    print(f"  BAB: +{c.base_attack_bonus}")
except Exception as e:
    print(f"✗ Character module FAILED: {e}")

# Test GUI module
try:
    import character_sheet_gui
    print(f"✓ GUI module: Imports successfully")
except Exception as e:
    print(f"✗ GUI module FAILED: {e}")

print("=" * 70)
print("All import tests completed!")
