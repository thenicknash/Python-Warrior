import items
import new_player
from father_profession import *
from player_education import *

# Name assignment
print("\nWhat is your name?  ")
player_name = input()

# Backstory
print("\nFrom what kingdom do you reign?")
player_kingdom = input()

# Lineage
print("\nWhat was your father's profession?")
print("Peasant   Farmer   Artisian   Merchant   Knight   Nobility\n")
player_father_job = input()

# Education
print("\nWhat level of education have you received?")
print("None   Entry   Apprentice   Expert   Mastery\n")
player_education = input()

# Build player
new_player = new_player.MainCharacter(player_name, player_kingdom, player_father_job, player_education)

print()
# Prints intro message
print(new_player, "\n\n")
print("====== STATS ======")
print("Name: {}".format(new_player.name))
print("LVL: {}".format(new_player.level))
print("HP: {}".format(new_player.hit_points))
print("Strength: {}".format(new_player.strength))
print("Stamina: {}".format(new_player.stamina))
print("Intelligence: {}".format(new_player.intelligence))
print("Heart: {}".format(new_player.heart))
print("Luck: {}".format(new_player.luck))
print("Charisma: {}".format(new_player.charisma))
print("Defense: {}".format(new_player.defense))
print("===================")
print("\n")
