import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def display_auction():
    print(logo)
    print("Welcome to the secret auction program.")


def get_auctions():
    os.system('cls ||clear')

    name = input("What is your name: ")
    bid = int(input("Wh'ts your bid? $"))

    return name, bid


def get_winner(bidders):
    best = sorted(bidders.items(), key=lambda name: name[1], reverse=True)
    return best[0]


def main():
    bidders = {}
    running_app = True

    while running_app:
        name, bid = get_auctions()
        bidders[name] = bid

        continue_bid = input("Are there any other bidders? Yes or No").lower()

        if continue_bid != "yes":
            running_app = False
            winner = get_winner(bidders)
            print(f"The winner is : {winner[0]} with {winner[1]}")


main()
