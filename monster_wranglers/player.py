import pygame
from pygame.sprite import Sprite
from config import *


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets\\images\\knight.png")
        self.rect = self.image.get_rect()

        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2

        self.lives = 5
        self.velocity = 8
        self.warps = 2

        self.catch_sound = pygame.mixer.Sound("assets\\sounds\\catch.wav")
        self.die_sound = pygame.mixer.Sound("assets\\sounds\\die.wav")

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity

    def reset(self):
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2

    def warp(self):
        pass
