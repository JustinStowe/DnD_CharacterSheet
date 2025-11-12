"""
Test all prestige classes from all sourcebooks
"""
import sys
sys.path.insert(0, '..')

from prestige_classes import (
    get_all_prestige_classes,
    get_prestige_class_info,
    PRESTIGE_CLASS_DEFINITIONS
)

print("=" * 80)
print("PRESTIGE CLASS TEST - ALL SOURCEBOOKS")
print("=" * 80)

# Get all prestige classes
all_classes = get_all_prestige_classes()
print(f"\n✓ Total Prestige Classes Available: {len(all_classes)}")

# Count by sourcebook
core_dmg = ['Arcane Archer', 'Arcane Trickster', 'Assassin', 'Blackguard', 
            'Dragon Disciple', 'Duelist', 'Dwarven Defender', 'Eldritch Knight',
            'Horizon Walker', 'Loremaster', 'Mystic Theurge', 'Shadowdancer']

faerun = ['Harper Scout', 'Spellsword', 'Red Wizard', 'Guild Thief', 'Shadow Adept',
          'Arcane Devotee', 'Divine Champion', 'Divine Disciple', 'Harper Priest',
          'Runecaster', 'Silverstar', 'Hospitaler', 'Incantatrix', 'Acolyte of the Ego',
          'Acolyte of the Skin', 'Shaaryan Hunter', 'Monk of the Long Death',
          'Zhentarim Soldier', 'Zhentarim Spy']

tome_blood = ['Abjurer', 'Alienist', 'Bladesinger', 'Blood Magus', 'Candle Caster',
              'Geomancer', 'Master Transmogrifist', 'Pale Master', 'Ruathar',
              'Seeker of the Song', 'Void Disciple', 'Waverider']

sword_fist = ['Cavalier', 'Darkwood Stalker', 'Drunken Master', 'Exotic Weapon Master',
              'Frenzied Berserker', 'Gladiator', 'Ironguard', 'Kensai',
              'Monk of the Enabled Hand', 'Ravager', 'Reaping Mauler', 'Stonelord',
              'War Chanter', 'Wildrunner']

song_silence = ['Battle Dancer', 'Fochlucan Lyrist', 'Harper Agent', 'Lyric Thaumaturge',
                'Master of Masks', 'Metalsmith', 'Nameless One', 'Justiciar',
                'Master Specialist', 'Virtuoso', 'Vigilante', "Fortune's Friend",
                'Thief-Acrobat']  # Note: Arcane Trickster removed (duplicate from Core DMG)

print("\n" + "=" * 80)
print("PRESTIGE CLASSES BY SOURCEBOOK")
print("=" * 80)

print(f"\n📖 Core DMG: {len([c for c in core_dmg if c in all_classes])} classes")
for pc in core_dmg:
    if pc in all_classes:
        print(f"   ✓ {pc}")
    else:
        print(f"   ✗ MISSING: {pc}")

print(f"\n📖 Magic of Faerûn: {len([c for c in faerun if c in all_classes])} classes")
for pc in faerun:
    if pc in all_classes:
        print(f"   ✓ {pc}")
    else:
        print(f"   ✗ MISSING: {pc}")

print(f"\n📖 Tome and Blood: {len([c for c in tome_blood if c in all_classes])} classes")
for pc in tome_blood:
    if pc in all_classes:
        print(f"   ✓ {pc}")
    else:
        print(f"   ✗ MISSING: {pc}")

print(f"\n📖 Sword and Fist: {len([c for c in sword_fist if c in all_classes])} classes")
for pc in sword_fist:
    if pc in all_classes:
        print(f"   ✓ {pc}")
    else:
        print(f"   ✗ MISSING: {pc}")

print(f"\n📖 Song and Silence: {len([c for c in song_silence if c in all_classes])} classes")
for pc in song_silence:
    if pc in all_classes:
        print(f"   ✓ {pc}")
    else:
        print(f"   ✗ MISSING: {pc}")

# Test a few specific classes from each sourcebook
print("\n" + "=" * 80)
print("DETAILED CLASS INFORMATION TESTS")
print("=" * 80)

test_classes = [
    ('Bladesinger', 'Tome and Blood'),
    ('Kensai', 'Sword and Fist'),
    ('Battle Dancer', 'Song and Silence'),
    ('Red Wizard', 'Magic of Faerûn'),
    ('Mystic Theurge', 'Core DMG')
]

for class_name, sourcebook in test_classes:
    info = get_prestige_class_info(class_name)
    if info:
        print(f"\n✓ {class_name} ({sourcebook})")
        print(f"   Hit Die: d{info['hit_die']}")
        print(f"   BAB: {info['bab_progression']}")
        print(f"   Skills: {info['skill_points']}/level")
        print(f"   Description: {info['description']}")
        if 'requirements' in info:
            print(f"   Requirements: {len(info['requirements'])} categories")
    else:
        print(f"\n✗ {class_name} ({sourcebook}) - NOT FOUND!")

# Verify all classes have required fields
print("\n" + "=" * 80)
print("DATA VALIDATION")
print("=" * 80)

required_fields = ['hit_die', 'bab_progression', 'fort_progression', 'ref_progression',
                   'will_progression', 'skill_points', 'is_prestige', 'description']

errors = []
for class_name in all_classes:
    info = get_prestige_class_info(class_name)
    for field in required_fields:
        if field not in info:
            errors.append(f"{class_name} missing field: {field}")

if errors:
    print(f"\n✗ Found {len(errors)} validation errors:")
    for error in errors:
        print(f"   - {error}")
else:
    print(f"\n✓ All {len(all_classes)} prestige classes have valid data structures!")

# Summary
print("\n" + "=" * 80)
print("TEST SUMMARY")
print("=" * 80)
print(f"\nTotal Prestige Classes: {len(all_classes)}")
print(f"  - Core DMG: {len([c for c in core_dmg if c in all_classes])}")
print(f"  - Magic of Faerûn: {len([c for c in faerun if c in all_classes])}")
print(f"  - Tome and Blood: {len([c for c in tome_blood if c in all_classes])}")
print(f"  - Sword and Fist: {len([c for c in sword_fist if c in all_classes])}")
print(f"  - Song and Silence: {len([c for c in song_silence if c in all_classes])}")

expected_total = len(core_dmg) + len(faerun) + len(tome_blood) + len(sword_fist) + len(song_silence)
expected_unique = expected_total  # All classes are unique now (Arcane Trickster removed from Song & Silence)

if len(all_classes) == expected_unique:
    print(f"\n🎉 SUCCESS! All {len(all_classes)} unique prestige classes loaded correctly!")
else:
    print(f"\n⚠️  Expected {expected_unique} unique classes, but found {len(all_classes)}")

print("\n" + "=" * 80)
