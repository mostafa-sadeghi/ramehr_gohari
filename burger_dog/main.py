import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .5




score = 0
burger_points = 0
burger_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

ORANGE = (246, 170, 54)
BLACK = (0,0,0)
WHITE = (255, 255, 255)


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")

FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/Algerian Regular.ttf", 32)

points_text = font.render(f"Burger points: {burger_points}", True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render(f"Score: {score}", True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("Burger DOG", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH/2
title_rect.y = 10

eaten_text = font.render(f"Burgers Eaten: {burger_eaten}", True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH/2
eaten_rect.y = 50


lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-10, 10)

boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH-10, 50)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)

    pygame.display.update()


pygame.quit()