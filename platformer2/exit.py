import pygame
from pygame.sprite import Sprite
from constants import TILE_SIZE
class ExitDoor(Sprite):
    def __init__(self, x,y):
        super().__init__()
        image = pygame.image.load("platformer2/img/exit.png")
        self.image = pygame.transform.scale(image,(TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft = (x,y))
    

    