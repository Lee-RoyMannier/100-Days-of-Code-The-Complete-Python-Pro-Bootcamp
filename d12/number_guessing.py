from random import randint


def get_difficulty(DIFFICULTY):
    game_diff = input("Choose a difficulty. Easy or Hard ")
    life = DIFFICULTY.get(game_diff)
    return life


def is_correct(guess, answer):
    if guess < answer:
        print("Too low")
        return False
    elif guess > answer:
        print("Too high")
        return False
    else:
        print("GG")
        return True


print("Welcome to the Number Guessing Game !")
DIFFICULTY = {
    "easy": 10,
    "hard": 5,
}
life = get_difficulty(DIFFICULTY)
answer = randint(1, 100)
app_running = True

while app_running:
    print(f"You have {life} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    if not is_correct(guess, answer):
        life -= 1
        if life == 0:
            print(f"You loose, the answer was {answer}")
            app_running = False

    else:
        app_running = False
