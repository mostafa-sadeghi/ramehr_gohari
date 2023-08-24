from config import *
import pygame
import random
from game import Game
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

my_game = Game(player, monster_group, display_surface)
running = my_game.pause_game(
    "Monster Game", "Press 'Enter' to continue ...", running)
my_game.start_new_round()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.warp()
    display_surface.fill((0, 0, 0))
    player_group.update()
    player_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)
    my_game.update()
    my_game.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
