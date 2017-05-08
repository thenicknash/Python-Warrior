player_response = None

def intro_scene_pt_1(name, kingdom):
	player_response = None
	"""Set-ups the first interactive scene in the story"""
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
	player_response = input("> ")

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

	intro_scene_pt_2()

def intro_scene_pt_2():
	'''This progresses story'''
	# Contact with the shady characters
	print("\nYou are about to exit the inn when a voice shouts at you.\n")
	print("--\"Where do you think you're going, bub?\" the growly voice questions.\n")
	print("Before you can fully turn around, two hands grab your oversize shirt and proceed to thrust you against the wall.\n")
	print("Quickly, you shove the medium-sized man off of you. Four now surround and corner you. The one farthest right stands between you and the door.\n")
	print("--\"What the hell is your problem?\" you yell. At this point, the few patrons left are all gawking.\n")
	print("The four laugh and mock your apparent frazzled look. Who would not be flustered though? The man who shoved you against the wall speaks up.\n")
	print("--\"See, we don't like you's around here. We know your kind. You're a scout for Ezera!\"\n")
	print("--\"Ezera? I don't even know what that is!\"\n")
	print("--\"We'll see what you say after this!\"\n")
	
	begin_intro_battle()

def begin_intro_battle():
	'''This initiates the battle'''
	print("\n\nENTER Y TO BEGIN BATTLE!")
	answer = input("> ")
	if answer == "Y" or answer == "y":
		pass
	else:
		print('\nPlease enter the correct value (Y)\n')
		begin_intro_battle()
