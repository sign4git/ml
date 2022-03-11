from turtle import Turtle

POSITION = (0, 0)
SPEED = 0.1
SPEED_MULTIPLIER = 0.9
DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(POSITION)
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.x_dir = DISTANCE
        self.y_dir = DISTANCE
        self.ball_speed = SPEED

    def move(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def rebound_y(self):
        self.y_dir *= -1

    def rebound_x(self):
        self.x_dir *= -1
        self.ball_speed *= SPEED_MULTIPLIER

    def change_direction(self):
        self.goto(0, 0)
        self.ball_speed = SPEED
        self.rebound_x()
