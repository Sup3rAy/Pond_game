from turtle import Turtle


class ScoreBar(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x, y)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def l_score_up(self):
        self.l_score += 1
        self.clear()
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def r_score_up(self):
        self.r_score += 1
        self.clear()
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
