import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game import Game
from player import Player

pygame.init()


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
player = Player(player_bullet_group)
game = Game(player, alien_group, player_bullet_group, alien_bullet_group)
game.start_new_round()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    display_surface.fill((0, 0, 0))
    game.draw(display_surface)
    game.update()
    player.draw(display_surface)
    player.update()
    alien_group.update()
    alien_group.draw(display_surface)
    player_bullet_group.update()
    player_bullet_group.draw(display_surface)
    alien_bullet_group.update()
    # alien_bullet_group.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
