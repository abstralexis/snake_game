# Classes for the snake
import pygame

class NewSnake:
    def __init__(self, window: pygame.display) -> None:
        """
        Initialise snake
        """
        self.win = window
        self.win_height = self.win.get_height()
        self.win_width = self.win.get_width()

        self.length = 5                     # Starting length
        self.x, self.y = 0, 0               # Starting head coords
        self.SIZE = 20                      # Size of squares

        self.velocity = 1                   
        self.vector = (self.velocity, 0)    # Default vector, velocity to the right


    def head(self) -> pygame.Rect:
        """
        Returns a pygame rect with the head of the snake
        """
        return pygame.Rect(self.x, self.y, self.SIZE, self.SIZE)


    def up(self) -> None:
        """
        Changes vector to up
        """
        self.vector = (0, -self.velocity)


    def down(self) -> None:
        """
        Changes vector to down
        """
        self.vector = (0, self.velocity)


    def left(self) -> None:
        """
        Changes vector to left
        """
        self.vector = (-self.velocity, 0)


    def right(self) -> None:
        """
        Changes vector to right
        """
        self.vector = (self.velocity, 0)


    def move(self) -> None:
        """
        Changes coordinates of the head by a vector
        """
        self.x += self.vector[0] * self.SIZE
        self.y += self.vector[1] * self.SIZE