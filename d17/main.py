from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
game_one = True


snake = Snake()
food = Food()
sb = Scoreboard()

while game_one:
    screen.update()
    sleep(0.1)
    snake.move()
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)

    if snake.segments[0].distance(food) <= 15:
        sb.increase_score()
        food.generate_food()
        snake.extend_segment()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        sb.game_over()
        game_one = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            sb.game_over()
            game_one = False

screen.exitonclick()
