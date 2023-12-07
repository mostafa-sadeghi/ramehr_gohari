import pygame

from constants import *
from enemy import Enemy
from lava import Lava
from exit import ExitDoor

def draw_grid(screen):
    for line in range(20):
        pygame.draw.line(screen, (255, 255, 255),
                         (line*TILE_SIZE, 0), (line*TILE_SIZE, SCREEN_HEIGTH))

        if line < 12:
            pygame.draw.line(screen, (255, 255, 255),
                             (0, line*TILE_SIZE), (SCREEN_WIDTH, line*TILE_SIZE))


class World:
    def __init__(self, data, blob_group, lava_group, exit_group) -> None:
        self.tile_list = []

        dirt_img = pygame.image.load("platformer2\img\dirt.png")
        grass_img = pygame.image.load("platformer2\img\grass.png")
        self.blob_group = blob_group
        self.lava_group = lava_group
        self.exit_group = exit_group
        for row_index, row in enumerate(data):
            for tile_index, tile in enumerate(row):
                if tile == 1:
                    img = pygame.transform.scale(
                        dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = tile_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                        grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = tile_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    blob = Enemy(tile_index * TILE_SIZE,row_index * TILE_SIZE +15)
                    self.blob_group.add(blob)

                if tile == 6:
                    lava = Lava(tile_index * TILE_SIZE,(row_index+1) * TILE_SIZE)
                    self.lava_group.add(lava)

                if tile == 7:
                    door = ExitDoor(tile_index * TILE_SIZE,row_index * TILE_SIZE)
                    self.exit_group.add(door)


    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
