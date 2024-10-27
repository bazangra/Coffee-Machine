from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def process_coins():
    print("Insert coins")
    Quarters = float(input("How many quarters: "))
    Dimes = float(input("How many dimes: "))
    Cents = float(input("How many cents: "))
    Pennies = float(input("How many pennies: "))
    money_inserted = float((0.25 * Quarters) + (0.1 * Dimes) + (0.05 * Cents) + (0.01 * Pennies))
    return money_inserted

cont = True

while cont:
    choice = input(f'What would you like? {menu.get_items()}:' ).lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        cont = False
    elif choice == "espresso":
        if coffee_maker.is_resource_sufficient(choice):
            money_inserted = process_coins()
            if check_coins(choice):
                money += float(MENU[choice]["cost"])
                resources["water"] = resources["water"] - float(MENU[choice]["ingredients"]["water"])
                resources["coffee"] = resources["coffee"] - float(MENU[choice]["ingredients"]["coffee"])
                print(f"Here is your espresso. Enjoy!")
