from turtle import Turtle


class Pad(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def up(self):
        ycor = self.ycor() + 30
        self.goto(self.xcor(), ycor)

    def down(self):
        ycor = self.ycor() - 30
        self.goto(self.xcor(), ycor)
