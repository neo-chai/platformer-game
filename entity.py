import globals
class entity:

	def __init__(self,image,pos):
		self.image=image
		self.pos=pos
class platform(entity):
	def __init__(self,pos):	
		self.image=globals.platform
		self.pos=pos
class player(entity):
	def __init__(self,pos):
		self.image=globals.character
		self.pos=pos
		self.speed_y=0
		self.speed_x=0