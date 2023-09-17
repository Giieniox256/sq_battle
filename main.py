import pygame
import sys
from data.settings import *
from data.level import Level

# https://docs.replit.com/tutorials/python/2d-platform-game

# Pygame setup
pygame.init()
pygame.display.set_caption('SQ_Game')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(lvl_map_1, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')  # clear screen before put new frame

    level.run()  # draw level and character

    pygame.display.update()  # redraw screen to see objects
    clock.tick(120)
