from random import randint
from characters import *
from character_builder_simulation import *

# Battle begins
def introduction_battle(strength, defense, name, hp, level):
	print("\n===========================BATTLE==============================\n")
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
	battle_choice = input("> ")
	if battle_choice == '1':
		# Player attack mechanics
		player_att_dmg = int(0.1 * (strength * randint(1, 5)))
		player_def_buffer = int(0.04 * (2 * randint(1,5)))
		player_total_dmg = player_att_dmg - player_def_buffer
		goon.hit_points -= player_total_dmg
		print("\n=============================================")
		print("\n{} attacked GOON and delivered {} damage!\n".format(name.upper(), player_total_dmg))
		# Enemy Attack mechanics
		enemy_att_dmg = int(0.1 * (3 * randint(1, 5)))
		enemy_def_buffer = int(0.04 * (defense * randint(1,5)))
		enemy_total_dmg = enemy_att_dmg - enemy_def_buffer
		print("\nGOON attacked {} and delivered {} damage!\n".format(name.upper(), enemy_total_dmg))
		hp -= enemy_total_dmg
		print("=============================================")
		# If statement that keeps the battle going until someone dies/faints
		if goon.hit_points > 0 and hp > 0:
			while(goon.hit_points > 0 and hp > 0):
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
				battle_choice = input("> ")
				if battle_choice == '1':
					# Player attack
					player_att_dmg = int(0.1 * (strength * randint(1, 5)))
					player_def_buffer = int(0.04 * (2 * randint(1,5)))
					player_total_dmg = player_att_dmg - player_def_buffer
					goon.hit_points -= player_total_dmg
					print("\n=============================================")
					print("\n{} attacked GOON and delivered {} damage!\n".format(name.upper(), player_total_dmg))
					# Enemy Attack
					enemy_att_dmg = int(0.1 * (3 * randint(1, 5)))
					enemy_def_buffer = int(0.04 * (defense * randint(1,5)))
					enemy_total_dmg = enemy_att_dmg - enemy_def_buffer
					if enemy_total_dmg < 0:
						enemy_total_dmg = 0
					print("\nGOON attacked {} and delivered {} damage!\n".format(name.upper(), enemy_total_dmg))
					hp -= enemy_total_dmg
					print("=============================================")
		# End of Battle!
		if hp <= 0:
			print("\n==============Oh no! {} was slain by {}!================\n".format(name, goon.name))
		elif goon.hit_points <= 0:
			print("\n==============Victory! {} slayed the {}!================\n".format(name, goon.name))
	elif battle_choice == '2':
		pass
	elif battle_choice == '3':
		pass
	elif battle_choice == '4':
		pass
	else: 
		if battle_choice != '1' and battle_choice != '2' and battle_choice != '3' and battle_choice != '4':
			while(battle_choice != '1' and battle_choice != '2' and battle_choice != '3' and battle_choice != '4'):
				if battle_choice == '1':
					pass
				elif battle_choice == '2':
					pass
				elif battle_choice == '3':
					pass
				elif battle_choice == '4':
					pass

