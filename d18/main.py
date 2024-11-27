from time import sleep
from turtle import Screen
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
pr = Pad(350, 0)
pf = Pad(-350, 0)
score = Scoreboard()
b = Ball()
screen.onkey(pr.up, "Up")
screen.onkey(pr.down, "Down")
screen.onkey(pf.up, "W")
screen.onkey(pf.down, "S")

game = True


while game:
    sleep(0.1)
    screen.update()
    b.move()

    if b.ycor() >= 390 or b.ycor() <= - 390:
        b.bounce()

    if b.distance(pr) < 50 and b.xcor() > 340 or b.distance(pf) < 50 and b.xcor() < 340:
        b.bounce_x()
        b.incr_speed()

    if b.xcor() > 410:
        score.upleft()
        score.update_score()
        b.ball_init()

    if b.xcor() < -410:
        score.upright()
        score.update_score()
        b.ball_init()


screen.exitonclick()
