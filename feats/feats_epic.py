"""

D&D 3rd Edition Feats from Epic Level Handbook

Epic feats for characters level 21 and above

"""

EPIC_LEVEL_HANDBOOK_FEATS = {

    'Additional Magic Item Space': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, Int 25, or Wis 25, 21st level',
        'benefit': 'Choose one type of magic item not included in the standard body slots. You can now use an item in this location as if it were a regular magic item slot.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time, it applies to a new type of item.'
    },

    'Armor Skin': {
        'type': 'Epic',
        'prerequisites': 'Con 21',
        'benefit': 'You gain a 1 natural armor bonus to AC, or your existing natural armor bonus increases by 1.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Augmented Alchemy': {
        'type': 'Epic',
        'prerequisites': 'Int 21, Alchemy 24 ranks',
        'benefit': 'Whenever creating an alchemical item or substance, you can augment it to increase its DC by 20 and double its normal effects. Creating an augmented alchemical item costs twice the normal amount.',
        'special': 'This does not apply to alchemical items that don\'t have a listed DC.'
    },

    'Automatic Quicken Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Quicken Spell, Spellcraft 30 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You can cast one spell per day of 6th level or lower quickened as a free action. This does not adjust the spell\'s level.',
        'special': 'You can gain this feat multiple times. Each time, you can quicken one additional spell per day.'
    },

    'Automatic Silent Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Silent Spell, Spellcraft 24 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You can cast any spell without verbal components, without using a higher-level spell slot.',
        'special': 'As a special use of this feat, you can also cast any three spells per day silently without using a higher-level spell slot.'
    },

    'Automatic Still Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Still Spell, Spellcraft 27 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You can cast any spell without somatic components, without using a higher-level spell slot.',
        'special': 'As a special use of this feat, you can also cast any three spells per day stilled without using a higher-level spell slot.'
    },

    'Bane of Enemies': {
        'type': 'Epic',
        'prerequisites': 'Wilderness Lore 24 ranks, five or more favored enemies',
        'benefit': 'Any weapon you wield against a favored enemy is treated as a bane weapon for that creature type, gaining a 2 enhancement bonus and dealing 2d6 extra damage.',
        'special': ''
    },

    'Beast Companion': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 25, Animal Companion class feature',
        'benefit': 'Your animal companion can be a magical beast, which must be approved by your DM.',
        'special': ''
    },

    'Beast Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 25, Knowledge (nature) 24 ranks, wild shape 6/day',
        'benefit': 'You can use wild shape to take the form of a magical beast.',
        'special': ''
    },

    'Blinding Speed': {
        'type': 'Epic',
        'prerequisites': 'Dex 25',
        'benefit': 'You can act as if hasted for 5 rounds per day as a free action.',
        'special': 'You can gain this feat multiple times, gaining 5 additional rounds per day each time.'
    },

    'Bonus Domain': {
        'type': 'Epic',
        'prerequisites': 'Wis 21, ability to cast 9th-level divine spells',
        'benefit': 'You gain the granted power of one additional domain and can prepare one domain spell of each level from this domain.',
        'special': ''
    },

    'Bulwark of Defense': {
        'type': 'Epic',
        'prerequisites': 'Con 25, defensive stance 3/day',
        'benefit': 'While in a defensive stance, you gain 12 to Strength, 16 to Constitution, 4 resistance bonus on all saves, and 6 dodge bonus to AC.',
        'special': ''
    },

    'Chaotic Rage': {
        'type': 'Epic',
        'prerequisites': 'Rage 5/day, chaotic alignment',
        'benefit': 'While raging, you can inspire allies within 60 feet to enter a similar rage. Affected creatures gain 4 to Strength and Constitution, 2 bonus on Will saves, and -2 to AC.',
        'special': 'This is a mind-affecting effect.'
    },

    'Combat Archery': {
        'type': 'Epic',
        'prerequisites': 'Dodge, Mobility, Point Blank Shot, base attack bonus 21',
        'benefit': 'You do not provoke attacks of opportunity when firing a bow while in a threatened area.',
        'special': ''
    },

    'Craft Epic Magic Arms and Armor': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Craft Magic Arms and Armor, Knowledge (arcana) 28 ranks, Spellcraft 28 ranks',
        'benefit': 'You can craft magic arms and armor with enhancement bonuses of 6 or higher, or with special abilities that have a total value of 6 or more.',
        'special': ''
    },

    'Craft Epic Rod': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Craft Rod, Knowledge (arcana) 32 ranks, Spellcraft 32 ranks',
        'benefit': 'You can craft epic rods.',
        'special': ''
    },

    'Craft Epic Staff': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Craft Staff, Knowledge (arcana) 35 ranks, Spellcraft 35 ranks',
        'benefit': 'You can craft epic staves.',
        'special': ''
    },

    'Craft Epic Wondrous Item': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Craft Wondrous Item, Knowledge (arcana) 26 ranks, Spellcraft 26 ranks',
        'benefit': 'You can craft wondrous items exceeding the normal limits.',
        'special': ''
    },

    'Damage Reduction': {
        'type': 'Epic',
        'prerequisites': 'Con 21',
        'benefit': 'You gain damage reduction 3/-, or your existing damage reduction increases by 3.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Death of Enemies': {
        'type': 'Epic',
        'prerequisites': 'Bane of Enemies, Wilderness Lore 30 ranks',
        'benefit': 'You can make a death attack against favored enemies. If you study a favored enemy for 3 rounds and then make a sneak attack that successfully deals damage, the target must make a Fortitude save (DC 10 1/2 your level your Wisdom modifier) or die.',
        'special': ''
    },

    'Deafening Song': {
        'type': 'Epic',
        'prerequisites': 'Perform 24 ranks, bardic music class feature',
        'benefit': 'You can use bardic music to deafen enemies within 30 feet for as long as you sing and for 1 round thereafter.',
        'special': ''
    },

    'Dexterous Fortitude': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, slippery mind class feature',
        'benefit': 'Once per round, you can add your Dexterity modifier in place of your Constitution modifier to a Fortitude save.',
        'special': ''
    },

    'Dexterous Will': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, slippery mind class feature',
        'benefit': 'Once per round, you can add your Dexterity modifier in place of your Wisdom modifier to a Will save.',
        'special': ''
    },

    'Diminutive Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Ability to wild shape into a Huge animal',
        'benefit': 'You can use wild shape to assume a Diminutive size form.',
        'special': ''
    },

    'Dire Charge': {
        'type': 'Epic',
        'prerequisites': 'Str 25, Power Attack, Improved Bull Rush, base attack bonus 25',
        'benefit': 'If you charge a foe, you can make a full attack at the end of your charge.',
        'special': ''
    },

    'Distant Shot': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Far Shot, Point Blank Shot, Spot 20 ranks',
        'benefit': 'You can throw or fire projectiles at any distance with no maximum range and no range increment penalty.',
        'special': ''
    },

    'Dragon Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 30, Beast Wild Shape, Magical Beast Wild Shape, Knowledge (nature) 30 ranks, wild shape 6/day',
        'benefit': 'You can use wild shape to assume a dragon form.',
        'special': ''
    },

    'Efficient Item Creation': {
        'type': 'Epic',
        'prerequisites': 'Item creation feat to be selected, Knowledge (arcana) 24 ranks, Spellcraft 24 ranks',
        'benefit': 'When you create a magic item using the selected item creation feat, you spend only half the normal XP and half the normal gold piece cost.',
        'special': 'You can gain this feat multiple times, selecting a different item creation feat each time.'
    },

    'Energy Resistance': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Choose one type of energy (acid, cold, electricity, fire, or sonic). You gain resistance 10 to that energy type, or your existing resistance increases by 10.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time, it applies to a different type of energy.'
    },

    'Enhance Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Maximize Spell',
        'benefit': 'Add 2 to the save DC of one spell you cast.',
        'special': 'You can gain this feat multiple times. Each time you select it, you gain an additional daily use.'
    },

    'Epic Dodge': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Dodge, Tumble 30 ranks, improved evasion, defensive roll class feature',
        'benefit': 'Once per round as a reaction, you can automatically avoid damage from one attack against you.',
        'special': ''
    },

    'Epic Endurance': {
        'type': 'Epic',
        'prerequisites': 'Con 25, Endurance',
        'benefit': 'Whenever you make a check for performing a physical action that extends over a period of time, you get a 10 bonus on the check.',
        'special': ''
    },

    'Epic Fortitude': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain a 4 bonus on all Fortitude saving throws.',
        'special': ''
    },

    'Epic Inspiration': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, Perform 30 ranks, bardic music class feature',
        'benefit': 'You can inspire allies to superhuman achievement. Once per day, you can use bardic music to grant allies within 60 feet a 4 insight bonus to AC, saving throws, attack rolls, and damage rolls for as long as they hear you sing and for 5 rounds thereafter.',
        'special': ''
    },

    'Epic Leadership': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, Leadership, Leadership score 25',
        'benefit': 'You attract a cohort and followers as if your Leadership score were 10 higher than normal.',
        'special': 'You can gain this feat multiple times. Each time you do, your effective Leadership score increases by an additional 10.'
    },

    'Epic Prowess': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain a 1 bonus on all attack rolls.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Epic Reflexes': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain a 4 bonus on all Reflex saving throws.',
        'special': ''
    },

    'Epic Reputation': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain a 4 bonus on all Diplomacy and Intimidate checks.',
        'special': ''
    },

    'Epic Skill Focus': {
        'type': 'Epic',
        'prerequisites': '20 ranks in the skill selected',
        'benefit': 'You gain a 10 bonus on all skill checks with one chosen skill.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different skill.'
    },

    'Epic Speed': {
        'type': 'Epic',
        'prerequisites': 'Dex 21, Run',
        'benefit': 'Your speed increases by 30 feet.',
        'special': 'This is treated as an enhancement bonus and does not stack with magical enhancement bonuses to speed.'
    },

    'Epic Spell Focus': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Focus and Spell Focus in the school selected, ability to cast at least one 9th-level spell of the school',
        'benefit': 'Add 1 to the DC for all saving throws against spells from the school of magic you select.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take it, it applies to a different school of magic.'
    },

    'Epic Spell Penetration': {
        'type': 'Epic',
        'prerequisites': 'Greater Spell Penetration, Spell Penetration',
        'benefit': 'You get a 2 bonus on caster level checks to overcome spell resistance.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Epic Spellcasting': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 24 ranks, Knowledge (arcana) 24 ranks, and ability to cast 9th-level arcane spells OR Spellcraft 24 ranks, Knowledge (religion) 24 ranks, and ability to cast 9th-level divine spells OR Spellcraft 24 ranks, Knowledge (nature) 24 ranks, and ability to cast 9th-level divine spells',
        'benefit': 'You can develop and cast epic spells. See Chapter 2 for information on epic spells.',
        'special': 'If you meet the prerequisites for this feat more than once, you can apply this feat to a different epic spell list for each time you meet those prerequisites.'
    },

    'Epic Toughness': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain 30 hit points.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Epic Weapon Focus': {
        'type': 'Epic',
        'prerequisites': 'Weapon Focus in the weapon to be chosen',
        'benefit': 'You gain a 2 bonus on all attack rolls you make using the selected weapon.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different weapon.'
    },

    'Epic Weapon Specialization': {
        'type': 'Epic',
        'prerequisites': 'Epic Weapon Focus, Weapon Focus, Weapon Specialization all in the weapon to be chosen',
        'benefit': 'You gain a 4 bonus on all damage rolls you make using the selected weapon.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different weapon.'
    },

    'Epic Will': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'You gain a 4 bonus on all Will saving throws.',
        'special': ''
    },

    'Exceptional Deflection': {
        'type': 'Epic',
        'prerequisites': 'Dex 21, Wis 19, Deflect Arrows, Improved Unarmed Strike',
        'benefit': 'You can deflect any ranged attack (including spells that require a ranged touch attack) that is aimed at you as if it were an arrow.',
        'special': ''
    },

    'Extended Life Span': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your maximum age is increased by 50 of the normal maximum for your race.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Familiar Spell': {
        'type': 'Epic',
        'prerequisites': 'Int 25 if you have an arcane spellcasting familiar OR Wis 25 if you have a divine spellcasting familiar',
        'benefit': 'Choose one spell you know of 8th level or lower. Your familiar can now cast this spell once per day at your caster level (save DC is based on your familiar\'s ability scores).',
        'special': 'You can gain this feat multiple times. Each time, select a new spell to give to your familiar.'
    },

    'Fast Healing': {
        'type': 'Epic',
        'prerequisites': 'Con 25',
        'benefit': 'You gain fast healing 3, or your existing fast healing improves by 3.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Fine Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Ability to wild shape into a Diminutive creature',
        'benefit': 'You can use wild shape to assume a Fine size form.',
        'special': ''
    },

    'Forge Epic Ring': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Forge Ring, Knowledge (arcana) 35 ranks, Spellcraft 35 ranks',
        'benefit': 'You can craft magic rings that exceed the normal limits.',
        'special': ''
    },

    'Gargantuan Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Ability to wild shape into a Huge animal',
        'benefit': 'You can use wild shape to assume a Gargantuan size form.',
        'special': ''
    },

    'Great Charisma': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Charisma increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Constitution': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Constitution increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Dexterity': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Dexterity increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Intelligence': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Intelligence increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Smiting': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, smite ability',
        'benefit': 'Add 10 to the damage you deal with any smite attack.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Strength': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Strength increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Great Wisdom': {
        'type': 'Epic',
        'prerequisites': 'None',
        'benefit': 'Your Wisdom increases by 1 point.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Group Inspiration': {
        'type': 'Epic',
        'prerequisites': 'Perform 30 ranks, bardic music class feature',
        'benefit': 'You can use bardic music to grant bonuses to all allies within 60 feet simultaneously. All allies gain the benefits of your inspire courage, inspire competence, or inspire greatness abilities as long as they can hear you.',
        'special': ''
    },

    'Hindering Song': {
        'type': 'Epic',
        'prerequisites': 'Deafening Song, Perform 27 ranks, bardic music class feature',
        'benefit': 'Your bardic music forces enemies to save or be slowed (as the spell) for as long as you sing and for 1 round thereafter.',
        'special': ''
    },

    'Holy Strike': {
        'type': 'Epic',
        'prerequisites': 'Smite evil class feature, any good alignment',
        'benefit': 'Any weapon you wield is treated as a holy weapon (adding 2d6 damage to evil creatures).',
        'special': ''
    },

    'Ignore Material Components': {
        'type': 'Epic',
        'prerequisites': 'Eschew Materials, Spellcraft 25 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You can cast spells without using material components regardless of their cost.',
        'special': ''
    },

    'Improved Alignment-Based Casting': {
        'type': 'Epic',
        'prerequisites': 'Access to domain of Chaos, Evil, Good, or Law',
        'benefit': 'Add 3 to your caster level when casting alignment-based spells.',
        'special': 'You can gain this feat multiple times, applying it to a different alignment descriptor each time.'
    },

    'Improved Arrow of Death': {
        'type': 'Epic',
        'prerequisites': 'Dex 19, Wis 19, Point Blank Shot, Precise Shot, arrow of death class feature',
        'benefit': 'Add 2 to the DC of your arrows of death. You can generate one additional arrow of death per day.',
        'special': 'You can gain this feat multiple times. Each time, the DC increases by 2 and you gain one additional arrow of death per day.'
    },

    'Improved Aura of Courage': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, aura of courage class feature',
        'benefit': 'Your aura of courage grants a 8 morale bonus on saves against fear effects.',
        'special': ''
    },

    'Improved Aura of Despair': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, aura of despair class feature',
        'benefit': 'Your aura of despair causes a -4 morale penalty on saves.',
        'special': ''
    },

    'Improved Combat Casting': {
        'type': 'Epic',
        'prerequisites': 'Combat Casting',
        'benefit': 'You get a 10 bonus on Concentration checks to cast a spell or use a spell-like ability on the defensive or while grappling or pinned.',
        'special': ''
    },

    'Improved Combat Reflexes': {
        'type': 'Epic',
        'prerequisites': 'Dex 21, Combat Reflexes',
        'benefit': 'There is no limit to the number of attacks of opportunity you can make in one round.',
        'special': ''
    },

    'Improved Darkvision': {
        'type': 'Epic',
        'prerequisites': 'Darkvision',
        'benefit': 'Your darkvision extends to 120 feet.',
        'special': 'You can gain this feat multiple times. Each time, your darkvision increases by an additional 60 feet.'
    },

    'Improved Death Attack': {
        'type': 'Epic',
        'prerequisites': 'Death attack class feature, sneak attack 5d6',
        'benefit': 'Add 2 to the DC of your death attack.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Elemental Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 25, ability to wild shape into an elemental',
        'benefit': 'You can use wild shape to assume the form of an elder elemental.',
        'special': ''
    },

    'Improved Favored Enemy': {
        'type': 'Epic',
        'prerequisites': 'Five or more favored enemies',
        'benefit': 'Add 1 to the bonus you deal with weapon damage rolls against all your favored enemies.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Heighten Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Heighten Spell',
        'benefit': 'As Heighten Spell, but there is no limit to the level to which you can heighten the spell.',
        'special': ''
    },

    'Improved Ki Strike': {
        'type': 'Epic',
        'prerequisites': 'Wis 21, ki strike +4',
        'benefit': 'Your ki strike gains a 1 enhancement bonus, or your existing enhancement bonus increases by 1.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Low-Light Vision': {
        'type': 'Epic',
        'prerequisites': 'Low-light vision',
        'benefit': 'Your low-light vision improves, allowing you to see four times as far as a human in dim light.',
        'special': 'You can gain this feat multiple times. Each time you take it, the modifier doubles (8, 16, 32, and so on).'
    },

    'Improved Manyshot': {
        'type': 'Epic',
        'prerequisites': 'Dex 19, Manyshot, Point Blank Shot, Rapid Shot, base attack bonus 21',
        'benefit': 'As Manyshot, but the number of arrows you can fire with a single attack is limited only by your base attack bonus (two arrows, plus one arrow for every 5 points of base attack bonus above 6).',
        'special': 'Regardless of the number of arrows you fire, you only apply precision-based damage (such as sneak attack damage) once.'
    },

    'Improved Manifestation': {
        'type': 'Epic',
        'prerequisites': 'Character level 21st, ability to manifest powers',
        'benefit': 'Choose one power you know. You can manifest that power at a manifester level 4 higher than normal.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different power.'
    },

    'Improved Metamagic': {
        'type': 'Epic',
        'prerequisites': 'Four metamagic feats',
        'benefit': 'Choose one metamagic feat you know. The spell slot cost of that feat is reduced by 1 level (to a minimum of 1).',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different metamagic feat.'
    },

    'Improved Sneak Attack': {
        'type': 'Epic',
        'prerequisites': 'Sneak attack 8d6',
        'benefit': 'Your sneak attack damage increases by 1d6.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Spell Capacity': {
        'type': 'Epic',
        'prerequisites': 'Ability to cast spells of the normal maximum spell level in at least one spellcasting class',
        'benefit': 'You gain one spell slot per day of any level up to one level higher than the highest-level spell you can already cast. You must have the requisite ability score (10 spell level) to use this spell slot.',
        'special': 'You can gain this feat multiple times.'
    },

    'Improved Spell Resistance': {
        'type': 'Epic',
        'prerequisites': 'Must have spell resistance from a feat, class feature, or other permanent effect',
        'benefit': 'Your spell resistance increases by 2.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Stunning Fist': {
        'type': 'Epic',
        'prerequisites': 'Dex 19, Wis 19, Improved Unarmed Strike, Stunning Fist',
        'benefit': 'Add 2 to the DC of your stunning attack.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Improved Whirlwind Attack': {
        'type': 'Epic',
        'prerequisites': 'Int 13, Dex 23, Dodge, Expertise, Mobility, Spring Attack, Whirlwind Attack',
        'benefit': 'As a full-round action, you can make one melee attack at your full base attack bonus against each opponent you threaten.',
        'special': ''
    },

    'Infinite Deflection': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Combat Reflexes, Deflect Arrows, Improved Unarmed Strike',
        'benefit': 'You can deflect any number of ranged attacks each round as if using Deflect Arrows.',
        'special': ''
    },

    'Inspire Excellence': {
        'type': 'Epic',
        'prerequisites': 'Perform 30 ranks, bardic music class feature',
        'benefit': 'You can use song or poetics to grant a 4 competence bonus to one ability score to all allies within 60 feet for as long as you sing and for 5 rounds after you stop singing.',
        'special': ''
    },

    'Instant Reload': {
        'type': 'Epic',
        'prerequisites': 'Quick Draw, Rapid Reload, Weapon Focus (crossbow type to be selected)',
        'benefit': 'You can reload the selected type of crossbow as a free action.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take it, it applies to a different crossbow type.'
    },

    'Intensify Spell': {
        'type': 'Epic (Metamagic)',
        'prerequisites': 'Empower Spell, Maximize Spell, Spellcraft 30 ranks, ability to cast 9th-level arcane or divine spells',
        'benefit': 'All variable numeric effects of an intensified spell are maximized, then doubled. An intensified spell uses up a spell slot seven levels higher than the spell\'s actual level.',
        'special': 'You can\'t combine this with any other feat that affects variable, numeric effects of a spell.'
    },

    'Keen Strike': {
        'type': 'Epic',
        'prerequisites': 'Str 23, Wis 23, Improved Critical (unarmed strike), ki strike +3',
        'benefit': 'Your unarmed strike has a critical threat range of 19-20 and is treated as a slashing weapon.',
        'special': ''
    },

    'Lasting Inspiration': {
        'type': 'Epic',
        'prerequisites': 'Perform 25 ranks, bardic music class feature',
        'benefit': 'Your bardic music inspiration abilities last for ten times as long after you stop singing.',
        'special': ''
    },

    'Legendary Climber': {
        'type': 'Epic',
        'prerequisites': 'Dex 21, Balance 12 ranks, Climb 24 ranks',
        'benefit': 'You can ignore any check penalties for accelerated climbing or rapid climbing.',
        'special': ''
    },

    'Legendary Commander': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, Epic Leadership, Leadership, Diplomacy 30 ranks, must rule own kingdom and have a stronghold',
        'benefit': 'Multiply the number of followers of each level you can lead by 10.',
        'special': ''
    },

    'Legendary Leaper': {
        'type': 'Epic',
        'prerequisites': 'Jump 24 ranks',
        'benefit': 'The distance of your jumps is not restricted by your height.',
        'special': ''
    },

    'Legendary Rider': {
        'type': 'Epic',
        'prerequisites': 'Ride 24 ranks',
        'benefit': 'You suffer no reduction in rank when riding an unfamiliar mount, no penalty when riding bareback, and never need a Ride check to control a mount in combat.',
        'special': ''
    },

    'Legendary Tracker': {
        'type': 'Epic',
        'prerequisites': 'Wis 25, Track, Knowledge (nature) 30 ranks, Wilderness Lore 30 ranks',
        'benefit': 'You can track creatures across water, underwater, or through the air.',
        'special': ''
    },

    'Legendary Wrestler': {
        'type': 'Epic',
        'prerequisites': 'Str 21, Dex 21, Improved Unarmed Strike, Escape Artist 15 ranks',
        'benefit': 'You gain a 10 bonus on all grapple checks.',
        'special': ''
    },

    'Lingering Damage': {
        'type': 'Epic',
        'prerequisites': 'Sneak attack 8d6, crippling strike class feature',
        'benefit': 'Any time you deal damage with a sneak attack, the target takes that damage again on your next turn.',
        'special': ''
    },

    'Magical Beast Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 25, Beast Wild Shape, Knowledge (nature) 27 ranks, wild shape 6/day',
        'benefit': 'You can use wild shape to take the form of a magical beast.',
        'special': ''
    },

    'Master Staff': {
        'type': 'Epic',
        'prerequisites': 'Craft Staff, Spellcraft 15 ranks',
        'benefit': 'When you activate a staff, you can substitute a spell slot instead of using a charge.',
        'special': ''
    },

    'Master Wand': {
        'type': 'Epic',
        'prerequisites': 'Craft Wand, Spellcraft 15 ranks',
        'benefit': 'When you activate a wand, you can substitute a spell slot instead of using a charge.',
        'special': ''
    },

    'Multispell': {
        'type': 'Epic',
        'prerequisites': 'Quicken Spell, ability to cast 9th-level arcane or divine spells',
        'benefit': 'You can cast one additional quickened spell in a round.',
        'special': 'You can gain this feat multiple times. Each time, you can cast one additional quickened spell per round.'
    },

    'Overwhelming Critical': {
        'type': 'Epic',
        'prerequisites': 'Str 23, Cleave, Great Cleave, Improved Critical (chosen weapon), Power Attack, Weapon Focus (chosen weapon), base attack bonus 23',
        'benefit': 'When you score a critical hit with the chosen weapon, the target must make a Fortitude save (DC 10 1/2 your level) or be instantly slain.',
        'special': 'You can gain this feat multiple times. Its effects do not stack. Each time you take it, it applies to a different weapon.'
    },

    'Penetrate Damage Reduction': {
        'type': 'Epic',
        'prerequisites': 'Weapon Focus (chosen weapon)',
        'benefit': 'Your attacks with the chosen weapon are treated as either chaotic, evil, good, or lawful (your choice) for the purpose of overcoming damage reduction.',
        'special': 'You can gain this feat multiple times. Each time, it applies to a different weapon or different alignment.'
    },

    'Perfect Health': {
        'type': 'Epic',
        'prerequisites': 'Con 25, Great Fortitude',
        'benefit': 'You are immune to all nonmagical diseases, as well as all magical diseases of any spell level equal to or less than your character level - 10.',
        'special': ''
    },

    'Perfect Multiweapon Fighting': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, three or more arms, Greater Multiweapon Fighting, Improved Multiweapon Fighting, Multiweapon Fighting, base attack bonus 21',
        'benefit': 'You can make as many attacks with each extra off-hand weapon as with your primary weapon, using the same base attack bonus.',
        'special': ''
    },

    'Perfect Two-Weapon Fighting': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Greater Two-Weapon Fighting, Improved Two-Weapon Fighting, Two-Weapon Fighting, base attack bonus 21',
        'benefit': 'You can make as many attacks with your off-hand weapon as with your primary weapon, using the same base attack bonus.',
        'special': ''
    },

    'Permanent Emanation': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 25 ranks, ability to cast the spell to be made permanent',
        'benefit': 'Choose one spell that you know that has a range of personal and a duration measured in rounds. You can now use that spell as an emanation with a radius of 30 feet, and its duration is permanent.',
        'special': 'You can gain this feat multiple times. Each time, it applies to a different spell.'
    },

    'Planar Turning': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, ability to turn or rebuke undead',
        'benefit': 'You can use turn or rebuke attempts to turn or rebuke outsiders as if they were undead. You can also bolster outsiders as you can bolster undead.',
        'special': ''
    },

    'Plant Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Wis 25, Beast Wild Shape, Knowledge (nature) 24 ranks, wild shape 6/day',
        'benefit': 'You can use wild shape to assume plant form.',
        'special': ''
    },

    'Polyglot': {
        'type': 'Epic',
        'prerequisites': 'Int 25, Speak Language (five languages)',
        'benefit': 'You can speak all languages. If you are literate, you can also read and write all languages.',
        'special': ''
    },

    'Ranged Inspiration': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, Perform 30 ranks, bardic music class feature',
        'benefit': 'Double the range of your bardic music abilities.',
        'special': 'You can gain this feat multiple times. Each time you do, double the range again.'
    },

    'Rapid Inspiration': {
        'type': 'Epic',
        'prerequisites': 'Perform 25 ranks, bardic music class feature',
        'benefit': 'You can activate your bardic music abilities as a move-equivalent action or a swift action.',
        'special': ''
    },

    'Reflect Arrows': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Deflect Arrows, Improved Unarmed Strike',
        'benefit': 'When you deflect an arrow or other ranged attack, the attack is reflected back at the attacker.',
        'special': ''
    },

    'Righteous Strike': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, smite evil class feature',
        'benefit': 'Any weapon you wield against evil creatures is considered to be a holy weapon.',
        'special': ''
    },

    'Scribe Epic Scroll': {
        'type': 'Epic (Item Creation)',
        'prerequisites': 'Scribe Scroll, Spellcraft 24 ranks',
        'benefit': 'You can scribe scrolls of epic spells.',
        'special': ''
    },

    'Self-Concealment': {
        'type': 'Epic',
        'prerequisites': 'Dex 30, Hide 30 ranks, Tumble 30 ranks',
        'benefit': 'Attacks against you have a 10 miss chance. This does not stack with any other concealment ability.',
        'special': 'You can gain this feat multiple times. Each time, the miss chance increases by 10.'
    },

    'Sneak Attack of Opportunity': {
        'type': 'Epic',
        'prerequisites': 'Sneak attack 8d6, opportunist class feature',
        'benefit': 'Any time you make an attack of opportunity, you can apply your sneak attack damage as well.',
        'special': ''
    },

    'Spell Knowledge': {
        'type': 'Epic',
        'prerequisites': 'Int 25, ability to cast 9th-level arcane spells as a sorcerer or bard',
        'benefit': 'You learn one additional spell of any level up to one level higher than the highest-level spell you can already cast.',
        'special': 'You can gain this feat multiple times.'
    },

    'Spell Opportunity': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Combat Reflexes, Spellcraft 30 ranks',
        'benefit': 'Whenever a foe within 30 feet provokes an attack of opportunity, you can cast a quickened spell at that foe instead of making a melee attack.',
        'special': ''
    },

    'Spell Stowaway': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 30 ranks, caster level 20th',
        'benefit': 'Whenever you are subject to a spell, you can make a Spellcraft check. If the result equals or exceeds the spell\'s save DC (or the caster\'s level, if no save is allowed), you can choose to "catch" the spell as a free action. You can store the spell and then later cast it, even if it\'s not on your class spell list.',
        'special': 'You can gain this feat multiple times. Each time, you can store one additional spell.'
    },

    'Spellcasting Harrier': {
        'type': 'Epic',
        'prerequisites': 'Combat Reflexes',
        'benefit': 'Any spellcaster you threaten in melee provokes an attack of opportunity if they try to cast defensively. Your attack is resolved before the spell is cast.',
        'special': ''
    },

    'Spontaneous Spell': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, ability to cast spells of the normal maximum spell level in at least one divine spellcasting class',
        'benefit': 'Choose one divine spell you know of up to 9th level. You can now spontaneously convert prepared spells of that spell\'s level or higher into that spell, similar to a cleric spontaneously converting spells to cure or inflict spells.',
        'special': 'You can gain this feat multiple times. Each time, it applies to a different spell.'
    },

    'Storm of Throws': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Point Blank Shot, Quick Draw, Rapid Shot, base attack bonus 21',
        'benefit': 'As a full attack, you can throw a light weapon at your full base attack bonus at each opponent within 30 feet.',
        'special': ''
    },

    'Superior Initiative': {
        'type': 'Epic',
        'prerequisites': 'Improved Initiative',
        'benefit': 'You get a 8 bonus on initiative checks.',
        'special': ''
    },

    'Swarm of Arrows': {
        'type': 'Epic',
        'prerequisites': 'Dex 23, Manyshot, Point Blank Shot, Rapid Shot, Weapon Focus (any bow other than a crossbow), base attack bonus 21',
        'benefit': 'As a full-round action, you can fire an arrow at your full base attack bonus at each opponent within 30 feet.',
        'special': ''
    },

    'Tenacious Magic': {
        'type': 'Epic',
        'prerequisites': 'Spellcraft 15 ranks',
        'benefit': 'Choose one spell you know. Whenever you cast that spell, it is treated as if you had cast it using a spell slot four levels higher than normal. This has no effect on the casting time or other statistics, but it is much harder to dispel with dispel magic.',
        'special': 'You can gain this feat multiple times. Each time, it applies to a different spell.'
    },

    'Trap Sense': {
        'type': 'Epic',
        'prerequisites': 'Int 13, Search 25 ranks, trap sense class feature',
        'benefit': 'Your bonus on Reflex saves and AC against traps increases by 2.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Two-Weapon Rend': {
        'type': 'Epic',
        'prerequisites': 'Dex 25, Greater Two-Weapon Fighting, Improved Two-Weapon Fighting, Two-Weapon Fighting, base attack bonus 20',
        'benefit': 'If you hit an opponent with both your primary and off-hand weapons in the same round, you automatically rend your opponent. This deals additional damage equal to your base damage for your primary weapon plus 1-12 times your Strength modifier.',
        'special': ''
    },

    'Uncanny Accuracy': {
        'type': 'Epic',
        'prerequisites': 'Dex 21, Point Blank Shot, Precise Shot, base attack bonus 21',
        'benefit': 'Your ranged attacks ignore the AC bonus granted by cover to your targets (though you still can\'t target opponents with total cover).',
        'special': ''
    },

    'Undead Mastery': {
        'type': 'Epic',
        'prerequisites': 'Cha 21, ability to rebuke or command undead, caster level 20th',
        'benefit': 'When you rebuke or command undead, you can affect up to four times your cleric level in undead Hit Dice (rather than the normal limit of twice your cleric level in undead Hit Dice).',
        'special': ''
    },

    'Unholy Strike': {
        'type': 'Epic',
        'prerequisites': 'Smite good class feature, any evil alignment',
        'benefit': 'Any weapon you wield against good creatures is considered to be an unholy weapon.',
        'special': ''
    },

    'Vermin Wild Shape': {
        'type': 'Epic (Wild)',
        'prerequisites': 'Beast Wild Shape, Knowledge (nature) 24 ranks, wild shape 6/day',
        'benefit': 'You can use wild shape to assume vermin form.',
        'special': ''
    },

    'Zone of Animation': {
        'type': 'Epic',
        'prerequisites': 'Cha 25, ability to rebuke or command undead',
        'benefit': 'Any corpse within 60 feet of you that has been dead for less than 3 days animates as a zombie under your control. Your effective cleric level for the purpose of controlling undead increases by 4.',
        'special': ''
    }

}

# Backwards-compatible alias: older code refers to EPIC_FEATS
EPIC_FEATS = EPIC_LEVEL_HANDBOOK_FEATS
