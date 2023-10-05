import pygame

from constants import *


def draw_grid(screen):
    for line in range(20):
        pygame.draw.line(screen, (255, 255, 255),
                         (line*TILE_SIZE, 0), (line*TILE_SIZE, SCREEN_HEIGTH))

        if line < 12:
            pygame.draw.line(screen, (255, 255, 255),
                             (0, line*TILE_SIZE), (SCREEN_WIDTH, line*TILE_SIZE))


class World:
    def __init__(self, data) -> None:
        self.tile_list = []

        dirt_img = pygame.image.load("platformer2\img\dirt.png")
        grass_img = pygame.image.load("platformer2\img\grass.png")

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

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
