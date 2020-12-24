print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

cost = 0

# Ask size; $15 for small, $20 for medium, $25 for large.
if(size == "S"):
  cost = 15
elif(size == "M"):
  cost = 20
else:
  cost = 25

# Ask pepperoni; $2 for small, $3 for M and L.
if(add_pepperoni == "Y"):
  if(size == "S"):
    cost += 2
  else:
    cost += 3

# Ask extra cheese, $1 for all sizes.
if(extra_cheese == "Y"):
  cost += 1

print(f"Your final bill is: ${cost}.")