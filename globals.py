import pygame 
bg=pygame.image.load('blue.png')
character=pygame.image.load('kirby.png')
platform=pygame.image.load('platform_transparent.png')
scale = 4
character=pygame.transform.scale(character,(int(259/scale), int(196/scale)))
cannon=pygame.image.load('cannon.png')
cannonscale = 10
cannon=pygame.transform.scale(cannon,(int(1024/cannonscale), int(829/cannonscale)))
bottom=pygame.transform.scale(platform,(1400,1))
cannonball=pygame.image.load('cannonball.png')