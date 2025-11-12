"""
Test Magic of Faerûn prestige classes
"""
import sys
sys.path.insert(0, '..')

from prestige_classes import (
    get_all_prestige_classes,
    get_prestige_class_info,
    PRESTIGE_CLASS_DEFINITIONS
)

print("=" * 70)
print("Magic of Faerûn Prestige Classes")
print("=" * 70)

# Get all prestige classes
all_classes = get_all_prestige_classes()
print(f"\nTotal Prestige Classes Available: {len(all_classes)}")

# Count original vs Faerûn classes
original_classes = [
    'Arcane Archer', 'Arcane Trickster', 'Assassin', 'Blackguard', 
    'Dragon Disciple', 'Duelist', 'Dwarven Defender', 'Eldritch Knight',
    'Horizon Walker', 'Loremaster', 'Mystic Theurge', 'Shadowdancer'
]

faerun_classes = [c for c in all_classes if c not in original_classes]
print(f"Core D&D Prestige Classes: {len(original_classes)}")
print(f"Magic of Faerûn Prestige Classes: {len(faerun_classes)}")

print("\n" + "=" * 70)
print("Magic of Faerûn Prestige Classes:")
print("=" * 70)

for pc_name in sorted(faerun_classes):
    info = get_prestige_class_info(pc_name)
    print(f"\n{pc_name}")
    print(f"  Hit Die: d{info['hit_die']}")
    print(f"  BAB: {info['bab_progression']}")
    print(f"  Saves: Fort {info['fort_progression']}, Ref {info['ref_progression']}, Will {info['will_progression']}")
    print(f"  Skill Points: {info['skill_points']}")
    
    if info.get('spellcasting_advancement'):
        print(f"  ✓ Advances spellcasting")
    
    print(f"  Description: {info['description']}")
    
    # Show key requirements
    req = info.get('requirements', {})
    if 'race' in req:
        print(f"  Req - Race: {req['race']}")
    if 'alignment' in req:
        print(f"  Req - Alignment: {req['alignment']}")
    if 'bab' in req:
        print(f"  Req - BAB: +{req['bab']}")
    if 'special' in req:
        print(f"  Req - Special: {req['special']}")

# Test a few specific classes
print("\n" + "=" * 70)
print("Detailed Requirements Examples:")
print("=" * 70)

print("\nRed Wizard:")
red_wizard = get_prestige_class_info('Red Wizard')
print(f"  Requirements:")
for key, value in red_wizard['requirements'].items():
    print(f"    {key}: {value}")

print("\nHarper Scout:")
harper = get_prestige_class_info('Harper Scout')
print(f"  Requirements:")
for key, value in harper['requirements'].items():
    print(f"    {key}: {value}")

print("\nSpellsword:")
spellsword = get_prestige_class_info('Spellsword')
print(f"  Requirements:")
for key, value in spellsword['requirements'].items():
    print(f"    {key}: {value}")

print("\n" + "=" * 70)
print(f"Testing Complete! {len(all_classes)} prestige classes available.")
print("=" * 70)
