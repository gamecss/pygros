import pygame
from .globalvars import *


def judgeline(screen, x=None, y=None):
    if not x and not y:
        raise ValueError("No x or y set or =0")
    if x and y:
        raise ValueError("only can set x or y")
    judgeline_i = 0
    scrinfo = pygame.display.Info()
    if x:
        pygame.draw.line(screen, (254, 255, 169), (x - 3, 0), (x - 3, scrinfo.current_h), 3)
        judgelines[judgeline_i] = x
    elif y:
        pygame.draw.line(screen, (254, 255, 169), (0, scrinfo.current_h - y),
                         (scrinfo.current_w, scrinfo.current_h - y), 3)
        judgelines[judgeline_i] = y
    judgeline_i += 1


class Key:
    def tap(judgeLine, dirc, pos, spd):
        pass
