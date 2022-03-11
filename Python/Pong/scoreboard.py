from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 190)
        self.write(f"{self.left_score}", align="center", font=("Arial", 60, "normal"))
        self.goto(100, 190)
        self.write(f"{self.right_score}", align="center", font=("Arial", 60, "normal"))
