import pygame
from pygame.locals import *
from constants import *
from player import Player
from world import draw_grid, World
from levels import level0_data
from button import Button

pygame.init()
level = 0
max_level = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()

sky_image = pygame.image.load('platformer2\img\sky.png')
sun_image = pygame.image.load('platformer2\img\sun.png')
restart_button_image = pygame.image.load('platformer2/img/restart_btn.png')
start_button_image = pygame.image.load('platformer2/img/start_btn.png')
start_button_image = pygame.transform.scale(start_button_image,(start_button_image.get_width()*0.6 , start_button_image.get_height()*0.6))
exit_button_image = pygame.image.load('platformer2/img/exit_btn.png')
exit_button_image = pygame.transform.scale(exit_button_image, (exit_button_image.get_width()*0.6, exit_button_image.get_height()*0.6))

restart_button = Button(SCREEN_WIDTH/2,SCREEN_HEIGTH/2, restart_button_image)
start_button = Button(SCREEN_WIDTH/2-250,SCREEN_HEIGTH/2, start_button_image)
exit_button = Button(SCREEN_WIDTH/2+250,SCREEN_HEIGTH/2, exit_button_image)



blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_door_group = pygame.sprite.Group()
world = World(level0_data.world_data,blob_group,lava_group,exit_door_group)
player = Player(100, SCREEN_HEIGTH-130)
game_status = "playing"
main_menu = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_image, (0, 0))
    # screen.blit(sun_image, (100, 100))

    if main_menu:
        start_button.draw(screen)
        if start_button.clicked():
            main_menu = False
        exit_button.draw(screen)
        if exit_button.clicked():
            running = False
    else:
        draw_grid(screen)
        world.draw(screen)
        game_status =player.update(screen, world.tile_list, blob_group, lava_group,exit_door_group,game_status)
        if game_status == "game_over":
            restart_button.draw(screen)
            if restart_button.clicked():
                game_status = "playing"
                player.reset(100, SCREEN_HEIGTH-130)
        if game_status == "exit":
            level+=1
            if level <= max_level:
                pass




        blob_group.update()
        lava_group.update()
        lava_group.draw(screen)
        blob_group.draw(screen)
        exit_door_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
