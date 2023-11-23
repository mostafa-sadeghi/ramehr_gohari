from pygame.sprite import Sprite
import pygame
from constants import *

class Lava(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("platformer2/img/lava.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE/2))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)


    