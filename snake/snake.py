from random import randint

import pygame

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("snake game")

FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20
head_x = WINDOW_WIDTH / 2
head_y = WINDOW_HEIGHT / 2

snake_dx = 0
snake_dy = 0

score = 0

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font('fonts/Franxurter.ttf',32)


title_text = font.render("Snake", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)


gameover_text = font.render("Game Over", True, RED, DARKGREEN)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

continue_text = font.render("PRESS 'ENTER' To continue...", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50)


pickup_sound = pygame.mixer.Sound("sounds/click_sound.wav")
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

body_coords = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = 1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dy = -1 * SNAKE_SIZE
                snake_dx = 0
            if event.key == pygame.K_DOWN:
                snake_dy = 1 * SNAKE_SIZE
                snake_dx = 0
    body_coords.insert(0, head_coord)
    body_coords.pop()
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT:

        display_surface.blit(gameover_text, gameover_rect)

        # TODO
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    if head_rect.colliderect(apple_rect):
        score += 1
        pickup_sound.play()
        apple_x = randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        body_coords.append(head_coord)


    display_surface.fill(WHITE)
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)




    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
