import turtle
import time
import random


def go_up():
    if head.dir != "down":
        head.dir = "up"


def go_right():
    if head.dir != "left":
        head.dir = "right"


def go_left():
    if head.dir != "right":
        head.dir = "left"


def go_down():
    if head.dir != "up":
        head.dir = "down"


def move_snake():
    if head.dir == "up":
        yposition = head.ycor()
        head.sety(yposition + 20)
    if head.dir == "down":
        yposition = head.ycor()
        head.sety(yposition - 20)
    if head.dir == "right":
        xposition = head.xcor()
        head.setx(xposition + 20)
    if head.dir == "left":
        xposition = head.xcor()
        head.setx(xposition - 20)


window = turtle.Screen()
window.title("Snake game")
window.bgcolor('blue')
window.setup(width=600, height=600)
window.tracer(0)
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")


head = turtle.Turtle()
head.shape("square")
head.penup()
head.speed("fastest")
# head.goto(0,100)
head.dir = "none"


food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed("fastest")
food.penup()
food.shapesize(0.5, 0.5)
food_initial_x = random.randint(-300, 300)
food_initial_y = random.randint(-300, 300)
food.goto(food_initial_x, food_initial_y)

snake_body = []
while True:
    window.update()

    if head.distance(food) < 15:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)
        new_body = turtle.Turtle()
        new_body.speed("fastest")
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        snake_body.append(new_body)
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index-1].xcor()
        y = snake_body[index-1].ycor()
        snake_body[index].goto(x, y)

    if len(snake_body):
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x, y)
    move_snake()
    time.sleep(0.1)
