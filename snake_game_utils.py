import random
import turtle


def make_screen():
    window = turtle.Screen()
    window.title("Snake game")
    window.bgcolor('blue')

    window.tracer(0)
    return window


def move_snake(head):
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


def reset(score_pen, head, snake_body,score, high_score):

    file = open("snake_game.csv", "w")
    file.write(f"{high_score}")

    score = 0
    print("snake_game_utils_score:", score)

    score_pen.clear()
    score_pen.write(f"Score: {score} HighScore: {high_score}",
                    align="center", font=("Arial", 30))
    head.goto(0, 0)
    head.dir = ""
    for body in snake_body:
        body.ht()
    snake_body.clear()
    return score, high_score


def change_food_position(food, window_width, window_height):
    food_initial_x = random.randint(-(window_width/2-50), window_width/2-50)
    food_initial_y = random.randint(-(window_height/2-50), window_height/2-50)
    food.goto(food_initial_x, food_initial_y)


def generate_turtle_object(shape, color):
    turtle_object = turtle.Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.speed("fastest")
    turtle_object.penup()
    return turtle_object
