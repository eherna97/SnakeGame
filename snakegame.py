from snake import Snake
import pygame

# initialize pygame module
pygame.init()
# in the block below, the following will happen:
# set w and h, make window resizable, set title of screen, init the screen!
screen_width = 700
screen_height = 500
flags = pygame.RESIZABLE | pygame.SCALED
pygame.display.set_caption("Classic Snake")
screen = pygame.display.set_mode([screen_width, screen_height], flags)
# simple loop for now that opens a window
game_running = True  # simple window condition
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in the case that the window is closed
            game_running = False 
