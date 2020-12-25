import random

#Exercise forbid the use of random.choice.

names_string = input("Give me everybody's names, separated by a comma. ")

# split function creates a list, based on supplied separator.
names = names_string.split(", ")

#Exercise forbid the use of random.choice. Otherwise, would have used random.choice(names)

# Need to include -1, because length of list with 3 entries would result in upper limit of 3, 
# or 4 possible choices. Could land on an empty choice. -1 will always bring-up the position of the last item.
random_choice = random.randint(0, (len(names) - 1))
#winner = names[random_choice]

#print(f"{winner} is going to buy the meal today.")
print(f"{names[random_choice]} is going to buy the meal today.")

