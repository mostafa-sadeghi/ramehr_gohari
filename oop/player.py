from typing import Any
import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, x, y, monster_group):
        super().__init__()
        image = pygame.image.load("knight.png")
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5
        self.monster_group = monster_group

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity

    def check_collisions(self):
        pygame.sprite.spritecollide(self, self.monster_group, True)
