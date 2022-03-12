from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_turtle()

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
