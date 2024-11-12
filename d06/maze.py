# URL : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    for i in range(3):
        turn_left()


def loops():
    if front_is_clear() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


def main():
    while not at_goal():
        loops()


main()
