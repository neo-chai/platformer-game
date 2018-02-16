import pygame
from entity import *
import events
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

		self.entities=[platform((150,600)),platform((600,500)),platform((800,250)),player((0,0))]
		# (self.platform,(150,600)),(self.platform,(600,500)),(self.platform, (800,250)), (self.bg,(0,0))
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type==pygame.KEYDOWN:
			if event.key==K_SPACE:
				return	
	def on_loop(self):
		pass
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
theApp= app()
theApp.on_execute()