from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_LIST = []
for number in range(-260, 280, 20):
    RANDOM_LIST.append(number)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=3)
        self.color(random.choice(COLORS))
        self.setheading(180)
        y_cor = random.choice(RANDOM_LIST)
        self.setposition(300, y_cor)
        self.moving_distance = STARTING_MOVE_DISTANCE
        self.incremental_distance = MOVE_INCREMENT

    def move(self, moving_distance):
        self.goto(self.xcor() - moving_distance, self.ycor())
