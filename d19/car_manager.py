from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed_car = STARTING_MOVE_DISTANCE

    def create_cars(self):
        counter_cars = randint(1, 6)
        if counter_cars == 1:
            car = Turtle("square")
            car.shapesize(1, 4)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300, randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.backward(self.speed_car)

    def increase_speed(self):
        self.speed_car += MOVE_INCREMENT
