import pygame
from pygame.locals import *
from constants import *


class Player:
    def __init__(self, x, y) -> None:

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for i in range(1, 5):
            image_right = pygame.image.load(f'platformer2/img/guy{i}.png')
            image_right = pygame.transform.scale(image_right, (40, 80))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_right.append(image_right)
            self.images_left.append(image_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vel_y = 0
        self.direction = 1

    def update(self, screen):
        dx = 0
        dy = 0
        walk_cooldown = 5

        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            self.vel_y = -15
        if keys[K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if keys[K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if not keys[K_LEFT] and not keys[K_RIGHT]:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.images_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]

        self.vel_y += 1

        dy += self.vel_y

        # TODO ##########################################################################

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > SCREEN_HEIGTH:
            self.rect.bottom = SCREEN_HEIGTH
            dy = 0

        screen.blit(self.image, self.rect)
