import pygame
from entity import *
import globals 
from pygame.locals import *
white=[255,255,255]
class app ():
	def __init__(self):
		self._running=True
		self.screen=None
		self.size=self.weight,self.height=1400,800
	def on_init(self):
		pygame.init()
		self.screen=pygame.display.set_mode(self.size,pygame.HWSURFACE|pygame.DOUBLEBUF)
		self._running=True
		self.character = player((0,0))
		self.cannon=cannon((400,0))
		self.entities=[platform((150,600)),platform((600,500)),platform((800,250)),self.character,bottom(),self.cannon]
		# (self.platform,(150,600)),(self.platform,(600,500)),(self.platform, (800,250)), (self.bg,(0,0))
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type==pygame.KEYDOWN:
			if event.key==K_SPACE:
				if self.character.remaining_jumps>0:
					self.character.speed_y -= 20
					self.character.remaining_jumps-=1
			if event.key==K_d:
				self.character.speed_x=5
			if event.key==K_a:
				self.character.speed_x=-5
		if event.type==pygame.KEYUP:
			if event.key==K_d:
				self.character.speed_x=0
			if event.key==K_a:
				self.character.speed_x=0
	def on_loop(self):
		for entity in self.entities:
			if entity.should_move():
				entity.move(self.entities)
				entity.speed_y+=1 
		self.cannon.loops_shot+=1
		if self.cannon.loops_shot > 100:
			self.cannon.loops_shot=0
			cannonpos=(self.cannon.pos[0]-100,self.cannon.pos[1])
			self.entities.append(cannonball(cannonpos,(0,5)))
	def on_render(self):
		self.screen.fill(white)
		self.screen.blit(globals.bg, (0,0))
		for entity in self.entities:
			self.screen.blit(entity.image,entity.pos)
		pygame.display.update()
	def on_cleanup(self):
		pygame.quit()
	def on_execute(self):
		if self.on_init()==False:
			self._running=False
		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()
clock = pygame.time.Clock()
clock.tick(60)
theApp= app()
theApp.on_execute()