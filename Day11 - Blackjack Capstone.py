
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_starting_hands():
    for i in range (2):
        player_hand.append(random.choice(cards))
        #computer_hand.append(random.choice(cards))


def hit():
    player_hand.append(random.choice(cards))

def calculate_score():
    total = 0
    for i in player_hand:
        total += i
    return total

calculate_score()

more_blackjack = True
while more_blackjack:

    # Get starting hands for player and computer.
    player_hand = []
    computer_hand = []

    get_starting_hands()

    print(f"Your starting hand is {player_hand}")
    print(f"The computer's starting hand is {computer_hand}")
    

    # Ask if player will hit or stand:
    playing = True
    
    while playing == True:
        if (input("Please enter 'hit' or 'stand': ")) == 'hit':
            hit()
            print(f"Your hand is {player_hand}")
            calculate_score()
        else:
            playing = False
    

    #Computer's Logic
        # If total of computer hand is less than 17, hit.




    # Logic to keep playing.
    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if keep_playing == 'n':
        more_blackjack = False