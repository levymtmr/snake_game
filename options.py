import pygame
pygame.init()

OPTIONS = {
    'screen_size': (300, 330),
    'start_positions': pygame.math.Vector2(30, 280),
    'walk': pygame.math.Vector2(1, 0),
    'up': pygame.math.Vector2(0, 1),
    'font': pygame.font.SysFont("comicsansms", 25)
}

COLORS = {
    'white': (250, 250, 250),
    'black': (0, 0, 0),
    'yellow': (255, 255, 102),
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'purple': (128, 0, 128)
}
