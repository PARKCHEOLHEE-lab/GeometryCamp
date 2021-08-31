import sys
import pygame
import random

pygame.init()


# object
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK_SIZE = 20
MOVE_SPEED = 1
STARTING_POINT = [(20,15), (19,15), (18,15)]


# screen
FPS = 20
SCREEN_COLOR = (0, 0, 0)
SCREEN_SIZE = (800, 600)
GRID_COLOR = (1, 1, 1)
X_LIMIT_MAX = SCREEN_SIZE[0] / BLOCK_SIZE
X_LIMIT_MIN = SCREEN_SIZE[0] - SCREEN_SIZE[0] - 1
Y_LIMIT_MAX = SCREEN_SIZE[1] / BLOCK_SIZE
Y_LIMIT_MIN = SCREEN_SIZE[1] - SCREEN_SIZE[1] - 1

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

KEY_DIRECTION = {
                 pygame.K_UP:    'N',
                 pygame.K_DOWN:  'S',
                 pygame.K_LEFT:  'W',
                 pygame.K_RIGHT: 'E'
                }

KEY_DIRECTION_REV = {
                     pygame.K_UP:    'S',
                     pygame.K_DOWN:  'N',
                     pygame.K_LEFT:  'E',
                     pygame.K_RIGHT: 'W'
                    }

def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

def draw_grid():
    for x in range(1, int(SCREEN_SIZE[0]/BLOCK_SIZE)):
        pygame.draw.line(screen, GRID_COLOR, (BLOCK_SIZE*x,0), (BLOCK_SIZE*x,SCREEN_SIZE[1]), 1)
    for y in range(1, int(SCREEN_SIZE[0]/BLOCK_SIZE)):
        pygame.draw.line(screen, GRID_COLOR, (0, BLOCK_SIZE*y), (SCREEN_SIZE[0], BLOCK_SIZE*y), 1)

class Snake:
    def __init__(self):
        self.positions = STARTING_POINT
        self.direction = ''
        self.rev_direction = ''

    def draw(self):
        for position in self.positions:
            draw_block(screen, GREEN, position)

    def move(self):
        head_position = self.positions[0]
        tail_position = self.positions[:-1]
        x, y = head_position
        if self.direction == 'N':
            self.positions = [(x, y-MOVE_SPEED)] + tail_position
        if self.direction == 'S':
            self.positions = [(x, y+MOVE_SPEED)] + tail_position
        if self.direction == 'W':
            self.positions = [(x-MOVE_SPEED, y)] + tail_position
        if self.direction == 'E':
            self.positions = [(x+MOVE_SPEED, y)] + tail_position

    def grow(self):
        tail_position = self.positions[-1]
        x, y = tail_position
        if self.direction == 'N':
            self.positions.append((x, y-MOVE_SPEED))
        if self.direction == 'S':
            self.positions.append((x, y+MOVE_SPEED))
        if self.direction == 'W':
            self.positions.append((x-MOVE_SPEED, y))
        if self.direction == 'E':
            self.positions.append((x+MOVE_SPEED, y))

class Apple:
    def __init__(self, position=(0,0)):
        self.position = position

    def draw(self):
        draw_block(screen, RED, self.position)

def run_game():
    
    snake = Snake()    
    random_start_apple = random.randint(1, X_LIMIT_MAX-2), random.randint(1, Y_LIMIT_MAX-2)
    apple = Apple(position=random_start_apple)
    start = False

    while True:
        
        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)
        random_grow_apple = random.randint(1, X_LIMIT_MAX-2), random.randint(1, Y_LIMIT_MAX-2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    if snake.direction != KEY_DIRECTION_REV[event.key]:
                        snake.direction = KEY_DIRECTION[event.key]

        if snake.positions[0] == apple.position:
            snake.grow()
            apple.position = random_grow_apple
        elif apple.position in snake.positions[1:]:
            while True:
                 apple.position = random_grow_apple
                 if not apple.position in snake.positions[1:]:
                     break

        # GAME-OVER Condition        
        if snake.positions[0] in snake.positions[1:] and start == True:
            run_game()
        elif snake.positions[0][0] >= X_LIMIT_MAX or snake.positions[0][0] <= X_LIMIT_MIN:
            run_game()
        elif snake.positions[0][1] >= Y_LIMIT_MAX or snake.positions[0][1] <= Y_LIMIT_MIN:
            run_game()
        elif snake.positions[0] != STARTING_POINT[0]:
            start = True

        # print(snake.positions)

        snake.draw()
        apple.draw()
        draw_grid()
        
        snake.move()
        pygame.display.update()


run_game()
pygame.quit()
