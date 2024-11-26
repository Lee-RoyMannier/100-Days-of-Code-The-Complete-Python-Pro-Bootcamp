from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True,
                   align="center", font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True,
                   align="center", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER: Score :{self.score}", True,
                   align="center", font=('Arial', 18, 'normal'))
