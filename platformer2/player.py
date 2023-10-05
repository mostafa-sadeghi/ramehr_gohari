import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y) -> None:
        img = pygame.image.load("platformer2\img\guy1.png")
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vel_y = 0

    def update(self, screen):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            dx -= 5
        if keys[K_RIGHT]:
            dx += 5

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)
