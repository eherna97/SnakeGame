from ll import Node
from snake import Snake
import pygame

BLACK = (0, 0, 0)

# initialize pygame module
pygame.init()


# in the block below, the following will happen:
# set w and h, make window resizable, set title bar elements, init the screen!
screen_width = 800# 740 : coolmathgames grid
screen_height = 600 # 540 : coolmathgames grid
flags = pygame.RESIZABLE | pygame.SCALED
pygame.display.set_caption("Classic Snake")
logo = pygame.image.load("images/snake_logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode([screen_width, screen_height], flags)

n = Node(screen, 0, 300)
# simple loop for now that opens a window
game_running = True  # simple window condition
while game_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in the case that the window is closed
            game_running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("A | <-")
                n.move_left()
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("D | ->")
                n.move_right()
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('W | ^')
                n.move_up()
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('S | v')
                n.move_down()
    
    screen.fill(BLACK)
    n = Node(screen, n.x, n.y)
    pygame.display.update()
