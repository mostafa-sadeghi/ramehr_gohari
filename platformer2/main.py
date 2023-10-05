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


world = World(level0_data.world_data)
player = Player(100, SCREEN_HEIGTH-130)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_image, (0, 0))
    screen.blit(sun_image, (100, 100))
    draw_grid(screen)
    world.draw(screen)
    player.update(screen)
    pygame.display.update()
    clock.tick(FPS)
