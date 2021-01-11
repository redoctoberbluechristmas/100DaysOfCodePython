
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(somehand):
    somehand.append(random.choice(cards))

# def calculate_score(somehand):
#     total = 0
#     for i in somehand:
#         total += i
#     return total

# Can make calculate_score more simple with sum function:

def calculate_score(somehand):
    return sum(somehand)


def get_starting_hands():
    for i in range (2):
        deal_card(player_hand)
        deal_card(computer_hand)

more_blackjack = True
while more_blackjack:

    player_hand = []
    computer_hand = []

    get_starting_hands()

    player_continue = True
    while player_continue:
        print(f"Your hand is {player_hand}")
        if input("Press 'hit' or 'stand' ") == 'hit':
            deal_card(player_hand)
            player_total = calculate_score(player_hand)
            if player_total > 21:
                print(f"You busted with a score of {player_total}, you lose.")
                player_continue = False
        else:
            print("Player stands.")
            player_continue = False

    player_total = calculate_score(player_hand)   
    computer_total = calculate_score(computer_hand)

    player_total = 21

    print(f"Before loop player total is: {player_total}")
    print(f"Before loop computer total is: {computer_total}")
    while player_total <= 21 and computer_total < 21 and computer_total < player_total:
        print("Shapoopy")
        print("deal_card(computer_hand)")
        computer_total += calculate_score(computer_hand)
        print(f"Inside loop {computer_total}")

    print(f"Your total is {player_total}")
    print(f"Dealer total is {computer_total}")

    if computer_total == 21:
        print("Dealer blackjack, you lose.")
    elif computer_total == player_total:
        print("Tie, dealer wins.")
    elif computer_total > 21:
        print("Dealer busted, you win.")
    elif computer_total > player_total:
        print(f"Dealer score is {computer_total}, your score is {player_total}. You lose.")

    # while computer_total < 21 and computer_total < player_total:
    #     deal_card(computer_hand)
    #     if computer_total == 21:
    #         print("Dealer blackjack, you lose.")
    #     elif computer_total > 21:
    #         print("Dealer bust, you lose.")


    # Logic to keep playing.
    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if keep_playing == 'n':
        more_blackjack = False