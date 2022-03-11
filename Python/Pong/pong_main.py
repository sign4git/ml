from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

POSITIONS = [(350, 0), (-350, 0)]
GAME_END_POINTS = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

game_on = True
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle(position=POSITIONS[0])
left_paddle = Paddle(position=POSITIONS[1])
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

while game_on:
    ball.move()
    time.sleep(ball.ball_speed)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.rebound_x()

    if ball.xcor() > 360:
        time.sleep(1)
        ball.change_direction()
        score.left_score += 1
        score.update_score()
    elif ball.xcor() < -360:
        time.sleep(1)
        ball.change_direction()
        score.right_score += 1
        score.update_score()

    if score.left_score >= 10 or score.right_score >= 10:
        game_on = False

screen.exitonclick()
