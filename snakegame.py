from ll import Node
from snake import Snake
import random
import pygame


# colors in the game
BLACK = (0, 0, 0)
GREEN = (57, 255, 20)
RED = (255, 0, 0)
BLUE = (177, 156, 217)
# initialize pygame module
pygame.init()

# in the block below, the following will happen:
# set w and h, make window resizable, set title bar elements, init the screen!
screen_width = 840  # 800 + 40 for borders
screen_height = 660  # 600 + 60 for borders
flags = pygame.RESIZABLE | pygame.SCALED
pygame.display.set_caption("Classic Snake")
logo = pygame.image.load("images/snake_logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode([screen_width, screen_height], flags)
screen.fill(BLACK)

# creating the Snake, initializing its x_y array
snake = Snake(GREEN, random.randint(1, 39) * 20, random.randint(1, 29) * 20)
x_y = [0,0]

#creating the apple, setting it's position, creating a list of positions it can't be in
apple = Node(RED, random.randint(1, 39) * 20, random.randint(1, 29) * 20)
apple_bad_pos = [snake.head.get_x(), snake.head.get_y()]
if apple.get_x() in apple_bad_pos and apple.get_y() in apple_bad_pos:
    apple.rect.x = random.randint(1, 39) * 20
    apple.rect.y = random.randint(1, 29) * 20

# adding the sprites to our sprite list
sprites_list = pygame.sprite.Group()
sprites_list.add(snake.head)
sprites_list.add(apple)

# initial state of the game
running = True

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
    
    # positions the head can't collide with
    apple_bad_pos = []

    # movement of the snake is handled in the next three lines
    if snake.head.next != None:
        snake.move(apple_bad_pos)
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
            apple.rect.x = random.randint(1, 39) * 20
            apple.rect.y = random.randint(1, 29) * 20
    
    # takes care of each frame / refresh of the screen
    screen.fill(BLACK)
    # draw some borders around the main screen
    pygame.draw.rect(screen, BLUE, [0, 0, screen_width, 20])
    pygame.draw.rect(screen, BLUE, [0, screen_height - 40, screen_width, 40])
    pygame.draw.rect(screen, BLUE, [0, 0, 20, screen_height])
    pygame.draw.rect(screen, BLUE, [screen_width - 20, 0, 20, screen_height])
    # refreshing sprites
    sprites_list.draw(screen)
    sprites_list.update()
    pygame.display.update()
    pygame.time.Clock().tick(11)
