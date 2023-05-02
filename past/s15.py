# import pygame
# pygame.init()
# WHITE = (255, 255, 255)
# screen = pygame.display.set_mode((700, 500))
# clock = pygame.time.Clock()

# rect_x = 0
# rect_y = 0
# rect_change_x = 1
# rect_change_y = 1

# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False
#     pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
#     rect_x += rect_change_x
#     rect_y += rect_change_y

#     if rect_y > 450 or rect_y < 0:
#         rect_change_y = -1 * rect_change_y
#     if rect_x > 650 or rect_x < 0:
#         rect_change_x = -1 * rect_change_x

#     pygame.display.flip()

#     clock.tick(200)


# import pygame
# pygame.init()
# WHITE = (255, 255, 255)
# BROWN = (234, 221, 202)
# GREEN = (0, 255, 0)
# screen = pygame.display.set_mode((700, 500))


# def draw_tree(screen, x, y):
#     pygame.draw.rect(screen, BROWN, [60+x, 400+y, 30, 45])
#     pygame.draw.polygon(
#         screen, GREEN, [[150+x, 400+y], [75+x, 250+y], [0+x, 400+y]])
#     pygame.draw.polygon(
#         screen, GREEN, [[140+x, 350+y], [75+x, 230+y], [10+x, 350+y]])


# draw_tree(screen,0,50)
# draw_tree(screen,200,50)
# draw_tree(screen,400,50)

# pygame.display.flip()
# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False



# exercise : با کمک تابع تمرین زیر را انجام بده
# یک تابع برای جمع دو عدد
# یکی برای  تفریق دو عدد
# یکی برای 