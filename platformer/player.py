import pygame
from pygame.sprite import Sprite
from config import *
vector = pygame.math.Vector2


class Player(Sprite):
    def __init__(self, x, y, grass_tiles, water_tiles):
        super().__init__()
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []

        for i in range(1, 9):
            self.move_right_sprites.append(pygame.transform.scale(
                pygame.image.load(f"assets/boy/Run ({i}).png"), (96, 96)))

        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(
                pygame.transform.flip(sprite, True, False))

        for i in range(1, 10):
            self.idle_right_sprites.append(pygame.transform.scale(
                pygame.image.load(f"assets/boy/Idle ({i}).png"), (96, 96)))

        self.idle_left_sprites = [pygame.transform.flip(
            sprite, True, False) for sprite in self.idle_right_sprites]

        self.current_sprite = 0
        self.image = self.move_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.grass_tiles = grass_tiles
        self.water_tiles = water_tiles

        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 15

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]

    def update(self, display_surface):
        # pygame.draw.rect(display_surface, (255,0,0), self.rect, 2)

        self.mask = pygame.mask.from_surface(self.image)
        mask_outline = self.mask.outline()
        # pygame.draw.lines(self.image, (0,255,255), True, mask_outline)

        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, 0.2)

        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, 0.2)

        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, 0.2)
            else:
                self.animate(self.idle_left_sprites, 0.2)

        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION

        self.velocity += self.acceleration
        self.position += self.velocity

        if self.position.x < 0:
            self.position.x = screen_width
        elif self.position.x > screen_width:
            self.position.x = 0

        self.rect.bottomleft = self.position

        collided_platforms = pygame.sprite.spritecollide(
            self, self.grass_tiles, False, pygame.sprite.collide_mask)
        if collided_platforms:
            if self.velocity.y >= 0:
                self.position.y = collided_platforms[0].rect.top + 15
                self.velocity.y = 0

        if pygame.sprite.spritecollide(self, self.water_tiles, False):
            print("You Can't Swim")

    def jump(self):
        if pygame.sprite.spritecollide(self, self.grass_tiles, False):
            self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED
