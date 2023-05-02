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
    # pygame.draw.rect(screen, GREEEN, [155, 150, 80, 75], width=10)
    # pygame.draw.line(screen, RED, [0,0],[100,100],5)
    # pygame.display.flip()
    # clock.tick(60)

    # y_offset = 0
    # while y_offset < 100:
    #     pygame.draw.line(screen,RED, [0, 10 + y_offset], [100, 110+y_offset])
    #     y_offset += 10
    # for y_offset in range(0,100,10):
    #     pygame.draw.line(screen,RED, [0, 10 + y_offset], [100, 110+y_offset])

    # for x_offset in range(30,300,30):
    #     pygame.draw.line(screen, BLACK, [x_offset,100], [x_offset-10, 90])
    #     pygame.draw.line(screen, BLACK, [x_offset,90], [x_offset-10, 100])

    # pygame.draw.ellipse(screen, BLACK, [20,20,250,100],2)

    # pygame.draw.polygon(screen, BLACK, [[100,100], [0,200],[200,200]],5)
#     score = 100
#     font = pygame.font.SysFont('Arial', 25, True, False)
#     text = font.render("Score: "+str(score), True, BLACK)
#     screen.blit(text, [0, 0])

#     pygame.display.flip()

# pygame.quit()
