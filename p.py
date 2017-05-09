from random import randint
from game_mechanics.main_player import *
from game_mechanics.player_builder import *
from story.story_introduction_menu import *
# You must comment out below line when playing full game
from tests.character_builder_simulation import *
from battles.intro_battle import *
# from game_mechanics.end_game import *

def screen_holder():
	"""This function is used to help the user pace his/her reading throughout the game
	"""
	print("\nPRESS ENTER TO CONTINUE")
	input("> ")
	print("\n\n")

def intro():
	# Initial player variables assigned
	player_name = None
	player_kingdom = None
	player_father_job = None
	player_education = None

	# # Delete this line after testing
	# # Also, uncomment the input lines in this file
	# player_name = "Nick"
	# player_kingdom = "Caal"
	# player_father_job = 'farmer'
	# player_education = 'entry'

	# Name assignment
	print("\nWhat is your name?  ")
	player_name = input("> ")

	# Backstory
	print("\nFrom what kingdom do you reign?")
	player_kingdom = input("> ")

	# Lineage
	print("\nWhat was your father's profession?")
	print("Peasant   Farmer   Artisian   Merchant   Knight   Nobility\n")
	player_father_job = input("> ")
	PlayerBuilder.player_father_job_tester(MainCharacter, player_father_job)

	# Education
	print("\nWhat level of education have you received?")
	print("None   Entry   Apprentice   Expert   Mastery\n")
	player_education = input("> ")
	PlayerBuilder.player_education_tester(MainCharacter, player_education)

	# Build player
	main_player = PlayerBuilder(player_name, player_kingdom, player_father_job, player_education)
	main_player.add_stats_father_job(player_father_job)
	main_player.add_stats_player_education(player_education)
	main_player.stats_safety_net()
	main_player.initial_stats_display()

	# Story intro scene
	intro_scene_pt_1(main_player.name, main_player.kingdom)

	# Intro battle scene
	print("\n===========================BATTLE==============================\n")
	introduction_battle(main_player.strength, main_player.defense, main_player.name, main_player.hit_points, main_player.level)

	# Add post-battle experience (WIN)
	main_player.add_experience_to_player(goon.experience_earned)

	# Check to see if player can level up &
	# Increase player's stats if player levels up
	main_player.exp_checker(main_player.experience, main_player.level)

	# Intro story continuation
	intro_scene_pt_3(main_player)

	# Running open world mechanics



	# # End game option
	# end_game_option()	


if __name__ == '__main__':

	# intro()

	# Simulates working code
	p_simulation()





