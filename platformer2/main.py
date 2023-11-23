import pygame
from pygame.locals import *
from constants import *
from player import Player
from world import draw_grid, World
from levels import level0_data


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()

sky_image = pygame.image.load('platformer2\img\sky.png')
sun_image = pygame.image.load('platformer2\img\sun.png')

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
world = World(level0_data.world_data,blob_group,lava_group)
player = Player(100, SCREEN_HEIGTH-130)
game_status = "playing"
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_image, (0, 0))
    screen.blit(sun_image, (100, 100))
    draw_grid(screen)
    world.draw(screen)
    game_status =player.update(screen, world.tile_list, blob_group, lava_group,game_status)
    blob_group.update()
    blob_group.draw(screen)
    lava_group.update()
    lava_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
