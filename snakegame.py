from ll import Node, LinkedList
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
screen_width = 800  # 740 : coolmathgames grid
screen_height = 600  # 540 : coolmathgames grid
flags = pygame.RESIZABLE | pygame.SCALED
pygame.display.set_caption("Classic Snake")
logo = pygame.image.load("images/snake_logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode([screen_width, screen_height], flags)

# creating the sprites in the game
snake = Snake(GREEN, random.randint(0, 39) * 20, random.randint(0, 29) * 20)
apple = Node(RED, random.randint(0, 39) * 20, random.randint(0, 29) * 20)
while apple.rect.x == snake.head.rect.x and apple.rect.y == snake.head.rect.y:
    apple.rect.x = random.randint(0, 39) * 20
    apple.rect.y = random.randint(0, 29) * 20

# adding the sprites to our sprite list
sprites_list = pygame.sprite.Group()
sprites_list.add(snake.head)
sprites_list.add(apple)

# initial variables
running = True
x_y = [0, 0]

#main game loop
while running:
    # handle exiting of the game via the title bar and key pressing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in the case that the window is closed
            running = False
        if event.type == pygame.KEYDOWN:
            state = True
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_y[0] = -20
                x_y[1] = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_y[0] = 20
                x_y[1] = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                x_y[0] = 0
                x_y[1] = -20
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                x_y[0] = 0
                x_y[1] = 20
    
    # movement of the snake is handled in the next three lines
    if snake.head.next != None:
        snake.move()
    snake.head.move(x_y[0], x_y[1])

    # if the snake goes out of bounds, exit game
    if snake.out_of_bounds():
        running = False
        break
    
    # handle the collision of the snake and the apple
    if snake.head.rect.colliderect(apple.rect):
        snake.grow(snake.head.get_x(), snake.head.get_y())
        curr_node = snake.head
        while curr_node.next != None:
            sprites_list.add(curr_node.next)
            curr_node = curr_node.next
        while apple.rect.x == snake.head.rect.x and apple.rect.y == snake.head.rect.y:
            apple.rect.x = random.randint(0, 39) * 20
            apple.rect.y = random.randint(0, 29) * 20
    
    # takes care of each frame / refresh of the screen
    screen.fill(BLACK)
    sprites_list.draw(screen)
    sprites_list.update()
    pygame.display.update()
    pygame.time.Clock().tick(12)
