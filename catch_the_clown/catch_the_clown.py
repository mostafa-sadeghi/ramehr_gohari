import pygame
import random

pygame.init()

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the clown game!")

FPS = 60
clock = pygame.time.Clock()
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY

clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

font = pygame.font.Font("Franxurter.ttf", 32)

title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render(f"Score: {score}", True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topleft = (WINDOW_WIDTH - 150, 10)

lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topleft = (WINDOW_WIDTH - 150, 50)

gameover_text = font.render("Game Over", True, (0,0,0))
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

continue_text = font.render("Click To continue...", True, (255,0,0))
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50)

click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("Bad Piggies Theme.mp3")
pygame.mixer.music.play(-1, 0.0)

background_image = pygame.image.load("background.png")
background_image_rect = background_image.get_rect()
background_image_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

clown_image = pygame.image.load("clown.png")
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_image_rect.collidepoint(event.pos):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION
                prev_dx = clown_dx
                prev_dy = clown_dy
                while (prev_dx == clown_dx and prev_dy == clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            else:
                miss_sound.play()
                player_lives -= 1

    clown_image_rect.x += clown_dx * clown_velocity
    clown_image_rect.y += clown_dy * clown_velocity

    if clown_image_rect.x <= 0 or clown_image_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_image_rect.y <= 0 or clown_image_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy
    score_text = font.render(f"Score: {score}", True, YELLOW)
    lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)

    if player_lives == 0:
        pygame.mixer.music.stop()
        display_surface.blit(gameover_text, gameover_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_paused = False
                    pygame.mixer.music.play(-1, 0.0)
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    clown_image_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_paused = False
                        running = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    display_surface.blit(background_image, background_image_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(clown_image, clown_image_rect)

    pygame.display.update()

pygame.quit()
