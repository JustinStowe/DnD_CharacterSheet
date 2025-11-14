"""

D&D 3rd Edition Feats from Complete Warrior

Feats for fighters, barbarians, monks, and other combat specialists

"""

COMPLETE_WARRIOR_FEATS = {

    'Brutal Throw': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'None',
        'benefit': 'You can add your Strength modifier instead of your Dexterity modifier to attack rolls with thrown weapons.',
        'special': 'A fighter may select Brutal Throw as one of his fighter bonus feats.'
    },

    'Combat Intuition': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Sense Motive 4 ranks, base attack bonus +5',
        'benefit': 'You gain a +4 bonus on Sense Motive checks to assess challenges. When making melee attacks against a creature attacked in the previous round, you gain +1 insight bonus on attack rolls.',
        'special': 'A fighter may select Combat Intuition as one of his fighter bonus feats.'
    },

    'Danger Sense': {
        'type': 'General',
        'prerequisites': 'Improved Initiative',
        'benefit': 'Once per day, you can reroll an initiative check you have just made and use the better roll.',
        'special': ''
    },

    'Death Blow': {
        'type': 'General',
        'prerequisites': 'Improved Initiative, base attack bonus +2',
        'benefit': 'You can perform a coup de grace attack as a standard action instead of a full-round action.',
        'special': ''
    },

    'Deft Opportunist': {
        'type': 'General',
        'prerequisites': 'Dex 15, Combat Reflexes',
        'benefit': 'You get a +4 bonus on attack rolls when making attacks of opportunity.',
        'special': ''
    },

    'Deft Strike': {
        'type': 'General',
        'prerequisites': 'Int 13, Combat Expertise, Spot 10 ranks, sneak attack',
        'benefit': 'As a standard action, you can pinpoint weak armor points. Your next attack ignores the targets armor bonus and natural armor bonus to AC.',
        'special': ''
    },

    'Devoted Inquisitor': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Smite evil, sneak attack',
        'benefit': 'When using sneak attack and smite evil against the same foe, the opponent must make a Will save or be dazed for 1 round. You can multiclass freely between paladin and rogue.',
        'special': 'You must remain lawful good to retain paladin abilities.'
    },

    'Devoted Performer': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Bardic music, smite evil',
        'benefit': 'Paladin and bard levels stack for smite evil damage and bardic music uses. You can multiclass freely between paladin and bard.',
        'special': 'You must remain lawful good to retain paladin abilities.'
    },

    'Devoted Tracker': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Track, smite evil, wild empathy',
        'benefit': 'Paladin and ranger levels stack for smite evil and wild empathy. You can multiclass freely between paladin and ranger.',
        'special': 'You must remain lawful good to retain paladin abilities.'
    },

    'Dual Strike': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Improved Two-Weapon Fighting, Two-Weapon Fighting',
        'benefit': 'As a standard action, you can make one melee attack with primary and off-hand weapons using the worse attack modifier.',
        'special': 'A fighter may select Dual Strike as one of his fighter bonus feats.'
    },

    'Expert Tactician': {
        'type': 'General',
        'prerequisites': 'Dex 13, Combat Reflexes, base attack bonus +2',
        'benefit': 'If you hit a creature with an attack of opportunity, you and all allies gain +2 circumstance bonus on melee attack rolls against that creature for 1 round.',
        'special': ''
    },

    'Extra Rage': {
        'type': 'General',
        'prerequisites': 'Rage or frenzy ability',
        'benefit': 'You can rage or frenzy two more times per day than you otherwise could.',
        'special': 'You can take this feat multiple times. Its effects stack.'
    },

    'Extra Smiting': {
        'type': 'General',
        'prerequisites': 'Smite ability, base attack bonus +4',
        'benefit': 'You gain two extra smite attempts per day.',
        'special': 'You can take this feat multiple times. Its effects stack.'
    },

    'Extra Stunning': {
        'type': 'General',
        'prerequisites': 'Stunning Fist, base attack bonus +2',
        'benefit': 'You gain the ability to make three extra stunning attacks per day.',
        'special': 'You can take this feat multiple times. Its effects stack.'
    },

    'Eyes in the Back of Your Head': {
        'type': 'General',
        'prerequisites': 'Wis 13, base attack bonus +1',
        'benefit': 'Attackers do not gain the usual +2 bonus when flanking you. You can still be sneak attacked when flanked.',
        'special': ''
    },

    'Faster Healing': {
        'type': 'General',
        'prerequisites': 'Base Fortitude save bonus +5',
        'benefit': 'You recover hit points and ability score points faster than normal based on activity level.',
        'special': ''
    },

    'Favored Power Attack': {
        'type': 'General',
        'prerequisites': 'Favored enemy ability, Power Attack, base attack bonus +4',
        'benefit': 'When using Power Attack against a favored enemy, you can subtract a number from melee attacks and add twice that number to melee damage (three times if using two-handed weapon).',
        'special': ''
    },

    'Fists of Iron': {
        'type': 'General',
        'prerequisites': 'Improved Unarmed Strike, Stunning Fist, base attack bonus +2',
        'benefit': 'You deal an extra 1d6 points of damage on successful unarmed attacks. Each attempt counts as one use of Stunning Fist.',
        'special': ''
    },

    'Fleet of Foot': {
        'type': 'General',
        'prerequisites': 'Dex 15, Run',
        'benefit': 'When running or charging, you can make a single direction change of 90 degrees or less.',
        'special': 'You cannot use this feat in medium or heavy armor, or carrying a medium or heavier load.'
    },

    'Flick of the Wrist': {
        'type': 'General',
        'prerequisites': 'Dex 17, Sleight of Hand 5 ranks, Quick Draw',
        'benefit': 'If you draw a light weapon and make a melee attack with it in the same round, you catch your opponent flat-footed for this attack only.',
        'special': 'You may use this feat only once per round and once per opponent per combat encounter.'
    },

    'Flying Kick': {
        'type': 'General',
        'prerequisites': 'Str 13, Jump 4 ranks, Improved Unarmed Strike, Power Attack',
        'benefit': 'When fighting unarmed and using the charge action, you deal an extra 1d12 points of damage with your unarmed attack.',
        'special': ''
    },

    'Freezing the Lifeblood': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Wis 17, Improved Unarmed Strike, Stunning Fist, base attack bonus +10',
        'benefit': 'You can make unarmed attacks that paralyze targets for 1d4+1 rounds on a failed Fortitude save.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats. Each attempt counts as one Stunning Fist use.'
    },

    'Greater Kiai Shout': {
        'type': 'General',
        'prerequisites': 'Cha 13, Kiai Shout, base attack bonus +9',
        'benefit': 'When you make a kiai shout, your opponents are panicked for 2d6 rounds on failed Will saves.',
        'special': 'The shout affects only opponents with fewer Hit Dice than you have.'
    },

    'Greater Resiliency': {
        'type': 'General',
        'prerequisites': 'Damage reduction as a class feature or innate ability',
        'benefit': 'Your damage reduction increases by 1.',
        'special': 'You may not take this feat more than once.'
    },

    'Greater Two-Weapon Defense': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Dex 19, Improved Two-Weapon Defense, Two-Weapon Defense, Two-Weapon Fighting, base attack bonus +11',
        'benefit': 'When wielding two weapons, you gain a +3 shield bonus to AC (increasing to +6 when fighting defensively or total defense).',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Hamstring': {
        'type': 'General',
        'prerequisites': 'Sneak attack ability, base attack bonus +4',
        'benefit': 'On sneak attack hit, you can forgo 2d6 sneak attack damage to reduce opponents base speed by half.',
        'special': ''
    },

    'Hold the Line': {
        'type': 'General',
        'prerequisites': 'Combat Reflexes, base attack bonus +2',
        'benefit': 'You may make an attack of opportunity against charging opponents who enter an area you threaten.',
        'special': ''
    },

    'Improved Buckler Defense': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Shield Proficiency',
        'benefit': 'When you attack with a weapon in your off hand, you may still apply your bucklers shield bonus to AC.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Combat Expertise': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Int 13, Combat Expertise, base attack bonus +6',
        'benefit': 'When using Combat Expertise, the number subtracted from attack rolls and added to AC can be any number up to your base attack bonus.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Familiar': {
        'type': 'General',
        'prerequisites': 'Ability to acquire a new familiar, compatible alignment, sufficient arcane caster level, and base attack bonus',
        'benefit': 'You can choose a familiar from an expanded list including creatures like worg, blink dog, hippogriff, and hell hound.',
        'special': ''
    },

    'Improved Favored Enemy': {
        'type': 'General',
        'prerequisites': 'Favored enemy ability, base attack bonus +5',
        'benefit': 'You deal an extra 3 points of damage to your favored enemies.',
        'special': ''
    },

    'Improved Mounted Archery': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Ride 1 rank, Mounted Archery, Mounted Combat',
        'benefit': 'The penalty for using ranged weapons when your mount is running is reduced from -4 to -2. You can attack at any time during your mounts move.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Rapid Shot': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Manyshot, Point Blank Shot, Rapid Shot',
        'benefit': 'When using Rapid Shot, you ignore the -2 penalty on all your ranged attack rolls.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Toughness': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Base Fortitude save bonus +2',
        'benefit': 'You gain a number of hit points equal to your current Hit Dice. Each time you gain HD, you gain 1 additional hit point.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Two-Weapon Defense': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Dex 17, Two-Weapon Defense, Two-Weapon Fighting, base attack bonus +6',
        'benefit': 'When wielding two weapons, you gain a +2 shield bonus to AC (increasing to +4 when fighting defensively or total defense).',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Improved Weapon Familiarity': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'You can treat all exotic weapons associated with your race as martial weapons rather than exotic weapons.',
        'special': ''
    },

    'Monkey Grip': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'You can use melee weapons one size category larger than you are with a -2 penalty on the attack roll.',
        'special': ''
    },

    'Pain Touch': {
        'type': 'General',
        'prerequisites': 'Wis 15, Stunning Fist, base attack bonus +2',
        'benefit': 'Victims of your successful stunning attacks become nauseated for 1 round after being stunned.',
        'special': ''
    },

    'Phalanx Fighting': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Proficiency with a heavy shield, base attack bonus +1',
        'benefit': 'If using a heavy shield and light weapon, you gain +1 bonus to AC. In formation with allies who have this feat, you form a shield wall granting +2 AC and +1 Reflex saves.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Pin Shield': {
        'type': 'General',
        'prerequisites': 'Two-Weapon Fighting, base attack bonus +4',
        'benefit': 'You can pin opponents shields with your off-hand weapon to negate their shield bonus to AC until the end of your action.',
        'special': ''
    },

    'Power Critical': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Weapon Focus with weapon, base attack bonus +4',
        'benefit': 'With your selected weapon, you gain a +4 bonus on rolls to confirm threats.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats. You can take it multiple times with different weapons.'
    },

    'Prone Attack': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Dex 15, Lightning Reflexes, base attack bonus +2',
        'benefit': 'You can attack from the prone position without penalty and regain your feet immediately as a free action if your attack succeeds.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Ranged Disarm': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Dex 15, Point Blank Shot, Precise Shot, base attack bonus +5',
        'benefit': 'You can make disarm attempts with ranged weapons against targets within 30 feet.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Rapid Throw': {
        'type': 'General',
        'prerequisites': 'Dex 15, proficiency with weapon, base attack bonus +2',
        'benefit': 'You can throw a melee weapon you are proficient with as if it were a ranged weapon with a 10-foot range increment.',
        'special': ''
    },

    'Weakening Touch': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Wis 17, Improved Unarmed Strike, Stunning Fist, base attack bonus +2',
        'benefit': 'You can make unarmed attacks that apply a -6 penalty to targets Strength score for 1 minute.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats. Each attempt counts as one Stunning Fist use.'
    },

    'Zen Archery': {
        'type': 'General',
        'prerequisites': 'Wis 13, base attack bonus +1',
        'benefit': 'You can use your Wisdom modifier instead of your Dexterity modifier when making ranged attack rolls.',
        'special': ''
    }

}
