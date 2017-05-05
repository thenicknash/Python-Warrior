from main_player import *

class PlayerBuilder(MainCharacter):

	def add_stats_player_education(self, player_education):
		'''Builds the stats on class call'''
		if player_education == "None" or player_education == "none":
			self.hit_points += 1
			self.strength += 2
			self.intelligence -= 3
			self.heart += 3
			self.charisma -= 2
			self.defense -= 1
		elif player_education == "Entry" or player_education == "entry":
			self.hit_points -= 3
			self.stamina += 1
			self.intelligence -= 2
			self.heart += 1
			self.luck += 2
			self.defense -= 1
		elif player_education == "Apprentice" or player_education == "apprentice":
			self.hit_points += 2
			self.strength -= 2
			self.stamina += 3
			self.heart += 1
			self.luck -= 3
			self.defense -= 1
		elif player_education == "Adept" or player_education == "adept":
			self.strength -= 3
			self.stamina += 3
			self.intelligence += 1
			self.luck -= 1
			self.charisma -= 2
			self.defense += 2
		elif player_education == "Expert" or player_education == "expert":
			self.hit_points -= 1
			self.stamina -= 3
			self.intelligence += 2
			self.heart -= 2
			self.luck += 1
			self.charisma += 3
		elif player_education == "Mastery" or player_education == "mastery":
			self.hit_points -= 1
			self.strength -= 3
			self.intelligence += 3
			self.heart -= 2
			self.luck += 2
			self.charisma += 1
		else:
			print("\nPlease enter one of the choices above!")



	def add_stats_father_job(self, father_job):
		'''Builds stats based on choice'''
		if father_job == "peasant" or father_job == "Peasant":
			self.hit_points +=1
			self.strength += 1
			self.stamina += 2
			self.intelligence -= 5
			self.heart += 5
			self.luck -= 2
			self.charisma -= 2
		elif father_job == "farmer" or father_job == "Farmer":
			self.hit_points -= 2
			self.strength += 2
			self.stamina += 5
			self.intelligence -= 2
			self.heart += 1
			self.charisma -= 5
			self.defense += 1
		elif father_job == "artisian" or father_job == "Artisian":
			self.hit_points += 5
			self.strength -= 5
			self.stamina -= 2
			self.intelligence += 1
			self.luck += 1
			self.charisma += 2
			self.defense -= 2
		elif father_job == "merchant" or father_job == "Merchant":
			self.hit_points -= 2
			self.stamina += 2
			self.intelligence += 5
			self.heart -= 2
			self.luck += 1
			self.charisma += 1
			self.defense -= 5
		elif father_job == "knight" or father_job == "Knight":
			self.hit_points += 1
			self.strength += 5
			self.stamina -= 2
			self.heart += 1
			self.luck -= 5
			self.charisma -= 2
			self.defense += 2
		elif father_job == "nobility" or father_job == "Nobility":
			self.strength -= 2
			self.stamina += 1
			self.intelligence += 1
			self.heart -= 5
			self.luck += 2
			self.charisma += 5
			self.defense -= 2
		else:
			print("\nPlease enter one of the choices above!")



	def stats_safety_net(self):
		if self.hit_points < 0:
			self.hit_points = 0
		elif self.strength < 0:
			self.strength = 0
		elif self.stamina < 0:
			self.stamina = 0
		elif self.intelligence < 0:
			self.intelligence = 0
		elif self.heart < 0:
			self.heart = 0
		elif self.luck < 0:
			self.luck = 0
		elif self.charisma < 0:
			self.charisma = 0
		elif self.defense < 0:
			self.defense = 0


	def player_education_tester(self, player_education):
		if (player_education != "none" and player_education != "None" and player_education != "entry" and player_education != "Entry" and player_education != "apprentice" and player_education != "Apprentice" and player_education != "adept" and player_education != "Adept" and player_education != "expert" and player_education != "Expert" and player_education != "mastery" and player_education != "Mastery"):
			while(player_education != "none" and player_education != "None" and player_education != "entry" and player_education != "Entry" and player_education != "apprentice" and player_education != "Apprentice" and player_education != "adept" and player_education != "Adept" and player_education != "expert" and player_education != "Expert" and player_education != "mastery" and player_education != "Mastery"):
				print("\n=============================")
				print("Please enter a valid choice!")
				print("=============================")
				print("\nWhat level of education have you received?")
				print("None   Entry   Apprentice   Expert   Mastery\n")
				player_education = input("> ")


	def player_father_job_tester(self, player_father_job):
		if (player_father_job != "peasant" and player_father_job != "Peasant" and player_father_job != "farmer" and player_father_job != "Farmer" and player_father_job != "artisian" and player_father_job != "Artisian" and player_father_job != "merchant" and player_father_job != "Merchant" and player_father_job != "knight" and player_father_job != "Knight" and player_father_job != "nobility" and player_father_job != "Nobility"):
			while(player_father_job != "peasant" and player_father_job != "Peasant" and player_father_job != "farmer" and player_father_job != "Farmer" and player_father_job != "artisian" and player_father_job != "Artisian" and player_father_job != "merchant" and player_father_job != "Merchant" and player_father_job != "knight" and player_father_job != "Knight" and player_father_job != "nobility" and player_father_job != "Nobility"):
				print("\n=============================")
				print("Please enter a valid choice!")
				print("=============================")
				print("\nWhat was your father's profession?")
				print("Peasant   Farmer   Artisian   Merchant   Knight   Nobility\n")
				player_father_job = input("> ")
