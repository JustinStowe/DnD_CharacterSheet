"""
D&D 3rd Edition Feats from Magic of Faerûn
Feats specific to the Forgotten Realms setting
"""

MAGIC_OF_FAERUN_FEATS = {
    'Arcane Preparation': {
        'type': 'General',
        'prerequisites': 'Sorcerer level 1st',
        'benefit': 'You may prepare a limited number of your spells ahead of time, just as a wizard does. The number of spells you can prepare is equal to your Charisma modifier.',
        'special': 'Already included in Tome and Blood but also appears in Magic of Faerûn.'
    },
    'Bloodline of Fire': {
        'type': 'General',
        'prerequisites': 'Sorcerer level 1st',
        'benefit': 'You gain a +4 bonus on saving throws against fire effects. Once per day, you can reroll a failed save against a fire effect.',
        'special': 'Your draconic bloodline manifests as resistance to fire.'
    },
    'Circle Leader': {
        'type': 'Metamagic',
        'prerequisites': 'Circle Magic, caster level 5th',
        'benefit': 'You can lead a circle of spellcasters to combine their magical power. When leading a circle, you can add the spell levels of other participants to increase your effective caster level.',
        'special': 'Requires cooperation from other willing spellcasters.'
    },
    'Circle Magic': {
        'type': 'General',
        'prerequisites': 'Caster level 1st',
        'benefit': 'You can participate in circle magic, combining your power with other spellcasters who also have this feat.',
        'special': 'This feat allows collaborative spellcasting.'
    },
    'Coronach': {
        'type': 'General',
        'prerequisites': 'Perform (ballad) 4 ranks, bardic music ability',
        'benefit': 'You can use your bardic music to perform a coronach, a lament for the dead. This grants all allies within 30 feet a +2 morale bonus on attack rolls and damage rolls against undead.',
        'special': ''
    },
    'Dancer': {
        'type': 'General',
        'prerequisites': 'Perform (dance) 2 ranks, Dex 13',
        'benefit': 'You gain a +2 bonus on Balance and Tumble checks. When using bardic music, you can incorporate dance to gain additional benefits.',
        'special': ''
    },
    'Daylight Adaptation': {
        'type': 'General',
        'prerequisites': 'Drow',
        'benefit': 'You do not take the standard penalties for being in bright light.',
        'special': 'Drow normally take penalties in sunlight.'
    },
    'Deep Denizen': {
        'type': 'General',
        'prerequisites': 'Underdark native',
        'benefit': 'You gain darkvision with a range of 60 feet. If you already have darkvision, its range increases by 30 feet.',
        'special': ''
    },
    'Delay Potion': {
        'type': 'Item Creation',
        'prerequisites': 'Brew Potion, Alchemy 8 ranks',
        'benefit': 'You can create potions with delayed activation. The potion activates when a specified condition is met.',
        'special': ''
    },
    'Dragon Familiar': {
        'type': 'General',
        'prerequisites': 'Ability to acquire a new familiar, compatible alignment, caster level 3rd',
        'benefit': 'You can select a pseudodragon, faerie dragon, or similarly tiny dragon as your familiar.',
        'special': ''
    },
    'Dracomancy': {
        'type': 'General',
        'prerequisites': 'Ability to cast arcane spells, Knowledge (arcana) 4 ranks',
        'benefit': 'You gain a +2 bonus on caster level checks when casting spells that affect dragons. Dragons take a -2 penalty on saves against your spells.',
        'special': ''
    },
    'Elemental Bloodline': {
        'type': 'General',
        'prerequisites': 'Sorcerer level 1st',
        'benefit': 'Choose one elemental type (air, earth, fire, or water). You gain resistance 5 to the associated energy type and a +2 bonus on saves against spells and effects from that elemental type.',
        'special': ''
    },
    'Enhanced Familiar': {
        'type': 'General',
        'prerequisites': 'Ability to summon a familiar, caster level 3rd',
        'benefit': 'Your familiar gains +2 hit points per level of the master and a +1 natural armor bonus.',
        'special': ''
    },
    'Extra Music': {
        'type': 'General',
        'prerequisites': 'Bardic music ability',
        'benefit': 'You can use your bardic music four extra times per day.',
        'special': ''
    },
    'Foe Hunter': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'Select a creature type. You gain a +2 bonus on Bluff, Listen, Sense Motive, Spot, and Survival checks when using these skills against creatures of that type. You also gain a +2 bonus on weapon damage rolls against creatures of that type.',
        'special': 'You can gain this feat multiple times, selecting a different creature type each time.'
    },
    'Forester': {
        'type': 'General',
        'prerequisites': 'Survival 4 ranks',
        'benefit': 'You gain a +2 bonus on Hide, Move Silently, and Survival checks in forest terrain.',
        'special': ''
    },
    'Highborn Drow': {
        'type': 'General',
        'prerequisites': 'Drow, Cha 13',
        'benefit': 'You gain additional spell-like abilities: dancing lights 1/day, faerie fire 1/day, and levitate 1/day.',
        'special': ''
    },
    'Highborn Elf': {
        'type': 'General',
        'prerequisites': 'Elf or half-elf, Cha 13',
        'benefit': 'You gain the ability to cast one 0-level arcane spell per day as a spell-like ability.',
        'special': ''
    },
    'Highborn Gnome': {
        'type': 'General',
        'prerequisites': 'Gnome, Cha 13',
        'benefit': 'You gain additional spell-like abilities: dancing lights 3/day, ghost sound 3/day, and prestidigitation 3/day.',
        'special': ''
    },
    'Horse Nomad': {
        'type': 'General',
        'prerequisites': 'Ride 4 ranks',
        'benefit': 'You gain a +2 bonus on Handle Animal and Ride checks. You can mount or dismount as a free action.',
        'special': ''
    },
    'Innate Spell': {
        'type': 'Special',
        'prerequisites': 'Quicken Spell, Spellcraft 24 ranks, ability to cast 9th-level spells',
        'benefit': 'Choose one spell you can cast. You can now cast that spell as a spell-like ability a number of times per day equal to your key ability modifier.',
        'special': 'Already included in Tome and Blood.'
    },
    'Insidious Magic': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'A spell with the insidious magic metamagic feat applied is difficult to detect with detect magic. An insidious spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Inscribe Rune': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 9th',
        'benefit': 'You can inscribe magical runes of power. Inscribing a rune takes one day for each 1,000 gp in its base price.',
        'special': ''
    },
    'Mercantile Background': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Appraise and Diplomacy checks.',
        'special': ''
    },
    'Militia': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain proficiency with all simple and martial weapons and with light armor.',
        'special': ''
    },
    'Plague Resistant': {
        'type': 'General',
        'prerequisites': 'Con 13',
        'benefit': 'You gain a +4 bonus on saving throws against disease.',
        'special': ''
    },
    'Resist Poison': {
        'type': 'General',
        'prerequisites': 'Con 13',
        'benefit': 'You gain a +4 bonus on saving throws against poison.',
        'special': ''
    },
    'Shadow Weave Magic': {
        'type': 'General',
        'prerequisites': 'Ability to cast arcane spells',
        'benefit': 'You draw your arcane power from the Shadow Weave instead of the standard Weave. Spells from the schools of divination, enchantment, evocation, and transmutation are cast at -1 caster level. Spells from the schools of illusion and necromancy are cast at +1 caster level.',
        'special': 'This is a significant choice that affects how your magic works.'
    },
    'Silver Palm': {
        'type': 'General',
        'prerequisites': 'Cha 13',
        'benefit': 'You gain a +2 bonus on Bluff and Diplomacy checks when offering bribes or haggling prices.',
        'special': ''
    },
    'Smooth Talk': {
        'type': 'General',
        'prerequisites': 'Cha 13',
        'benefit': 'You gain a +2 bonus on Bluff and Diplomacy checks.',
        'special': ''
    },
    'Spellcasting Prodigy': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Choose a spellcasting class. Your key ability score for that class is treated as 2 points higher for the purpose of determining bonus spells and spell DCs.',
        'special': 'Must be taken at 1st level.'
    },
    'Spell Power': {
        'type': 'General',
        'prerequisites': 'Caster level 1st',
        'benefit': 'Choose a school of magic. Add +1 to your caster level when casting spells from that school.',
        'special': 'You can gain this feat multiple times, selecting a different school each time.'
    },
    'Strong Soul': {
        'type': 'General',
        'prerequisites': 'Iron Will',
        'benefit': 'You gain a +1 bonus on Fortitude saves in addition to your Iron Will bonus.',
        'special': ''
    },
    'Survivor': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Fortitude saves and Survival checks.',
        'special': ''
    },
    'Tattoo Magic': {
        'type': 'General',
        'prerequisites': 'Spellcaster level 1st',
        'benefit': 'Magical tattoos you create or that are placed on you are more effective. Add +1 to the DC of spells cast from tattoos you created.',
        'special': ''
    },
    'Theocrat': {
        'type': 'General',
        'prerequisites': 'Wis 13, ability to cast divine spells',
        'benefit': 'You gain a +2 bonus on Diplomacy checks when dealing with followers of your deity.',
        'special': ''
    },
    'Thug': {
        'type': 'General',
        'prerequisites': 'Str 13',
        'benefit': 'You gain a +2 bonus on Intimidate checks and grapple checks.',
        'special': ''
    }
}
