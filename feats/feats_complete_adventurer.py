"""

D&D 3rd Edition Feats from Complete Adventurer

Feats for rogues, bards, rangers, scouts, and other skilled adventurers

"""

COMPLETE_ADVENTURER_FEATS = {

    'Appraise Magic Value': {
        'type': 'General',
        'prerequisites': 'Appraise 5 ranks, Knowledge (arcana) 5 ranks, Spellcraft 5 ranks',
        'benefit': 'If you know that an item is magical, you can use the Appraise skill to identify the item\'s properties. This use of the Appraise skill requires 8 hours of uninterrupted work and consumes 25 gp worth of special materials. The DC of the Appraise check is 10 + the caster level of the item.',
        'special': ''
    },

    'Ascetic Hunter': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Improved Unarmed Strike, favored enemy',
        'benefit': 'When you use an unarmed strike to deliver a stunning attack against a favored enemy, you can add one-half your favored enemy bonus on damage rolls to the DC of your stunning attempt. If you have levels in ranger and monk, those levels stack for the purpose of determining your unarmed strike damage. In addition, you can multiclass freely between the monk and ranger classes.',
        'special': 'You must still remain lawful in order to retain your monk abilities and take monk levels.'
    },

    'Ascetic Knight': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Improved Unarmed Strike, ability to smite evil',
        'benefit': 'Your paladin and monk levels stack for the purpose of determining your unarmed strike damage. Your paladin and monk levels also stack when determining the extra damage dealt by your smite evil ability. In addition, you can multiclass freely between the paladin and monk classes.',
        'special': 'You must still remain lawful good in order to retain your paladin abilities and take paladin levels, and you must remain lawful in order to continue advancing as a monk.'
    },

    'Ascetic Mage': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Improved Unarmed Strike, ability to spontaneously cast 2nd-level arcane spells',
        'benefit': 'As a swift action, you can sacrifice one of your daily allotment of spells to add a bonus to your unarmed strike attack rolls and damage rolls for 1 round equal to the level of the spell sacrificed. If you have levels in sorcerer and monk, those levels stack for the purpose of determining your AC bonus.',
        'special': 'You must still remain lawful in order to continue advancing as a monk.'
    },

    'Ascetic Rogue': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Improved Unarmed Strike, sneak attack',
        'benefit': 'When you use an unarmed strike with a sneak attack to deliver a stunning attack, you add 2 to the DC of your stunning attempt. If you have levels in rogue and monk, those levels stack for the purpose of determining your unarmed strike damage. In addition, you can multiclass freely between the monk and rogue classes.',
        'special': 'You must still remain lawful in order to retain your monk abilities and take monk levels.'
    },

    'Brachiation': {
        'type': 'General',
        'prerequisites': 'Climb 4 ranks, Jump 4 ranks',
        'benefit': 'You can move through wooded areas at your base land speed, ignoring any effects on movement due to terrain. You must be at least 20 feet from the ground to use this ability. This ability works only in medium and dense forests.',
        'special': ''
    },

    'Brutal Throw': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'None',
        'benefit': 'You can add your Strength modifier instead of your Dexterity modifier to attack rolls with thrown weapons.',
        'special': 'A fighter may select Brutal Throw as one of his fighter bonus feats.'
    },

    'Combat Intuition': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Sense Motive 4 ranks, base attack bonus +5',
        'benefit': 'As a free action, you can use Sense Motive to assess the challenge presented by a single opponent in relationship to your own level. You gain a +4 bonus on such checks and narrow the result to a single category. In addition, whenever you make a melee attack against a creature that you made a melee attack against during the previous round, you gain a +1 insight bonus on your melee attack rolls against that creature.',
        'special': 'A fighter may select Combat Intuition as one of his fighter bonus feats.'
    },

    'Danger Sense': {
        'type': 'General',
        'prerequisites': 'Improved Initiative',
        'benefit': 'Once per day, you can reroll an initiative check you have just made. You use the better of your two rolls. You must decide to reroll before the round starts.',
        'special': ''
    },

    'Death Blow': {
        'type': 'General',
        'prerequisites': 'Improved Initiative, base attack bonus +2',
        'benefit': 'You can perform a coup de grace attack against a helpless defender as a standard action. Doing this still provokes attacks of opportunity as normal.',
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
        'benefit': 'As a standard action, you can attempt to find a weak point in a visible target\'s armor. This requires a Spot check against a DC equal to your target\'s Armor Class. If you succeed, your next attack against that target ignores the target\'s armor bonus and natural armor bonus to AC.',
        'special': ''
    },

    'Devoted Inquisitor': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Smite evil, sneak attack',
        'benefit': 'When you successfully use your sneak attack ability and your smite evil ability against the same foe in a single attack, you can potentially daze your foe. An opponent affected by both abilities must make a Will saving throw or be dazed for 1 round. In addition, you can multiclass freely between the paladin and rogue classes.',
        'special': 'You must still remain lawful good in order to retain your paladin abilities and take paladin levels.'
    },

    'Devoted Performer': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Bardic music, smite evil',
        'benefit': 'If you have levels in paladin and bard, those levels stack for the purpose of determining the bonus damage dealt by your smite evil ability and determining the number of times per day that you can use your bardic music. In addition, you can multiclass freely between the paladin and bard classes.',
        'special': 'You must still remain lawful good in order to retain your paladin abilities and take paladin levels.'
    },

    'Devoted Tracker': {
        'type': 'General (Multiclass)',
        'prerequisites': 'Track, smite evil, wild empathy',
        'benefit': 'If you have levels in paladin and ranger, those levels stack for the purposes of determining the extra damage dealt by your smite evil ability and determining the bonus for your wild empathy class feature. If you have both the special mount and animal companion class features, you can designate your special mount as your animal companion. In addition, you can multiclass freely between the paladin and ranger classes.',
        'special': 'You must still remain lawful good in order to retain your paladin abilities and take paladin levels.'
    },

    'Disguise Spell': {
        'type': 'General',
        'prerequisites': 'Perform (any) 9 ranks, bardic music',
        'benefit': 'You can cast spells unobtrusively, mingling verbal and somatic components into your performances. To disguise a spell, make a Perform check as part of the action used to cast the spell. Onlookers must match or exceed your check result with a Spot check to detect that you\'re casting a spell.',
        'special': 'The act of casting still provokes attacks of opportunity as normal.'
    },

    'Dive for Cover': {
        'type': 'General',
        'prerequisites': 'Base Reflex save bonus +4',
        'benefit': 'If you fail a Reflex saving throw, you can immediately attempt the saving throw again. You must take the second result, whether it succeeds or fails. You become prone immediately after attempting the second roll.',
        'special': ''
    },

    'Dual Strike': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Improved Two-Weapon Fighting, Two-Weapon Fighting',
        'benefit': 'As a standard action, you can make a melee attack with your primary weapon and your off-hand weapon. Both attacks use the same attack roll to determine success, using the worse of the two weapons\'s attack modifiers. Each weapon deals its normal damage.',
        'special': 'A fighter may select Dual Strike as one of his fighter bonus feats.'
    },

    'Expert Tactician': {
        'type': 'General',
        'prerequisites': 'Dex 13, Combat Reflexes, base attack bonus +2',
        'benefit': 'If you hit a creature with an attack of opportunity, you and all your allies gain a +2 circumstance bonus on melee attack rolls and damage rolls against that creature for 1 round.',
        'special': ''
    },

    'Extra Music': {
        'type': 'General',
        'prerequisites': 'Bardic music',
        'benefit': 'You can use your bardic music four extra times per day.',
        'special': 'You can gain this feat multiple times. Its effects stack.'
    },

    'Extraordinary Concentration': {
        'type': 'General',
        'prerequisites': 'Concentration 15 ranks',
        'benefit': 'When concentrating to maintain a spell, you can make a Concentration check (DC 25 + spell level) to maintain concentration with just a move action. If you beat the DC by 10 or more, you can maintain concentration as a swift action.',
        'special': ''
    },

    'Extraordinary Spell Aim': {
        'type': 'General',
        'prerequisites': 'Spellcraft 15 ranks',
        'benefit': 'Whenever you cast a spell with an area, you can attempt to shape the spell\'s area so that one creature within the area is unaffected by the spell. To accomplish this, you must succeed on a Spellcraft check (DC 25 + spell level).',
        'special': 'Casting a spell affected by this feat requires a full-round action unless the spell\'s normal casting time is longer.'
    },

    'Force of Personality': {
        'type': 'General',
        'prerequisites': 'Cha 13',
        'benefit': 'You add your Charisma modifier instead of your Wisdom modifier to Will saves against mind-affecting spells and abilities.',
        'special': ''
    },

    'Goad': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Cha 13, base attack bonus +1',
        'benefit': 'As a move action, you can goad an opponent that threatens you, has line of sight to you, can hear you, and has an Intelligence of 3 or higher. When the goaded opponent starts its next turn, if it threatens you and has line of sight to you, it must make a Will saving throw or you are the only creature it can make melee attacks against during this turn.',
        'special': 'A fighter may select Goad as one of his fighter bonus feats.'
    },

    'Green Ear': {
        'type': 'General',
        'prerequisites': 'Perform (any) 10 ranks, bardic music',
        'benefit': 'You can alter any of your mind-affecting bardic music abilities or similar Perform-based abilities so that they influence only plant creatures instead of other creatures. However, plants receive a +5 bonus on Will saves against any of these effects.',
        'special': 'Plants are normally immune to all mind-affecting spells and abilities.'
    },

    'Hear the Unseen': {
        'type': 'General',
        'prerequisites': 'Listen 5 ranks, Blind-Fight',
        'benefit': 'As a move action that does not provoke attacks of opportunity, you can attempt a DC 25 Listen check. If successful, you can pinpoint the location of all foes within 30 feet, as long as you have line of effect to them.',
        'special': 'This feat does not work against perfectly silent opponents, such as incorporeal creatures.'
    },

    'Improved Diversion': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Bluff 4 ranks',
        'benefit': 'You can use Bluff to create a diversion to hide as a move action. You gain a +4 bonus on Bluff checks made for this purpose.',
        'special': 'A fighter may select Improved Diversion as one of his fighter bonus feats.'
    },

    'Improved Flight': {
        'type': 'General',
        'prerequisites': 'Ability to fly naturally, magically, or through shapechanging',
        'benefit': 'Your maneuverability class while flying improves by one step (clumsy to poor, poor to average, average to good, or good to perfect).',
        'special': ''
    },

    'Improved Swimming': {
        'type': 'General',
        'prerequisites': 'Swim 6 ranks',
        'benefit': 'You can swim at half your speed as a move action or at your speed as a full-round action.',
        'special': ''
    },

    'Insightful Reflexes': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You add your Intelligence modifier instead of your Dexterity modifier to Reflex saves.',
        'special': ''
    },

    'Jack of All Trades': {
        'type': 'General',
        'prerequisites': 'Int 13',
        'benefit': 'You can use any skill as if you had 12 ranks in that skill. This benefit allows you to attempt checks with skills that normally don\'t allow untrained skill checks such as Decipher Script and Knowledge.',
        'special': ''
    },

    'Leap Attack': {
        'type': 'General',
        'prerequisites': 'Jump 8 ranks, Power Attack',
        'benefit': 'You can combine a jump with a charge against an opponent. If you cover at least 10 feet of horizontal distance with your jump, and you end your jump in a square from which you threaten your target, you can double the extra damage dealt by your use of the Power Attack feat. With a two-handed weapon, you instead triple the extra damage from Power Attack.',
        'special': ''
    },

    'Lingering Song': {
        'type': 'General',
        'prerequisites': 'Bardic music',
        'benefit': 'If you use bardic music to inspire courage, inspire greatness, or inspire heroics, the effect lasts for 1 minute after an inspired ally stops hearing you play.',
        'special': ''
    },

    'Mobile Spellcasting': {
        'type': 'General',
        'prerequisites': 'Concentration 8 ranks',
        'benefit': 'You can make a special Concentration check (DC 20 + spell level) when casting a spell. If the check succeeds, you can cast the spell and move up to your speed as a single standard action. You can\'t use this ability to cast a spell that takes longer than 1 standard action to cast.',
        'special': 'You still provoke attacks of opportunity for casting spells from any creatures who threaten you at any point of your movement.'
    },

    'Natural Bond': {
        'type': 'General',
        'prerequisites': 'Animal companion',
        'benefit': 'Add three to your effective druid level for the purpose of determining the bonus Hit Dice, extra tricks, special abilities, and other bonuses that your animal companion receives.',
        'special': 'This bonus can never make your effective druid level exceed your character level.'
    },

    'Obscure Lore': {
        'type': 'General',
        'prerequisites': 'Bardic knowledge or lore class feature',
        'benefit': 'You gain a +4 insight bonus on checks using your bardic knowledge or lore class feature.',
        'special': ''
    },

    'Open Minded': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You immediately gain 5 skill points. Spend these skill points as normal. You cannot exceed the normal maximum ranks for your level in any skill.',
        'special': 'You can gain this feat multiple times. Each time, you immediately gain another 5 skill points.'
    },

    'Oversized Two-Weapon Fighting': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Str 13, Two-Weapon Fighting',
        'benefit': 'When wielding a one-handed weapon in your off hand, you take penalties for fighting with two weapons as if you were wielding a light weapon in your off hand.',
        'special': 'A fighter may select Oversized Two-Weapon Fighting as one of his fighter bonus feats.'
    },

    'Power Throw': {
        'type': 'General (Fighter Bonus)',
        'prerequisites': 'Str 13, Brutal Throw, Power Attack',
        'benefit': 'On your turn, before making any attack rolls, you can choose to subtract a number from all thrown weapon attack rolls and add the same number to all thrown weapon damage rolls. This number may not exceed your base attack bonus. The penalty and bonus apply until your next turn.',
        'special': 'A fighter may select Power Throw as one of his fighter bonus feats.'
    },

    'Quick Reconnoiter': {
        'type': 'General',
        'prerequisites': 'Listen 5 ranks, Spot 5 ranks',
        'benefit': 'You can make one Spot check and one Listen check each round as a free action. You also gain a +2 bonus on initiative checks.',
        'special': ''
    },

    'Razing Strike': {
        'type': 'General',
        'prerequisites': 'Sneak attack, ability to cast 3rd-level spells',
        'benefit': 'To activate this feat, you must sacrifice one of your daily allotment of spells (minimum 1st level). You gain an insight bonus on your melee attack rolls and damage rolls for 1 round. The bonus on attack rolls equals the level of the spell sacrificed. The bonuses apply against constructs (if arcane spell) or undead (if divine spell).',
        'special': 'This feat does not allow you to deliver critical hits or sneak attacks against constructs or undead.'
    },

    'Staggering Strike': {
        'type': 'General',
        'prerequisites': 'Base attack bonus +6, sneak attack',
        'benefit': 'If you deal damage with a melee sneak attack, you can also deliver a wound that limits your foe\'s mobility. For 1 round or until the target is healed, your target is treated as if it were staggered. A target can resist this effect by making a successful Fortitude save.',
        'special': 'Multiple staggering strikes on the same creature do not stack.'
    },

    'Subsonics': {
        'type': 'General',
        'prerequisites': 'Perform (any) 10 ranks, bardic music',
        'benefit': 'You can produce music or poetics so subtly that opponents do not notice it, yet your allies still gain all the usual benefits from your bardic music. You can also affect opponents within range with your music, but unless they can see you performing or have some other means of discovering it, they cannot determine the source of the effect.',
        'special': ''
    },

    'Tactile Trapsmith': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You add your Dexterity bonus rather than your Intelligence bonus on all Search and Disable Device checks. In addition, you receive no penalty on these checks for darkness or blindness.',
        'special': ''
    },

    'Versatile Performer': {
        'type': 'General',
        'prerequisites': 'Perform (any) 5 ranks',
        'benefit': 'Pick a number of Perform categories equal to your Intelligence bonus (minimum 1). For the purpose of making Perform checks, you are treated as having a number of ranks in those skills equal to the highest number of ranks you have in any Perform category. You gain a +2 bonus on a combined Perform check when using two or more forms of performance at the same time.',
        'special': 'You cannot change these categories once you have picked them.'
    },

    'Chant of Fortitude': {
        'type': 'Bardic Music',
        'prerequisites': 'Bardic music, Concentration 9 ranks, Perform (any) 9 ranks',
        'benefit': 'You can expend one daily use of your bardic music ability as an immediate action to provide all allies (including yourself) the benefit of the Diehard feat until the end of your next turn. You can use this feat multiple times consecutively to keep yourself and your allies conscious.',
        'special': 'This feat does not function in an area of magical silence.'
    },

    'Ironskin Chant': {
        'type': 'Bardic Music',
        'prerequisites': 'Bardic music, Concentration 12 ranks, Perform (any) 12 ranks',
        'benefit': 'As a swift action that does not provoke attacks of opportunity, you can expend one daily use of your bardic music ability to provide damage reduction of 5 to yourself or to one ally within 30 feet who can hear you until the start of your next turn.',
        'special': 'This feat does not function in an area of magical silence.'
    },

    'Lyric Spell': {
        'type': 'Bardic Music',
        'prerequisites': 'Bardic music, Perform (any) 9 ranks, ability to spontaneously cast 2nd-level arcane spells, caster level 6th',
        'benefit': 'You can expend daily uses of your bardic music to cast any arcane spell that you know and can cast spontaneously. Casting a spell requires one use of your bardic music ability, plus one additional use per level of the spell. Any spell cast using this feat gains your instrument as an additional arcane focus.',
        'special': 'You cannot use Lyric Spell to cast a spell improved by the Silent Spell metamagic feat.'
    },

    'Blindsense': {
        'type': 'Wild',
        'prerequisites': 'Wild shape class feature, Listen 4 ranks',
        'benefit': 'You can expend one daily use of wild shape to gain blindsense for 1 minute per Hit Die, enabling you to pinpoint the location of a creature within 30 feet if you have line of effect to that creature. You retain this benefit regardless of what form you are in.',
        'special': ''
    },

    'Climb Like an Ape': {
        'type': 'Wild',
        'prerequisites': 'Wild shape',
        'benefit': 'You can expend one daily use of wild shape to gain a climb speed equal to your base land speed for 10 minutes per Hit Die. This feat also grants you a +8 racial bonus on Climb checks and allows you to take 10 on Climb checks, even if rushed or threatened.',
        'special': ''
    },

    'Cougar\'s Vision': {
        'type': 'Wild',
        'prerequisites': 'Wild shape, Spot 2 ranks',
        'benefit': 'You can expend one daily use of wild shape to gain low-light vision for 1 hour per Hit Die. In addition, you gain a +4 bonus on all Spot checks. You retain these benefits regardless of what form you are in.',
        'special': ''
    },

    'Hawk\'s Vision': {
        'type': 'Wild',
        'prerequisites': 'Wild shape, Spot 4 ranks',
        'benefit': 'You can expend one of your daily uses of wild shape to gain a +8 bonus on your Spot checks for 1 hour per Hit Die. While this benefit is in effect, you take only half the normal penalty for range increment on ranged attacks.',
        'special': 'You retain these benefits regardless of what form you are in.'
    },

    'Savage Grapple': {
        'type': 'Wild',
        'prerequisites': 'Wild shape, sneak attack',
        'benefit': 'While you are in a wild shape, any time you make a successful grapple check to damage a creature with which you are already grappling, you can add your sneak attack damage as well. Creatures not subject to sneak attacks don\'t take this extra damage.',
        'special': ''
    },

    'Scent': {
        'type': 'Wild',
        'prerequisites': 'Wild shape',
        'benefit': 'You can expend one daily use of wild shape to gain the scent ability for 1 hour per Hit Die. While this benefit is in effect, you can detect opponents within 30 feet by sense of smell. If you have the Track feat, you can track creatures by scent. You retain this benefit regardless of what form you are in.',
        'special': ''
    },

}
