from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.back(10)


def anti_clock():
    tim.lt(30)


def clock():
    tim.rt(30)


def clear():
    tim.clear()


def circle():
    tim.circle(10)


screen.onkey(forward, "w")  # Move Forward
screen.onkey(backward, "s")  # Move Backward
screen.onkey(anti_clock, "a")  # Move Left
screen.onkey(clock, "d")  # Move Right
screen.onkey(clear, "c")  # Clear screen
screen.onkey(circle, "o")  # Draw a circle
screen.listen()
screen.exitonclick()
