from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("platformer2/img/blob.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.direction
        self.move_counter += 1
        if self.move_counter > 100:
            self.direction *= -1
            self.move_counter *= -1
    