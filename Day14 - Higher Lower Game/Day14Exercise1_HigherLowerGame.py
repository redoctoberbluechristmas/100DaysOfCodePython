import random
import art
from os import system
from game_data import data


# Need to select two celebrities
def choose_accounts():
    return random.choice(data)

def format_entry(choice):
    return f'{choice["name"]}, a {choice["description"]}, from {choice["country"]}'

def compare_accounts(player_choice, not_choice):
    if player_choice["follower_count"] > not_choice["follower_count"]:
        return -1
    else:
        return 1

score = 0

choice_a = choose_accounts()

# Start Loop Here
correct_choice = True
while correct_choice:
    print(art.logo)
    choice_b = choose_accounts()

    # Make it so you can't compare same things
    while choice_a == choice_b:
        choice_b = choose_accounts()

    print(f"Compare A: {format_entry(choice_a)}")
    print(art.vs)
    print(f"Against B: {format_entry(choice_b)}")

    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if player_choice == 'a':
        player_choice = choice_a
        not_choice = choice_b
    elif player_choice == 'b':
        player_choice = choice_b
        not_choice = choice_a

    system("clear")

    if compare_accounts(player_choice, not_choice) == 1:
        print(f"Sorry, that's wrong. Final score = {score}")
        correct_choice = False
        break
    else:
        score += 1
        print(f"Correct! Your score is {score}")
        choice_a = choice_b