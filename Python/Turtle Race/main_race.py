from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
color_list = ["violet", "blue", "green", "yellow", "orange", "red"]
start_height = -60
turtle_list = []
race_on = False
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win this race? Predict a color: ")

if user_guess in color_list:
    race_on = True


def create_turtle(height, turtle_color):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(turtle_color)
    turtle.goto(x=-230, y=height)
    turtle_list.append(turtle)


for color in color_list:
    create_turtle(height=start_height, turtle_color=color)
    start_height += 30

while race_on:
    for current_turtle in turtle_list:
        if current_turtle.xcor() > 230:
            race_on = False
            winning_turtle = current_turtle.pencolor()
            if winning_turtle == user_guess:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        random_distance = random.randint(0, 10)
        current_turtle.forward(random_distance)

screen.exitonclick()
