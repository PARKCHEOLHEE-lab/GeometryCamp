from typing import List, Tuple
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from window import SCREEN_W, SCREEN_H, WHITE, BLACK, DARK, RED, TITLE


draw = pygame.draw


class Application:

    def __init__(self):
        pygame.init()
        self.obstacles_size = 100
        self.obstacles_interval = [200, 800, 1400]


    def main_loop(self):
        while True:
            self.draw_cursor()
            self.draw_obstacles(self.obstacles_interval)
            self.draw_screen(DARK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            


    def new_obstacles(self, origin: List, size: int) -> List:
        pos_1 = [origin[0]/2, origin[1]/2]
        pos_2 = [origin[0]/2+size, origin[1]/2]
        pos_3 = [origin[0]/2+size, origin[1]/2+size]
        pos_4 = [origin[0]/2, origin[1]/2+size]
        return [pos_1, pos_2, pos_3, pos_4]


    def draw_obstacles(self, iterval: List):
        for x in iterval:
            for y in iterval:
                obstacle = self.new_obstacles([x,y], self.obstacles_size)
                draw.polygon(window, WHITE, obstacle)
        pygame.display.update()

    def draw_cursor(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw.circle(window, RED, [mouse_x,mouse_y], 5)

    def draw_screen(self, color: Tuple):
        window.fill(color)


if __name__ == "__main__":
    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(TITLE)

    application = Application()
    application.main_loop()