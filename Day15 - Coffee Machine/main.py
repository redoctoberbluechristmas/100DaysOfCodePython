def inventory_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_inventory(drink_type):
    for key in MENU[drink_type]["ingredients"]:
        if MENU[drink_type]["ingredients"][key] > resources[key]:
            print(f"Sorry, we're out of {key}.")
            quit()


def count_change():
    quarter_value = int(input("How many quarters?: ")) * 0.25
    dimes_value = int(input("How many dimes?: ")) * 0.10
    nickels_value = int(input("How many nickels?: ")) * 0.05
    pennies_value = int(input("How many pennies?: ")) * 0.01
    total_change = quarter_value + dimes_value + nickels_value + pennies_value
    return total_change


def process_transaction(drink_type, total_change):
    print("Please insert coins.")
    item_cost = MENU[drink_type]["cost"]

    add_to_register = 0
    amount_to_return = 0

    if total_change < item_cost:
        print("Sorry, that's not enough money. Money refunded.")
        exit
    elif total_change > item_cost:
        amount_to_return += (item_cost - total_change) * -1
        print(f"Your change is ${amount_to_return}. Thank you.")
        add_to_register += item_cost
    else:
        add_to_register += item_cost

    # Add money to register.
    resources["money"] += add_to_register

    # Subtract ingredients needed to make coffee.
    for key in MENU[drink_type]["ingredients"]:
        resources[key] -= MENU[drink_type]["ingredients"][key]

    # "Present" coffee to customer.

    print(f"Here is your {drink_type}. Enjoy!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

machine_on = True
while machine_on:

    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_order == "off":
        print("Turning-off.")
        machine_on = False
    elif customer_order == "report":
        inventory_report()
    else:
        check_inventory(customer_order)
        process_transaction(customer_order, count_change())
