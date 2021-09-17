import pygame
from numpy import array, cos, sin, linalg, deg2rad


class Wall:
    def __init__(self, color, start, end, width):
        self.color = color
        self.start = start
        self.end = end
        self.width = width

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)


class Raycasting:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.direction = array([cos(radius), sin(radius)])

    # def display(self, screen):
    #     pygame.draw.line(screen, (255,255,255), self.position, self.position+self.direction, 1)

    def cast(self, wall):
        x1 = wall.start[0]
        y1 = wall.start[1]
        x2 = wall.end[0]
        y2 = wall.end[1]
        x3 = self.position[0]
        y3 = self.position[1]
        x4 = self.position[0] + self.direction[0]
        y4 = self.position[1] + self.direction[1]
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        numerator = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)

        if denominator == 0:
            return None  

        t = numerator / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

        if (t > 0) and (t < 1) and (u > 0):
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            coordenates = array([x,y])
            return coordenates


class Light:
    def __init__(self, conf):
        self.position = array([0, 0])
        self.color = conf['color']
        self.width = conf['width']

    def display(self, screen, walls):
        self.rays = []
        for i in range(0, 360, 5):
            raycasting = Raycasting(self.position[0], self.position[1], deg2rad(i))
            self.rays.append(raycasting)

        for ray in self.rays:
            closest = 5000
            closestpt = None

            for wall in walls:
                casted = ray.cast(wall)
                if casted is not None:
                    distance = linalg.norm(casted - self.position)
                    if distance < closest:
                        closest = distance
                        closestpt = casted

            if closestpt is not None:
                pygame.draw.line(screen, self.color, self.position, array(closestpt, int), self.width)