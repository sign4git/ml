from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

is_game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # To stop animation

# TODO 1.INITIALIZE SNAKE BODY
snake = Snake()
# TODO 2. INITIALIZE SCOREBOARD
score = Scoreboard()
score.color("white")
score.display_score()
# TODO 3.CONTROL THE SNAKE
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO 4. SNAKE FOOD
food = Food()

# TODO 5.MOVE SNAKE BODY
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.update_score()
        score.display_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()  # GAME OVER
        is_game_on = False

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            is_game_on = False

screen.exitonclick()
