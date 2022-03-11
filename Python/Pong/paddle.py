from turtle import Turtle

WIDTH = 1
HEIGHT = 5
SHAPE = "square"
MODE = "user"
COLOR = "white"
STEPS = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.resizemode(MODE)
        self.turtlesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.goto(position)
        self.penup()
        self.color(COLOR)

    def up(self):
        self.goto(self.xcor(), self.ycor() + STEPS)

    def down(self):
        self.goto(self.xcor(), self.ycor() - STEPS)
