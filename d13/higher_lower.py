from data import datas, logo, vs
from random import choice


def display_info(compare):
    return f"{compare["name"]} a {compare["description"]}, from {compare["country"]}"


def compare(a, b, choice):
    if a["follower_count"] > b["follower_count"]:
        return choice == "a"
    else:
        return choice == "b"


def main():
    app_running = True
    score = 0

    compare_a = choice(datas)

    while app_running:
        print(logo)
        compare_b = choice(datas)

        if compare_a == compare_b:
            compare_b = choice(datas)

        print("Compare A: ", display_info(compare_a))
        print(vs)
        print("Compare B : ", display_info(compare_b))

        user_choice = input("Who has more followers: 'A' or 'B").lower()
        if compare(compare_a, compare_b, user_choice):
            score += 1
            compare_a = compare_b
            print("You're right !, score: ", score)
        else:
            print("LOOSE")
            app_running = False


main()
