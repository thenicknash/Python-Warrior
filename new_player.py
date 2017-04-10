class Hero():
	'''Establishes the player of the game
		
		methods:
		__init__
		__str__
	'''

	def __init__(self, name, kingdom, lineage, education, profession):
		self.name = name
		self.kingdom = kingdom
		self.lineage = lineage
		self.education = education
		self.profession = profession

	def __str__(self):
		print("===================== YOUR JOURNEY BEGINS =====================")
		return "{}, you shall make your motherland of {} proud! Along the way, your father's job being a {} may influence how others view you. Neverthless, with your level of education ({}), and your experience with the past profession of {}, you shall persist.".format(self.name, self.kingdom, self.lineage, self.education, self.profession)
