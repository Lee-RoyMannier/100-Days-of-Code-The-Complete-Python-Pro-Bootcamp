from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def is_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.penup()
        self.goto(0, -280)
