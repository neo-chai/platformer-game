import globals
import pygame
class entity:

	def __init__(self,image,pos):
		self.image=image
		self.pos=pos
		self.speed_y=5
		self.speed_x=0
		self.rect=pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
	def should_move(self):
		return False

	def move (self, entities):
		self.pos=(self.speed_x+self.pos[0], self.speed_y+self.pos[1])		

		self.rect.top=self.pos[1]
		for entity in entities:
			if not self==entity:
				if self.rect.colliderect(entity.rect):
					if isinstance (self,cannonball) and not isinstance(entity,cannon):
						entities.remove(self)
						if isinstance(entity,player):
							entity.hp-=1
					if self.speed_y<=0:
						self.rect.top=entity.rect.top+entity.rect.height
						self.pos=(self.pos[0],self.rect.top)
						self.speed_y=0
					else:
						self.rect.top=entity.rect.top-self.rect.height
						self.pos=(self.pos[0],self.rect.top)
						self.speed_y=0
						self.remaining_jumps=2
		self.rect.left=self.pos[0]
		for entity in entities:
			if not self==entity:
				if self.rect.colliderect(entity.rect):
					if self.speed_x<=0:
						self.rect.left=entity.rect.left+entity.rect.width
						self.pos=(self.rect.left,self.pos[1])
						self.speed_x=0
					else:
						self.rect.left=entity.rect.left-self.rect.width
						self.pos=(self.rect.left,self.pos[1])
						self.speed_x=0

class platform(entity):
	def __init__(self,pos):	
		entity.__init__(self, globals.platform,pos)

class player(entity):
	def __init__(self,pos):
		entity.__init__(self, globals.character,pos)
		self.remaining_jumps=0
		self.hp=10

	def should_move(self):
		return True


class bottom(platform):
	def __init__(self,):	
		entity.__init__(self, globals.bottom,(0,800))
class cannonball(entity):
	def __init__(self,pos,speed):
		entity.__init__(self, globals.cannonball,pos)
		self.speed_x=speed [0]
		self.speed_y=speed[1]
	def should_move(self):
		return True

class cannon (entity):
	def __init__(self,pos):	
		entity.__init__(self, globals.cannon,pos)
		self.loops_shot=0