"""
D&D 3rd Edition Complete Mage Feats
Feats for arcane spellcasters from the Complete Mage sourcebook
"""

COMPLETE_MAGE_FEATS = {
  "General Feats": {
    "Alacritous Cogitation": {
      "type": "General",
      "prerequisites": "Must prepare arcane spells",
      "benefit": "If you leave an arcane spell slot open when preparing spells, you can use that open slot to cast any arcane spell you know of the same level or lower. Casting the spell requires a full-round action. You can use this feat only once per day, regardless of the number of slots you leave open.",
      "special": "A wizard can select this feat as a wizard bonus feat."
    },
    "Captivating Melody": {
      "type": "General",
      "prerequisites": "Bardic music, ability to cast arcane spells",
      "benefit": "As a swift action before casting a spell, you can attempt a Perform check DC 15 + the level of the spell you intend to cast. If you succeed, you can sacrifice one of your daily uses of bardic music to increase the save DC of the next enchantment or illusion spell you cast in the same round by 2. If the Perform check fails, you still lose one daily use of bardic music but gain no benefit.",
      "special": "You can apply Captivating Melody only to spells cast by the same class that grants you your bardic music ability."
    },
    "Cloudy Conjuration": {
      "type": "General",
      "prerequisites": "Spell Focus (conjuration) or conjurer level 1st",
      "benefit": "When you cast a conjuration spell, you can choose to have a 5-foot-radius cloud of sickening smoke manifest. The cloud can appear in your space, adjacent to you, or in the space of or adjacent to your target. The cloud lasts for 1 round. Any living creature is sickened while inside it but not after exiting.",
      "special": "A conjurer can select this feat as a wizard bonus feat."
    },
    "Dazzling Illusion": {
      "type": "General",
      "prerequisites": "Spell Focus (illusion) or illusionist level 1st",
      "benefit": "When you cast an illusion spell, you can choose to render all enemies within 30 feet dazzled for 1 round. Blind creatures are immune to this effect.",
      "special": "An illusionist can select this feat as a wizard bonus feat."
    },
    "Defending Spirit": {
      "type": "General",
      "prerequisites": "Watchful spirit class feature (Wu Jen from Complete Arcane)",
      "benefit": "Your watchful spirit helps you defend yourself. If you use an initiative reroll from your watchful spirit class feature, you gain a +2 dodge bonus to your Armor Class for the duration of that encounter. Also, you gain one extra initiative reroll from your watchful spirit class feature.",
      "special": ""
    },
    "Delay Potion": {
      "type": "General",
      "prerequisites": "Knowledge (arcana) 1 rank",
      "benefit": "You can drink a potion and delay its effects for a number of hours equal to your Constitution modifier (minimum 1 hour). At any time during this period, you can activate the potion's effect as a swift action. If the duration expires before you activate the potion, it is wasted. You can delay only one potion at a time.",
      "special": ""
    },
    "Elemental Adept": {
      "type": "General",
      "prerequisites": "Elemental mastery class feature (Wu Jen from Complete Arcane)",
      "benefit": "Choose one spell of the element you have chosen for your elemental mastery class feature. You can now spontaneously cast that spell by sacrificing a prepared spell of equal or higher level. The spell you choose must be in your spellbook. When you gain a level, you can change the spell you can spontaneously cast by picking a new spell of the element you chose for elemental mastery.",
      "special": ""
    },
    "Energy Abjuration": {
      "type": "General",
      "prerequisites": "Spell Focus (abjuration) or abjurer level 1st",
      "benefit": "When you cast an abjuration spell, you can choose to gain a special energy resistance equal to 1 + the spell's level x 5. This energy resistance lasts for the duration of the abjuration spell you cast or until you are struck by any type of energy damage. The resistance applies to the first energy damage to which you are exposed.",
      "special": "An abjurer can select this feat as a wizard bonus feat."
    },
    "Favored Magic Foe": {
      "type": "General",
      "prerequisites": "Knowledge 6 ranks in appropriate skill OR favored enemy class feature",
      "benefit": "Choose a creature type for which you have the favored enemy class feature, or one associated with a Knowledge skill in which you have at least 6 ranks. You gain a +1 bonus on caster level checks to overcome the spell resistance of the chosen creature type, and such creatures take a -1 penalty on saves against your spells and spell-like abilities.",
      "special": "You can take this feat multiple times. Each time you take this feat, you choose a new creature type or subtype."
    },
    "Fearsome Necromancy": {
      "type": "General",
      "prerequisites": "Spell Focus (necromancy) or necromancer level 1st",
      "benefit": "Any foe required to save against a necromancy spell you cast is shaken for 1 round, regardless of the result of the save. This mind-affecting fear ability does not stack with any other fear effect.",
      "special": "A necromancer can select this feat as a wizard bonus feat."
    },
    "Hasty Spirit": {
      "type": "General",
      "prerequisites": "Watchful spirit class feature (Wu Jen from Complete Arcane)",
      "benefit": "If you use an initiative reroll from your watchful spirit class feature, you can take an extra move action on one of your turns during that encounter. Also, you gain one extra initiative reroll from your watchful spirit class feature.",
      "special": ""
    },
    "Insightful Divination": {
      "type": "General",
      "prerequisites": "Spell Focus (divination) or diviner level 1st",
      "benefit": "When you cast a divination spell, you gain an insight bonus equal to the spell's level - 1 on initiative checks and an equal insight bonus on the first save you make within the next 24 hours.",
      "special": "A diviner can select this feat as a wizard bonus feat."
    },
    "Magic Device Attunement": {
      "type": "General",
      "prerequisites": "Use Magic Device 1 rank",
      "benefit": "If you successfully activate an item with the Use Magic Device skill, you can take a free action to attune yourself to the item. For the next 24 hours, you can activate that item without making further Use Magic Device checks. You can attune yourself to only one item at a time.",
      "special": ""
    },
    "Master of Undeath": {
      "type": "General",
      "prerequisites": "Knowledge (religion) 5 ranks",
      "benefit": "When you create an undead creature, you can decide that it doesn't count against your normal limit of controlled undead creatures. In this case, you still control the creature, but only for a number of days equal to your caster level. When this duration ends, the undead immediately becomes hostile to you.",
      "special": "You can have only one creature of this kind at a time."
    },
    "Melodic Casting": {
      "type": "General",
      "prerequisites": "Perform 4 ranks, Spellcraft 4 ranks, bardic music class feature",
      "benefit": "Whenever a Concentration check would be required to cast a spell or use a spell-like ability, you can make a Perform check instead. In addition, you can cast spells and activate magic items by command word or spell completion while using a bardic music ability.",
      "special": ""
    },
    "Metamagic School Focus": {
      "type": "General",
      "prerequisites": "Spell Focus (chosen school) OR specialist wizard in chosen school",
      "benefit": "Choose a school of magic for which you have the Spell Focus feat, or the school in which you have specialized. Three times per day, you can reduce by one level the cost of a metamagic feat applied to a spell of the chosen school.",
      "special": "A wizard can select this feat as a wizard bonus feat. This feat can be taken more than once."
    },
    "Metamagic Spell Trigger": {
      "type": "General",
      "prerequisites": "Any metamagic feat, Use Magic Device 15 ranks OR Spellcraft 15 ranks",
      "benefit": "You can apply any one metamagic feat you know to a spell generated by a spell trigger item such as a wand or staff that you activate. You expend one extra charge for each change in spell level a metamagic feat normally requires.",
      "special": ""
    },
    "Piercing Evocation": {
      "type": "General",
      "prerequisites": "Spell Focus (evocation) OR evoker level 1st",
      "benefit": "When you cast an evocation spell that deals energy damage (acid, cold, fire, electricity, or sonic), you can choose for 10 points of energy damage dealt by the spell to become untyped damage to which energy resistance and immunity do not apply.",
      "special": "An evoker can select this feat as a wizard bonus feat."
    },
    "Ranged Recall": {
      "type": "General",
      "prerequisites": "Spellcraft 4 ranks, Point Blank Shot, Weapon Focus (ranged spell)",
      "benefit": "When you miss with a spell or spell-like ability ranged attack against a target within 30 feet, you can spend a swift action to reroll the attack with a -5 penalty. You can use this ability three times per day.",
      "special": ""
    },
    "Rapid Metamagic": {
      "type": "General",
      "prerequisites": "Spellcraft 12 ranks, ability to spontaneously cast spells",
      "benefit": "When you apply a metamagic feat to a spontaneously cast spell, the spell takes only its normal casting time instead of a full-round action.",
      "special": ""
    },
    "Somatic Weaponry": {
      "type": "General",
      "prerequisites": "Concentration 5 ranks, Spellcraft 5 ranks",
      "benefit": "When wielding a weapon or holding an item of comparable size in one or both hands, you can use that item to trace the somatic component of a spell, rather than using your fingers. This allows you to cast spells with somatic components even while your hands are full or occupied.",
      "special": "This feat doesn't allow you to use somatic components while grappling."
    },
    "Toughening Transmutation": {
      "type": "General",
      "prerequisites": "Spell Focus (transmutation) OR transmuter level 1st",
      "benefit": "Whenever you cast a transmutation spell, you can choose to grant yourself or any one creature targeted by the spell damage reduction 5/magic. This effect lasts for 1 round.",
      "special": "A transmuter can select this feat as a wizard bonus feat."
    },
    "Unsettling Enchantment": {
      "type": "General",
      "prerequisites": "Spell Focus (enchantment) OR enchanter level 1st",
      "benefit": "Any foe required to save against an enchantment spell you cast takes a -2 penalty on attack rolls and to AC for 1 round, regardless of the result of the save. This is a mind-affecting effect.",
      "special": "An enchanter can select this feat as a wizard bonus feat."
    },
    "Vengeful Spirit": {
      "type": "General",
      "prerequisites": "Watchful spirit class feature (Wu Jen from Complete Arcane)",
      "benefit": "If you use an initiative reroll from your watchful spirit class feature, the first creature to deal damage to you in the encounter immediately takes half the damage it dealt to you. This damage is untyped, so damage reduction and resistance or immunity does not apply. Also, you gain one extra initiative reroll from your watchful spirit class feature.",
      "special": ""
    }
  },
  "Heritage Feats": {
    "Fey Heritage": {
      "type": "Heritage",
      "prerequisites": "Nonlawful alignment",
      "benefit": "You gain a +3 bonus on Will saving throws against enchantment effects.",
      "special": ""
    },
    "Fey Legacy": {
      "type": "Heritage",
      "prerequisites": "Nonlawful alignment, Fey Heritage, character level 9th",
      "benefit": "You gain the following spell-like abilities, each usable once per day: confusion, dimension door, and summon nature's ally V. Your caster level equals your character level.",
      "special": ""
    },
    "Fey Power": {
      "type": "Heritage",
      "prerequisites": "Nonlawful alignment, Fey Heritage",
      "benefit": "Your caster level and save DCs for enchantment spells and warlock invocations increase by 1.",
      "special": ""
    },
    "Fey Presence": {
      "type": "Heritage",
      "prerequisites": "Nonlawful alignment, Fey Heritage, character level 6th",
      "benefit": "You gain the following spell-like abilities, each usable once per day: charm monster, deep slumber, and disguise self. Your caster level equals your character level.",
      "special": ""
    },
    "Fey Skin": {
      "type": "Heritage",
      "prerequisites": "Nonlawful alignment, Fey Heritage",
      "benefit": "You gain damage reduction overcome by cold iron equal to 1 + the number of feats you have that list Fey Heritage as a prerequisite. This value stacks with any similar damage reduction you might have from your type, subtype, race, or class.",
      "special": ""
    },
    "Fiendish Heritage": {
      "type": "Heritage",
      "prerequisites": "Non-good alignment",
      "benefit": "You gain a +4 bonus on Fortitude saving throws against poison. You also gain a +1 bonus on saving throws against spells or other effects produced by good creatures.",
      "special": ""
    },
    "Fiendish Legacy": {
      "type": "Heritage",
      "prerequisites": "Non-good alignment, Fiendish Heritage, character level 9th",
      "benefit": "You gain the following spell-like abilities, each usable once per day: teleport (self plus 50 pounds of objects only), summon monster V (fiendish creatures only), and unholy blight. Your caster level equals your character level.",
      "special": ""
    },
    "Fiendish Power": {
      "type": "Heritage",
      "prerequisites": "Non-good alignment, Fiendish Heritage",
      "benefit": "Your caster level and save DCs for evil spells and warlock invocations increase by 1.",
      "special": ""
    },
    "Fiendish Presence": {
      "type": "Heritage",
      "prerequisites": "Non-good alignment, Fiendish Heritage, character level 6th",
      "benefit": "You gain the following spell-like abilities, each usable once per day: cause fear, detect thoughts, and suggestion. Your caster level equals your character level.",
      "special": ""
    },
    "Fiendish Resistance": {
      "type": "Heritage",
      "prerequisites": "Non-good alignment, Fiendish Heritage",
      "benefit": "You gain resistance to acid and fire equal to three times the number of feats you have that list Fiendish Heritage as a prerequisite. These values stack with any resistance to acid or fire you might have from your type, subtype, race, or class.",
      "special": ""
    }
  },
  "Reserve Feats": {
    "Acidic Splatter": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have an acid spell of 2nd level or higher available to cast, you can throw an orb of acid as a ranged touch attack. The attack has a range of 5 feet per level of the highest-level acid spell you have available to cast and deals 1d6 points of damage per level of that acid spell.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting acid spells."
    },
    "Aquatic Breath": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a water spell of 3rd level or higher available to cast, you can breathe normally in both air and water. This supernatural quality requires no activation.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting water spells."
    },
    "Blade of Force": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a 3rd-level or higher force spell available to cast, you can surround a melee weapon or a single piece of ammunition with a thin field of force. Activating this ability is a swift action. The next attack made with that weapon deals an extra 1 point of damage per level of the highest-level force spell you have available to cast. Furthermore, that weapon ignores the miss chance normally granted to an incorporeal creature.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting force spells."
    },
    "Borne Aloft": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 5th-level spells",
      "benefit": "As long as you have an air spell of 5th level or higher available to cast, you can fly up to 30 feet (perfect maneuverability) as a move action once per round. You must begin and end this flight solidly supported, or you fall. You can't use this ability if you wear heavy armor or carry a heavy load.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting air spells."
    },
    "Clap of Thunder": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a sonic spell of 3rd level or higher available to cast, you can deliver a melee touch attack as a standard action. This attack deals 1d6 points of sonic damage per level of the highest-level sonic spell you have available to cast. Additionally, the subject must succeed on a Fortitude save or be deafened for 1 round.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting sonic spells."
    },
    "Clutch of Earth": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have an earth spell of 2nd level or higher available to cast, you can spend a standard action to reduce the speed of any landbound creature within 30 feet of you. The creature's normal land speed, as well as its burrow and climb speeds, decrease by 5 feet per level of the highest-level earth spell you have available to cast, to a minimum speed of 5 feet. This effect lasts for 1 round. A successful Fortitude save negates this effect and renders the target immune to the feat's effect for 24 hours.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting earth spells."
    },
    "Dimensional Jaunt": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 4th-level spells",
      "benefit": "As long as you have a teleportation spell of 4th level or higher available to cast, you can spend a standard action to teleport yourself and carried objects up to your heavy load a distance of 5 feet per level of the highest-level teleportation spell you have available to cast. You can teleport only to a location that you can see.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting teleportation spells."
    },
    "Dimensional Reach": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a conjuration (summoning) spell of 3rd level or higher available to cast, you can transport small items directly into your hand as a standard action. You must have line of sight to an item you wish to transport in this way, and it must be unattended. This ability works at a range of up to 5 feet per level of the highest-level summoning spell you have available to cast, and the item can weigh up to 2 pounds per level of that spell.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting conjuration (summoning) spells."
    },
    "Drowning Glance": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 4th-level spells",
      "benefit": "As long as you have a water spell of 4th level or higher available to cast, you can use a standard action to transform a small portion of the air in a living creature's lungs to water, making it difficult for the creature to breathe. The subject must be within 30 feet. The target becomes exhausted for 1 round; if it succeeds on a Fortitude save, it is instead fatigued for 1 round. Whether or not a targeted creature successfully saves, it is immune to any further uses of your Drowning Glance for 24 hours.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting water spells. Creatures that can breathe water or who don't breathe are immune to this effect."
    },
    "Face-Changer": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a glamer spell of 3rd level or higher available to cast, you can alter your appearance as the spell disguise self, except that the duration lasts 1 minute per level of the glamer spell. This illusory transformation requires a full-round action to activate.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting glamer spells."
    },
    "Fiery Burst": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have a fire spell of 2nd level or higher available to cast, you can spend a standard action to create a 5-foot-radius burst of fire at a range of 30 feet. This burst deals 1d6 points of fire damage per level of the highest-level fire spell you have available to cast. A successful Reflex save halves the damage.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting fire spells."
    },
    "Hurricane Breath": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have an air spell of 2nd level or higher available to cast, you can attempt to knock a single creature within 30 feet back with a blast of wind. This requires a standard action and functions much like a bull rush (roll 1d20 + the level of the highest-level air spell you have available to cast, opposed by your opponent's Strength check). If you succeed, you push the creature back 5 feet.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting air spells."
    },
    "Invisible Needle": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a force spell of 3rd level or higher available to cast, you can use a standard action to hurl a tiny needle-shaped projectile created from pure force. This attack requires a successful ranged attack roll (not a ranged touch attack), and the dart has a range of 5 feet per level of the force spell. The needle deals 1d4 points of damage per level of the highest-level force spell you have available. Because it is composed of force, the needle can strike incorporeal creatures.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting force spells."
    },
    "Magic Disruption": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have an abjuration spell of 3rd level or higher available to cast, you can attempt to interrupt another character's spellcasting with a tiny burst of magic. As an immediate action, you can force any character within 30 feet currently casting a spell to make a Concentration check (DC 15 + the level of the highest-level abjuration spell you have available to cast). If the check fails, the spell's save DC and caster level are reduced by 2 to a minimum caster level of 1st.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting abjuration spells."
    },
    "Magic Sensitive": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a divination spell of 3rd level or higher available to cast, you can sense magical auras as if you had cast detect magic. The range of your detection is equal to 5 feet per level of the highest-level divination spell you have available to cast. Activating or concentrating on this ability requires a standard action.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting divination spells."
    },
    "Minor Shapeshift": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 4th-level spells",
      "benefit": "As long as you have a polymorph spell of 4th level or higher available to cast, you can spend a swift action to grant yourself one of the following benefits: Might (+2 bonus on melee damage rolls), Mobility (+2 competence bonus on Balance, Climb, Jump, and Swim checks), Savagery (primary claw attack dealing 1d6 points of damage), Speed (5-foot enhancement bonus to any one movement mode), or Vigor (temporary hit points equal to your HD).",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting polymorph spells. The chosen benefit lasts for a number of rounds equal to the level of the highest-level polymorph spell you have available to cast."
    },
    "Mystic Backlash": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 5th-level spells",
      "benefit": "As long as you have an abjuration spell of 5th level or higher available to cast, you can make another creature's spellcasting harmful to itself. Use of this feat requires a melee touch attack that does not provoke attacks of opportunity. As a standard action, with a successful touch you can infuse another creature with baneful magic for a number of rounds equal to the level of the highest-level abjuration spell you have available. A successful Will save reduces this duration to 1 round. For the duration of the effect, each time the target completes the casting of a spell, it takes damage equal to the level of the abjuration spell that determined the effect's duration.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting abjuration spells."
    },
    "Shadow Veil": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have a darkness spell of 2nd level or higher available to cast, you can obscure the vision of a subject within 30 feet as a standard action. If the subject fails a Will save, it treats all other creatures and objects as though they had concealment and takes a -5 penalty on Spot checks for 1 round.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting darkness spells."
    },
    "Sickening Grasp": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have a necromancy spell of 3rd level or higher available to cast, any living creature you hit with a melee touch attack becomes sickened for a number of rounds equal to the level of the highest-level necromancy spell you have available to cast. The subject can reduce this duration to 1 round with a successful Fortitude save.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting necromancy spells."
    },
    "Storm Bolt": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have an electricity spell of 3rd level or higher available to cast, you can fire a 20-foot line of electricity as a standard action. This bolt deals 1d6 points of electricity damage per level of the highest-level electricity spell you have available to cast.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting electricity spells."
    },
    "Summon Elemental": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 4th-level spells",
      "benefit": "As long as you have a summoning spell of 4th level or higher available to cast, you can summon a Small elemental (air, earth, fire, or water\u2014your choice) within a range of 30 feet. The elemental acts as if summoned by a summon monster spell. The duration of the summoning is equal to 1 round per level of the highest-level conjuration (summoning) spell you have available to cast. You can have only one summoned elemental from this feat at a time. If you have a conjuration (summoning) spell of 6th level or higher available to cast, you can summon a Medium elemental instead. If you have a conjuration (summoning) spell of 8th level or higher available to cast, you can summon a Large elemental instead.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting conjuration (summoning) spells. You must remain close to the elemental you summon\u2014if at the end of your turn you are more than 30 feet from the elemental, it disappears."
    },
    "Sunlight Eyes": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have a light spell of 2nd level or higher available to cast, you can take a swift action to grant yourself the ability to see normally in any conditions of illumination (shadowy illumination, darkness, and magical shadow or darkness). The range of this vision is 10 feet per level of the highest-level light spell you have available to cast, and the effect lasts for 1 round.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting light spells."
    },
    "Touch of Distraction": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have an enchantment spell of 3rd level or higher available to cast, you can cloud the mind of a creature within 30 feet as a standard action. The target takes a -2 penalty on its next single attack roll or Reflex saving throw. If the target makes no attacks or Reflex saves within a number of rounds equal to the level of the highest-level enchantment spell you have available to cast, the effect ends. Multiple uses of this feat don't stack.",
      "special": "This is an enchantment (compulsion, mind-affecting) effect."
    },
    "Wind-Guided Arrows": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 3rd-level spells",
      "benefit": "As long as you have an air spell of 3rd level or higher available to cast, you can spend an immediate action to alter slightly the course of an arrow, crossbow bolt, spear, or other ranged weapon already in flight. You can't change the weapon's target, but you can apply a +2 bonus or -2 penalty on its attack roll. You and the target can be no farther apart than 10 feet per level of the highest-level air spell you have available, since the guidance occurs at the end of the weapon's flight. This feat works only on thrown or projectile weapons.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting air spells."
    },
    "Winters Blast": {
      "type": "Reserve",
      "prerequisites": "Ability to cast 2nd-level spells",
      "benefit": "As long as you have a cold spell of 2nd level or higher available to cast, you can create a 15-foot cone-shaped burst of cold. This cone deals 1d4 points of cold damage per level of the highest-level cold spell you have available to cast. A successful Reflex save halves the damage.",
      "special": "As a secondary benefit, you gain a +1 competence bonus to your caster level when casting cold spells."
    }
  },
  "Tactical Feats": {
    "Battlecaster Defense": {
      "type": "Tactical",
      "prerequisites": "Combat Casting, base attack bonus +1, caster level 1st",
      "benefit": "You gain access to three tactical maneuvers while spellcasting in melee: Defensive Targeting (gain +2 bonus on touch attacks after successful defensive casting), Practiced Defense (gain +10 bonus on Concentration checks if you cast defensively in 2 consecutive rounds), and Safe Retreat (movement doesn't provoke attacks of opportunity after successful defensive casting).",
      "special": "These benefits apply equally to psionic manifestations or spell-like abilities used defensively."
    },
    "Battlecaster Offense": {
      "type": "Tactical",
      "prerequisites": "Combat Casting or warmage edge, base attack bonus +1, Spellcraft 4 ranks",
      "benefit": "You gain access to two tactical maneuvers: Spell and Sword (gain +1 bonus on first melee attack roll after dealing spell damage) and Sword and Spell (gain +1 bonus to spell save DC after making a melee attack).",
      "special": ""
    },
    "Energy Gestalt": {
      "type": "Tactical",
      "prerequisites": "Spell Focus (evocation), caster level 3rd",
      "benefit": "You gain access to three tactical maneuvers when dealing damage with pairs of energy-based spells in 2 successive rounds: Acrid Fumes (acid then fire spell nauseates creatures), Brittle Blast (cold then sonic spell deals extra damage to objects/constructs), and Improved Conduction (cold then electricity spell slows creatures).",
      "special": ""
    },
    "Metamagic Vigor": {
      "type": "Tactical",
      "prerequisites": "Two or more metamagic feats",
      "benefit": "You gain access to two tactical maneuvers when casting metamagic-enhanced spells in 2 consecutive rounds: Metamagic Intensity (gain +1 bonus to caster level with same metamagic feat) and Metamagic Versatility (gain +1 bonus to spell save DC with different metamagic feats).",
      "special": "Only actual metamagic feats allow this feat to function, not metamagic effects from magic items."
    },
    "Residual Magic": {
      "type": "Tactical",
      "prerequisites": "Spellcraft 12 ranks, any metamagic feat",
      "benefit": "You gain access to two tactical maneuvers: Enduring Potency (treat wand/scroll spell as cast from daily allotment for improved effects) and Lingering Metamagic (apply one metamagic effect from previous spell to current casting without changing spell level).",
      "special": ""
    }
  },
  "Metamagic Feats": {
    "Retributive Spell": {
      "type": "Metamagic",
      "prerequisites": "None",
      "benefit": "When you cast a spell modified by this metamagic feat, the spell has no immediate effect. Any time you are dealt damage by a melee attack during the next 24 hours, you can choose to cast the spell on that attacker as an immediate action. Once activated, a retributive spell disappears. You can have only one retributive spell cast at a time.",
      "special": "A retributive spell uses up a spell slot one level higher than the spell's actual level. This feat applies only to spells that target a creature."
    }
  }
}