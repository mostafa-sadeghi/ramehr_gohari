
import time

from snake_game_utils import move_snake, reset,\
    change_food_position,\
    make_screen, generate_turtle_object


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


def full_screen():
    global window_width, window_height
    window.setup(width=1520, height=800)
    window_width = 1520
    window_height = 800
    border_pen.clear()

    # window.screensize(canvwidth=1520, canvheight=800)


window_width = 600
window_height = 600
window = make_screen()
# window.screensize(canvwidth=window_width, canvheight=window_height)
window.setup(width=window_width, height=window_height)
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")
window.onkey(full_screen, "f")


score = 0

head = generate_turtle_object("square", "black")
head.dir = "none"


food = generate_turtle_object("circle", "red")
food.shapesize(0.5, 0.5)
change_food_position(food, window_width, window_height)

score_pen = generate_turtle_object("square", "white")
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(f"Score: {score}", align="center", font=("Arial", 30))

border_pen = generate_turtle_object("square", "black")
border_pen.hideturtle()
border_pen.goto(-(window_height//2), (window_width//2 - 50))
border_pen.pendown()
for i in range(2):
    border_pen.forward(window_width - 10)
    border_pen.right(90)
    border_pen.forward(window_width-60)
    border_pen.right(90)

snake_body = []
while True:
    window.update()

    # print(window_width)
    # print(window_height)
    if head.distance(food) < 15:
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="center", font=("Arial", 30))
        change_food_position(food, window_width, window_height)
        new_body = generate_turtle_object("square", "grey")
        snake_body.append(new_body)
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index-1].xcor()
        y = snake_body[index-1].ycor()
        snake_body[index].goto(x, y)

    if len(snake_body):
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x, y)

    if (head.xcor() > (window_width/2 - 10)) or (head.xcor() < -(window_width/2-10)) \
            or (head.ycor() > (window_width/2 - 65)) or (head.ycor() < -(window_width/2-10)):
        score = reset(score_pen, head, snake_body, score)
        print("snake_game_score:", score)

    move_snake(head)

    for body in snake_body:
        if head.distance(body) < 20:
            score = reset(score_pen, head, snake_body, score)

    time.sleep(0.2)
