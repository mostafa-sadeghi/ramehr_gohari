import pygame
from pygame.locals import *
from constants import *
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.jumped = False
        self.inair = False
        self.ghost_img = pygame.image.load("platformer2/img/ghost.png")

        for i in range(1, 5):
            image_right = pygame.image.load(f'platformer2/img/guy{i}.png')
            image_right = pygame.transform.scale(image_right, (40, 80))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_right.append(image_right)
            self.images_left.append(image_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = x
        self.rect.y = y

        self.vel_y = 0
        self.direction = 1

    def update(self, screen, tile_list, blob_group, lava_group, game_status):
        dx = 0
        dy = 0
        walk_cooldown = 5
        if game_status == "playing":
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and not self.jumped and not self.inair:
                self.vel_y = -15
                self.jumped = True
            if  not keys[K_SPACE]:
                self.jumped = False

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
                # if self.direction == 1:
                #     self.image = self.images_right[self.index]
                # if self.direction == -1:
                #     self.image = self.images_left[self.index]

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
            if self.vel_y > 10:
                self.vel_y = 10

            dy += self.vel_y

            for tile in tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >=0:
                    
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom
        
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_status = 'game_over'
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_status = 'game_over'
            
            
            self.rect.x += dx
            self.rect.y += dy
        
        elif game_status == "game_over":
            self.image = self.ghost_img
            
            if self.rect.bottom> 100:
                self.rect.y -= 5
                
        

        if self.rect.bottom > SCREEN_HEIGTH:
            self.rect.bottom = SCREEN_HEIGTH
            dy = 0

       
        screen.blit(self.image, self.rect)
        return game_status

