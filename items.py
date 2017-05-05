class Item():
	"""The base class for all items"""

	def __init__(self, name, description, value): 
		self.name = name
		self.description = description
		self.value = value
	
	def __str__(self):
		return("{}".format(self.name))


class OneHandedIronSword(Item):
	"""The first one-handed weapon in the game."""
	def __init__(self):
		self.name = "One-Handed Iron Sword"
		self.description = "Fairly inefficient iron sword. Good for beginners."
		self.attack = 2

	
one_hand_iron_sword = OneHandedIronSword()
