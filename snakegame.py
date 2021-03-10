from snake import Snake
import pygame

#initialize pygame module
pygame.init()
# set w and h, make window resizable
screen_width = 700
screen_height = 500
flags = pygame.RESIZABLE | pygame.SCALED
#start the actual screen
screen = pygame.display.set_mode([screen_width, screen_height], flags)


