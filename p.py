import items
import new_player

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

# Job
print("\nWhat was your profession?")
print("Peasant   Farmer   Schoolboy   Squire   Baron-Son\n")
player_profession = input()

# Education
print("\nWhat level of education have you received?")
print("None   Entery   Apprentice   Expert   Mastery\n")
player_education = input()


# Build player
new_player = new_player.Hero(player_name, player_kingdom, player_father_job, player_education, player_profession)

print()
print(new_player, "\n")