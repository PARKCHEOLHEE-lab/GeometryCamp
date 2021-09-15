import pygame
from numpy import array

class Limits:
    def __init__(self, color, start, end, width):
        self.color = color
        self.start = start
        self.end = end
        self.width = width

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)