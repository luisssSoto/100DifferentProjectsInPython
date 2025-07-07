from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

my_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

introduction = f"What would you like? ({my_menu.get_items()}): "
user_answer = input(introduction)
while user_answer != "off":
    if user_answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_drink = my_menu.find_drink(user_answer)
        if user_drink is not None:
            print(f"user's drink: {user_drink.name}, cost: {user_drink.cost}, ingredients: {user_drink.ingredients}")
            if coffee_maker.is_resource_sufficient(user_drink) == True and money_machine.make_payment(user_drink.cost) == True:
                coffee_maker.make_coffee(user_drink)
    user_answer = input(introduction)
if user_answer == "off":
    for i in range(3, 0, -1):
        print("Turning off in:", i)
        time.sleep(1)
    print("Bye!")