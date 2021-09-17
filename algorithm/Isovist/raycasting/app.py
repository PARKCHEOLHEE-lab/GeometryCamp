import numpy as np
import json
import pygame
import numpy as np
from src.ray import Light, Raycasting, Wall


class Application:
    def load_json(self, file_path):
        with open(file_path, 'r') as c:
            return json.load(c)

    def __init__(self):
        pygame.init()
        self.fps = 60
        self.running = True
        self.conf = self.load_json('conf.json')
        self.width = self.conf['general']['width']
        self.height = self.conf['general']['height']
        self.title = self.conf['general']['title']
        self.screen_color = self.conf['general']['color']
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

        self.walls = []
        self.wall_color = self.conf['walls']['color']
        self.wall_width = self.conf['walls']['width']
        self.wall_coord = self.conf['walls']['walls']

        self.light = Light(self.conf['ray'])

    def draw_wall(self):
        walls = []
        for i in range(len(self.wall_coord)):
            walls.extend([self.wall_coord[i][0], self.wall_coord[i][1]])

        for i in range(1, len(walls), 2):
            wall = Wall(self.wall_color, walls[i-1], walls[i], self.wall_width)
            self.walls.append(wall)
            wall.display(self.screen)


    def draw_light(self):
        cursor_position = pygame.mouse.get_pos()
        cursor_x, cursor_y = cursor_position
        cursor_rad = 3
        self.light.position[0] = cursor_x
        self.light.position[1] = cursor_y
        pygame.draw.circle(self.screen, self.light.color, cursor_position, cursor_rad)


    def run(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.screen_color)
            self.draw_wall()
            self.draw_light()
            self.light.display(self.screen, self.walls)
            self.clock.tick(self.fps)
            pygame.display.update()


if __name__ == "__main__":
    app = Application()
    app.run()
