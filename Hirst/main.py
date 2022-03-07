from turtle import Turtle, Screen
from random import choice

color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112),
              (215, 130, 165), (215, 56, 27)]
turtle = Turtle()
screen = Screen()
turtle.pensize(5)
turtle.penup()
current_turn = "right"
turtle.setheading(200)
turtle.forward(200)
turtle.setheading(0)


def print_row():
    screen.colormode(255)
    turtle.pencolor(choice(color_list))
    turtle.dot()
    turtle.forward(20)


def turn_left():
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)


def turn_right():
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)


for _ in range(10):
    for _ in range(10):
        print_row()
    if current_turn == "right":
        turn_left()
        current_turn = "left"
    else:
        turn_right()
        current_turn = "right"

screen.exitonclick()
