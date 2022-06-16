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


def draw(screen: pygame.display, snake: snakeclasses.NewSnake) -> None:
    """
    Main drawing method
    """
    screen.fill(BLACK)
    grid(screen)
    pygame.draw.rect(screen, GREEN, snake.head())


def drawtail(screen: pygame.display, coords: list) -> None:
    """
    Method for drawing the snake tail
    """
    for coordinates in coords:
        segment_x = coordinates[0]
        segment_y = coordinates[1]
        segment_rect = pygame.Rect(segment_x, segment_y, BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(screen, GREEN, segment_rect)


def main() -> None:
    """
    Main program 
    """
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # The snake class takes a pygame display as an argument
    snake = snakeclasses.NewSnake(win)

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

        draw(win, snake)
        drawtail(win, snake.tail_coords)
        pygame.display.update()
        clock.tick(12)          # It's snake, we don't need super high fps.


if __name__ == "__main__":
    main()
