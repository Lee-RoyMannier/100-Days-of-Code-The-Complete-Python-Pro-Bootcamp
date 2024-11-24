from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

app_running = True
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while app_running:

    user_choice = input(f"Please chooce your coffee: {menu.get_items()}")

    if user_choice == "report":
        money_machine.report()
        coffe_maker.report()
    elif user_choice == "quit":
        app_running = False
    else:
        print("Your choice: ", user_choice)

        coff = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(coff) and money_machine.make_payment(coff.cost):
            coffe_maker.make_coffee(coff)
