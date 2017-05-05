# Enemy classes
class Goon():
	"""This is the basic enemy class that the player encounters.
	"""
	def __init__(self):
		self.name = "Goon"
		self.level = 1
		self.hit_points = 10
		self.strength = 2
		self.stamina = 3
		self.intelligence = 1
		self.heart = 0
		self.luck = 0
		self.charisma = 0
		self.defense = 2
		self.experience_earned = 10

goon = Goon()
