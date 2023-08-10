import pygame
import random
from monster import Monster
from player import Knight
from game import Game
pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wranglers")

monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

knight_group = pygame.sprite.Group()

for i in range(12):

    knight = Knight(i * 64, WINDOW_HEIGHT - 64)
    knight_group.add(knight)


my_game = Game(monster_group, knight_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill((0, 0, 0))
    monster_group.draw(display_surface)
    monster_group.update()

    knight_group.draw(display_surface)
    knight_group.update()
    my_game.update()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
