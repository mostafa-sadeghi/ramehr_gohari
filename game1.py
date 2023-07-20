# https://www.iconarchive.com/
# https://pinetools.com/flip-image
from random import randint
import pygame


def change_coin_position():
    coin_rect.x = WINDOWS_WIDTH + 100
    coin_rect.y = randint(75, WINDOW_HEIGHT - 32)


pygame.init()
WINDOWS_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("First Pygame Project")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
display_surface.fill(BLACK)

VELOCITY = 5
FPS = 60
PLAYER_STARTING_LIVES = 5
COIN_STARTING_VELOCITY = 4
COIN_ACCELERATION = 0.5


clock = pygame.time.Clock()

score = 0
player_lives = PLAYER_STARTING_LIVES

coin_velocity = COIN_STARTING_VELOCITY


font = pygame.font.Font("Algerian Regular.ttf", 22)

score_text = font.render(f"Score:{score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (75, 20)


title_text = font.render("Feed the dragon", False, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOWS_WIDTH / 2
title_rect.y = 20


lives_text = font.render(f"Lives: {player_lives}", False, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOWS_WIDTH - 75, 20)


game_over_text = font.render(f"Game Over.", False, BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2)


continue_text = font.render("press any key to continue...", True, RED)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2 + 30)


dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOWS_WIDTH, 0)


sound1 = pygame.mixer.Sound('sound.wav')
sound1.play()


player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.x = 0
player_rect.bottom = WINDOW_HEIGHT

coin_image = pygame.transform.scale(pygame.image.load("coin.png"), (28, 32))
coin_rect = coin_image.get_rect()
change_coin_position()

miss_sound = pygame.mixer.Sound("sound.wav")

pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.play(-1, 0.0)

# The main loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            player_rect.centerx = mouse_x
            player_rect.centery = mouse_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_rect.top > 75:
        player_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += VELOCITY

    if coin_rect.x < 0:
        change_coin_position()
        player_lives -= 1
        miss_sound.play()
    else:
        coin_rect.x -= coin_velocity

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_velocity += COIN_ACCELERATION
        change_coin_position()

    if player_lives == 0:
        
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT/2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    lives_text = font.render(f"Lives: {player_lives}", False, GREEN, DARKGREEN)
    score_text = font.render(f"Score:{score}", True, GREEN, DARKGREEN)

    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(player_image, player_rect)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOWS_WIDTH, 75), 6)

    display_surface.blit(coin_image, coin_rect)

    pygame.display.update()
    clock.tick(FPS)
# End the game
pygame.quit()
