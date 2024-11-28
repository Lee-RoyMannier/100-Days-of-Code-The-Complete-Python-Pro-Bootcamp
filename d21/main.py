from turtle import Turtle, Screen, shape, textinput
import pandas as pd

screen = Screen()
screen.title("U.S State Game")
img = "blank_states_img.gif"
screen.addshape(img)
shape(img)
states = pd.read_csv("50_states.csv")
score = 0

for i in range(0, len(states)):
    new_state = textinput(title=f"{score}/{len(states)} States Correct",
                          prompt="What(s another state's name?)")
    if new_state.capitalize() in states.state.to_list():
        score += 1
        state = Turtle()
        state.hideturtle()
        choice = states[states.state == new_state.capitalize()]
        x = choice.x.item()
        y = choice.y.item()
        state.penup()
        state.goto(float(x), float(y))
        state.write(new_state.capitalize())
    else:
        continue

screen.exitonclick()
