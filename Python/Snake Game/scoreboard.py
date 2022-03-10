from turtle import Turtle

POSITION = (0, 280)
FONT_TYPE = "normal"
FONT_SIZE = 10
FONT_NAME = "Arial"
FONT = (FONT_NAME, FONT_SIZE, FONT_TYPE)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(POSITION)
        self.hideturtle()

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=FONT)
