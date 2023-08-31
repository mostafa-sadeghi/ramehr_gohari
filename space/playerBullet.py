from pygame.sprite import Sprite
import pygame


class PlayerBullet(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("green_laser.png")
