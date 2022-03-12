from turtle import Turtle

FONT = ("Courier", 10, "normal")
LEVEL_POSITION = (-260, 280)
GAME_OVER_POSITION = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(LEVEL_POSITION)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write(f"GAME OVER", align="center", font=FONT)
