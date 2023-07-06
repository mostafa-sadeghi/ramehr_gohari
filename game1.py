# https://www.iconarchive.com/
# https://pinetools.com/flip-image
import pygame
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
clock = pygame.time.Clock()


dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOWS_WIDTH, 0)

font1 = pygame.font.SysFont('Terminal', 62)
text1 = font1.render("Dragon Game!", False, GREEN, DARKGREEN)
text1_rect = text1.get_rect()
text1_rect.center = (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2)

font2 = pygame.font.Font('Algerian Regular.ttf', 64)
text2 = font2.render("Dragon!", False, GREEN)
text2_rect = text2.get_rect()
text2_rect.center = (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2 + 100)

sound1 = pygame.mixer.Sound('sound.wav')
sound1.play()


player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.x = 0
player_rect.bottom = WINDOW_HEIGHT

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
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOWS_WIDTH:
        player_rect.x += VELOCITY
    if keys[pygame.K_UP] and player_rect.top > 75:
        player_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += VELOCITY

    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(player_image, player_rect)
    # display_surface.blit(text1, text1_rect)
    # display_surface.blit(text2, text2_rect)

    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOWS_WIDTH, 75), 6)

    pygame.display.update()
    clock.tick(FPS)
# End the game
pygame.quit()
