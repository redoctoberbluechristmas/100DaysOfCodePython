
import random
from logo import logo

print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
TARGET_NUMBER = random.randint(0, 100)
print(f"Psssst, the correct answer is {TARGET_NUMBER}")
attempts_remaining = 10
if input("Choose a difficult. Type 'easy' or 'hard': ") == 'hard':
    attempts_remaining = 5

def check_guess(user_guess):
    if user_guess > TARGET_NUMBER:
        print("Too high.")
        return attempts_remaining - 1
    elif user_guess < TARGET_NUMBER:
        print("Too low")
        return attempts_remaining - 1
    else:
        print("You guessed the number!")
        return -1


print(f"You have {attempts_remaining} attempts remaining to guess the number.")
guessing = True
while guessing:
    attempts_remaining = check_guess(int(input("Make a guess: ")))
    if attempts_remaining == 0:
        print("Sorry, you somehow lost the game.")
        guessing = True
        break
    elif attempts_remaining == -1:
        print(f"Correct, you have guessed the number!")
        guessing = True
        break
    print(f"You have {attempts_remaining} attempts remaining.")