import pygame
from random import randint
import sys
import snakeclasses

# Constants
WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
# I used grey insead of white for the grid as white was too in-your-face.
GREY = (100, 100, 100)
# A more subdued green (easier on the eyes)
GREEN = (0, 100, 0)
RED = (100, 0, 0)

BLOCKSIZE = 20 #Set the size of the grid block

# Functions + Methods
def grid(window) -> None:
    """
    Draw the grid on the window

    Grid for loop, thanks to the answer in
    https://stackoverflow.com/questions/61061963/
    """
    for x in range(WIDTH // BLOCKSIZE):
        for y in range(HEIGHT // BLOCKSIZE):
            rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
                               BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(window, GREY, rect, 1)


def draw(
    screen: pygame.display, 
    snake: snakeclasses.NewSnake,
    apple: pygame.Rect
    ) -> None:
    """
    Main drawing method
    """
    screen.fill(BLACK)
    grid(screen)
    pygame.draw.rect(screen, GREEN, snake.head())
    pygame.draw.rect(screen, RED, apple)



def drawtail(screen: pygame.display, coords: list) -> None:
    """
    Method for drawing the snake tail
    """
    for coordinates in coords:
        segment_x = coordinates[0]
        segment_y = coordinates[1]
        segment_rect = pygame.Rect(segment_x, segment_y, BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(screen, GREEN, segment_rect)


def apple(screen: pygame.display, snake: snakeclasses.NewSnake) -> pygame.Rect:
    """
    Method for generating an apple 
    """
    grid_width = (WIDTH // 20) - 1
    grid_height = (HEIGHT // 20) - 1

    global apple_x
    global apple_y
    apple_x = randint(0, grid_width) * 20
    apple_y = randint(0, grid_height) * 20

    applerect = pygame.Rect(apple_x, apple_y, BLOCKSIZE, BLOCKSIZE)
    return applerect


def apple_collision(snake: snakeclasses.NewSnake) -> bool:
    """
    Returns the state of the apple. False = not collided, True = Collided.
    """
    return True if (apple_x, apple_y) == (snake.x, snake.y) else False


def out_of_bounds_check(screen: pygame.display, snake: snakeclasses.NewSnake):
    """
    Exits the game if the snake goes out of bounds
    """
    if (snake.x < 0) or (snake.x > 500) or (snake.y < 0) or (snake.y > 500):
        pygame.quit()
        sys.exit()


def main() -> None:
    """
    Main program 
    """
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # The snake class takes a pygame display as an argument
    snake = snakeclasses.NewSnake(win)
    applerect = apple(win, snake) # Generate first apple

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        snake.tail()    # Update the coordinates for the tail segments

        # Input checker
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.up()
        elif keys[pygame.K_DOWN]:
            snake.down()
        elif keys[pygame.K_LEFT]:
            snake.left()
        elif keys[pygame.K_RIGHT]:
            snake.right()

        snake.move()

        if apple_collision(snake):
            applerect = apple(win, snake) # generate new apple coords
            snake.eat()

        out_of_bounds_check(win, snake)

        draw(win, snake, applerect)
        drawtail(win, snake.tail_coords)
        pygame.display.update()
        clock.tick(12)          # It's snake, we don't need super high fps.


if __name__ == "__main__":
    main()
