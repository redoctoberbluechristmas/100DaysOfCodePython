from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_machine = CoffeeMaker()
my_menu = Menu()
machine_on = True
while machine_on:
    options = my_menu.get_items()
    customer_order = input(f"What would you like? ({options}) ")
    if customer_order == "off":
        print("Turning off.")
        machine_on = False
    elif customer_order == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(customer_order)
        if my_coffee_machine.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_machine.make_coffee(drink)
