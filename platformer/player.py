import pygame
from pygame.sprite import Sprite
from config import *
vector = pygame.math.Vector2
class Player(Sprite):
    def __init__(self, x, y, grass_tiles, water_tiles):
        super().__init__()
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        self.grass_tiles = grass_tiles
        self.water_tiles = water_tiles

        self.position = vector(x,y)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 15

    def update(self):
        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION

        if keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION

        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION

        self.velocity += self.acceleration
        self.position += self.velocity

        if self.position.x < 0:
            self.position.x = screen_width
        elif self.position.x > screen_width:
            self.position.x = 0

        self.rect.bottomleft = self.position

        collided_platforms = pygame.sprite.spritecollide(self, self.grass_tiles, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        if pygame.sprite.spritecollide(self, self.water_tiles, False):
            print("You Can't Swim")

    def jump(self):
        if pygame.sprite.spritecollide(self,self.grass_tiles, False):
            self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED