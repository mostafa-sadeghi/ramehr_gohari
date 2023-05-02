import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode()


joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Error, I didn't find any joystick")
else:
    print("ok")
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()


clock = pygame.time.Clock()
x_coord = 10
y_coord = 10
w = 10
h = 10

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False
        if event.type == pygame.JOYBUTTONDOWN:
            print("Button Pressed")
            if my_joystick.get_button(6):
                w *= 2
                # Control Left Motor using L2
            elif my_joystick.get_button(7):
                h *= 2
                # Control Right Motor using R2
        elif event.type == pygame.JOYBUTTONUP:
            print("Button Released")

    if joystick_count != 0:
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
        x_coord += int(horiz_axis_pos * 10)
        y_coord += int(vert_axis_pos * 10)
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [x_coord, y_coord, w, h])
    pygame.display.flip()
    clock.tick(60)


'''

The PS4 buttons are numbered as the following:

0 = SQUARE

1 = X

2 = CIRCLE

3 = TRIANGLE

4 = L1

5 = R1

6 = L2

7 = R2

8 = SHARE

9 = OPTIONS

10 = LEFT ANALOG PRESS

11 = RIGHT ANALOG PRESS

12 = PS4 ON BUTTON

13 = TOUCHPAD PRESS




'''
