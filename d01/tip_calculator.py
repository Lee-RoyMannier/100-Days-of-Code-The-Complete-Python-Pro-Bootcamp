def display_welcoming():
    print("Welcome to the tip calculator!")


def get_tip(bill, percentage, people):
    return (bill/people) + (bill/people)*(percentage/100)


def main():
    display_welcoming()
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much ? 10 / 12 / 15"))
    split = int(input("How many people ?"))

    tip_per_person = get_tip(bill, tip, split)

    print(f"each person should pay: ${round(tip_per_person, 2)}")


main()
