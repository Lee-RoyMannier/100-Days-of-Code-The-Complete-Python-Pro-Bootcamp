from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.penup()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_init(self):
        self.goto(0, 0)

    def incr_speed(self):
        self.x_move += 3
        self.y_move += 3
