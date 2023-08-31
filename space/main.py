import pygame

pygame.init()


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
