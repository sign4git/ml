from snake import Snake
import time
from turtle import Screen

initialize_game = True

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # To stop animation
a = 10

# TODO 1.INITIALIZE SNAKE BODY
snake = Snake()

# TODO 2.CONTROL THE SNAKE
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO 3.MOVE SNAKE BODY
while initialize_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
