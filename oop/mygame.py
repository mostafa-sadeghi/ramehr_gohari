import pygame
import random
from monster import Monster
from player import Player
pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wranglers")

monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill((0, 0, 0))
    monster_group.draw(display_surface)
    monster_group.update()

    player_group.draw(display_surface)
    player_group.update()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
