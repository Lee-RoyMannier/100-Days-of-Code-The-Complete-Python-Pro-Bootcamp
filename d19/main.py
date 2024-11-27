import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
timmy = Player()
game_is_on = True
board = Scoreboard()
cars = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(timmy.move, "Up")
    cars.create_cars()
    cars.move()

    for car in cars.cars:
        if car.distance(timmy) < 20:
            board.game_ove()
            game_is_on = False

    if timmy.is_finished():
        board.increase_level()
        cars.increase_speed()
        timmy.reset_turtle()


screen.exitonclick()
