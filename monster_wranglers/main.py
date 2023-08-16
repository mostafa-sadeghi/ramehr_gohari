from config import *
import pygame
import random
from player import Player
pygame.init()


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster")

FPS = 60
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)


monster_group = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill((0, 0, 0))
    player_group.update()
    player_group.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
