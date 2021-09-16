import numpy as np
import json
import pygame
from src.ray import Limits

class Application:
    
    def load_json(self, file_path):
        with open(file_path, 'r') as c:
            return json.load(c)


    def __init__(self):
        pygame.init()

        # app configuration
        self.running = True
        self.conf = self.load_json('conf.json')
        self.width = self.conf['general']['width']
        self.height = self.conf['general']['height']
        self.title = self.conf['general']['title']
        self.screen_color = self.conf['general']['color']
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        # obstacles configuration
        self.wall_color = self.conf['walls']['color']
        self.wall_width = self.conf['walls']['width']
        self.wall_coord = self.conf['walls']['walls']


        
    def draw_wall(self):
        walls = []
        for i in range(len(self.wall_coord)):
            walls.extend([self.wall_coord[i][0], self.wall_coord[i][1]])

        for i in range(1, len(walls), 2):
            wall = Limits(self.wall_color, walls[i-1], walls[i], self.wall_width)
            wall.display(self.screen)


    def run(self):
        while self.running:
            self.screen.fill(self.screen_color)
            self.draw_wall()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


    



if __name__ == "__main__":
    application = Application()
    application.run()
