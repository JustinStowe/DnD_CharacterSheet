"""

D&D 3rd Edition Feats from Complete Champion

Feats for champions of good, paladins, and righteous warriors

"""

COMPLETE_CHAMPION_FEATS = {

    'Air Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain sacred bonus to AC increasing by 1 per 4 character levels. Thrown/projectile weapons have 50% miss chance against you.',
        'special': 'You can select this feat multiple times. You gain one additional daily use each time. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Animal Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain ability to enhance yourself with animal characteristics (Apes Fury, Cheetahs Sprint, Hawks Flight, or Serpents Strike).',
        'special': 'You can select this feat multiple times. You can have multiple abilities active simultaneously but only activate one ability per round.'
    },

    'Awesome Smite': {
        'type': 'Tactical',
        'prerequisites': 'Power Attack, base attack bonus +6, smite ability',
        'benefit': 'Enables three tactical maneuvers: Demolishing Smite (ignore DR), Overwhelming Smite (trip attack), and Seeking Smite (ignore miss chance).',
        'special': ''
    },

    'Battle Blessing': {
        'type': 'General',
        'prerequisites': 'Ability to cast paladin spells',
        'benefit': 'Cast most paladin spells faster: standard action becomes swift action, full round becomes standard action.',
        'special': ''
    },

    'Bestial Charge': {
        'type': 'Tactical',
        'prerequisites': 'Base attack bonus +4, wild shape class feature',
        'benefit': 'Enables three tactical maneuvers: Pouncing Charge (full attack after charge), Striking Charge (extra reach), and Twisting Charge (change direction).',
        'special': ''
    },

    'Chaos Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Roll 1d6 to determine random bonuses: odd adds to attack rolls, even adds to AC. Die increases to d8 at 10th level, d10 at 15th level.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Charnel Miasma': {
        'type': 'Reserve',
        'prerequisites': 'Access to the Death domain',
        'benefit': 'Exude scent of grave. Force foes within 30 feet to make Will saves or become shaken. Gain +1 competence bonus to caster level for death spells.',
        'special': ''
    },

    'Death Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Cause one melee weapon to radiate negative energy for 1 minute. Successful hits force Fortitude saves or grant negative levels.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Destruction Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Reduce struck opponents armor or natural armor bonus by 1 per hit. At 10th level, reduce by 2 per hit.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Earth Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Ignore effects of difficult terrain for yourself or make terrain difficult to move through within 30 feet.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Elemental Essence': {
        'type': 'Wild',
        'prerequisites': 'Any other wild feat, wild shape class feature',
        'benefit': 'Spend a wild shape use to surround limbs/weapons with chosen energy (acid, cold, electricity, or fire). Deal 1d6 extra damage and gain resistance 5.',
        'special': 'You can select this feat multiple times for different energy types. You cannot activate multiple types simultaneously.'
    },

    'Evil Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Surround yourself and allies within 30 feet with aura granting damage reduction that can only be overcome by good weapons.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Fire Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Sheathe yourself in harmless flames for 1 minute. Melee attacks deal extra fire damage. Injured foes must save or burn for 1d4 rounds.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Fragile Construct': {
        'type': 'Reserve',
        'prerequisites': 'Access to the Destruction domain',
        'benefit': 'Reduce hardness or damage reduction of touched object/construct by highest-level Destruction domain spell available.',
        'special': ''
    },

    'Good Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Surround yourself and allies within 30 feet with aura granting damage reduction that can only be overcome by evil weapons.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Great and Small': {
        'type': 'Wild',
        'prerequisites': 'Wild shape class feature, ability to assume the form of a Large creature',
        'benefit': 'Grow or shrink one size category by spending a wild shape use.',
        'special': ''
    },

    'Healing Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain or grant yourself fast healing as a swift action for 1 minute.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Holy Potency': {
        'type': 'Tactical',
        'prerequisites': 'Base attack bonus +4, ability to spontaneously cast cure or inflict spells, ability to turn or rebuke undead',
        'benefit': 'Enables maneuvers to manipulate positive or negative energy.',
        'special': ''
    },

    'Holy Warrior': {
        'type': 'Reserve',
        'prerequisites': 'Ability to cast 4th-level spells, access to the War domain',
        'benefit': 'Gain bonus on weapon damage rolls based on highest-level War domain spell available.',
        'special': ''
    },

    'Imbued Healing': {
        'type': 'Metamagic',
        'prerequisites': 'Ability to cast conjuration healing spells, access to one or more domains',
        'benefit': 'Provide beneficial carrier effects with healing spells (you choose the benefit).',
        'special': ''
    },

    'Knowledge Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain bonuses on attack rolls and damage rolls against specific creature types based on Knowledge checks.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Law Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain bonus on attack rolls or to AC until your next action.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Luck Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Improve a damage roll to average result as a free action once per day.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Magic Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Make ranged touch attack dealing 1d6 damage per two character levels.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Mitigate Suffering': {
        'type': 'Reserve',
        'prerequisites': 'Ability to cast 2nd-level spells',
        'benefit': 'Temporarily restore ability damage or damage that has been dealt to ability scores.',
        'special': ''
    },

    'Plant Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain +2 bonus to natural armor and fortification effect based on character level.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Protection Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Create 30-foot-radius protective aura centered on yourself protecting against specific threats.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Protective Ward': {
        'type': 'Reserve',
        'prerequisites': 'Access to the Protection domain',
        'benefit': 'Grant bonus to AC to yourself or an ally within 30 feet based on highest-level Protection domain spell available.',
        'special': ''
    },

    'Retrieve Spell': {
        'type': 'Divine',
        'prerequisites': 'Any two divine feats, ability to turn or rebuke undead',
        'benefit': 'Spend turn/rebuke attempts to regain a previously cast spell.',
        'special': ''
    },

    'Spiritual Counter': {
        'type': 'Divine',
        'prerequisites': 'Any other divine feat, ability to turn or rebuke undead',
        'benefit': 'Spend turn/rebuke attempts to counterspell.',
        'special': ''
    },

    'Spontaneous Domains': {
        'type': 'General',
        'prerequisites': 'Ability to cast 3rd-level spells',
        'benefit': 'Leave your domain spell slots open to be filled at need. Access to two or more domains.',
        'special': ''
    },

    'Strength Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Gain adamantine slam attack and ability to overcome hardness with melee attacks.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Sun Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Cause your melee weapon to glow and deal extra sacred damage based on character level.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Swift Call': {
        'type': 'General',
        'prerequisites': 'Special mount class feature',
        'benefit': 'Call special mount as a swift action instead of a standard action.',
        'special': ''
    },

    'Swift Wild Shape': {
        'type': 'Wild',
        'prerequisites': 'Dex 13, Fast Wild Shape, wild shape class feature',
        'benefit': 'You can use wild shape as a swift action.',
        'special': ''
    },

    'Touch of Healing': {
        'type': 'Reserve',
        'prerequisites': 'Ability to cast 2nd-level spells',
        'benefit': 'Heal 3 points of damage per level of highest-level healing spell you have available.',
        'special': ''
    },

    'Travel Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Move your speed as a swift action.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Trickery Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Create a simulacrum of yourself that can perform certain actions based on your level.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Umbral Shroud': {
        'type': 'Reserve',
        'prerequisites': 'Ability to cast 3rd-level spells',
        'benefit': 'Impose a miss chance on enemies attacks based on spells available.',
        'special': ''
    },

    'Venoms Gift': {
        'type': 'Wild',
        'prerequisites': 'Two other wild feats, wild shape class feature, ability to assume plant form',
        'benefit': 'Imbue your natural attacks with poison for 1 round per level.',
        'special': ''
    },

    'War Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Improve your ability to fight defensively.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    },

    'Water Devotion': {
        'type': 'Domain',
        'prerequisites': 'None',
        'benefit': 'Summon a water elemental with HD based on your character level.',
        'special': 'You can select this feat multiple times. If you can turn/rebuke undead, gain extra uses by expending turn/rebuke attempts.'
    }

}
