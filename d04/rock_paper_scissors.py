from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]

bot_choice = randint(0, len(game_list)-1)

user_choice = input(
    "Entrer votre choix: 0 pour rock - 1 pour paper - 2 Pour scissors")

if not user_choice in ("0", "1", "2"):
    print("ERROR INPUT")
else:
    user_choice = int(user_choice)
    print("BOT : ")
    print(game_list[bot_choice])
    print("USER : ")
    print(game_list[user_choice])
    if user_choice == bot_choice:
        print("DRAW")
    elif (bot_choice == 0 and user_choice == 2):
        print("Bot win")
    elif (user_choice == 0 and bot_choice == 2) or user_choice > bot_choice:
        print("User win")
    else:
        print("Bot win")
