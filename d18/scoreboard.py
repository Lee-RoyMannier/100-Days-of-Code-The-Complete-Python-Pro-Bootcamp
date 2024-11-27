from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score : {self.score_l}", True,
                   align="center", font=('Arial', 18, 'normal'))
        self.goto(100, 200)
        self.write(f"Score : {self.score_r}", True,
                   align="center", font=('Arial', 18, 'normal'))

    def upleft(self):
        self.score_l += 1

    def upright(self):
        self.score_r += 1
