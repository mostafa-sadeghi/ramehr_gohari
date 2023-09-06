from pygame.sprite import Sprite
import pygame

from alienBullet import AlienBullet


class Alien(Sprite):
    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("alien.png")
        self.rect = self.rect.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("alien_fire.wav")

    def update(self):
        self.rect.x += self.direction * self.velocity
        self.fire()
        # TODO

    def fire(self):
        AlienBullet(self.rect.x, self.rect.y, self.bullet_group)

    def reset(self):
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1
