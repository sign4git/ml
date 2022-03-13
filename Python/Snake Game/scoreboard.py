from turtle import Turtle

POSITION = (0, 280)
FONT_TYPE = "normal"
FONT_SIZE = 10
FONT_NAME = "Arial"
FONT = (FONT_NAME, FONT_SIZE, FONT_TYPE)

with open("data.txt") as file:
    HIGH_SCORE = int(file.read())
    print(HIGH_SCORE)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high = HIGH_SCORE
        self.penup()
        self.goto(POSITION)
        self.hideturtle()

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high}", False, align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align="center", font=FONT)

    def update_high_score(self):
        if self.score > self.high:
            self.high = self.score
            with open("data.txt", mode="w") as file_write:
                file_write.write(str(self.high))
        self.score = 0
        self.display_score()
