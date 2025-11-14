"""
D&D 3rd Edition Core Feats from Player's Handbook
General, Combat, Metamagic, Item Creation, and other feat types
"""

PLAYERS_HANDBOOK_FEATS = {
    'Acrobatic': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Jump checks and Tumble checks.',
        'special': ''
    },
    'Agile': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Balance checks and Escape Artist checks.',
        'special': ''
    },
    'Alertness': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Listen checks and Spot checks.',
        'special': 'A familiar grants its master Alertness as long as it is within 5 feet.'
    },
    'Animal Affinity': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Handle Animal checks and Ride checks.',
        'special': ''
    },
    'Armor Proficiency (Light)': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You can wear light armor without penalty.',
        'special': 'All characters except wizards, sorcerers, and monks are proficient with light armor.'
    },
    'Armor Proficiency (Medium)': {
        'type': 'General',
        'prerequisites': 'Armor Proficiency (Light)',
        'benefit': 'You can wear medium armor without penalty.',
        'special': 'Fighters, paladins, rangers, clerics, druids, and bards are proficient with medium armor.'
    },
    'Armor Proficiency (Heavy)': {
        'type': 'General',
        'prerequisites': 'Armor Proficiency (Medium)',
        'benefit': 'You can wear heavy armor without penalty.',
        'special': 'Fighters, paladins, and clerics are proficient with heavy armor.'
    },
    'Athletic': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Climb checks and Swim checks.',
        'special': ''
    },
    'Augment Summoning': {
        'type': 'General',
        'prerequisites': 'Spell Focus (Conjuration)',
        'benefit': 'Each creature you conjure with any summon spell gains a +4 enhancement bonus to Strength and Constitution.',
        'special': ''
    },
    'Blind-Fight': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'In melee, every time you miss because of concealment, you can reroll your miss chance percentile roll one time to see if you actually hit. You take only half the usual penalty to speed for being unable to see. Darkness and poor visibility in general reduces your speed to three-quarters normal instead of one-half.',
        'special': ''
    },
    'Brew Potion': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 3rd',
        'benefit': 'You can create a potion of any 3rd-level or lower spell that you know and that targets one or more creatures. Brewing a potion takes one day.',
        'special': ''
    },
    'Cleave': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Power Attack',
        'benefit': 'If you deal a creature enough damage to make it drop (typically by dropping it to below 0 hit points or killing it), you get an immediate, extra melee attack against another creature within reach. You can use this ability once per round.',
        'special': ''
    },
    'Combat Casting': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +4 bonus on Concentration checks made to cast a spell or use a spell-like ability while on the defensive or while you are grappling or pinned.',
        'special': ''
    },
    'Combat Expertise': {
        'type': 'Combat',
        'prerequisites': 'Int 13',
        'benefit': 'When you use the attack action or the full attack action in melee, you can take a penalty of as much as -5 on your attack roll and add the same number (+5 or less) as a dodge bonus to your Armor Class.',
        'special': 'A fighter may select Combat Expertise as one of his fighter bonus feats.'
    },
    'Combat Reflexes': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'You may make a number of additional attacks of opportunity equal to your Dexterity bonus. You can also make attacks of opportunity while flat-footed.',
        'special': 'A fighter may select Combat Reflexes as one of his fighter bonus feats.'
    },
    'Craft Magic Arms and Armor': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 5th',
        'benefit': 'You can create any magic weapon, armor, or shield whose prerequisites you meet.',
        'special': ''
    },
    'Craft Rod': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 9th',
        'benefit': 'You can create any rod whose prerequisites you meet.',
        'special': ''
    },
    'Craft Staff': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 12th',
        'benefit': 'You can create any staff whose prerequisites you meet.',
        'special': ''
    },
    'Craft Wand': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 5th',
        'benefit': 'You can create a wand of any 4th-level or lower spell that you know.',
        'special': ''
    },
    'Craft Wondrous Item': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 3rd',
        'benefit': 'You can create any wondrous item whose prerequisites you meet.',
        'special': ''
    },
    'Deceitful': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Disguise checks and Forgery checks.',
        'special': ''
    },
    'Deflect Arrows': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Improved Unarmed Strike',
        'benefit': 'You must have at least one hand free to use this feat. Once per round when you would normally be hit with a ranged weapon, you may deflect it so that you take no damage from it.',
        'special': 'A monk may select Deflect Arrows as a bonus feat at 2nd level, even if she does not meet the prerequisites. A fighter may select Deflect Arrows as one of his fighter bonus feats.'
    },
    'Diehard': {
        'type': 'General',
        'prerequisites': 'Endurance',
        'benefit': 'When reduced to between -1 and -9 hit points, you automatically become stable. You may choose to act as if you were disabled, rather than dying. You must make this decision as soon as you are reduced to negative hit points.',
        'special': ''
    },
    'Diligent': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Appraise checks and Decipher Script checks.',
        'special': ''
    },
    'Dodge': {
        'type': 'Combat',
        'prerequisites': 'Dex 13',
        'benefit': 'During your action, you designate an opponent and receive a +1 dodge bonus to Armor Class against attacks from that opponent.',
        'special': 'A fighter may select Dodge as one of his fighter bonus feats.'
    },
    'Empower Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'All variable, numeric effects of an empowered spell are increased by one-half. An empowered spell uses up a spell slot two levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Endurance': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +4 bonus on the following checks and saves: hourly Swim checks to avoid becoming fatigued, Constitution checks to continue running, Constitution checks to hold your breath, Constitution checks to avoid damage from starvation or thirst, Fortitude saves to avoid damage from hot or cold environments, and Fortitude saves to resist suffocation or drowning.',
        'special': 'A ranger automatically gains Endurance as a bonus feat at 3rd level.'
    },
    'Enlarge Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can alter a spell with a range of close, medium, or long to increase its range by 100%. An enlarged spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Eschew Materials': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You can cast spells without material components if the component\'s cost is 1 gp or less.',
        'special': ''
    },
    'Exotic Weapon Proficiency': {
        'type': 'Combat',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'You make attack rolls with the weapon normally. Choose one type of exotic weapon (such as bastard sword or whip). You understand how to use that type of exotic weapon in combat.',
        'special': 'You can gain Exotic Weapon Proficiency multiple times. A fighter may select Exotic Weapon Proficiency as one of his fighter bonus feats.'
    },
    'Extend Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'An extended spell lasts twice as long as normal. An extended spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Extra Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke creatures',
        'benefit': 'Each time you take this feat, you can use your ability to turn or rebuke creatures four more times per day than normal.',
        'special': 'You can gain Extra Turning multiple times.'
    },
    'Far Shot': {
        'type': 'Combat',
        'prerequisites': 'Point Blank Shot',
        'benefit': 'When you use a projectile weapon, its range increment increases by one-half (multiply by 1-1/2). When you use a thrown weapon, its range increment is doubled.',
        'special': 'A fighter may select Far Shot as one of his fighter bonus feats.'
    },
    'Forge Ring': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 12th',
        'benefit': 'You can create any ring whose prerequisites you meet.',
        'special': ''
    },
    'Great Cleave': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Cleave, Power Attack, base attack bonus +4',
        'benefit': 'This feat works like Cleave, except that there is no limit to the number of times you can use it per round.',
        'special': 'A fighter may select Great Cleave as one of his fighter bonus feats.'
    },
    'Great Fortitude': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Fortitude saving throws.',
        'special': ''
    },
    'Greater Spell Focus': {
        'type': 'General',
        'prerequisites': 'Spell Focus',
        'benefit': 'Add +1 to the Difficulty Class for all saving throws against spells from the school of magic you select. This bonus stacks with the bonus from Spell Focus.',
        'special': 'You can gain this feat multiple times.'
    },
    'Greater Spell Penetration': {
        'type': 'General',
        'prerequisites': 'Spell Penetration',
        'benefit': 'You get a +2 bonus on caster level checks to overcome a creature\'s spell resistance. This bonus stacks with the one from Spell Penetration.',
        'special': ''
    },
    'Greater Weapon Focus': {
        'type': 'Combat',
        'prerequisites': 'Weapon Focus, fighter level 8th',
        'benefit': 'You gain a +1 bonus on all attack rolls you make using the selected weapon. This bonus stacks with the bonus from Weapon Focus.',
        'special': 'A fighter may select Greater Weapon Focus as one of his fighter bonus feats. You can gain Greater Weapon Focus multiple times.'
    },
    'Greater Weapon Specialization': {
        'type': 'Combat',
        'prerequisites': 'Greater Weapon Focus, Weapon Focus, Weapon Specialization, fighter level 12th',
        'benefit': 'You gain a +2 bonus on all damage rolls you make using the selected weapon. This bonus stacks with other bonuses on damage rolls, including the one from Weapon Specialization.',
        'special': 'A fighter may select Greater Weapon Specialization as one of his fighter bonus feats. You can gain Greater Weapon Specialization multiple times.'
    },
    'Heighten Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'A heightened spell has a higher spell level than normal (up to a maximum of 9th level). Unlike other metamagic feats, Heighten Spell actually changes the effective level of the spell that it modifies.',
        'special': ''
    },
    'Improved Bull Rush': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Power Attack',
        'benefit': 'When you perform a bull rush, you do not provoke an attack of opportunity from the defender. You also gain a +4 bonus on the opposed Strength check you make to push back the defender.',
        'special': 'A fighter may select Improved Bull Rush as one of his fighter bonus feats.'
    },
    'Improved Critical': {
        'type': 'Combat',
        'prerequisites': 'Proficient with weapon, base attack bonus +8',
        'benefit': 'When using the weapon you selected, your threat range is doubled.',
        'special': 'You can gain Improved Critical multiple times. A fighter may select Improved Critical as one of his fighter bonus feats.'
    },
    'Improved Counterspell': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'When counterspelling, you may use a spell of the same school that is one or more spell levels higher than the target spell.',
        'special': ''
    },
    'Improved Disarm': {
        'type': 'Combat',
        'prerequisites': 'Int 13, Combat Expertise',
        'benefit': 'You do not provoke an attack of opportunity when you attempt to disarm an opponent, nor does the opponent have a chance to disarm you. You also gain a +4 bonus on the opposed attack roll you make to disarm your opponent.',
        'special': 'A fighter may select Improved Disarm as one of his fighter bonus feats. A monk may select Improved Disarm as a bonus feat at 6th level, even if she does not meet the prerequisites.'
    },
    'Improved Familiar': {
        'type': 'General',
        'prerequisites': 'Ability to acquire a new familiar, compatible alignment, sufficiently high level',
        'benefit': 'When choosing a familiar, you may choose from an expanded list of creatures.',
        'special': ''
    },
    'Improved Feint': {
        'type': 'Combat',
        'prerequisites': 'Int 13, Combat Expertise',
        'benefit': 'You can make a Bluff check to feint in combat as a move action.',
        'special': 'A fighter may select Improved Feint as one of his fighter bonus feats.'
    },
    'Improved Grapple': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Improved Unarmed Strike',
        'benefit': 'You do not provoke an attack of opportunity when you make a touch attack to start a grapple. You also gain a +4 bonus on all grapple checks.',
        'special': 'A fighter may select Improved Grapple as one of his fighter bonus feats. A monk may select Improved Grapple as a bonus feat at 1st level, even if she does not meet the prerequisites.'
    },
    'Improved Initiative': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'You get a +4 bonus on initiative checks.',
        'special': 'A fighter may select Improved Initiative as one of his fighter bonus feats.'
    },
    'Improved Overrun': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Power Attack',
        'benefit': 'When you attempt to overrun an opponent, the target may not choose to avoid you. You also gain a +4 bonus on your Strength check to knock down your opponent.',
        'special': 'A fighter may select Improved Overrun as one of his fighter bonus feats.'
    },
    'Improved Precise Shot': {
        'type': 'Combat',
        'prerequisites': 'Dex 19, Point Blank Shot, Precise Shot, base attack bonus +11',
        'benefit': 'Your ranged attacks ignore the AC bonus granted to targets by anything less than total cover, and the miss chance granted to targets by anything less than total concealment.',
        'special': 'A fighter may select Improved Precise Shot as one of his fighter bonus feats.'
    },
    'Improved Shield Bash': {
        'type': 'Combat',
        'prerequisites': 'Shield Proficiency',
        'benefit': 'When you perform a shield bash, you may still apply the shield\'s shield bonus to your AC.',
        'special': 'A fighter may select Improved Shield Bash as one of his fighter bonus feats.'
    },
    'Improved Sunder': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Power Attack',
        'benefit': 'When you strike at an object held or carried by an opponent, you do not provoke an attack of opportunity. You also gain a +4 bonus on any attack roll made to attack an object held or carried by another character.',
        'special': 'A fighter may select Improved Sunder as one of his fighter bonus feats.'
    },
    'Improved Trip': {
        'type': 'Combat',
        'prerequisites': 'Int 13, Combat Expertise',
        'benefit': 'You do not provoke an attack of opportunity when you attempt to trip an opponent while you are unarmed. You also gain a +4 bonus on your Strength check to trip your opponent.',
        'special': 'A fighter may select Improved Trip as one of his fighter bonus feats. A monk may select Improved Trip as a bonus feat at 6th level, even if she does not meet the prerequisites.'
    },
    'Improved Turning': {
        'type': 'General',
        'prerequisites': 'Ability to turn or rebuke creatures',
        'benefit': 'You turn or rebuke creatures as if you were one level higher than you actually are in the class that grants you the ability.',
        'special': ''
    },
    'Improved Two-Weapon Fighting': {
        'type': 'Combat',
        'prerequisites': 'Dex 17, Two-Weapon Fighting, base attack bonus +6',
        'benefit': 'You get a second attack with your off-hand weapon, albeit at a -5 penalty.',
        'special': 'A fighter may select Improved Two-Weapon Fighting as one of his fighter bonus feats. A ranger who has chosen the two-weapon combat style is treated as having Improved Two-Weapon Fighting, even if he does not have the prerequisites for it, but only when he is wearing light or no armor.'
    },
    'Improved Unarmed Strike': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'You are considered to be armed even when unarmed. You do not provoke attacks of opportunity from armed opponents when you attack them while unarmed.',
        'special': 'A monk gains Improved Unarmed Strike as a bonus feat at 1st level. A fighter may select Improved Unarmed Strike as one of his fighter bonus feats.'
    },
    'Investigator': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Gather Information checks and Search checks.',
        'special': ''
    },
    'Iron Will': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Will saving throws.',
        'special': ''
    },
    'Leadership': {
        'type': 'General',
        'prerequisites': 'Character level 6th',
        'benefit': 'You attract loyal companions and devoted followers, subordinates who assist you.',
        'special': ''
    },
    'Lightning Reflexes': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Reflex saving throws.',
        'special': ''
    },
    'Magical Aptitude': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Spellcraft checks and Use Magic Device checks.',
        'special': ''
    },
    'Manyshot': {
        'type': 'Combat',
        'prerequisites': 'Dex 17, Point Blank Shot, Rapid Shot, base attack bonus +6',
        'benefit': 'As a standard action, you may fire two arrows at a single opponent within 30 feet. Both arrows use the same attack roll to determine success and deal damage normally.',
        'special': 'A fighter may select Manyshot as one of his fighter bonus feats. A 6th-level ranger who has chosen the archery combat style is treated as having Manyshot even if he does not have the prerequisites for it, but only when he is wearing light or no armor.'
    },
    'Martial Weapon Proficiency': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'You make attack rolls with the weapon normally. Choose a type of martial weapon. You understand how to use that type of martial weapon in combat.',
        'special': 'Barbarians, fighters, paladins, and rangers are proficient with all martial weapons. You can gain Martial Weapon Proficiency multiple times.'
    },
    'Maximize Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'All variable, numeric effects of a spell are maximized. A maximized spell uses up a spell slot three levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Mobility': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Dodge',
        'benefit': 'You get a +4 dodge bonus to Armor Class against attacks of opportunity caused when you move out of or within a threatened area.',
        'special': 'A fighter may select Mobility as one of his fighter bonus feats.'
    },
    'Mounted Archery': {
        'type': 'Combat',
        'prerequisites': 'Ride 1 rank, Mounted Combat',
        'benefit': 'The penalty you take when using a ranged weapon while mounted is halved: -2 instead of -4 if your mount is taking a double move, and -4 instead of -8 if your mount is running.',
        'special': 'A fighter may select Mounted Archery as one of his fighter bonus feats.'
    },
    'Mounted Combat': {
        'type': 'Combat',
        'prerequisites': 'Ride 1 rank',
        'benefit': 'Once per round when your mount is hit in combat, you may attempt a Ride check to negate the hit.',
        'special': 'A fighter may select Mounted Combat as one of his fighter bonus feats.'
    },
    'Natural Spell': {
        'type': 'General',
        'prerequisites': 'Wis 13, wild shape ability',
        'benefit': 'You can complete the verbal and somatic components of spells while in a wild shape. You substitute various noises and gestures for the normal verbal and somatic components of a spell.',
        'special': ''
    },
    'Negotiator': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Diplomacy checks and Sense Motive checks.',
        'special': ''
    },
    'Nimble Fingers': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Disable Device checks and Open Lock checks.',
        'special': ''
    },
    'Persuasive': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Bluff checks and Intimidate checks.',
        'special': ''
    },
    'Point Blank Shot': {
        'type': 'Combat',
        'prerequisites': 'None',
        'benefit': 'You get a +1 bonus on attack and damage rolls with ranged weapons at ranges of up to 30 feet.',
        'special': 'A fighter may select Point Blank Shot as one of his fighter bonus feats.'
    },
    'Power Attack': {
        'type': 'Combat',
        'prerequisites': 'Str 13',
        'benefit': 'On your action, before making attack rolls for a round, you may choose to subtract a number from all melee attack rolls and add the same number to all melee damage rolls.',
        'special': 'A fighter may select Power Attack as one of his fighter bonus feats.'
    },
    'Precise Shot': {
        'type': 'Combat',
        'prerequisites': 'Point Blank Shot',
        'benefit': 'You can shoot or throw ranged weapons at an opponent engaged in melee without taking the standard -4 penalty on your attack roll.',
        'special': 'A fighter may select Precise Shot as one of his fighter bonus feats.'
    },
    'Quick Draw': {
        'type': 'Combat',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'You can draw a weapon as a free action instead of as a move action.',
        'special': 'A fighter may select Quick Draw as one of his fighter bonus feats.'
    },
    'Quicken Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'Casting a quickened spell is a free action. You can perform another action, even casting another spell, in the same round as you cast a quickened spell. A quickened spell uses up a spell slot four levels higher than the spell\'s actual level.',
        'special': ''
    },
    'Rapid Reload': {
        'type': 'Combat',
        'prerequisites': 'Weapon Proficiency (crossbow type chosen)',
        'benefit': 'The time required for you to reload your chosen type of crossbow is reduced to a free action (for a hand or light crossbow) or a move action (for a heavy crossbow).',
        'special': 'A fighter may select Rapid Reload as one of his fighter bonus feats.'
    },
    'Rapid Shot': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Point Blank Shot',
        'benefit': 'You can get one extra attack per round with a ranged weapon. The attack is at your highest base attack bonus, but each attack you make in that round (the extra one and the normal ones) takes a -2 penalty.',
        'special': 'A fighter may select Rapid Shot as one of his fighter bonus feats. A 2nd-level ranger who has chosen the archery combat style is treated as having Rapid Shot, even if he does not have the prerequisites for it, but only when he is wearing light or no armor.'
    },
    'Ride-By Attack': {
        'type': 'Combat',
        'prerequisites': 'Ride 1 rank, Mounted Combat',
        'benefit': 'When you are mounted and use the charge action, you may move and attack as if with a standard charge and then move again.',
        'special': 'A fighter may select Ride-By Attack as one of his fighter bonus feats.'
    },
    'Run': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'When running, you move five times your normal speed (if wearing medium, light, or no armor and carrying no more than a medium load) or four times your speed (if wearing heavy armor or carrying a heavy load).',
        'special': ''
    },
    'Scribe Scroll': {
        'type': 'Item Creation',
        'prerequisites': 'Caster level 1st',
        'benefit': 'You can create a scroll of any spell that you know.',
        'special': 'All wizards gain Scribe Scroll as a bonus feat at 1st level.'
    },
    'Self-Sufficient': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Heal checks and Survival checks.',
        'special': ''
    },
    'Shield Proficiency': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You can use a shield and take only the standard penalties.',
        'special': 'Barbarians, bards, clerics, druids, fighters, paladins, and rangers automatically have Shield Proficiency as a bonus feat.'
    },
    'Shot on the Run': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Dodge, Mobility, Point Blank Shot, base attack bonus +4',
        'benefit': 'When using the attack action with a ranged weapon, you can move both before and after the attack, provided that your total distance moved is not greater than your speed.',
        'special': 'A fighter may select Shot on the Run as one of his fighter bonus feats.'
    },
    'Silent Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'A silent spell can be cast with no verbal components. A silent spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Simple Weapon Proficiency': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You make attack rolls with simple weapons normally.',
        'special': 'All characters except druids, monks, and wizards are automatically proficient with all simple weapons.'
    },
    'Skill Focus': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +3 bonus on all checks involving that skill. Choose a skill. If you have 10 or more ranks in that skill, this bonus increases to +6.',
        'special': 'You can gain this feat multiple times.'
    },
    'Snatch Arrows': {
        'type': 'Combat',
        'prerequisites': 'Dex 15, Deflect Arrows, Improved Unarmed Strike',
        'benefit': 'When using the Deflect Arrows feat, you may catch the weapon instead of just deflecting it.',
        'special': 'A fighter may select Snatch Arrows as one of his fighter bonus feats.'
    },
    'Spell Focus': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Add +1 to the Difficulty Class for all saving throws against spells from the school of magic you select.',
        'special': 'You can gain this feat multiple times.'
    },
    'Spell Mastery': {
        'type': 'Special',
        'prerequisites': 'Wizard level 1st',
        'benefit': 'Each time you take this feat, choose a number of spells equal to your Intelligence modifier. From that point on, you can prepare these spells without referring to a spellbook.',
        'special': 'You can gain this feat multiple times.'
    },
    'Spell Penetration': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on caster level checks to overcome a creature\'s spell resistance.',
        'special': ''
    },
    'Spirited Charge': {
        'type': 'Combat',
        'prerequisites': 'Ride 1 rank, Mounted Combat, Ride-By Attack',
        'benefit': 'When mounted and using the charge action, you deal double damage with a melee weapon (or triple damage with a lance).',
        'special': 'A fighter may select Spirited Charge as one of his fighter bonus feats.'
    },
    'Spring Attack': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Dodge, Mobility, base attack bonus +4',
        'benefit': 'When using the attack action with a melee weapon, you can move both before and after the attack, provided that your total distance moved is not greater than your speed.',
        'special': 'A fighter may select Spring Attack as one of his fighter bonus feats.'
    },
    'Stealthy': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Hide checks and Move Silently checks.',
        'special': ''
    },
    'Still Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'A stilled spell can be cast with no somatic components. A stilled spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Stunning Fist': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Wis 13, Improved Unarmed Strike, base attack bonus +8',
        'benefit': 'You must declare that you are using this feat before you make your attack roll. Stunning Fist forces a foe damaged by your unarmed attack to make a Fortitude saving throw (DC 10 + 1/2 your character level + your Wis modifier), in addition to dealing damage normally.',
        'special': 'A monk may select Stunning Fist as a bonus feat at 1st level, even if she does not meet the prerequisites. A fighter may select Stunning Fist as one of his fighter bonus feats.'
    },
    'Sunder': {
        'type': 'Combat',
        'prerequisites': 'Str 13, Power Attack',
        'benefit': 'When you strike at an object held or carried by an opponent, you do not provoke an attack of opportunity.',
        'special': 'A fighter may select Sunder as one of his fighter bonus feats.'
    },
    'Toughness': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain +3 hit points.',
        'special': 'You can gain this feat multiple times.'
    },
    'Track': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'To find tracks or to follow them for 1 mile requires a successful Survival check. You must make another Survival check every time the tracks become difficult to follow.',
        'special': 'A ranger gains Track as a bonus feat at 1st level.'
    },
    'Trample': {
        'type': 'Combat',
        'prerequisites': 'Ride 1 rank, Mounted Combat',
        'benefit': 'When you attempt to overrun an opponent while mounted, your target may not choose to avoid you. Your mount may make one hoof attack against any target you knock down.',
        'special': 'A fighter may select Trample as one of his fighter bonus feats.'
    },
    'Two-Weapon Defense': {
        'type': 'Combat',
        'prerequisites': 'Dex 15, Two-Weapon Fighting',
        'benefit': 'When wielding a double weapon or two weapons (not including natural weapons or unarmed strikes), you gain a +1 shield bonus to your AC.',
        'special': 'A fighter may select Two-Weapon Defense as one of his fighter bonus feats. A ranger who has chosen the two-weapon combat style is treated as having Two-Weapon Defense, but only when wearing light or no armor.'
    },
    'Two-Weapon Fighting': {
        'type': 'Combat',
        'prerequisites': 'Dex 15',
        'benefit': 'Your penalties on attack rolls for fighting with two weapons are reduced. The penalty for your primary hand lessens by 2 and the one for your off hand lessens by 6.',
        'special': 'A fighter may select Two-Weapon Fighting as one of his fighter bonus feats. A ranger who has chosen the two-weapon combat style is treated as having Two-Weapon Fighting, even if he does not have the prerequisites for it, but only when he is wearing light or no armor.'
    },
    'Weapon Finesse': {
        'type': 'Combat',
        'prerequisites': 'Base attack bonus +1',
        'benefit': 'With a light weapon, rapier, whip, or spiked chain made for a creature of your size category, you may use your Dexterity modifier instead of your Strength modifier on attack rolls.',
        'special': 'A fighter may select Weapon Finesse as one of his fighter bonus feats.'
    },
    'Weapon Focus': {
        'type': 'Combat',
        'prerequisites': 'Proficiency with weapon, base attack bonus +1',
        'benefit': 'You gain a +1 bonus on all attack rolls you make using the selected weapon.',
        'special': 'You can gain Weapon Focus multiple times. A fighter may select Weapon Focus as one of his fighter bonus feats.'
    },
    'Weapon Specialization': {
        'type': 'Combat',
        'prerequisites': 'Weapon Focus, fighter level 4th',
        'benefit': 'You gain a +2 bonus on all damage rolls you make using the selected weapon.',
        'special': 'You can gain Weapon Specialization multiple times. A fighter may select Weapon Specialization as one of his fighter bonus feats.'
    },
    'Whirlwind Attack': {
        'type': 'Combat',
        'prerequisites': 'Dex 13, Int 13, Combat Expertise, Dodge, Mobility, Spring Attack, base attack bonus +4',
        'benefit': 'When you use the full attack action, you can give up your regular attacks and instead make one melee attack at your full base attack bonus against each opponent within reach.',
        'special': 'A fighter may select Whirlwind Attack as one of his fighter bonus feats.'
    },
    'Widen Spell': {
        'type': 'Metamagic',
        'prerequisites': 'None',
        'benefit': 'You can alter a burst, emanation, line, or spread shaped spell to increase its area. Any numeric measurements of the spell\'s area increase by 100%. A widened spell uses up a spell slot three levels higher than the spell\'s actual level.',
        'special': ''
    }
}
