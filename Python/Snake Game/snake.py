from turtle import Turtle

INITIAL_POSITION = [(40, 0), (20, 0), (0, 0)]
ANGLE = 90
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.initialize_snake()
        self.head = self.snake_segments[0]

    def initialize_snake(self):
        for position in INITIAL_POSITION:
            turtle = Turtle("square")
            turtle.penup()
            turtle.goto(position)
            turtle.color("white")
            self.snake_segments.append(turtle)

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[segment - 1].xcor()
            y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
