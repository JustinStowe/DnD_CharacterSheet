"""
D&D 3rd Edition Feats from Song and Silence
Feats focused on rogues and bards
"""

SONG_AND_SILENCE_FEATS = {
    'Acrobatic Strike': {
        'type': 'General',
        'prerequisites': 'Dex 15, Dodge, Mobility, Spring Attack, Jump 8 ranks, Tumble 8 ranks, base attack bonus +8',
        'benefit': 'When you use the Spring Attack feat, you deal an extra 1d6 points of damage.',
        'special': ''
    },
    'Ambidexterity': {
        'type': 'General',
        'prerequisites': 'Dex 15',
        'benefit': 'You ignore the standard -4 penalty to your off-hand when fighting with two weapons.',
        'special': 'This feat is replaced by Two-Weapon Fighting in the 3.5 revision.'
    },
    'Apprentice': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Choose a trade or craft. You gain a +2 bonus on related skill checks and can make a living through your trade.',
        'special': ''
    },
    'Artist': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on two Perform skills of your choice.',
        'special': ''
    },
    'Blooded': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Initiative checks.',
        'special': ''
    },
    'Brachiation': {
        'type': 'General',
        'prerequisites': 'Climb 4 ranks',
        'benefit': 'You can move through trees and other overhead structures at your normal speed. You can also charge and run while brachiating.',
        'special': ''
    },
    'Bullheaded': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +1 bonus on Will saves and a +2 bonus on Intimidate checks.',
        'special': ''
    },
    'Captivating Melody': {
        'type': 'General',
        'prerequisites': 'Perform 9 ranks, bardic music ability',
        'benefit': 'When you use your bardic music to fascinate creatures, you can affect an additional number of creatures equal to your Charisma modifier.',
        'special': ''
    },
    'Daring Outlaw': {
        'type': 'General',
        'prerequisites': 'Sneak attack class feature, bardic music class feature',
        'benefit': 'Your rogue and bard levels stack for determining the effects of your bardic music and sneak attack abilities.',
        'special': ''
    },
    'Dash': {
        'type': 'General',
        'prerequisites': 'Dex 13',
        'benefit': 'Your speed increases by 5 feet.',
        'special': ''
    },
    'Disguise Spell': {
        'type': 'Metamagic',
        'prerequisites': 'Bardic music ability, Perform 12 ranks',
        'benefit': 'You can disguise your spellcasting as a musical performance. Onlookers must make a Spot check (DC 25) to notice you are casting a spell. A disguised spell uses up a spell slot one level higher than the spell\'s actual level.',
        'special': ''
    },
    'Distracting Attack': {
        'type': 'General',
        'prerequisites': 'Int 13, Combat Expertise, sneak attack class feature',
        'benefit': 'When you make a successful sneak attack, you can forgo sneak attack damage to impose a -4 penalty on your opponent\'s next attack roll.',
        'special': ''
    },
    'Earthy': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Perform (comedy) checks and Perform (oratory) checks.',
        'special': ''
    },
    'Extra Music': {
        'type': 'General',
        'prerequisites': 'Bardic music ability',
        'benefit': 'You can use your bardic music four extra times per day.',
        'special': 'Also appears in other sourcebooks.'
    },
    'Fleet of Foot': {
        'type': 'General',
        'prerequisites': 'Dex 15, Run',
        'benefit': 'When running or charging, you can make a single direction change of 90 degrees or less.',
        'special': ''
    },
    'Flick of the Wrist': {
        'type': 'General',
        'prerequisites': 'Quick Draw, Sleight of Hand 5 ranks',
        'benefit': 'You can draw a light weapon as a free action and make a Sleight of Hand check to conceal the fact that you have drawn it.',
        'special': ''
    },
    'Flying Kick': {
        'type': 'General',
        'prerequisites': 'Str 13, Jump 4 ranks, Improved Unarmed Strike, Power Attack',
        'benefit': 'When you charge, you can make a Jump check to increase your damage. Add +1 to damage for every 5 feet you jump (maximum +4).',
        'special': ''
    },
    'Greased Lightning': {
        'type': 'General',
        'prerequisites': 'Dex 17, Dodge, Mobility, Spring Attack, base attack bonus +9',
        'benefit': 'When you use the Spring Attack feat, you provoke no attacks of opportunity.',
        'special': ''
    },
    'Hidden Talent': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on two skills of your choice that are not class skills.',
        'special': ''
    },
    'Improved Bardic Music': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 6 ranks',
        'benefit': 'Add +2 to the DC of all saving throws against your bardic music effects.',
        'special': ''
    },
    'Improved Fascinate': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 9 ranks',
        'benefit': 'When you use your fascinate ability, affected creatures take a -4 penalty on their saving throws against enchantment spells you cast.',
        'special': ''
    },
    'Improved Inspire Courage': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 6 ranks',
        'benefit': 'Your inspire courage ability grants a +3 morale bonus instead of +2.',
        'special': ''
    },
    'Improved Sneak Attack': {
        'type': 'General',
        'prerequisites': 'Sneak attack +2d6',
        'benefit': 'Add +1d6 to your sneak attack damage.',
        'special': 'You can gain this feat multiple times.'
    },
    'Improved Two-Weapon Fighting': {
        'type': 'Combat',
        'prerequisites': 'Dex 17, Two-Weapon Fighting, base attack bonus +6',
        'benefit': 'You get a second attack with your off-hand weapon, albeit at a -5 penalty.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Jack of All Trades': {
        'type': 'General',
        'prerequisites': 'Int 13',
        'benefit': 'You can use any skill untrained, even those that normally require training.',
        'special': ''
    },
    'Lingering Song': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 6 ranks',
        'benefit': 'Your bardic music effects last for an additional 2 rounds after you stop performing.',
        'special': ''
    },
    'Lucky': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Once per day, you can reroll one roll that you have just made. You must take the result of the reroll, even if it\'s worse.',
        'special': ''
    },
    'Magecraft': {
        'type': 'General',
        'prerequisites': 'Int 13',
        'benefit': 'You gain a +3 bonus on checks with one type of item creation feat.',
        'special': ''
    },
    'Melodic Casting': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Concentration 6 ranks',
        'benefit': 'You can maintain bardic music and cast a spell in the same round.',
        'special': ''
    },
    'Nimble Fingers': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Disable Device checks and Open Lock checks.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Opportunist': {
        'type': 'General',
        'prerequisites': 'Dex 15, Combat Reflexes',
        'benefit': 'Once per round, you can make an attack of opportunity against an opponent who has just been struck for damage in melee by another character.',
        'special': ''
    },
    'Persuasive': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You get a +2 bonus on all Bluff checks and Intimidate checks.',
        'special': 'Already in Player\'s Handbook.'
    },
    'Quick Reconnoiter': {
        'type': 'General',
        'prerequisites': 'Search 5 ranks, Spot 5 ranks',
        'benefit': 'You can make a Search check or Spot check as a move action instead of a standard action.',
        'special': ''
    },
    'Shadowdancer': {
        'type': 'General',
        'prerequisites': 'Hide 8 ranks, Move Silently 8 ranks, Perform (dance) 5 ranks',
        'benefit': 'You gain a +2 bonus on Hide and Move Silently checks when in areas of shadowy illumination.',
        'special': ''
    },
    'Sharp-Shooting': {
        'type': 'General',
        'prerequisites': 'Point Blank Shot, Precise Shot',
        'benefit': 'You can ignore up to 5 points of armor or natural armor bonus when making ranged attacks.',
        'special': ''
    },
    'Skill Mastery': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'Choose a number of skills equal to 3 + your Intelligence modifier. You can take 10 on checks with these skills even under stress.',
        'special': ''
    },
    'Slippery Mind': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'If you are affected by an enchantment and fail your save, you can attempt another save 1 round later at the same DC. You only get this one extra chance to succeed.',
        'special': ''
    },
    'Song of the Heart': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 9 ranks',
        'benefit': 'Your inspire courage and inspire greatness abilities grant a +2 bonus (instead of +1) to saves against fear and charm effects.',
        'special': ''
    },
    'Songcraft': {
        'type': 'General',
        'prerequisites': 'Bardic music ability, Perform 6 ranks',
        'benefit': 'You gain a +2 bonus on Perform checks when using bardic music.',
        'special': ''
    },
    'Spellcaster': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Concentration and Spellcraft checks.',
        'special': ''
    },
    'Streetwise': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Bluff checks and Gather Information checks.',
        'special': ''
    },
    'Sudden Strike': {
        'type': 'General',
        'prerequisites': 'Dex 13, sneak attack class feature',
        'benefit': 'Once per round, when you would normally deal sneak attack damage, you can forgo that damage to make an immediate extra attack against the same opponent.',
        'special': ''
    },
    'Tactile Trapsmith': {
        'type': 'General',
        'prerequisites': 'Disable Device 5 ranks',
        'benefit': 'You can find and disable traps by touch alone. You do not need light to use Disable Device or Search to find traps.',
        'special': ''
    },
    'Thick Skinned': {
        'type': 'General',
        'prerequisites': 'Con 13',
        'benefit': 'You gain +3 hit points.',
        'special': ''
    },
    'Trustworthy': {
        'type': 'General',
        'prerequisites': 'None',
        'benefit': 'You gain a +2 bonus on Diplomacy checks and Gather Information checks.',
        'special': ''
    },
    'Urban Tracking': {
        'type': 'General',
        'prerequisites': 'Gather Information 4 ranks',
        'benefit': 'You can track people through cities and other urban areas using Gather Information.',
        'special': ''
    }
}
