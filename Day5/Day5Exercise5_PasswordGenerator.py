#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy version (letters, numbers, and symbols in fixed order.)

password = ""

for i in range(0, nr_letters):
  password += random.choice(letters)
  #password += letters[random.randint(0, (len(letters) -1))]

for i in range(0, nr_numbers):
  password += random.choice(numbers)
  #password += numbers[random.randint(0, (len(numbers) -1))]

for i in range(0, nr_symbols):
  password += random.choice(symbols)
  #password += symbols[random.randint(0, (len(symbols) -1))]

print(f"Your password is {password}")

# Harder version (order of characters randomized)

password_block = list(password)


print(f"This is the random password list: {password_block}")

random_password = ""
random.shuffle(password_block)

for char in password_block:
  random_password += char

### Tried to use this as well, but it's less elegant###
# random_password = ''.join(random.sample(password_block, len(password_block)))

print(f"This is your randomized password: {random_password}")