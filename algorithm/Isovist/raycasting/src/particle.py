import pygame
from numpy import array

class Limits:
    def __init__(self, start, end, color, width):
        self.start = start
        self.end = end
        self.color = color
        self.width = width
    
    def display(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)