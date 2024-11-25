from turtle import Turtle, Screen
from random import randint


class TurtleRace(Turtle):
    def __init__(self, color, x, y):
        super().__init__()  # Initialize the Turtle class
        self.color(color)  # Set the turtle's color
        self.shape("turtle")  # Set the shape of the turtle
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(x, y)  # Move the turtle to the specified position


turtles = []
race = True
colors = ["red", "yellow", "green", "black", "purple", "pink"]
y_pos = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(500, 400)
user_choice = screen.textinput("turtleVictory", "enter the color of ur turtle")

for turtle_index in range(6):
    tim = TurtleRace(colors[turtle_index], -230, y_pos[turtle_index])
    turtles.append(tim)

while race:
    for t in turtles:
        t.forward(randint(3, 13))
        if t.xcor() >= 230:
            race = False
            if t.pencolor() == user_choice:
                print("YOU WIN")
            else:
                print(f"SORRY YOU LOOSE the turtle {t.pencolor()} win")

screen.exitonclick()
