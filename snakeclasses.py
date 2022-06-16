# Classes for the snake
import pygame
from collections import deque

class NewSnake:
    def __init__(self, window: pygame.display) -> None:
        """
        Initialise snake
        """
        self.win = window
        self.win_height = self.win.get_height()
        self.win_width = self.win.get_width()

        self.length = 0                     # Not counting head
        self.x, self.y = 0, 0               # Starting head coords
        self.SIZE = 20                      # Size of squares

        self.velocity = 1                   
        self.vector = (self.velocity, 0)    # Default vector, velocity to the right

        self.tail_coords = [(self.x, self.y)]      # List to store tail coords


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


    def tail(self):
        """
        Function that updates the list with the coordinates of the tail to draw
        """
        dequeue = deque(self.tail_coords)           # dequeue object
        dequeue.rotate(1)                           # shift coords to the right
        shift_list = list(dequeue)                  # convert object into list
        shift_list[0] = (self.x, self.y)            # add head coords to tail
        self.tail_coords = shift_list               # update self.tail_coords
