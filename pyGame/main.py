import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_PER_SECOND = 60
BALL_RADIUS = 5
BALL_MOVE_SPEED_ABS = 5
BAR_WIDTH = 100
BAR_HEIGHT = 10
BAR_CONTROL_SPEED = 15

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

ball_pos_x = SCREEN_WIDTH / 2
ball_pos_y = SCREEN_HEIGHT / 2

ball_move_speed_x = BALL_MOVE_SPEED_ABS
ball_move_speed_y = BALL_MOVE_SPEED_ABS

bar_pos_x = SCREEN_WIDTH / 2
bar_pos_y = SCREEN_HEIGHT - 50


def bounce(limit, ball_pos__, ball_move_speed__):
    if ball_move_speed__ > 0:
        if ball_pos__ + ball_move_speed__ > limit:
            return -BALL_MOVE_SPEED_ABS
        else:
            return BALL_MOVE_SPEED_ABS
            
    else:
        if ball_pos__ + ball_move_speed__ < 0:
            return BALL_MOVE_SPEED_ABS
        else:
            return -BALL_MOVE_SPEED_ABS


# OBB Oriented Bounding Box

while True:
    clock.tick(FRAME_PER_SECOND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        if bar_pos_x - BAR_CONTROL_SPEED >= -BALL_MOVE_SPEED_ABS:
            bar_pos_x -= BAR_CONTROL_SPEED
        print('left')
    elif key_event[pygame.K_RIGHT]:
        if bar_pos_x + BAR_CONTROL_SPEED <= SCREEN_WIDTH - BAR_WIDTH:
            bar_pos_x += BAR_CONTROL_SPEED
        print('right')

    screen.fill(black)

    ball_move_speed_x = bounce(SCREEN_WIDTH, ball_pos_x, ball_move_speed_x)
    ball_move_speed_y = bounce(SCREEN_HEIGHT, ball_pos_y, ball_move_speed_y)
    ball_pos_x += ball_move_speed_x
    ball_pos_y += ball_move_speed_y
    ball_pos = (ball_pos_x, ball_pos_y)

    bar_condition = (bar_pos_x, bar_pos_y, BAR_WIDTH, BAR_HEIGHT)

    pygame.draw.circle(screen, white, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, white, bar_condition)
    pygame.display.update()