from game_mechanics.main_player import *
from game_mechanics.player_builder import *
from battles.intro_battle import *


def screen_holder():
	print("\nPRESS ENTER TO CONTINUE")
	input("> ")
	print("\n\n")

def p_simulation():
	'''Builds a character for quicker game testing'''

	# Initial player variables assigned
	player_name = None
	player_kingdom = None
	player_father_job = None
	player_education = None

	# Name assignment
	# print("\nWhat is your name?  ")
	player_name = "Nick"

	# Backstory
	# print("\nFrom what kingdom do you reign?")
	player_kingdom = "Caal"

	# Lineage
	# print("\nWhat was your father's profession?")
	# print("Peasant   Farmer   Artisian   Merchant   Knight   Nobility\n")
	player_father_job = "Farmer"
	PlayerBuilder.player_father_job_tester(MainCharacter, player_father_job)

	# Education
	# print("\nWhat level of education have you received?")
	# print("None   Entry   Apprentice   Expert   Mastery\n")
	player_education = "Expert"
	PlayerBuilder.player_education_tester(MainCharacter, player_education)

	# Build player
	main_player = PlayerBuilder(player_name, player_kingdom, player_father_job, player_education)
	main_player.add_stats_father_job(player_father_job)
	main_player.add_stats_player_education(player_education)
	main_player.stats_safety_net()
	main_player.initial_stats_display()

	# Story intro scene
	intro_scene_pt_1(main_player.name, main_player.kingdom)
	intro_scene_pt_2()

	# Intro battle 
	print("\n===========================BATTLE==============================\n")
	introduction_battle(main_player.strength, main_player.defense, main_player.name, main_player.hit_points, main_player.level)

	# Post battle exp & lvl up
	main_player.add_experience_to_player(goon.experience_earned)
	main_player.exp_checker(main_player.experience, main_player.level)

	# Screen holder
	print("\nPRESS ENTER TO CONTINUE")
	input("> ")

	# Post battle story
	intro_scene_pt_3(main_player)


player_response = None

def intro_scene_pt_1(name, kingdom):
	"""Set-ups the first interactive scene in the story"""
	screen_holder()
	print("\n\nThe wind calmly whistles past your ear. The night is still, and you are nearing a quiet town. 'Finally', you think. 'I cannot wait to spend the night in an actual bed.'")
	print("\nYou step into town under an entrance arch. A single road runs through the middle of the small hub of buildings. Glancing about, you do not see a single soul. You decide to head towards the inn.")
	print("\nPushing the door open, you step into the local tavern. A few shady characters glare silently at you. The bartender is maticulously scrubbing the bar with a ragged cloth. You head towards him.")
	print("\nThe bartender looks up.")
	print("\n--\"Awful late for a nobody to be wonderin' round here, eh?\" the bartender chuckles.")
	# Choice set
	print("\n1. Got any available rooms?")
	print("2. What do you mean by that?")
	print("3. Awful late for a smart ass with a patchy beard.")
	print("4. Who are those guys over there?\n")

	print("Please select a response with the corresponding number:")
	player_response = "2"

	'''The first response if elif else statement in the intro scene'''
	if player_response == "1":
		print("\nThe bartender shrugs. \"Not for you, I don't.\" He proceeds to turn his back to you while now cleaning the inside of an ale mug with the same rag.\n")
	elif player_response == "2":
		print("\n--\"What do you think I mean? Clearly, you aren't from here. Who the hell are ya?\" the bartender queries.")
		print("\n--\"My name is {}. I'm from the {} region,\" you firmly answer.".format(name, kingdom))
		print("\n--\"Well,\" the worker started, \"if you're looking for a room, we don't have any here.\"")
	elif player_response == "3":
		print("\nThe bartender stops scrubbing. \"You have a lot of nerve. Walking into a tavern where nobody here is kin to you.\"")
		print("\n--\"How would you know that?\" you curiously asked.")
		print("\n--\"I know everyone in this town. I don't know you. You best be on your way, pissant.\" The bartender scoffs as you turn to head back out of the innhouse.\n")
	elif player_response == "4":
		print("\n--\"Them? Hah, why don't you find out for yourself?\" the bartender chuckled once more.\n")
	else:
		if player_response != "1" and player_response != "2" and player_response != "3"  and player_response != "4":
			while(player_response != "1" and player_response != "2" and player_response != "3"  and player_response != "4"):
				# print("\n\"Awful late for a nobody to be wonderin' round here, eh?\" the bartender chuckles.")
				print("\n-----------Please enter a valid response!-----------")
				print("\n1. Got any available rooms?")
				print("2. What do you mean by that?")
				print("3. Awful late for a smart ass with a patchy beard.")
				print("4. Who are those guys over there?\n")
				print("\nPlease select a response with the corresponding number:")
				player_response = input("> ")
				if player_response == "1":
					print("\nThe bartender shrugs. \"Not for you, I don't.\" He proceeds to turn his back to you while now cleaning the inside of an ale mug with the same rag.")
					print("\n\'Rude\' you think to yourself. You wait a moment to see if the bartender will turn back towards you.")
					print("\nIt appears not.")
				elif player_response == "2":
					print("\n--\"What do you think I mean? Clearly, you aren't from here. Who the hell are ya?\" the bartender queries.")
					print("\n--\"My name is {}. I'm from the {} region,\" you firmly answer.".format(name, kingdom))
					print("\n--\"Well,\" the worker started, \"if you're looking for a room, we don't have any here.\"")
					print("\n--\"But the sign out front-\"")
					print("\n--\"None for you. Get out!\"")
					print("\n--\"Eh, screw this place anyways,\" you mutter to yourself.")
				elif player_response == "3":
					print("\nThe bartender stops scrubbing. \"You have a lot of nerve. Walking into a tavern where nobody here is kin to you.\"")
					print("\n--\"How would you know that?\" you curiously asked.")
					print("\n--\"I know everyone in this town. I don't know you. You best be on your way, pissant.\" The bartender scoffs as you turn to head back out of the innhouse.\n")
				elif player_response == "4":
					print("\n--\"Them? Hah, why don't you find out for yourself?\" the bartender chuckled once more.\n")



def intro_scene_pt_2():
	# Contact with the shady characters
	print("\nYou are about to exit the inn when a voice shouts at you.\n")
	print("--\"Where do you think you're going, bub?\" the growly voice questions.\n")
	print("Before you can fully turn around, two hands grab your oversize shirt and proceed to thrust you against the wall.\n")
	print("Quickly, you shove the medium-sized man off of you. Four now surround and corner you. The one farthest right stands between you and the door.\n")
	screen_holder()
	print("--\"What the hell is your problem?\" you yell. At this point, the few patrons left are all gawking.\n")
	print("The four laugh and mock your apparent frazzled look. Who would not be flustered though? The man who shoved you against the wall speaks up.\n")
	print("--\"See, we don't like you's around here. We know your kind. You're a scout for Ezera!\"\n")
	print("--\"Ezera? I don't even know what that is!\"\n")
	print("--\"We'll see what you say after this!\"\n")


def intro_scene_pt_3(main_player):
	"""Post-battle narrative. Leads into open world game mechanics.
	"""

	# Conversation with shady individuals
	print("After pummeling your attacker, you toss him into the far left goon. As they tumble to the ground, you turn your attention to the two blocking you from the door.\n")
	print("--\"Who's next?\" you ask. You eagerly hope the two thugs sense your newly forced confidence.\n")
	print("--\"Let's get out of here,\" the smaller of the two says. \"We'll be back for you, spy!\"\n")
	print("The three conscious goons quickly file out of the pub. Your bloodied attacker lies knocked out cold on the bar floor.\n")
	print("\'Spy? Maybe they weren't lying\' you think to yourself as you walk towards the prostrated goon. You glare down over him.\n")
	moral_choice_1 = moral_choice_with_goon()
	if moral_choice_1 == '1':
		main_player.good_moral_stats_multiplier()
		print("\nYou sigh as you walk back towards the bar. You motion the wide-eyed bartend towards you.\n")
		print("--\"Give me a glass full of water, please.\" you calmly order. The man reaches under the counter and retrieves a clean glass. He then promptly fills it.\n")
		print("--\"You're a better man than me,\" he admits as he hands you the glass. \"Guess those boys had you wrong.\"\n")
		print("--\"Guess so,\" you mumble. Now, standing over the sleeping man, you pour the water onto his face.\n")
		screen_holder()
		print("--\"AGGGHHH!\" the goon belts. He snaps into a seated position. Panting heavily, he looks up at you. He rises to his feet though he is a little wobbly.\n")
		print("--\"What? Are you going to gloat over your victory?\" he mocks. The goon clenches his left side. You gave him quite the beating to his torso.\n")
		screen_holder()
		print("--\"You attacked me! You're lucky that I didn't leave you here like your friends. Now, tell me, who are you?\"\n")
		screen_holder()
		print("--\"Oh, be off with it. My name is Reginald. I am a member of the Pyres. That's all I'll tell you.\"\n")
		print("--\"You genuinely thought I was a spy?\" you ask.\n")
		screen_holder()
		print("--\"You think me a liar? Nonsense. I might be a part of Zida's rough patriot army, but I'm still a patriot. There's been no peace since the war started with Ezera, land of the eezites.\"\n")
		print("--\"Well, I am no spy. I come from {}. I've never even heard of Ezera.\"\n".format(main_player.kingdom))
		print("--\"Lucky you,\" Reginald chuckled. He steps towards you and stretches out his hand. \"Maybe we started off on the wrong foot. Welcome to Zida.\"\n")
		print("You can tell that he believes you now. You shake his hand.\n")
		screen_holder()
		print("--\"By the way,\" Reginald started, \"who are you?\"\n")
		print("--\"{}.\"\n".format(main_player.name))
		print("--\"Well, if I were you, I'd leave this place. It's not for someone foreign.\"\n")
		print("--\"I was beginning to feel the same. Thanks.\"\n")
		screen_holder()
		print("You proceed to gather your belongings and exit the tavern.\n")

	elif moral_choice_1 == '2':
		main_player.bad_moral_stats_multiplier()
		print("\nYou snarl at the downed man.\n")
		print("--\"Ptt!\"\n")
		print("You spit on the man. Looking up, the bar is silent. You scan the entire room. All eyes scowl at you.")
		screen_holder()
		print("--\"Have a nice night.\" you sarcastically remark.\n")
		print("You exit the tavern.\n")
	else:
		print("\n--------------------------------------")
		print('Please choose a valid option!')
		print("--------------------------------------")
		intro_scene_pt_3()


def moral_choice_with_goon():
	"""Moral choice that will influence character.
	"""
	print("===============")
	print("WHAT DO YOU DO?")
	print("===============")
	print("\n1. Help the goon")
	print("2. Leave the goon\n")
	moral_choice = input("> ")
	return moral_choice
	return moral_choice

