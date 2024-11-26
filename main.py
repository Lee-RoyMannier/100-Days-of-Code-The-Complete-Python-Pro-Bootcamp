from turtle import Turtle, Screen
import random

colors = ["blue", "red", "yellow", "green", "black", "pink"]
square = Turtle()
square.speed("fastest")
for i in range(int(360/5)):
    square.color(random.choice(colors))
    square.circle(50)
    square.setheading(square.heading() + 5)


screen = Screen()
screen.exitonclick()
