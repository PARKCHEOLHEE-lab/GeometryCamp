import pygame

pygame.init()

# screen
SCREEN_COLOR = (0, 0, 0)
SCREEN_SIZE = (800, 600)
FPS = 30


# object
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK_SIZE = 10
MOVE_SPEED = 1

block_position = [25, 25]
move_direction = ''

screen = pygame.display.set_mode(SCREEN_SIZE)
done = False
clock = pygame.time.Clock()


def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def run_game():
    global done, last_moved_time, move_direction
    
    while not done:
        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_direction = 'N'
                elif event.key == pygame.K_DOWN:
                    move_direction = 'S'
                elif event.key == pygame.K_LEFT:
                    move_direction = 'W'
                elif event.key == pygame.K_RIGHT:
                    move_direction = 'E'

        if move_direction == 'N':
            block_position[1] -= MOVE_SPEED
        elif move_direction == 'S':
            block_position[1] += MOVE_SPEED
        elif move_direction == 'W':
            block_position[0] -= MOVE_SPEED
        elif move_direction == 'E':
            block_position[0] += MOVE_SPEED

        draw_block(screen, GREEN, block_position)
        pygame.display.update()

run_game()
pygame.quit()
