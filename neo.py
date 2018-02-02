import pygame
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
		self.bg=pygame.image.load('blue.png')
		self.platform=pygame.image.load('platform_transparent.png')
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
			
	def on_loop(self):
		pass
	def on_render(self):
		self.screen.fill(white)
		self.screen.blit(self.bg,(0,0))
		self.screen.blit(self.platform, (200,600))
		self.screen.blit(self.platform, (600,500))
		self.screen.blit(self.platform, (800,250))
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