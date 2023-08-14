from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

items = Menu()

money_machine = MoneyMachine()

coffee_machine = CoffeeMaker()

while is_on:

    choice = input(f"What would you like? ({items.get_items()}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        if money_machine.profit != 0:
            money_machine.report()

    else:
        drink = items.find_drink(choice)

        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
