# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):” Done
# a. Check the user’s input to decide what to do next. Done
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer. Done
# c. Create a function in order to check if the user's input is right. Done

def check_input_drink(drink, menu):
    """it returns the drink chosen by the user if it exists"""
    if drink == "off":
        return drink
    elif drink == "report":
        return "report"
    elif drink not in menu:
        is_drink_exist = False
        while not is_drink_exist:
            print(f"Sorry but the drink you entered doesn't exist. try it again.")
            drink = input("What would you like? (espresso/latte/cappuccino).")
            if drink in menu or drink == "off" or drink == "report":
                is_drink_exist = True
    return drink

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. Done
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens. Done

# TODO: 3. Print report. Done
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO: 4. Check resources sufficient? Done
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# d. Create a function to handle the user's order

def are_sufficient_resources(drink, menu, resource):
    """it handles the resources"""
    is_enough_resources = False
    match drink:
        case "espresso":
            resource["water"] -= menu[drink]["ingredients"]["water"]
            resource["coffee"] -= menu[drink]["ingredients"]["coffee"]
            if resource["water"] < 0:
                print(f"Sorry there is not enough water")
            if resource["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
            if resource["water"] >= 0 and resource["coffee"] >= 0:
                is_enough_resources = True
            else:
                resource["water"] += menu[drink]["ingredients"]["water"]
                resource["coffee"] += menu[drink]["ingredients"]["coffee"]
        case "latte":
            resource["water"] -= menu[drink]["ingredients"]["water"]
            resource["milk"] -= menu[drink]["ingredients"]["milk"]
            resource["coffee"] -= menu[drink]["ingredients"]["coffee"]
            if resource["water"] < 0:
                print(f"Sorry there is not enough water")
            if resource["milk"] < 0:
                print(f"Sorry there is not enough milk")
            if resource["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
            if resource["water"] >= 0 and resource["milk"] >= 0 and resource["coffee"] >= 0:
                is_enough_resources = True
            else:
                resource["water"] += menu[drink]["ingredients"]["water"]
                resource["milk"] += menu[drink]["ingredients"]["milk"]
                resource["coffee"] += menu[drink]["ingredients"]["coffee"]
        case "cappuccino":
            resource["water"] -= menu[drink]["ingredients"]["water"]
            resource["milk"] -= menu[drink]["ingredients"]["milk"]
            resource["coffee"] -= menu[drink]["ingredients"]["coffee"]
            if resource["water"] < 0:
                print(f"Sorry there is not enough water")
            if resource["milk"] < 0:
                print(f"Sorry there is not enough milk")
            if resource["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
            if resource["water"] >= 0 and resource["milk"] >= 0 and resource["coffee"] >= 0:
                is_enough_resources = True
            else:
                resource["water"] += menu[drink]["ingredients"]["water"]
                resource["milk"] += menu[drink]["ingredients"]["milk"]
                resource["coffee"] += menu[drink]["ingredients"]["coffee"]
    return is_enough_resources

# TODO: 5. Process coins. Done
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

import time
def are_sufficient_coins(drink, menu, resource, profits):
    print("Please insert coins.")
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    are_fake_coins = True
    while are_fake_coins is True:
        try:
            quarters = int(input("how many quarters? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            are_fake_coins = False
        except ValueError:
            are_fake_coins = True
            print(f"Sorry but it seems you entered incorrect values. Try again. (only integers)")
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    change = total_amount - menu[drink]["cost"]
    if change < 0:
        resource["water"] += menu[drink]["ingredients"]["water"]
        resource["coffee"] += menu[drink]["ingredients"]["coffee"]
        if drink != "espresso":
            resource["milk"] += menu[drink]["ingredients"]["milk"]
        print(f"Sorry that: ${round(total_amount, 2)} is not enough money. Money refunded.")
        return False
    else:
        profits += menu[drink]["cost"]
        if "profit" not in resource:
            resource["profit"] = profits
        else:
            resource["profit"] += profits
        print(f"Here is {round(change, 2)} in change.")
        return True

def serves_order(drink):
    for i in range(3, 0, -1):
        print(f"Your drink will be ready in: {i}")
        time.sleep(1)
    return f"Here is your {drink} ☕. Enjoy!"


# TODO: 6. Check transaction successful? Done
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# TODO: Fix some details
# a. give better format to the print resources. Done
# b. add more resilient to fails at the time to add the coins. Done
# c. add two decimals after the point in profits. Done
# d. fix the bug when the user don't put the enough money... NOT discount any resources

# TODO: 7. Make Coffee. Done
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

from menu import MENU, resources, profit

turn_on = True
while turn_on:
    user_drink = input("What would you like? (espresso/latte/cappuccino).")
    drink_chosen = check_input_drink(user_drink, MENU)
    if drink_chosen == "off":
        print(f"turning {drink_chosen}")
        break
    elif drink_chosen == "report":
        report_log = f"report:\nWater: {resources["water"]} ml.\nMilk: {resources["milk"]} ml.\nCoffee: {resources["coffee"]} gr.\n"
        if "profit" in resources:
            report_log += f"Money: ${resources["profit"]} dollars."
        print(report_log)
    else:
        if are_sufficient_resources(drink_chosen, MENU, resources) and are_sufficient_coins(drink_chosen, MENU, resources, profit):
            print(serves_order(drink_chosen))






