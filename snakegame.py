from ll import Node
from snake import Snake
import random
import pygame
import sys

pygame.init()  # init pygames module

# Game Defines  --------------------------------------------------------------------------

BLACK = (0, 0, 0)
GREEN = (52, 222, 0)
RED = (255, 0, 0)
BLUE = (177, 156, 217)
WHITE = (246, 246, 246)

WIDTH = 840
HEIGHT = 660

FONT = pygame.font.Font(None, 30)

START_TEXT = "Press 'SPACE' to start"
SCORE_TEXT = "Length: "
END_TEXT = "Press 'SPACE' to play again"

# Game Functions -------------------------------------------------------------------------


# function that initializes the screen of the game
#
def init_screen() -> pygame.display:
    flags = pygame.RESIZABLE | pygame.SCALED
    pygame.display.set_caption("Classic Snake")
    logo = pygame.image.load("images/snake_logo.png")
    pygame.display.set_icon(logo)

    new_screen = pygame.display.set_mode([WIDTH, HEIGHT], flags)
    new_screen.fill(BLACK)

    return new_screen


# function that loads the sprites and sprite_list of game
#
def load_sprites() -> tuple:
    snake = Snake(GREEN, random.randint(1, 39) * 20, random.randint(1, 29) * 20)
    apple = Node(RED, random.randint(1, 39) * 20, random.randint(1, 29) * 20)

    if apple.x == snake.head.x and apple.y == snake.head.y:
        apple.rect.x = random.randint(1, 39) * 20
        apple.rect.y = random.randint(1, 29) * 20

    new_sprites_list = pygame.sprite.Group()
    new_sprites_list.add(snake.head)
    new_sprites_list.add(apple)

    return snake, apple, new_sprites_list


# function that deploys the borders of the main game
#
def draw_borders(screen: pygame.display) -> None:
    pygame.draw.rect(screen, WHITE, [0, 0, WIDTH, 20])
    pygame.draw.rect(screen, WHITE, [0, HEIGHT - 40, WIDTH, 40])
    pygame.draw.rect(screen, WHITE, [0, 0, 20, HEIGHT])
    pygame.draw.rect(screen, WHITE, [WIDTH - 20, 0, 20, HEIGHT])


# function that renders text onto the game screen
#
def render_text(text: str, pos: tuple, color: tuple) -> tuple:
    surface = FONT.render(text, True, color)
    rect = surface.get_rect(center=pos)

    return surface, rect


# function that initiates the start sequence of the game screen
#
def start_screen(screen: pygame.display) -> None:
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [420 - 120, 330 - 30, 240, 60], 5)

        score_surface, score_rect = render_text(SCORE_TEXT, (760, 640), BLACK)
        start_surface, start_rect = render_text(START_TEXT, (420, 330), WHITE)

        draw_borders(screen)

        screen.blit(score_surface, score_rect)
        screen.blit(start_surface, start_rect)
        pygame.display.update()


# function that contains the main logic of the game, returns the final score
#
def run_snake_game(screen: pygame.display) -> int:
    snake, apple, sprites_list = load_sprites()
    x_y = [0, 0]  # controls the advancement in x and y direction
    direction = None  # stores current direction of the snake
    running = True  # boolean determines if the game is over or not

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    if snake.head.next is not snake.tail and direction == "RIGHT":
                        break
                    x_y = [-20, 0]
                    direction = "LEFT"

                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    if snake.head.next is not snake.tail and direction == "LEFT":
                        break
                    x_y = [20, 0]
                    direction = "RIGHT"

                if event.key == pygame.K_UP or event.key == ord("w"):
                    if snake.head.next is not snake.tail and direction == "DOWN":
                        break
                    x_y = [0, -20]
                    direction = "UP"

                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    if snake.head.next is not snake.tail and direction == "UP":
                        break
                    x_y = [0, 20]
                    direction = "DOWN"

        # movement of the snake is handled in the next three lines
        if snake.head.next is not None:
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
            snake.grow(snake.head.x, snake.head.y)
            curr_node = snake.head
            while curr_node.next != snake.tail:
                sprites_list.add(curr_node.next)
                curr_node = curr_node.next

            # get the position that an apple should not spawn in
            apple_bad_pos = [[sprite.x, sprite.y] for sprite in sprites_list]
            while [apple.x, apple.y] in apple_bad_pos:
                apple.rect.x = random.randint(1, 39) * 20
                apple.rect.y = random.randint(1, 29) * 20

        # fill the screen with black for next frame
        screen.fill(BLACK)

        score = str(snake.length)
        score_surface, score_rect = render_text(SCORE_TEXT + score, (760, 640), BLACK)

        draw_borders(screen)

        # refreshing sprites and updating the screen
        sprites_list.update()
        sprites_list.draw(screen)
        screen.blit(score_surface, score_rect)
        pygame.display.update()
        pygame.time.Clock().tick(11)

    return snake.length  # return the final score


# function that initiates the end sequence of the end screen
#
def end_screen(screen: pygame.display, score: int) -> None:
    replay = False

    while not replay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    replay = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [420 - 150, 330 - 30, 300, 60], 5)

        end_score_text = SCORE_TEXT + str(score)
        score_surface, score_rect = render_text(end_score_text, (760, 640), BLACK)
        end_surface, end_rect = render_text(END_TEXT, (420, 330), WHITE)

        draw_borders(screen)

        screen.blit(score_surface, score_rect)
        screen.blit(end_surface, end_rect)
        pygame.display.update()

# Runner ---------------------------------------------------------------------------------


def main() -> None:
    screen = init_screen()

    while True:
        start_screen(screen)
        score = run_snake_game(screen)
        end_screen(screen, score)


if __name__ == "__main__":
    main()

pygame.quit()  # un-init pygame module
