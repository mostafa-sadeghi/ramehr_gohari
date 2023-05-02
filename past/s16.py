# Adding two numbers

# def add(number1, number2):
#     """Returns sum of two numbers
#     Parameters:
#     number1: int,
#     number2: int,
#     Returns: int
#     """
#     return number1 + number2
# if __name__ == '__main__':
#     print(add(2, 3))

# variable scope
# local scope
# def f():
#     x = 22


# f()

# print(x)

# global
# x = 0

# def f():
#     global x
#     x += 1


# f()
# f()
# f()

# print(x)


# def f(x):
#     x += 1
#     print(x)


# y = 10
# f(y)
# print(y)

import pygame
WHITE = (255, 255, 255)


def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, y + 65, 100, 100])


pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
x_pos = 10
y_pos = 10
draw_snowman(screen, x_pos, y_pos)
# draw_snowman(screen, 300, 10)
# draw_snowman(screen, 10, 300)
# draw_snowman(screen, 300, 300)
pygame.display.flip()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_pos -= 3
            elif event.key == pygame.K_RIGHT:
                x_pos += 3

    # pos = pygame.mouse.get_pos()
    # print("mouse position is:", pos)
    draw_snowman(screen, x_pos, y_pos)

    pygame.display.flip()
    clock.tick(2)
