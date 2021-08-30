import pygame
import sys
from .globalvars import *


# holdimg = pygame.image.load("hold.png")
# dragimg = pygame.image.load("drag.png")
# flickimg = pygame.image.load("flick.png")


class Keys:
    def tap(screen, judgeLine, pos, spd):
        resfolder = sys.path[0]
        tapimg = pygame.image.load(resfolder + "/res/tap.png").convert_alpha()
        screen.blit(tapimg, (judgelines[judgeLine], pos))

