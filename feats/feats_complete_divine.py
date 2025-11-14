"""

D&D 3rd Edition Feats from Complete Divine

Feats for clerics, paladins, druids, and other divine spellcasters

"""

COMPLETE_DIVINE_FEATS = {

    'Arcane Disciple': {
        'type': 'General',
        'prerequisites': 'Knowledge (religion) 4 ranks, Spellcraft 4 ranks, able to cast arcane spells, alignment matches deitys alignment',
        'benefit': 'Add chosen domains spells to your class arcane spell list. You use Wisdom for save DCs and must have Wisdom 10 + spell level.',
        'special': 'You can take this feat multiple times, selecting a different domain each time.'
    },

    'Augment Healing': {
        'type': 'General',
        'prerequisites': 'Heal 4 ranks',
        'benefit': 'Add 2 points per spell level to damage healed by Conjuration Healing spells you cast.',
        'special': ''
    },

    'Boars Ferocity': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'If hit points reduced to 0 or less but not killed, you can spend a wild shape use to continue acting.',
        'special': ''
    },

    'Cheetahs Speed': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'You can spend a wild shape use to increase your land speed to 50 feet or sprint at 10 times normal speed once per hour.',
        'special': ''
    },

    'Consecrate Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any good alignment',
        'benefit': 'A spell modified gains the good descriptor. Half damage results from divine power and bypasses resistance/immunity.',
        'special': 'Uses a spell slot one level higher than actual.'
    },

    'Corrupt Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Any evil alignment',
        'benefit': 'A spell modified gains the evil descriptor. Half damage results from divine power and bypasses resistance/immunity.',
        'special': 'Uses a spell slot one level higher than actual.'
    },

    'Disciple of the Sun': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn undead, good alignment',
        'benefit': 'You can spend two turn attempts to destroy undead instead of turning them.',
        'special': ''
    },

    'Divine Cleansing': {
        'type': 'Divine',
        'prerequisites': 'Turn or rebuke undead ability',
        'benefit': 'Spend turn/rebuke attempt to grant +2 sacred bonus on Fortitude saves to allies within 60 feet.',
        'special': ''
    },

    'Divine Metamagic': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'Spend turn/rebuke attempts to apply metamagic feats to divine spells without increasing spell slot level.',
        'special': 'You can take this feat multiple times for different metamagic feats.'
    },

    'Divine Might': {
        'type': 'Divine',
        'prerequisites': 'Str 13, turn or rebuke undead ability, Power Attack',
        'benefit': 'Spend turn/rebuke attempt to add Charisma bonus to weapon damage for 1 full round.',
        'special': ''
    },

    'Divine Resistance': {
        'type': 'Divine',
        'prerequisites': 'Turn or rebuke undead ability, Divine Cleansing',
        'benefit': 'Spend turn/rebuke attempt to grant resistance to cold 5, electricity 5, and fire 5 to allies within 60 feet.',
        'special': ''
    },

    'Divine Shield': {
        'type': 'Divine',
        'prerequisites': 'Turn or rebuke undead ability, proficiency with a shield',
        'benefit': 'Spend turn/rebuke attempt to grant shield a bonus equal to Charisma modifier.',
        'special': ''
    },

    'Divine Spell Power': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn or rebuke undead, able to cast 1st-level divine spells',
        'benefit': 'Spend turn/rebuke attempt to add bonus to caster level of next divine spell based on turning check.',
        'special': ''
    },

    'Divine Vigor': {
        'type': 'Divine',
        'prerequisites': 'Turn or rebuke undead ability',
        'benefit': 'Spend turn/rebuke attempt to increase base speed by 10 feet and gain temporary hit points.',
        'special': ''
    },

    'Domain Focus': {
        'type': 'General',
        'prerequisites': 'Access to relevant domain',
        'benefit': 'Cast domain spells at +1 caster level.',
        'special': 'You can take this feat multiple times for different domains.'
    },

    'Domain Spontaneity': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'Convert prepared divine spells into domain spells spontaneously.',
        'special': 'You can take this feat multiple times for different domains.'
    },

    'Eagles Wings': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'Spend a wild shape use to grow feathery wings and fly at 60 feet average maneuverability.',
        'special': ''
    },

    'Elemental Healing': {
        'type': 'Divine',
        'prerequisites': 'Ability to rebuke creatures with an elemental subtype',
        'benefit': 'Spend rebuke attempt to heal elemental creatures within 60 feet.',
        'special': ''
    },

    'Elemental Smiting': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn creatures with an elemental subtype',
        'benefit': 'Spend turn attempt to deal bonus damage equal to cleric level against elemental creatures.',
        'special': ''
    },

    'Elephants Hide': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape into a Large creature',
        'benefit': 'Spend a wild shape use to gain +7 natural armor bonus for 10 minutes.',
        'special': ''
    },

    'Empower Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'Your turning damage is multiplied by 1.5.',
        'special': ''
    },

    'Extra Wild Shape': {
        'type': 'Wild',
        'prerequisites': 'Ability to use wild shape',
        'benefit': 'You use wild shape two more times per day.',
        'special': 'You can take this feat multiple times. Its effects stack.'
    },

    'Fast Wild Shape': {
        'type': 'Wild',
        'prerequisites': 'Dex 13, ability to use wild shape',
        'benefit': 'You can use wild shape as a move-equivalent action.',
        'special': ''
    },

    'Glorious Weapons': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'Spend turn/rebuke attempt to align melee weapons of allies within 60 feet.',
        'special': ''
    },

    'Grizzlys Claws': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'Spend a wild shape use to gain two claw attacks for 1 hour.',
        'special': ''
    },

    'Improved Smiting': {
        'type': 'General',
        'prerequisites': 'Cha 13, smite ability',
        'benefit': 'Smite attacks overcome alignment-based damage reduction and deal +1d6 damage to specific alignments.',
        'special': ''
    },

    'Lions Pounce': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'When you charge, spend a wild shape use to make a full attack at the end of the charge.',
        'special': ''
    },

    'Oaken Resilience': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape into a plant',
        'benefit': 'Spend a wild shape use to gain immunity to critical hits, poison, sleep, paralysis, polymorph, and stunning.',
        'special': ''
    },

    'Practiced Spellcaster': {
        'type': 'General',
        'prerequisites': 'Spellcraft 4 ranks',
        'benefit': 'Your caster level for chosen spellcasting class increases by 4 (not exceeding HD).',
        'special': 'You can take this feat multiple times for different spellcasting classes.'
    },

    'Profane Boost': {
        'type': 'Divine',
        'prerequisites': 'Ability to rebuke undead',
        'benefit': 'Spend rebuke attempt to maximize inflict spells on creatures within 60 feet.',
        'special': ''
    },

    'Quicken Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke undead',
        'benefit': 'You can turn or rebuke undead as a free action.',
        'special': ''
    },

    'Rapid Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Spells with casting times longer than 1 standard action can be cast more quickly.',
        'special': 'Uses a spell slot one level higher than actual.'
    },

    'Reach Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Cast touch spells at 30-foot range as rays (ranged touch attacks).',
        'special': 'Uses a spell slot two levels higher than actual.'
    },

    'Sacred Boost': {
        'type': 'Divine',
        'prerequisites': 'Ability to turn undead',
        'benefit': 'Spend turn attempt to maximize cure spells on creatures within 60 feet.',
        'special': ''
    },

    'Sacred Healing': {
        'type': 'Divine',
        'prerequisites': 'Heal 8 ranks, ability to turn undead',
        'benefit': 'Spend turn attempt to grant fast healing 3 to living creatures within 60 feet.',
        'special': ''
    },

    'Serpents Venom': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'Spend a wild shape use to gain a secondary bite attack with toxic venom.',
        'special': ''
    },

    'Spell Focus (Chaos, Evil, Good, or Law)': {
        'type': 'General',
        'prerequisites': 'Relevant alignment',
        'benefit': 'Add 1 to save DC for alignment descriptor spells matching your alignment.',
        'special': 'You can take this feat twice for different alignments.'
    },

    'Spontaneous Healer': {
        'type': 'General',
        'prerequisites': 'Knowledge (religion) 4 ranks, nonevil alignment, able to cast cure spells',
        'benefit': 'You can spontaneously cast cure spells.',
        'special': ''
    },

    'Spontaneous Summoner': {
        'type': 'General',
        'prerequisites': 'Wis 13, Knowledge (nature) 4 ranks, any neutral alignment, able to cast summon natures ally',
        'benefit': 'You can spontaneously cast summon natures ally spells.',
        'special': ''
    },

    'Spontaneous Wounder': {
        'type': 'General',
        'prerequisites': 'Wis 13, Knowledge (religion) 4 ranks, nongood alignment, able to cast inflict spells',
        'benefit': 'You can spontaneously cast inflict spells.',
        'special': ''
    },

    'Swim Like a Fish': {
        'type': 'Wild',
        'prerequisites': 'Ability to wild shape',
        'benefit': 'Spend a wild shape use to gain gills and Swim speed of 40 feet for 1 hour.',
        'special': ''
    },

    'Transdimensional Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Spells affect creatures on coexistent planes and extradimensional spaces.',
        'special': 'Uses a spell slot one level higher than actual.'
    },

    'True Believer': {
        'type': 'General',
        'prerequisites': 'Choose single deity, alignment within one step of deitys',
        'benefit': 'Once per day gain +2 insight bonus on one save. Allows use of relics.',
        'special': ''
    },

    'Wolverines Rage': {
        'type': 'Wild',
        'prerequisites': 'Wild shape',
        'benefit': 'If damaged last round, spend a wild shape use to enter a 5-round rage.',
        'special': ''
    }

}
