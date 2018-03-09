import pygame 
bg=pygame.image.load('blue.png')
character=pygame.image.load('kirby.png')
platform=pygame.image.load('platform_transparent.png')
scale = 4
character=pygame.transform.scale(character,(259/scale, 196/scale))