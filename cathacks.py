# cat hacks
# an audiovisual project

import pygame
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((700, 630))
pygame.display.set_caption('CAT HACKS')
icon = pygame.image.load('cat_32.png')   # import favicon
pygame.display.set_icon(icon)   # set favicon

# default surface
bg = pygame.Surface(display.get_size())
bg = bg.convert()
bg.fill((250, 250, 250))

# audio setup
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.load("lemon_demon_cat_hacks.ogg")
pygame.mixer.music.play()

# game loop
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    