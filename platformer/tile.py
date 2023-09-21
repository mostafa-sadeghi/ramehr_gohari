import pygame.image
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, x, y, image_int, main_group, sub_group=""):
        super().__init__()
        if image_int == 1:
            self.image = pygame.image.load("assets/dirt.png")
        elif image_int == 2:
            self.image = pygame.image.load("assets/grass.png")
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.image.load("assets/water.png")
            sub_group.add(self)

        main_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

