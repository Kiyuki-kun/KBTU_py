import sys
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 25
BALL_SIZE = 50
MOVE_STEP = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_vel[1] = -MOVE_STEP
            if event.key == pygame.K_DOWN:
                ball_vel[1] = MOVE_STEP
            if event.key == pygame.K_LEFT:
                ball_vel[0] = -MOVE_STEP
            if event.key == pygame.K_RIGHT:
                ball_vel[0] = MOVE_STEP

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_vel[1] = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_vel[0] = 0
    
    if ball_vel[0] != 0:
        if ball_pos[0] + ball_vel[0] + BALL_RADIUS > WIDTH or ball_pos[0] + ball_vel[0] - BALL_RADIUS < 0:
            ball_pos[0] += ball_vel[0]
        else:
            ball_pos[0] += ball_vel[0] * (BALL_SIZE / MOVE_STEP)

    if ball_vel[1] != 0:
        if ball_pos[1] + ball_vel[1] + BALL_RADIUS > HEIGHT or ball_pos[1] + ball_vel[1] - BALL_RADIUS < 0:
            ball_pos[1] += ball_vel[1]
        else:
            ball_pos[1] += ball_vel[1] * (BALL_SIZE / MOVE_STEP)

    if ball_pos[0] - BALL_RADIUS < 0:
        ball_pos[0] = BALL_RADIUS
    if ball_pos[0] + BALL_RADIUS > WIDTH:
        ball_pos[0] = WIDTH - BALL_RADIUS
    if ball_pos[1] - BALL_RADIUS < 0:
        ball_pos[1] = BALL_RADIUS
    if ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_pos[1] = HEIGHT - BALL_RADIUS

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, ball_pos, BALL_RADIUS)

    pygame.display.flip()

    pygame.time.Clock().tick(60)