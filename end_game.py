
def end_game_option():
	'''Gives the player the option to restart the game or quit'''
	print("\nGAME OVER\n")
	print("Would you like to play again? (Y/N)")
	player_input = input("> ")
	if player_input == "Y" and player_input == "y":
		
	elif player_input == "N" and player_input == "n":
		pass
	else:
		if player_input != "Y" and player_input != "y" and player_input != "N" and player_input != "n":
			while(player_input != "Y" and player_input != "y" and player_input != "N" and player_input != "n"):
				print("\nPlease enter 'Y' or 'N'.\n")
				print("\nGAME OVER\n")
				print("Would you like to play again? (Y/N)")
				player_input = input("> ")
