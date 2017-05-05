from random import randint
from characters import *
from character_builder_simulation import *
from items import *

# Battle begins
def introduction_battle(strength, defense, name, hp, level):
	battle_hud(strength, defense, name, hp, level)
	battle_choice = input("> ")
	if battle_choice == '1':
		# Needed to put this code in the if statement as opposed to separating into another function
		# due to the HP stats for the main player not being communicated between functions
		# Player attack
		player_att_dmg = int(0.1 * (strength * randint(1, 5)))
		player_def_buffer = int(0.04 * (2 * randint(1,5)))
		player_total_dmg = player_att_dmg - player_def_buffer
		if player_total_dmg < 0:
			player_total_dmg = 0
		goon.hit_points -= player_total_dmg
		# Enemy Attack
		enemy_att_dmg = int(0.1 * (goon.strength * randint(1, 5)))
		enemy_def_buffer = int(0.04 * (defense * randint(1,5)))
		enemy_total_dmg = enemy_att_dmg - enemy_def_buffer
		if enemy_total_dmg < 0:
			enemy_total_dmg = 0
		hp -= enemy_total_dmg

		print("\n-------------------------------------------------------------------------------")
		print("\n{} attacked GOON and delivered {} damage!\n".format(name.upper(), player_total_dmg))
		print("\nGOON attacked {} and delivered {} damage!\n".format(name.upper(), enemy_total_dmg))
		print("-------------------------------------------------------------------------------")

	elif battle_choice == '2':
		special_attack_button_pressed(strength, defense, name, hp, level)
	elif battle_choice == '3':
		items_button_pressed(strength, defense, name, hp, level)
		pass
	elif battle_choice == '4':
		run_button_pressed(strength, defense, name, hp, level)
	else: 
		print("\n\nPlease choose a valid option!\n")

	# End of Battle!
	if hp <= 0:
		print("\n==============Oh no! {} was slain by {}!================\n".format(name.upper(), goon.name.upper()))
		return 
	elif goon.hit_points <= 0:
		print("\n==============Victory! {} slayed the {}!================\n".format(name.upper(), goon.name.upper()))
		return

	introduction_battle(strength, defense, name, hp, level)

# The battle HUD during the player's battle
def battle_hud(strength, defense, name, hp, level):
	"""The battle display that appears every time. """
	# Battle HUD
	print("\n-------------------------------")
	# Main player
	print("{}".format(name.upper(), level))
	print("LVL: {}".format(level))
	print("HP: {}".format(hp))
	print("STR: {}".format(strength))
	print("DEF: {}".format(defense))
	print("\n")
	# Enemy player
	print("{}".format(goon.name))
	print("LVL: {}".format(goon.level))
	print("HP: {}".format(goon.hit_points))
	print("STR: {}".format(goon.strength))
	print("DEF: {}".format(goon.defense))
	print("-------------------------------\n")
	# Battle options
	print("1. Attack     3. Item")
	print("2. Special    4. Run\n")

# Below are the methods that are being called based on the player's input

# Option 2 (Special)
def special_attack_button_pressed(strength, defense, name, hp, level):
	"""This function accesses the player's special attacks
	"""
	print("\nYou do not have any special attacks!")


# Option 3 (Bag)
def items_button_pressed(strength, defense, name, hp, level):
	"""This function accesses the player's item bag
	"""
	print("\n----------------------------------------")
	print("What item would you like to use?:")
	# Items will be placed here
	print("\n")
	print("Enter \'back\' to return to battle.")
	print("----------------------------------------\n")
	bag_choice = input("> ")
	if bag_choice == "back" or bag_choice == "Back":
		pass
	else:
		print("\n\nPlease choose a valid option!\n")
		items_button_pressed(strength, defense, name, hp, level)


# Option 4 (Run)
def run_button_pressed(strength, defense, name, hp, level):
	"""This function allows player to run from the battle
	"""
	print("\nYou cannot flee from this battle!")





