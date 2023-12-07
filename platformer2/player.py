import pygame
from pygame.locals import *
from constants import *
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.reset(x,y)
        

    def update(self, screen, tile_list, blob_group, lava_group,exit_door_group, game_status):
        if self.direction == 1:
            rect = pygame.Rect(self.rect.x + 20, self.rect.y + 5, self.image.get_width()-30,self.image.get_height()-10)
        else:
            rect = pygame.Rect(self.rect.x + 10 , self.rect.y+ 5 , self.image.get_width()-30,self.image.get_height()-10)

        dx = 0
        dy = 0
        walk_cooldown = 5
        if game_status == "playing":
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and not self.jumped and not self.inair:
                self.vel_y = -15
                self.jumped = True
                self.inair = True
            if  not keys[K_SPACE]:
                self.jumped = False

            if keys[K_LEFT]:
                self.idle = False
                dx -= 5
                self.counter += 1
                self.direction = -1
            if keys[K_RIGHT]:
                self.idle = False
                dx += 5
                self.counter += 1
                self.direction = 1
            if not keys[K_LEFT] and not keys[K_RIGHT]:
                self.counter += 1
                self.idle = True

            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.idle:
                if self.direction == 1:
                    self.image = self.images_idle_right[self.index]
                if self.direction == -1:
                    self.image = self.images_idle_left[self.index]

            else:    
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10

            dy += self.vel_y

            for tile in tile_list:
                if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width()-30,self.image.get_height()-10):
                    dx = 0
                if tile[1].colliderect(rect.x, rect.y + dy, self.image.get_width()-30,self.image.get_height()-10):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - rect.top
                        self.vel_y = 0
                    elif self.vel_y >=0:
                        self.inair = False
                        self.vel_y = 0
                        dy = tile[1].top - rect.bottom
        
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_status = 'game_over'
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_status = 'game_over'
            if pygame.sprite.spritecollide(self, exit_door_group, False):
                game_status = 'exit'
            
            
            
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
        # pygame.draw.rect(screen, (145,10,178), rect, 4)
        return game_status


    def reset(self, x,y):
        self.images_right = []
        self.images_left = []
        self.images_idle_right = []
        self.images_idle_left = []
        self.index = 0
        self.counter = 0
        self.jumped = False
        self.inair = False
        self.idle = True
        self.ghost_img = pygame.image.load("platformer2/img/ghost.png")

        for i in range(1, 9):
            image_right = pygame.image.load(f'platformer2/img/boy/Run ({i}).png')
            image_right = pygame.transform.scale(image_right, (TILE_SIZE*1.3, TILE_SIZE*1.1))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_right.append(image_right)
            self.images_left.append(image_left)

        for i in range(1, 10):
            image_right = pygame.image.load(f'platformer2/img/boy/Idle ({i}).png')
            image_right = pygame.transform.scale(image_right, (TILE_SIZE*1.3, TILE_SIZE*1.1))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_idle_right.append(image_right)
            self.images_idle_left.append(image_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = x
        self.rect.y = y

        self.vel_y = 0
        self.direction = 1

