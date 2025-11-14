"""
D&D 3rd Edition Feats from Sword and Fist
Feats focused on fighters and monks
"""

SWORD_AND_FIST_FEATS = {
    'Absorb Blow': {
        'type': 'General',
        'prerequisites': 'Con 13, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'Once per round, you can attempt to avoid damage from a single melee attack. Make a Fortitude save (DC = damage dealt). On a success, you take half damage.',
        'special': ''
    },
    'Armor Optimization': {
        'type': 'General',
        'prerequisites': 'Base Fortitude save +3',
        'benefit': 'Choose one type of armor. You reduce the armor check penalty by 1 and increase the maximum Dex bonus by 1 when wearing that armor.',
        'special': 'You can gain this feat multiple times, each time selecting a different type of armor.'
    },
    'Circle Kick': {
        'type': 'General',
        'prerequisites': 'Dex 13, Improved Unarmed Strike, Mobility',
        'benefit': 'When using a full attack action with unarmed strikes, you can give up your regular attacks and make one attack at your highest bonus against each opponent within reach.',
        'special': ''
    },
    'Close-Quarters Fighting': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +3',
        'benefit': 'You do not provoke attacks of opportunity when you attack with a light weapon while in a grapple.',
        'special': ''
    },
    'Clever Wrestling': {
        'type': 'General',
        'prerequisites': 'Int 13, Improved Unarmed Strike, Combat Expertise',
        'benefit': 'You can use your Intelligence modifier instead of your Strength modifier on grapple checks.',
        'special': ''
    },
    'Crush': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'When you successfully pin an opponent, you deal unarmed strike damage as well.',
        'special': ''
    },
    'Defensive Strike': {
        'type': 'General',
        'prerequisites': 'Int 13, Combat Expertise, Dodge',
        'benefit': 'When fighting defensively or using Combat Expertise and an opponent misses you, you can make an attack of opportunity against that opponent.',
        'special': 'You can use this feat once per round.'
    },
    'Defensive Throw': {
        'type': 'General',
        'prerequisites': 'Dex 13, Improved Unarmed Strike, Improved Trip',
        'benefit': 'If an opponent attacks you and misses while you are fighting defensively or using Combat Expertise, you can make an immediate trip attempt against that opponent as a free action.',
        'special': 'You can use this feat once per round.'
    },
    'Devastating Strike': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Unarmed Strike, Stunning Fist, base attack bonus +5',
        'benefit': 'Your unarmed strikes deal damage as if you were one size category larger.',
        'special': ''
    },
    'Dirty Fighting': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +4 bonus on melee damage when flanking an opponent. This replaces the normal +2 bonus.',
        'special': ''
    },
    'Dual Strike': {
        'type': 'General',
        'prerequisites': 'Dex 15, Two-Weapon Fighting, base attack bonus +10',
        'benefit': 'When fighting with two weapons, you can attack a single opponent with both weapons as a standard action.',
        'special': ''
    },
    'Prone Attack': {
        'type': 'General',
        'prerequisites': 'Dex 15, Improved Unarmed Strike, base attack bonus +2',
        'benefit': 'You can attack from a prone position without penalty.',
        'special': ''
    },
    'Energy Charge': {
        'type': 'General',
        'prerequisites': 'Str 13, Power Attack, Cleave, base attack bonus +9',
        'benefit': 'When you charge, you can make a full attack at the end of your charge instead of a single attack.',
        'special': ''
    },
    'Eyes in the Back of Your Head': {
        'type': 'General',
        'prerequisites': 'Wis 13, Alertness',
        'benefit': 'Opponents do not gain a +2 bonus to attack you when flanking you.',
        'special': ''
    },
    'Fists of Iron': {
        'type': 'General',
        'prerequisites': 'Improved Unarmed Strike, Stunning Fist',
        'benefit': 'Your unarmed attacks are treated as armed for purposes of dealing damage to objects and creatures with damage reduction.',
        'special': ''
    },
    'Fleet Charge': {
        'type': 'General',
        'prerequisites': 'Run, base attack bonus +3',
        'benefit': 'When you charge, you can move up to four times your speed instead of twice your speed.',
        'special': ''
    },
    'Focused': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Concentration checks and Sense Motive checks.',
        'special': ''
    },
    'Formation Expert': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +2',
        'benefit': 'You gain a +2 bonus on attack rolls when adjacent to an ally.',
        'special': ''
    },
    'Greater Resiliency': {
        'type': 'General',
        'prerequisites': 'Con 13, Endurance, Toughness',
        'benefit': 'You gain damage reduction 1/-.',
        'special': ''
    },
    'Greater Two-Weapon Fighting': {
        'type': 'Combat',
        'prerequisites': 'Dex 19, Two-Weapon Fighting, Improved Two-Weapon Fighting, base attack bonus +11',
        'benefit': 'You get a third attack with your off-hand weapon, albeit at a -10 penalty.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Hamstring': {
        'type': 'General',
        'prerequisites': 'Sneak attack class feature',
        'benefit': 'When you deal sneak attack damage with a slashing weapon, you can forgo 2d6 sneak attack damage to reduce your opponent\'s speed by 10 feet for 1 minute.',
        'special': ''
    },
    'Hear the Unseen': {
        'type': 'General',
        'prerequisites': 'Wis 13, Blind-Fight',
        'benefit': 'When you cannot see an attacker, you only suffer a 25% miss chance instead of the normal 50% miss chance.',
        'special': ''
    },
    'Improved Buckler Defense': {
        'type': 'General',
        'prerequisites': 'Shield Proficiency',
        'benefit': 'You can use a buckler and still use your buckler hand for other purposes without losing your AC bonus.',
        'special': ''
    },
    'Improved Familiar': {
        'type': 'General',
        'prerequisites': 'Ability to acquire a familiar',
        'benefit': 'You can acquire more powerful familiars.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Improved Grapple': {
        'type': 'General',
        'prerequisites': 'Dex 13, Improved Unarmed Strike',
        'benefit': 'You do not provoke attacks of opportunity when grappling. You also gain a +4 bonus on grapple checks.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Improved Ki Strike': {
        'type': 'General',
        'prerequisites': 'Wis 13, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'Your unarmed strikes are treated as magic weapons for purposes of overcoming damage reduction.',
        'special': ''
    },
    'Improved Mounted Archery': {
        'type': 'General',
        'prerequisites': 'Mounted Archery, Mounted Combat, Ride 9 ranks',
        'benefit': 'When mounted, you can make a full attack with a ranged weapon.',
        'special': ''
    },
    'Improved Rapid Shot': {
        'type': 'General',
        'prerequisites': 'Point Blank Shot, Rapid Shot, Manyshot, Dex 19, base attack bonus +12',
        'benefit': 'When using Rapid Shot, you can make one additional attack at your highest attack bonus.',
        'special': ''
    },
    'Improved Weapon Familiarity': {
        'type': 'General',
        'prerequisites': 'Proficiency with exotic weapon, base attack bonus +8',
        'benefit': 'Choose one exotic weapon you are proficient with. It is now treated as a martial weapon for you.',
        'special': 'You can gain this feat multiple times.'
    },
    'Instant Stand': {
        'type': 'General',
        'prerequisites': 'Dex 15',
        'benefit': 'You can stand up from prone as a free action.',
        'special': ''
    },
    'Karmic Strike': {
        'type': 'General',
        'prerequisites': 'Dex 13, Combat Reflexes',
        'benefit': 'When an opponent makes a melee attack against you and hits, you can make a single attack against that opponent as a free action. You suffer a -4 AC penalty for 1 round.',
        'special': 'You can use this feat once per round.'
    },
    'Knockback': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Bull Rush, Power Attack',
        'benefit': 'When you deal damage with a melee attack, you can immediately make a bull rush attempt as a free action.',
        'special': ''
    },
    'Knockdown': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Trip, Power Attack',
        'benefit': 'When you deal 10 or more points of damage with a melee attack, you can immediately make a trip attempt as a free action.',
        'special': ''
    },
    'Lightning Fists': {
        'type': 'General',
        'prerequisites': 'Dex 15, Improved Unarmed Strike, base attack bonus +3',
        'benefit': 'You can make one extra unarmed attack per round at your highest attack bonus, but all unarmed attacks suffer a -2 penalty.',
        'special': ''
    },
    'Monkey Grip': {
        'type': 'General',
        'prerequisites': 'Str 13, base attack bonus +1',
        'benefit': 'You can use weapons designed for creatures one size larger than you, but you suffer a -2 penalty on attack rolls.',
        'special': ''
    },
    'Pin Shield': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Disarm, Improved Shield Bash',
        'benefit': 'When you successfully disarm an opponent of their shield using a shield bash, you can immediately make a grapple check to pin the shield.',
        'special': ''
    },
    'Power Critical': {
        'type': 'General',
        'prerequisites': 'Weapon Focus with chosen weapon, base attack bonus +4',
        'benefit': 'Choose one weapon. Your threat range with that weapon increases by 1.',
        'special': 'You can gain this feat multiple times.'
    },
    'Prone Combat': {
        'type': 'General',
        'prerequisites': 'Dex 13, Dodge',
        'benefit': 'When fighting while prone, you gain a +4 dodge bonus to AC against ranged attacks and a +2 dodge bonus against melee attacks.',
        'special': ''
    },
    'Push Back': {
        'type': 'General',
        'prerequisites': 'Improved Unarmed Strike, Improved Trip',
        'benefit': 'When you successfully trip an opponent with an unarmed attack, you can push them back 5 feet.',
        'special': ''
    },
    'Rapid Stunning': {
        'type': 'General',
        'prerequisites': 'Dex 13, Wis 13, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'You can use Stunning Fist twice per round, but each use counts against your daily limit.',
        'special': ''
    },
    'Roundabout Kick': {
        'type': 'General',
        'prerequisites': 'Str 13, Improved Unarmed Strike, Power Attack',
        'benefit': 'As a standard action, you can make a single unarmed attack that affects all opponents adjacent to you.',
        'special': ''
    },
    'Shield Charge': {
        'type': 'General',
        'prerequisites': 'Improved Shield Bash, Shield Proficiency, base attack bonus +3',
        'benefit': 'When you charge with a shield, you can make a shield bash attack at the end of your charge and deal double damage.',
        'special': ''
    },
    'Shield Expert': {
        'type': 'General',
        'prerequisites': 'Shield Proficiency, base attack bonus +6',
        'benefit': 'You do not suffer the attack penalty for using a shield as a weapon.',
        'special': ''
    },
    'Shield Sling': {
        'type': 'General',
        'prerequisites': 'Str 13, Power Attack, Improved Shield Bash',
        'benefit': 'You can throw your shield as a ranged weapon. It deals damage as a club of its size and has a range increment of 10 feet.',
        'special': ''
    },
    'Shield Wall': {
        'type': 'General',
        'prerequisites': 'Shield Proficiency, base attack bonus +2',
        'benefit': 'When standing adjacent to an ally with a shield, you both gain a +2 shield bonus to AC.',
        'special': ''
    },
    'Spinning Hurl': {
        'type': 'General',
        'prerequisites': 'Dex 13, Improved Unarmed Strike, Improved Trip',
        'benefit': 'When you successfully trip an opponent, you can throw them 5 feet in any direction. They land prone and take 1d6 damage.',
        'special': ''
    },
    'Stone Power': {
        'type': 'General',
        'prerequisites': 'Str 15, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'Your unarmed strikes deal damage as if you were using a weapon two sizes larger.',
        'special': ''
    },
    'Street Smart': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Bluff checks and Gather Information checks.',
        'special': ''
    },
    'Superior Expertise': {
        'type': 'General',
        'prerequisites': 'Int 13, Combat Expertise, base attack bonus +6',
        'benefit': 'When using Combat Expertise, you can take a penalty of up to your base attack bonus (instead of up to 5).',
        'special': ''
    },
    'Swarm': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +5',
        'benefit': 'You gain a +2 bonus on attack rolls when adjacent to two or more allies.',
        'special': ''
    },
    'Throw Anything': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You do not suffer the -4 penalty for throwing improvised weapons.',
        'special': ''
    },
    'Weapon Supremacy': {
        'type': 'General',
        'prerequisites': 'Weapon Focus with chosen weapon, Weapon Specialization with chosen weapon, fighter level 18',
        'benefit': 'You gain a +2 bonus on damage rolls with your chosen weapon. This stacks with Weapon Specialization.',
        'special': ''
    },
    'Zanji Punch': {
        'type': 'General',
        'prerequisites': 'Str 13, Improved Unarmed Strike, Stunning Fist, base attack bonus +3',
        'benefit': 'You can forgo your Stunning Fist to deal an extra 1d6 points of damage instead.',
        'special': ''
    }
}
