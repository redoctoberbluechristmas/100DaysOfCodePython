import random

player_hand = []
dealer_hand = []

def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(somehand):
    # if 11 in somehand and 10 in somehand and len(somehand) == 2:
    if sum(somehand) == 21 and len(somehand == 2):
        print
    
    
    
    return sum(somehand)


for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())


print(calculate_score(player_hand))

print(player_hand)

