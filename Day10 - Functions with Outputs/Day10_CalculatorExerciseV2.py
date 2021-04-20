from os import system

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

in_calculator = True
while in_calculator:

    num1 = int(input("What's the first number?: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:

        operation_choice = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        function = operations[operation_choice]
        result = function(num1,num2)

        print(f"{num1} {operation_choice} {num2} = {result}")

        what_to_do = input(f"Type 'y' to continue calculating with {result}, type 'n' to restart, type anything else to exit: ")

        if what_to_do == 'y':
            num1 = result
        elif what_to_do == 'n':
            should_continue = False
        else:
            should_continue = False
            in_calculator = False