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

# Functions + Methods
def grid(window) -> None:
    """
    Draw the grid on the window
    """
    BLOCKSIZE = 20 #Set the size of the grid block

    """
    Grid for loop, thanks to the answer in
    https://stackoverflow.com/questions/61061963/
    """
    for x in range(WIDTH // BLOCKSIZE):
        for y in range(HEIGHT // BLOCKSIZE):
            rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
                               BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(window, GREY, rect, 1)


def draw(screen, snake) -> None:
    """
    Main drawing method
    """
    screen.fill(BLACK)
    grid(screen)
    pygame.draw.rect(screen, GREEN, snake.head())


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

            # Input checker
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        snake.up()
                    case pygame.K_DOWN:
                        snake.down()
                    case pygame.K_LEFT:
                        snake.left()
                    case pygame.K_RIGHT:
                        snake.right()

        snake.move()

        draw(win, snake)
        pygame.display.update()
        clock.tick(12)          # It's snake, we don't need super high fps.


if __name__ == "__main__":
    main()
    