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


def reset():
    global score
    score = 0
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=("Arial", 30))
    head.goto(0, 0)
    head.dir = ""
    for body in snake_body:
        body.ht()
    snake_body.clear()


def change_food_position():
    food_initial_x = random.randint(-250, 250)
    food_initial_y = random.randint(-250, 250)
    food.goto(food_initial_x, food_initial_y)


def generate_turtle_object(shape, color):
    turtle_object = turtle.Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.speed("fastest")
    turtle_object.penup()
    return turtle_object


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


score = 0

head = generate_turtle_object("square", "black")
head.dir = "none"


food = generate_turtle_object("circle", "red")
food.shapesize(0.5, 0.5)
change_food_position()

score_pen = generate_turtle_object("square", "white")
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(f"Score: {score}", align="center", font=("Arial", 30))


snake_body = []
while True:
    window.update()

    if head.distance(food) < 15:
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="center", font=("Arial", 30))
        change_food_position()
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

    if head.xcor() > 290 or head.xcor() < -290 \
            or head.ycor() > 290 or head.ycor() < -290:
        reset()

    move_snake()

    for body in snake_body:
        if head.distance(body) < 20:
            reset()

    time.sleep(0.15)
