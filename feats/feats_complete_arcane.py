"""

D&D 3rd Edition Feats from Complete Arcane

Feats for wizards, sorcerers, bards, and other arcane spellcasters

"""

COMPLETE_ARCANE_FEATS = {

    'Arcane Defense': {
        'type': 'General',
        'prerequisites': 'Spell Focus in the chosen school',
        'benefit': 'You get a +3 bonus on your saving throws against spells from the chosen school.',
        'special': 'You can gain this feat multiple times, but its effects do not stack. Each time you take the feat, it applies to a new school of magic.'
    },

    'Arcane Mastery': {
        'type': 'General',
        'prerequisites': 'Ability to cast arcane spells or use spell-like abilities including invocations',
        'benefit': 'You can take 10 on caster level checks as if the caster level check was a skill check.',
        'special': ''
    },

    'Arcane Preparation': {
        'type': 'General',
        'prerequisites': 'Ability to cast arcane spells without preparation',
        'benefit': 'Each day, you can use one or more of your spell slots to prepare spells you know, usually for the purpose of applying a metamagic feat to the spell but without an increase in casting time.',
        'special': ''
    },

    'Battle Caster': {
        'type': 'General',
        'prerequisites': 'Ability to ignore arcane spell failure chance from armor',
        'benefit': 'You are able to wear armor one category heavier than you can normally wear while still avoiding the chance of arcane spell failure.',
        'special': 'This ability does not extend to shields, nor does it apply to spells gained from spellcasting classes other than the class that provides the ability to cast arcane spells while in armor.'
    },

    'Black Lore of Moil': {
        'type': 'Metamagic',
        'prerequisites': 'Spell Focus (necromancy), caster level 7th',
        'benefit': 'Any necromancy spell you cast can be cast instead as a Moilian spell, dealing an extra 1d6 points of negative energy damage (1d6 per two spell levels).',
        'special': 'Moilian spells require the creation and expenditure of a Moilian rune-bone.'
    },

    'Born of the Three Thunders': {
        'type': 'Metamagic',
        'prerequisites': 'Knowledge (nature) 4 ranks, Energy Substitution (electricity)',
        'benefit': 'When you cast a spell with the electricity or sonic descriptor that deals hit point damage, half deals as electricity and half as sonic damage. The spell concludes with a thunderclap that stuns creatures unless they save.',
        'special': 'You are automatically dazed for 1 round after casting a Three Thunders spell.'
    },

    'Chain Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'Any spell that specifies a single target and has a range greater than touch can be chained to affect secondary targets equal to your caster level (maximum 20).',
        'special': 'A chained spell uses up a spell slot three levels higher than the spells actual level.'
    },

    'Communicator': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You can use arcane mark, comprehend languages, and message as spell-like abilities once per day each.',
        'special': ''
    },

    'Cooperative Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'You and another spellcaster with this feat can simultaneously cast the same spell. Add +2 to the save DC and +1 to caster level checks.',
        'special': 'A cooperative spell uses up a spell slot of the same level as the spells actual level.'
    },

    'Craft Contingent Spell': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 11th',
        'benefit': 'You can make contingent any spell that you know. Crafting takes one day per 1,000 gp in the spells base price.',
        'special': ''
    },

    'Delay Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'When casting a spell, you set a delay of 1 to 5 rounds before it takes effect.',
        'special': 'Only area, personal, and touch spells can be affected by this feat. A delayed spell uses up a spell slot three levels higher than the spells actual level.'
    },

    'Double Wand Wielder': {
        'type': 'General',
        'prerequisites': 'Craft Wand, Two-Weapon Fighting',
        'benefit': 'As a full-round action, you can wield a wand in each hand. Each use of the secondary wand expends 2 charges instead of 1.',
        'special': ''
    },

    'Draconic Breath': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'As a standard action, you can change arcane spell energy into a breath weapon. The breath weapon is a 30-foot cone or 60-foot line dealing 2d6 points of damage per level of the spell expended.',
        'special': ''
    },

    'Draconic Claw': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'You gain claws. In any round when you cast a spell with a casting time of 1 standard action, you can make a single claw attack as a swift action.',
        'special': ''
    },

    'Draconic Flight': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'After you cast an arcane spell with a casting time of 1 standard action, you gain a fly speed equal to 10 feet per level of the spell for the remainder of your turn.',
        'special': ''
    },

    'Draconic Heritage': {
        'type': 'Draconic',
        'prerequisites': 'Sorcerer level 1st',
        'benefit': 'Choose one dragon and gain the indicated skill as a class skill. You gain a bonus on saving throws against sleep and paralysis.',
        'special': 'This draconic heritage cannot be changed once the feat has been taken.'
    },

    'Draconic Legacy': {
        'type': 'Draconic',
        'prerequisites': 'Any four draconic feats',
        'benefit': 'Based on your draconic heritage, add specified spells to your list of spells known.',
        'special': ''
    },

    'Draconic Power': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'Your caster level increases by 1, and you add 1 to the save DC of all arcane spells with the energy descriptor matching your draconic heritage.',
        'special': ''
    },

    'Draconic Presence': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'You gain a spell-like ability based on your draconic heritage. When you cast a spell, lower-level opponents must make a Will save or become frightened.',
        'special': ''
    },

    'Draconic Resistance': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'You gain resistance to energy of the type of your Draconic Heritage equal to 5 + 1 per 3 draconic feats you have.',
        'special': ''
    },

    'Draconic Skin': {
        'type': 'Draconic',
        'prerequisites': 'Draconic Heritage',
        'benefit': 'Your natural armor increases by 1. This bonus increases by 1 for every 4 additional draconic feats you have (maximum 5).',
        'special': ''
    },

    'Energy Admixture': {
        'type': 'Metamagic',
        'prerequisites': 'Energy Substitution',
        'benefit': 'You can double the damage dealt by an energy spell by adding an additional energy type to the spell.',
        'special': 'An energy admixture spell uses up a spell slot one level higher than the spells actual level.'
    },

    'Energy Substitution': {
        'type': 'Metamagic',
        'prerequisites': 'Any other metamagic feat, Knowledge (arcana) 5 ranks',
        'benefit': 'Select an energy type. You can cast spells that deal energy damage of one type as if they dealt energy damage of your chosen type instead.',
        'special': 'You can gain this feat multiple times, selecting a different energy type each time.'
    },

    'Explosive Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Creatures caught in an explosive spell are blasted to the edge of the spells area.',
        'special': 'An explosive spell uses up a spell slot one level higher than the spells actual level.'
    },

    'Extra Edge': {
        'type': 'General',
        'prerequisites': 'Warmage level 4th',
        'benefit': 'You gain +1 bonus to your warmage edge ability, plus you gain an additional 14 warmage levels worth of advancement.',
        'special': ''
    },

    'Extra Invocation': {
        'type': 'General',
        'prerequisites': 'Ability to use lesser invocations',
        'benefit': 'You learn an additional invocation of one grade less than your current highest grade of invocation.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Extra Slot': {
        'type': 'General',
        'prerequisites': 'Caster level 4th',
        'benefit': 'You gain an extra spell slot up to one level lower than your current highest-level spell slot.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Extra Spell': {
        'type': 'General',
        'prerequisites': 'Caster level 3rd',
        'benefit': 'You learn an additional spell up to one level lower than your current highest-level spells.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Fortify Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can cast spells at high caster level to overcome spell resistance without increasing the spells level or casting time.',
        'special': ''
    },

    'Heighten Spell-Like Ability': {
        'type': 'General',
        'prerequisites': 'Spell-like ability at caster level 6th or higher',
        'benefit': 'You can use a spell-like ability at a higher level (up to 3 times per day).',
        'special': ''
    },

    'Innate Spell': {
        'type': 'General',
        'prerequisites': 'Quicken Spell, Silent Spell, Still Spell',
        'benefit': 'You can use one spell as a spell-like ability once per round.',
        'special': ''
    },

    'Maximize Spell-Like Ability': {
        'type': 'General',
        'prerequisites': 'Spell-like ability at caster level 6th or higher',
        'benefit': 'You can use a spell-like ability with its variable numeric effects maximized up to 3 times per day.',
        'special': ''
    },

    'Mage Slayer': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Spellcraft 2 ranks, base attack bonus +3',
        'benefit': 'You gain +1 bonus on Will saves against spellcasters you threaten. Spellcasters you threaten cannot cast defensively.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Pierce Magical Concealment': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Con 13, Blind-Fight, Mage Slayer',
        'benefit': 'You ignore spell-based concealment of creatures you attack.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Pierce Magical Protection': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Con 13, Mage Slayer',
        'benefit': 'You ignore spell-based bonuses to Armor Class when attacking creatures.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Practiced Spellcaster': {
        'type': 'General',
        'prerequisites': 'Spellcraft 4 ranks',
        'benefit': 'Your caster level for a chosen spellcasting class increases by 4, but not above your HD.',
        'special': 'You can gain this feat multiple times, applying it to a different spellcasting class each time.'
    },

    'Ranged Spell Specialization': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Weapon Focus (ranged spell), caster level 4th',
        'benefit': 'You gain +2 bonus on damage rolls with ranged spells.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Reckless Wand Wielder': {
        'type': 'General',
        'prerequisites': 'Craft Wand, Use Magic Device 1 rank',
        'benefit': 'You can increase a wands caster level by expending an additional charge.',
        'special': ''
    },

    'Sudden Empower': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'You can increase a spells variable numeric effects by 50% without special preparation (1/day).',
        'special': ''
    },

    'Sudden Enlarge': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can double a spells duration without special preparation (1/day).',
        'special': ''
    },

    'Sudden Maximize': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'You can maximize a spells variable numeric effects without special preparation (1/day).',
        'special': ''
    },

    'Sudden Quicken': {
        'type': 'Metamagic',
        'prerequisites': 'Quicken Spell, Sudden Empower, Sudden Extend, Sudden Maximize, Sudden Silent, Sudden Still',
        'benefit': 'You can cast spells as a swift action without special preparation (1/day).',
        'special': ''
    },

    'Sudden Silent': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can cast spells without verbal components without special preparation (1/day).',
        'special': ''
    },

    'Sudden Still': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can cast spells without somatic components without special preparation (1/day).',
        'special': ''
    },

    'Sudden Widen': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can increase a spells numeric measurements by 50% without special preparation (1/day).',
        'special': ''
    },

    'Touch Spell Specialization': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Weapon Focus (touch spell), caster level 4th',
        'benefit': 'You gain +2 bonus on damage rolls with touch spells.',
        'special': 'A fighter may select this feat as one of his fighter bonus feats.'
    },

    'Transdimensional Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Your spells affect creatures in coexistent planes and extradimensional spaces whose entrances fall within the spells area.',
        'special': 'A transdimensional spell uses up a spell slot one level higher than the spells actual level.'
    },

    'Twin Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any metamagic feat',
        'benefit': 'You can simultaneously cast a single spell twice.',
        'special': 'A twin spell uses up a spell slot six levels higher than the spells actual level.'
    },

    'Wandstrike': {
        'type': 'General',
        'prerequisites': 'Use Magic Device 4 ranks',
        'benefit': 'You can make a touch attack with a wand to deal 1d6 damage and target the creature hit with the spells effect.',
        'special': ''
    }

}
