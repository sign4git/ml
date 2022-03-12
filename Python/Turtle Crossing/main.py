import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car_list = []
moving_distance = 0

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    cars_not_colliding = True
    time.sleep(0.1)
    screen.update()
    cars = CarManager()
    if moving_distance == 0:
        moving_distance = cars.moving_distance
    for car in car_list:
        if car.distance(cars) <= 80:
            cars_not_colliding = False
        car.move(moving_distance)
    if cars_not_colliding:
        car_list.append(cars)
    else:
        cars.hideturtle()

    if player.ycor() >= player.finish_line:
        player.reset_turtle()
        moving_distance += cars.incremental_distance
        score.update_level()
        for car in car_list:
            car.hideturtle()
        car_list.clear()

    for car in car_list:
        if player.ycor() == car.ycor() and player.distance(car) < 30:
            score.game_over()
            game_is_on = False
        elif player.distance(car) < 15:
            score.game_over()
            game_is_on = False

screen.exitonclick()
