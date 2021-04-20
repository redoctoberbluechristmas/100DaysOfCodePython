import random
from os import system

def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(somehand):
    # if 11 in somehand and 10 in somehand and len(somehand) == 2:
    if sum(somehand) == 21 and len(somehand) == 2:
        return 0
    if sum(somehand) > 21 and 11 in somehand:
        somehand.remove(11)
        somehand.append(1)
    
    return sum(somehand)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw, dealer wins."
    elif dealer_score == 0:
        return "Dealer has blackjack, dealer wins."
    elif user_score == 0:
        return "Player has blackjack, player wins."
    elif user_score > 21:
        return "Player busts, loses."
    elif dealer_score > 21:
        return "Dealer busts, player wins."
    elif user_score > dealer_score:
        return "Player wins."
    else:
        return "Dealer wins."


# player_score = calculate_score(player_hand)
# dealer_score = calculate_score(dealer_hand)

def play_game():
    system("clear")
    player_hand = []
    dealer_hand = []
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())


    # Get the player's hand
    while not is_game_over:

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(player_score)
        print(dealer_score)


        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Would you like to draw another card?: ")
            if user_should_deal == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True

    # Get the dealer's hand
    while dealer_score < 17 and dealer_score != 0:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(compare(player_score, dealer_score))
while input("Do you want to play a game of Blackjack? Type 'y or 'n' ") == 'y':
    play_game()