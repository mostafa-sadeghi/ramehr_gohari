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
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
display_surface.fill(BLACK)

# pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
# pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)


# pygame.draw.circle(display_surface, BLACK,
#                    (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2), 200, 6)
# pygame.draw.circle(display_surface, YELLOW,
#                    (WINDOWS_WIDTH/2, WINDOW_HEIGHT/2), 195, 0)

# pygame.draw.rect(display_surface, RED, (500, 0, 100, 100))
# pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

dragon_left_image = pygame.image.load("dragon_l.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


# The main loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(dragon_left_image, dragon_left_rect)

    pygame.display.update()
# End the game
pygame.quit()
