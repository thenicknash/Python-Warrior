from new_player import *

class FatherProfession(MainCharacter):
	"""Assigns the player's past and alter's base stats"""

	def add_stats(self, father_job):
		"""Adjust stats based on the selection"""
		if father_job == "peasant" or father_job == "Peasant":
			self.hit_points +1
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


camel = FatherProfession("Nick", "Caal", "Farmer", "Entry")
camel.add_stats("hi")

print("\n\n====== STATS ======")
print("Name: {}".format(camel.name))
print("LVL: {}".format(camel.level))
print("HP: {}".format(camel.hit_points))
print("Strength: {}".format(camel.strength))
print("Stamina: {}".format(camel.stamina))
print("Intelligence: {}".format(camel.intelligence))
print("Heart: {}".format(camel.heart))
print("Luck: {}".format(camel.luck))
print("Charisma: {}".format(camel.charisma))
print("Defense: {}".format(camel.defense))
print("===================")
print("\n")
