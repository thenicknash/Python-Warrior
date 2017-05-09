from random import randint

class MainCharacter():
	"""Builds the main character that the user will control
	"""
	def __init__(self, name, kingdom, lineage, education):
		# Base stats
		self.level = 1
		self.experience = 0
		self.hit_points = 10
		self.strength = 5
		self.stamina = 10
		self.intelligence = 5
		self.heart = 5
		self.luck = 3
		self.charisma = 5
		self.defense = 5
		# Player name, kingdom
		self.name = name
		self.kingdom = kingdom
		# Father's profession (alters stats based upon choice)
		self.lineage = lineage
		# Player education (alters stats based upon choice)
		self.education = education


	def __str__(self):
		print("\n\n===================== YOUR JOURNEY BEGINS =====================")
		if self.lineage == "artisian" and self.lineage == "Artisian":
			return "{}, you shall make your motherland of {} proud! Along the way, your father's job being an {} may influence how others view you. Nevertheless, with your level of education ({}), you shall surely succeed in this new land named Zida.".format(self.name, self.kingdom, self.lineage, self.education)
		else:
			return "{}, you shall make your motherland of {} proud! Along the way, your father's job being a {} may influence how others view you. Nevertheless, with your level of education ({}), you shall surely succeed in this new land named Zida.".format(self.name, self.kingdom, self.lineage, self.education)


	def initial_stats_display(self):
		'''Prints intro message'''
		print(self, "\n\n")
		print("====== STATS ======")
		print("Name: {}".format(self.name))
		print("LVL: {}".format(self.level))
		print("HP: {}".format(self.hit_points))
		print("Strength: {}".format(self.strength))
		print("Stamina: {}".format(self.stamina))
		print("Intelligence: {}".format(self.intelligence))
		print("Heart: {}".format(self.heart))
		print("Luck: {}".format(self.luck))
		print("Charisma: {}".format(self.charisma))
		print("Defense: {}".format(self.defense))
		print("===================")
		print("\n")
		
	def new_stats_display(self):
		'''Displays newly obtained stats'''
		print("\n")
		print("====== STATS ======")
		print("Name: {}".format(self.name))
		print("LVL: {}".format(self.level))
		print("HP: {}".format(self.hit_points))
		print("Strength: {}".format(self.strength))
		print("Stamina: {}".format(self.stamina))
		print("Intelligence: {}".format(self.intelligence))
		print("Heart: {}".format(self.heart))
		print("Luck: {}".format(self.luck))
		print("Charisma: {}".format(self.charisma))
		print("Defense: {}".format(self.defense))
		print("===================")
		print("\n")

	def add_experience_to_player(self, experience):
		'''This function adds experience to the main player
		'''
		try:
			self.experience += experience
			print("\n{} gained {} EXP!\n".format(self.name, experience))
		except TypeError:
			print("\nNot an integer!\n")


	def exp_checker(self, exp, level):
		'''This function checks to see if the player is able to level up or not
		'''
		if exp == 10:
			self.level = 2
			self.random_stats_multiplier_on_lvl_up()
		if exp == 50:
			self.level = 3
			self.random_stats_multiplier_on_lvl_up()
		if exp == 100:
			self.level = 4
			self.random_stats_multiplier_on_lvl_up()
		if exp == 200:
			self.level = 5
			self.random_stats_multiplier_on_lvl_up()
		if exp == 400:
			self.level = 6
			self.random_stats_multiplier_on_lvl_up()
		if exp == 800:
			self.level = 7
			self.random_stats_multiplier_on_lvl_up()
		if exp == 1500:
			self.level = 8
			self.random_stats_multiplier_on_lvl_up()
		if exp == 2500:
			self.level = 9
			self.random_stats_multiplier_on_lvl_up()
		if exp == 4000:
			self.level = 10
			self.random_stats_multiplier_on_lvl_up()

		if self.level == level + 1:
			print("\nCONGRATS! {} LEVELED UP TO LEVEL {}!".format(self.name.upper(), self.level))
			self.new_stats_display()
		elif self.level == level + 2:
			print("\nWHOA! {} LEVELED UP TO LEVEL {}!".format(self.name.upper(), self.level))
			self.random_stats_multiplier_on_lvl_up()
			self.new_stats_display()
		elif self.level == level + 3:
			print("\nINCREDIBLE! {} LEVELED UP TO LEVEL {}!".format(self.name.upper(), self.level))
			self.random_stats_multiplier_on_lvl_up()
			self.random_stats_multiplier_on_lvl_up()
			self.new_stats_display()


	def random_stats_multiplier_on_lvl_up(self):
		self.hit_points += randint(1,3)
		self.strength += randint(1,3)
		self.stamina += randint(1,3)
		self.intelligence += randint(1,3)
		self.heart += randint(1,3)
		self.luck += randint(1,3)
		self.charisma += randint(1,3)
		self.defense += randint(1,3)


	def good_moral_stats_multiplier(self):
		"""Stats that are totaled when player chooses good moral option.
		"""
		self.hit_points += randint(1,3)
		self.heart += randint(1,3)


	def bad_moral_stats_multiplier(self):
		"""Stats that are totaled when player chooses bad moral option.
		"""
		self.strength += randint(1,3)
		self.defense += randint(1,3)
		self.heart -= randint(1,5)



