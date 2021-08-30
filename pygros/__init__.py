from .chart import *
import pygame


def phigame():
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption("Phigros")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        judgeline(screen, y=483)
        Keys.tap(screen, 0, 50, 0)
        pygame.display.update()
