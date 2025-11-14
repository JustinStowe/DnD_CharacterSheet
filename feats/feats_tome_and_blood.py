"""
D&D 3rd Edition Feats from Tome and Blood
Feats focused on arcane and divine spellcasters
"""

TOME_AND_BLOOD_FEATS = {
    'Arcane Preparation': {
        'type': 'General',
        'prerequisites': 'Sorcerer or bard level 1st',
        'benefit': 'You may "prepare" your spells ahead of time, just as a wizard does. The number of spells you can prepare is equal to your Charisma modifier. You still use up spell slots when you cast spells.',
        'special': 'This feat allows spontaneous casters to gain some of the benefits of preparing spells.'
    },
    'Automatic Quicken Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Quicken Spell, Spellcraft 30 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You may cast all 0-, 1st-, 2nd-, and 3rd-level spells as quickened spells without using higher-level spell slots. All limitations and conditions of Quicken Spell apply.',
        'special': 'This is an extremely powerful feat for high-level spellcasters.'
    },
    'Automatic Silent Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Silent Spell, Spellcraft 27 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You may cast all spells of 6th level and lower as silent spells without using higher-level spell slots.',
        'special': ''
    },
    'Automatic Still Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Still Spell, Spellcraft 27 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You may cast all spells of 6th level and lower as stilled spells without using higher-level spell slots.',
        'special': ''
    },
    'Chain Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can modify a spell that affects a single target to affect multiple targets in a chain. After the initial target, the spell can jump to a number of secondary targets equal to your caster level (maximum 20). Each secondary target must be within 30 feet of the previous target. A chained spell uses up a spell slot three levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Delay Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can cast a spell and delay its effect. The spell activates when a specified condition occurs. A delayed spell uses up a spell slot three levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Effortless Magic': {
        'type': 'General',
        'prerequisites': 'Spellcaster level 10th, ability to spontaneously cast spells',
        'benefit': 'You can cast one spell per day as a free action, as long as its casting time is normally 1 standard action. The spell must be one you can cast spontaneously.',
        'special': ''
    },
    'Empower Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'When you turn or rebuke undead, you add your Charisma bonus to the turning damage.',
        'special': ''
    },
    'Energy Admixture': {
        'type': 'Metamagic',
        'prerequisites': 'Energy Substitution',
        'benefit': 'You can cast a spell that uses energy to deal damage and choose to have it deal both its normal energy type and the energy type you selected with Energy Substitution. The spell uses up a spell slot four levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Energy Substitution': {
        'type': 'Metamagic',
        'prerequisites': 'Knowledge (arcana) 5 ranks or Knowledge (nature) 5 ranks',
        'benefit': 'Choose one type of energy: acid, cold, electricity, fire, or sonic. You can then modify any spell with an energy descriptor by substituting the spell\'s normal energy type with the chosen type. An energy substituted spell uses up a spell slot of the same level as the spell\'s actual level.',
        'special': 'You can gain this feat multiple times, selecting a different energy type each time.'
    },
    'Eschew Materials': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You can cast spells without needing material components, provided the component has no listed cost.',
        'special': 'This feat is already in the Player\'s Handbook but is particularly useful for spellcasters.'
    },
    'Extend Rage': {
        'type': 'General',
        'prerequisites': 'Barbarian rage ability',
        'benefit': 'Each of your rages lasts an additional 5 rounds beyond its normal duration.',
        'special': ''
    },
    'Extra Slot': {
        'type': 'General',
        'prerequisites': 'Spellcaster level 3rd',
        'benefit': 'You gain one extra spell slot. You must specify the level of the slot (it cannot exceed the highest level spell you can cast minus one).',
        'special': 'You can gain this feat multiple times, selecting a different spell level each time.'
    },
    'Extra Smiting': {
        'type': 'General',
        'prerequisites': 'Smite ability',
        'benefit': 'You can use your smite ability two extra times per day.',
        'special': ''
    },
    'Extra Spell': {
        'type': 'General',
        'prerequisites': 'Spellcaster level 1st',
        'benefit': 'You add one spell to your list of spells known. The spell must be of a level you can already cast.',
        'special': 'You can gain this feat multiple times. This is particularly useful for sorcerers and bards.'
    },
    'Extra Wild Shape': {
        'type': 'General',
        'prerequisites': 'Wild shape ability',
        'benefit': 'You can use your wild shape ability two extra times per day.',
        'special': ''
    },
    'Innate Spell': {
        'type': 'Special',
        'prerequisites': 'Quicken Spell, Spellcraft 24 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'Choose one spell you can cast. You can now cast that spell as a spell-like ability a number of times per day equal to your key ability modifier (minimum 1). An innate spell has no verbal, somatic, material, focus, or XP components.',
        'special': 'The spell must be one you know and can cast. You can gain this feat multiple times.'
    },
    'Maximize Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'Once per day, when you turn or rebuke undead, you can maximize the result. All variable, numeric effects of the turning are maximized.',
        'special': ''
    },
    'Persistent Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Extend Spell',
        'benefit': 'A persistent spell has a duration of 24 hours. The spell must have a duration of at least 1 round and must affect one or more targets or an area. A persistent spell uses up a spell slot six levels higher than the spell\'s actual level.',
        'special': 'This is extremely powerful for long-duration buffs.'
    },
    'Quicken Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'You can turn or rebuke undead as a free action. You may still only make one turning attempt per round.',
        'special': ''
    },
    'Rapid Spontaneous Casting': {
        'type': 'General',
        'prerequisites': 'Ability to spontaneously cast cure or inflict spells',
        'benefit': 'You can spontaneously cast cure or inflict spells as a free action (instead of a full-round action). You may do this a number of times per day equal to your Wisdom modifier (minimum 1).',
        'special': ''
    },
    'Reaching Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can alter a spell with a range of touch to have a range of 30 feet. A reaching spell uses up a spell slot two levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Repeat Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'A repeated spell is automatically cast again at the beginning of your next turn. No matter how many times the spell is repeated, it counts as one spell for the purposes of dispelling. A repeated spell uses up a spell slot three levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Sacred Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Ability to cast divine spells',
        'benefit': 'Half of the damage dealt by a sacred spell is converted to sacred energy and is not subject to energy resistance or immunity. A sacred spell uses up a spell slot two levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Sacred Vengeance': {
        'type': 'General',
        'prerequisites': 'Smite evil or smite good ability',
        'benefit': 'Once per day, when you successfully smite a foe, you can immediately make another smite attempt as a free action.',
        'special': ''
    },
    'Scribe Tattoo': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 3rd',
        'benefit': 'You can create magical tattoos. Scribing a tattoo takes one day for each 1,000 gp in its base price.',
        'special': 'Magical tattoos function as scrolls but are inscribed on the body.'
    },
    'Server': {
        'type': 'General',
        'prerequisites': 'Ability to scry',
        'benefit': 'When you use a scrying spell and the target fails its save, you can also cast one of the following spells through the sensor: comprehend languages, detect magic, read magic, or tongues.',
        'special': ''
    },
    'Spell Focus': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Add +1 to the DC for all saving throws against spells from the school of magic you select.',
        'special': 'You can gain this feat multiple times. This is already in the Player\'s Handbook.'
    },
    'Spell Thematics': {
        'type': 'General',
        'prerequisites': 'Spellcraft 4 ranks',
        'benefit': 'Your spells have a distinctive visual or auditory signature. You gain a +2 bonus on Spellcraft checks to identify spells you cast.',
        'special': 'This is primarily a roleplaying feat.'
    },
    'Spontaneous Divination': {
        'type': 'General',
        'prerequisites': 'Knowledge (arcana) 4 ranks or Knowledge (religion) 4 ranks, ability to cast divination spells',
        'benefit': 'You can spontaneously convert prepared spells into divination spells of the same level that you know.',
        'special': ''
    },
    'Spontaneous Wounder': {
        'type': 'General',
        'prerequisites': 'Ability to spontaneously cast inflict spells',
        'benefit': 'When you spontaneously cast an inflict spell, you add your Wisdom modifier to the damage dealt.',
        'special': ''
    },
    'Sudden Empower': {
        'type': 'General',
        'prerequisites': 'Empower Spell',
        'benefit': 'Once per day, you can apply the effect of Empower Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Enlarge': {
        'type': 'General',
        'prerequisites': 'Enlarge Spell',
        'benefit': 'Once per day, you can apply the effect of Enlarge Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Extend': {
        'type': 'General',
        'prerequisites': 'Extend Spell',
        'benefit': 'Once per day, you can apply the effect of Extend Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Maximize': {
        'type': 'General',
        'prerequisites': 'Maximize Spell',
        'benefit': 'Once per day, you can apply the effect of Maximize Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Quicken': {
        'type': 'General',
        'prerequisites': 'Quicken Spell',
        'benefit': 'Once per day, you can apply the effect of Quicken Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Silent': {
        'type': 'General',
        'prerequisites': 'Silent Spell',
        'benefit': 'Once per day, you can apply the effect of Silent Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Still': {
        'type': 'General',
        'prerequisites': 'Still Spell',
        'benefit': 'Once per day, you can apply the effect of Still Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Sudden Widen': {
        'type': 'General',
        'prerequisites': 'Widen Spell',
        'benefit': 'Once per day, you can apply the effect of Widen Spell to a spell as you cast it without increasing the spell\'s level or casting time.',
        'special': ''
    },
    'Tattoo Focus': {
        'type': 'General',
        'prerequisites': 'Scribe Tattoo',
        'benefit': 'Your magical tattoos are more potent. Add +1 to the DC for all saving throws against spells cast from your tattoos.',
        'special': ''
    },
    'Twin Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can cast a spell that affects a single target twice, with each casting affecting a different target. Both targets must be within the spell\'s range and within 30 feet of each other. A twinned spell uses up a spell slot four levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Zones of Silence': {
        'type': 'General',
        'prerequisites': 'Ability to cast silence',
        'benefit': 'You can control the shape of the silence spell, creating "holes" in the area of effect.',
        'special': ''
    }
}
