import items
from new_player import *
from player_builder import *

# Initial player variables assigned
player_name = None
player_kingdom = None
player_father_job = None
player_education = None

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
new_player = PlayerBuilder(player_name, player_kingdom, player_father_job, player_education)
new_player.add_stats_father_job(player_father_job)
new_player.add_stats_player_education(player_education)
new_player.stats_safety_net()
new_player.intro_message()

