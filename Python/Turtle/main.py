from turtle import Turtle, Screen
from random import choice

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.color("blue")
# for i in range(3, 11):
#     angle = 360 / i
#     r = choice(range(0, 256))
#     g = choice(range(0, 256))
#     b = choice(range(0, 256))
#     for sides in range(i):
#         screen.colormode(255)
#         my_turtle.pencolor(r, g, b)
#         my_turtle.forward(100)
#         my_turtle.right(angle)

direction_list = [2, 4, 6, 8]


def directions(direction):
    if direction == 2:
        my_turtle.left(90)
        my_turtle.forward(50)
    if direction == 4:
        my_turtle.right(90)
        my_turtle.forward(50)
    if direction == 6:
        my_turtle.forward(50)
    if direction == 8:
        my_turtle.backward(50)


while True:
    my_turtle.speed("fastest")
    r = choice(range(0, 256))
    g = choice(range(0, 256))
    b = choice(range(0, 256))
    screen.colormode(255)
    my_turtle.pencolor(r, g, b)
    my_turtle.circle(100)
    my_turtle.left(5)

screen.exitonclick()
