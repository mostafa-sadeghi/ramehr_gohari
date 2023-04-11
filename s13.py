import pygame
# initialize the game engine
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cool Game')
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User Pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User released the key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")

    # Game logic
    # drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEEN, [155, 150, 80, 75], width=10)
    pygame.draw.li
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
