print("Welcome to the tip calculator.")
total_bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 * total_bill
number_of_diners = int(input("How many people to split the bill? "))

#formating to get two decimal places when rounded.
individual_share = "{:.2f}".format((total_bill + tip) / number_of_diners)

print(f"Each person should pay: $ {individual_share}")



#Alternate way to resolve individual_share display issue with casting.

# from decimal import Decimal

# print("Welcome to the tip calculator.")
# total_bill = float(input("What is the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 * total_bill
# number_of_diners = int(input("How many people to split the bill? "))

# individual_share = round(Decimal(str((total_bill + tip) / number_of_diners)), 2)

# print(f"Each person should pay: $ {individual_share}")
