import pygame
from options import OPTIONS, COLORS


class Player:

    def __init__(self, screen):
        self.level = 1
        self.pos = OPTIONS.get('start_positions')
        self.screen = screen
        self.player_height = 12
        self.color = COLORS.get('green')
        self.speed = 1
        self.snake_size_block = [self.pos]
        self.rect = pygame.Rect(self.pos, (10, 10))

    def walk_right(self):
        self.pos = self.pos + OPTIONS.get('walk') * self.speed
        self.snake_size_block.append(self.pos)
        self.update()

    def walk_left(self):
        self.pos = self.pos - OPTIONS.get('walk') * self.speed
        self.snake_size_block.append(self.pos)
        self.update()

    def up(self):
        self.pos = self.pos - OPTIONS.get('up') * self.speed
        self.snake_size_block.append(self.pos)
        self.update()

    def down(self):
        self.pos = self.pos + OPTIONS.get('up') * self.speed
        self.snake_size_block.append(self.pos)
        self.update()

    def update(self):
        for i in self.snake_size_block:
            self.rect = pygame.Rect(i, (10, 10))
            pygame.draw.rect(self.screen, self.color, self.rect)

    def clean(self):
        if len(self.snake_size_block) > self.level:
            self.snake_size_block.pop(0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.update()

    def check_touch(self):
        head_posistion = self.snake_size_block[0]
        if head_posistion in self.snake_size_block[1:]:
            pygame.quit()

    def level_up(self):
        self.level = self.level + 1
        self.speed = self.speed + 0.20
        self.update()
