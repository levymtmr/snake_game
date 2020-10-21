import pygame
import random
from options import OPTIONS, COLORS
from player import Player
pygame.init()


screen = pygame.display.set_mode(OPTIONS.get('screen_size'))
pygame.display.set_caption('Snake Game')

snake = Player(screen)
clock = pygame.time.Clock()
pos_x = random.randint(1, 299)
pos_y = random.randint(1, 299)

while True:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            snake.walk_right()
        if event.key == pygame.K_LEFT:
            snake.walk_left()
        if event.key == pygame.K_UP:
            snake.up()
        if event.key == pygame.K_DOWN:
            snake.down()

    screen.fill(COLORS.get('black'))
    border_game_rect = pygame.draw.polygon(screen, COLORS.get('red'),
                                           ((1, 20), (299, 20), (299, 328), (0, 328)), 1)
    enemi_rect = pygame.Rect(
        (pos_x, pos_y), (10, 10))
    pygame.draw.rect(screen, COLORS.get('purple'), enemi_rect)

    snake.draw()
    snake.clean()
    snake.check_touch()
    score = OPTIONS.get('font').render(
        'Score -> {}'.format(snake.level), True, COLORS.get('yellow'))
    screen.blit(score, [1, 1])
    if enemi_rect.colliderect(snake.rect) == 1:
        pos_x = random.randint(25, 280)
        pos_y = random.randint(25, 280)
        snake.level_up()

    if border_game_rect.colliderect(snake.rect) == 0:
        pygame.quit()

    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
