from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.display()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.display()

    def display(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"LEVEL: {self.level} ", True,  align="center", font=FONT)

    def game_ove(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER ", True, align="center", font=FONT)
