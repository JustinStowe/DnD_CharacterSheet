"""
D&D 3rd Edition Epic Feats from Epic Level Handbook
Feats available to characters level 21+
"""

EPIC_FEATS = {
    'Epic Weapon Focus': {
        'type': 'Epic',
        'prerequisites': 'Fighter level 8th, Weapon Focus',
        'benefit': '+2 bonus on attack rolls with one weapon type (stacks with Weapon Focus)',
        'special': 'Can be taken multiple times for different weapons'
    },
    'Epic Weapon Specialization': {
        'type': 'Epic',
        'prerequisites': 'Fighter level 12th, Weapon Specialization',
        'benefit': '+4 bonus on damage rolls with one weapon type (stacks with Weapon Specialization)',
        'special': 'Can be taken multiple times for different weapons'
    },
    'Epic Toughness': {
        'type': 'Epic',
        'prerequisites': 'Constitution 21+',
        'benefit': '+30 hit points',
        'special': 'Can be taken multiple times'
    },
    'Epic Fortitude': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Fortitude saves',
        'special': 'Can be taken multiple times'
    },
    'Epic Reflexes': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Reflex saves',
        'special': 'Can be taken multiple times'
    },
    'Epic Will': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+4 bonus on Will saves',
        'special': 'Can be taken multiple times'
    },
    'Armor Skin': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 natural armor bonus to AC',
        'special': 'Can be taken multiple times (max +10)'
    },
    'Blinding Speed': {
        'type': 'Epic',
        'prerequisites': 'Dexterity 25+',
        'benefit': 'Act as if affected by haste for 5 rounds per day',
        'special': 'Can be taken multiple times (adds 5 rounds each)'
    },
    'Combat Insight': {
        'type': 'Epic',
        'prerequisites': 'Wisdom 21+, BAB +15',
        'benefit': 'Add Wisdom modifier to melee attack rolls',
        'special': 'Does not stack with other Wisdom bonuses to attack'
    },
    'Damage Reduction': {
        'type': 'Epic',
        'prerequisites': 'Constitution 21+',
        'benefit': 'Gain DR 3/—',
        'special': 'Can be taken multiple times (adds DR 3/—)'
    },
    'Devastating Critical': {
        'type': 'Epic',
        'prerequisites': 'Str 25+, Cleave, Great Cleave, Improved Critical, Power Attack, BAB +20',
        'benefit': 'When you score a critical hit with the chosen weapon, target must make Fort save (DC 10 + 1/2 HD + Str mod) or die instantly',
        'special': 'Choose one weapon type'
    },
    'Epic Dodge': {
        'type': 'Epic',
        'prerequisites': 'Dex 25+, Dodge, Defensive Roll, Improved Evasion, BAB +15',
        'benefit': 'Once per round, automatically avoid one attack that would hit you',
        'special': 'You must be aware of attack'
    },
    'Epic Endurance': {
        'type': 'Epic',
        'prerequisites': 'Constitution 25+, Endurance',
        'benefit': '+10 bonus on Concentration checks, sleep in armor without fatigue',
        'special': ''
    },
    'Epic Prowess': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 bonus on all attack rolls',
        'special': 'Can be taken multiple times'
    },
    'Epic Reputation': {
        'type': 'Epic',
        'prerequisites': 'Charisma 25+',
        'benefit': '+4 bonus on Bluff, Diplomacy, Gather Information, Intimidate, Perform checks',
        'special': ''
    },
    'Epic Skill Focus': {
        'type': 'Epic',
        'prerequisites': 'Skill Focus with the skill, 20 ranks in skill',
        'benefit': '+10 bonus to the chosen skill (stacks with Skill Focus)',
        'special': 'Can be taken multiple times for different skills'
    },
    'Epic Speed': {
        'type': 'Epic',
        'prerequisites': 'Dexterity 21+',
        'benefit': 'Base land speed increases by 30 feet',
        'special': 'Can be taken multiple times'
    },
    'Epic Spell Focus': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Focus in the school, ability to cast 9th-level spells',
        'benefit': '+1 bonus to the DC of all spells from the chosen school (stacks with Spell Focus and Greater Spell Focus)',
        'special': 'Can be taken multiple times for different schools'
    },
    'Epic Spell Penetration': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Penetration, ability to cast 9th-level spells',
        'benefit': '+2 bonus on caster level checks to overcome spell resistance (stacks with Spell Penetration)',
        'special': 'Can be taken multiple times'
    },
    'Epic Spellcasting': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 24 ranks, Knowledge (arcana) 24 ranks (or Knowledge (religion) for divine), ability to cast 9th-level spells',
        'benefit': 'Can develop and cast epic spells',
        'special': 'Most powerful epic feat for spellcasters'
    },
    'Fast Healing': {
        'type': 'Epic',
        'prerequisites': 'Constitution 25+',
        'benefit': 'Gain fast healing 3',
        'special': 'Can be taken multiple times (adds fast healing 3)'
    },
    'Great Constitution': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Constitution',
        'special': 'Can be taken multiple times'
    },
    'Great Dexterity': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Dexterity',
        'special': 'Can be taken multiple times'
    },
    'Great Intelligence': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Intelligence',
        'special': 'Can be taken multiple times'
    },
    'Great Strength': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Strength',
        'special': 'Can be taken multiple times'
    },
    'Great Wisdom': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Wisdom',
        'special': 'Can be taken multiple times'
    },
    'Great Charisma': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': '+1 to Charisma',
        'special': 'Can be taken multiple times'
    },
    'Great Smiting': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Smite evil class ability',
        'benefit': 'Add Charisma bonus to damage when using smite evil (in addition to level)',
        'special': ''
    },
    'Improved Aura of Courage': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Aura of courage class ability',
        'benefit': 'Aura of courage grants immunity to fear instead of +4 bonus',
        'special': ''
    },
    'Improved Combat Casting': {
        'type': 'Epic',
        'prerequisites': 'Combat Casting, Concentration 25 ranks',
        'benefit': '+4 bonus on Concentration checks to cast defensively, no attacks of opportunity when casting',
        'special': ''
    },
    'Improved Combat Reflexes': {
        'type': 'Epic',
        'prerequisites': 'Dex 21+, Combat Reflexes',
        'benefit': 'No limit to attacks of opportunity per round',
        'special': 'Still limited by reach'
    },
    'Improved Ki Strike': {
        'type': 'Epic',
        'prerequisites': 'Wis 21+, Ki strike class ability',
        'benefit': 'Ki strike counts as +1 enhancement bonus higher for overcoming DR',
        'special': 'Can be taken multiple times'
    },
    'Improved Sneak Attack': {
        'type': 'Epic',
        'prerequisites': 'Sneak attack +8d6',
        'benefit': '+1d6 to sneak attack damage',
        'special': 'Can be taken multiple times'
    },
    'Improved Spell Capacity': {
        'type': 'Epic',
        'prerequisites': 'Ability to cast spells of the normal maximum spell level in at least one class',
        'benefit': 'Gain one spell slot of up to 10th-13th level (10th with first feat, 11th with second, etc.)',
        'special': 'Can be taken multiple times, choose spell level each time'
    },
    'Improved Stunning Fist': {
        'type': 'Epic',
        'prerequisites': 'Dex 19+, Wis 19+, Stunning Fist, BAB +15',
        'benefit': '+2 DC for stunning fist attacks',
        'special': 'Can be taken multiple times'
    },
    'Improved Whirlwind Attack': {
        'type': 'Epic',
        'prerequisites': 'Int 13+, Dex 23+, Combat Expertise, Dodge, Mobility, Spring Attack, Whirlwind Attack, BAB +25',
        'benefit': 'Can make one extra attack at your highest BAB during Whirlwind Attack',
        'special': ''
    },
    'Infinite Deflection': {
        'type': 'Epic',
        'prerequisites': 'Dex 25+, Deflect Arrows, Improved Unarmed Strike, BAB +25',
        'benefit': 'Deflect any number of ranged attacks per round',
        'special': 'Must be aware and have hand free'
    },
    'Instant Reload': {
        'type': 'Epic',
        'prerequisites': 'Quick Draw, Rapid Reload, Weapon Focus (crossbow)',
        'benefit': 'Reload any crossbow as a free action',
        'special': ''
    },
    'Legendary Commander': {
        'type': 'Epic',
        'prerequisites': 'Cha 25+, Epic Leadership, Leadership',
        'benefit': 'Attract cohort and followers as if character level is 4 levels higher',
        'special': ''
    },
    'Legendary Rider': {
        'type': 'Epic',
        'prerequisites': 'Ride 24 ranks',
        'benefit': '+10 to Ride checks, can make Ride check as free action',
        'special': ''
    },
    'Legendary Tracker': {
        'type': 'Epic',
        'prerequisites': 'Wis 25+, Track, 30 ranks in Survival',
        'benefit': 'Track creatures across water, through air, or through solid rock',
        'special': ''
    },
    'Overwhelming Critical': {
        'type': 'Epic',
        'prerequisites': 'Str 23+, Cleave, Great Cleave, Improved Critical, Power Attack, BAB +20',
        'benefit': 'When you score a critical hit, target takes +1d6 damage per die of weapon base damage',
        'special': 'Choose one weapon type'
    },
    'Perfect Health': {
        'type': 'Epic',
        'prerequisites': 'Con 25+, Great Fortitude',
        'benefit': 'Immune to all non-magical diseases, +4 to saves vs magical diseases',
        'special': ''
    },
    'Permanent Emanation': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 25 ranks, ability to cast the spell',
        'benefit': 'One spell with area "emanation from you" becomes permanent',
        'special': 'Can be taken multiple times for different spells'
    },
    'Polyglot': {
        'type': 'Epic',
        'prerequisites': 'Int 25+, Speak Language (10 languages)',
        'benefit': 'Can speak all languages',
        'special': ''
    },
    'Spell Knowledge': {
        'type': 'Epic',
        'prerequisites': 'Ability to cast spells',
        'benefit': 'Learn one additional spell of any level you can cast',
        'special': 'Can be taken multiple times'
    },
    'Spell Opportunity': {
        'type': 'Epic',
        'prerequisites': 'Combat Casting, Spellcraft 25 ranks',
        'benefit': 'Cast a quickened spell as an attack of opportunity',
        'special': ''
    },
    'Spell Stowaway': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 24 ranks, caster level 15th',
        'benefit': 'When targeted by a spell, can make Spellcraft check to "catch" the spell and cast it later',
        'special': ''
    },
    'Spontaneous Spell': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 25 ranks, ability to cast the spell',
        'benefit': 'Cast one chosen spell spontaneously by sacrificing a prepared spell',
        'special': 'For prepared spellcasters. Can be taken multiple times'
    },
    'Superior Initiative': {
        'type': 'Epic',
        'prerequisites': 'Improved Initiative',
        'benefit': '+8 bonus on initiative checks (stacks with Improved Initiative for total +12)',
        'special': ''
    },
    'Swarm of Arrows': {
        'type': 'Epic',
        'prerequisites': 'Dex 23+, Point Blank Shot, Rapid Shot, Manyshot, BAB +25',
        'benefit': 'As full attack, fire arrows at full BAB at all targets in 30 ft. area',
        'special': ''
    },
    'Tenacious Magic': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 15 ranks',
        'benefit': 'Choose one spell you can cast, it requires two successful dispels to remove',
        'special': 'Can be taken multiple times for different spells'
    },
    'Uncanny Accuracy': {
        'type': 'Epic',
        'prerequisites': 'Dex 21+, Point Blank Shot, Precise Shot, BAB +20',
        'benefit': 'Ranged attacks ignore miss chance from concealment (except total concealment)',
        'special': ''
    }
}
