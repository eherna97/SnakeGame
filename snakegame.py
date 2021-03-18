from ll import Node
from snake import Snake
import random
import pygame


# colors in the game
BLACK = (0, 0, 0)
GREEN = (57, 255, 20)
RED = (255, 0, 0)
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

#sprites in the game
head = Node(GREEN, random.randint(0, 39) * 20, random.randint(0, 29) * 20)
apple = Node(RED, random.randint(0, 39) * 20, random.randint(0, 29) * 20)
while apple.rect.x == head.rect.x and apple.rect.y == head.rect.y:
    apple.rect.x = random.randint(0, 39) * 20
    apple.rect.y = random.randint(0, 29) * 20

sprites_list = pygame.sprite.Group()
sprites_list.add(head)
sprites_list.add(apple)

# simple loop for now that opens a window
game_running = True  # simple window condition
while game_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in the case that the window is closed
            game_running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                #print("A | <-")
                head.move_left()
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                #print("D | ->")
                head.move_right()
            if event.key == pygame.K_UP or event.key == ord('w'):
                #print('W | ^')
                head.move_up()
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                #print('S | v')
                head.move_down()
    
    sprites_list.update()


    #blocks_hit = pygame.sprite.spritecollide(apple, sprites_list, False)
    #for apple in blocks_hit:
    if head.rect.colliderect(apple.rect):
        apple.rect.x = random.randint(0, 40) * 20
        apple.rect.y = random.randint(0, 30) * 20

    screen.fill(BLACK)
    sprites_list.draw(screen)
    #sprites_list.update() 
    #head = Node(screen, GREEN, head.x, head.y)
    #apple = Node(screen, RED, food.x, food.y)
    pygame.display.update()
