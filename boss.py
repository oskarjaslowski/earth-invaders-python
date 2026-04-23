import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/boss_m.png').convert_alpha()
        self.rect = self.image.get_rect(center =(x,y))
        self.value = 5000
        self.enemy_lives = 10000

    def update(self, direction):
        self.rect.x += direction