from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.generate_food()

    def generate_food(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.penup()
        self.goto(x, y)
