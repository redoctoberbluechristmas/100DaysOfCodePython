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

# first_num = int(input("What's the first number?: "))

# Display operations
print("+")
print("-")
print("*")
print("/")

first_num = int(input("What is the first number? "))

keep_calculating = True
while keep_calculating:
  
    operation = input("Pick an operation: ")
    second_num = int(input("What's the next number?: "))

    if operation == "+":
        result = add(first_num, second_num)

    elif operation == "-":
        result = subtract(first_num, second_num)

    elif operation == "*":
        result = multiply(first_num, second_num)

    elif operation == "/":
        result = divide(first_num, second_num)

    print(f"The result is: {result}")

    more_calculation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or press any other key to exit.")
    if more_calculation == 'n':
        first_num = int(input("What is the first number? "))
    elif more_calculation == 'y':
        first_num = result
        print(f"{result} is the first number.")
    else:
        print("Goodbye")
        keep_calculating = False

