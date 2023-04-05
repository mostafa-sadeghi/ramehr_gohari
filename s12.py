# user_input = ''
# while user_input != 'quit':
#     user_input = input(
#         'enter a name or `quit` to exit from the program:> ').lower()

# print("Thank you for joining us.")


# done = False
# while not done:
#     quit = input('Do you want to quit? ').lower()
#     if quit.startswith('y'):
#         done = True


import random

# my_number = random.randrange(50)
# print(my_number)

# my_number = random.randrange(100,201)
# print(my_number)

# my_list = ["rock", "paper","scissors"]
# random_index = random.randrange(3)
# print(my_list[random_index])

# my_number = random.random()
# print(my_number)

# my_number = random.random() * 5 + 10
# print(my_number)

# a = 0

# for i in range(10):
#     a += 1
# for i in range(10):
#     a += 1
# print(a)


# a = 0
# for i in range(10):
#     a += 1
#     for j in range(10):
#         a += 1

# print(a)


import turtle

COLORS = ["red", "green", "blue"]
s = turtle.Screen()

p = turtle.Pen()
p.shape('turtle')
# draw triangle
for i in range(3):
    p.color(COLORS[i])
    p.forward(100)
    p.left(120)
# draw square
for i in range(4):
    p.color(COLORS[i % 3])
    p.forward(100)
    p.left(90)
# draw pentagon
for i in range(5):
    p.color(COLORS[i % 3])
    p.fd(100)
    p.left(72)
# draw hexagon
for i in range(6):
    p.color(COLORS[i % 3])
    p.fd(100)
    p.lt(60)


s.exitonclick()
