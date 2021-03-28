from ll import Node
from snake import Snake
import random
import pygame


# colors in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (57, 255, 20)
RED = (255, 0, 0)
BLUE = (177, 156, 217)
WINDOW_WHITE = (246, 246, 246)

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

# creating the game font, default
game_font = pygame.font.Font(None, 30)

# creating the Snake, initializing its x_y change array
snake = Snake(GREEN, random.randint(1, 39) * 20, random.randint(1, 29) * 20)
x_y = [0,0]

#creating the apple, setting it's position, creating a list of positions it can't be in
apple = Node(RED, random.randint(1, 39) * 20, random.randint(1, 29) * 20)
if apple.get_x() == snake.head.get_x() and apple.get_y() == snake.head.get_y():
    apple.rect.x = random.randint(1, 39) * 20
    apple.rect.y = random.randint(1, 29) * 20

# adding the sprites to our sprite list
sprites_list = pygame.sprite.Group()
sprites_list.add(snake.head)
sprites_list.add(apple)

# initial state of the game
running = True
direction = None

#main game loop
while running:
    last_change = [snake.head.get_x(), snake.head.get_y()]
    # handle exiting of the game via the title bar and key pressing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in the case that the window is closed
            running = False
        if event.type == pygame.KEYDOWN:
            state = True
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if snake.head.next != None and direction == "RIGHT":
                    break
                x_y[0] = -20
                x_y[1] = 0
                direction = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if snake.head.next != None and direction == "LEFT":
                    break
                x_y[0] = 20
                x_y[1] = 0
                direction = "RIGHT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                if snake.head.next != None and direction == "DOWN":
                    break
                x_y[0] = 0
                x_y[1] = -20
                direction = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if snake.head.next != None and direction == "UP":
                    break
                x_y[0] = 0
                x_y[1] = 20
                direction = "DOWN"

    # movement of the snake is handled in the next three lines
    if snake.head.next != None:
        snake.move()
    snake.head.move(x_y[0], x_y[1])

    # handle the snake going out of bounds
    if snake.out_of_bounds():
        running = False
    
    # handle the collision of the snake head and snake body
    for sprite in sprites_list:
        if sprite == snake.head or sprite == apple:
            continue
        if snake.head.rect.colliderect(sprite.rect):
            running = False


    # handle the collision of the snake and the apple
    if snake.head.rect.colliderect(apple.rect):
        snake.grow(snake.head.get_x(), snake.head.get_y())
        curr_node = snake.head
        while curr_node.next != snake.tail:
            sprites_list.add(curr_node.next)
            curr_node = curr_node.next
        
        # get the position that an apple should not spawn in
        apple_bad_pos = [[sprite.get_x(),sprite.get_y()] for sprite in sprites_list]
        # respawns the apple in a good position
        while [apple.get_x(), apple.get_y()] in apple_bad_pos:
            apple.rect.x = random.randint(1, 39) * 20
            apple.rect.y = random.randint(1, 29) * 20
    
    # fill the screen with black for next frame
    screen.fill(BLACK)

    # taking care of creating a surface for the score each frame
    score_text = "Length: " + str(snake.length)
    score_surface = game_font.render(score_text, True, BLACK)
    score_rect = score_surface.get_rect(center = (760, 640))

    # draw some borders around the main screen
    pygame.draw.rect(screen, WINDOW_WHITE, [0, 0, screen_width, 20])
    pygame.draw.rect(screen, WINDOW_WHITE, [0, screen_height - 40, screen_width, 40])
    pygame.draw.rect(screen, WINDOW_WHITE, [0, 0, 20, screen_height])
    pygame.draw.rect(screen, WINDOW_WHITE, [screen_width - 20, 0, 20, screen_height])

    # refreshing sprites and updating the screen
    sprites_list.update()
    sprites_list.draw(screen)
    screen.blit(score_surface, score_rect)
    pygame.display.update()
    pygame.time.Clock().tick(11)

# un-init the pygame modules that were init
pygame.quit()

