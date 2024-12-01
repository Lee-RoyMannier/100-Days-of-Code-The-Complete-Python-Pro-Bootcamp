from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("d17/data.txt", "r") as f:
            self.high_score = int(f.read())
        self.display()

    def display(self):
        self.clear()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} Best: {self.high_score}", True,
                   align="center", font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.display()
