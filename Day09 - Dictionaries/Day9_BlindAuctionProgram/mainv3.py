from logo import logo
from os import system
print(logo)


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    #bidding_record passed as parameter. It is a dictionary.
    for bidder in bidding_record:
        #By passing the key, bidder, to dict, we get the value for bid amount.
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # To bids dict, just adding a key of "name" with value of price, so "Kyle": 1, "Junghee": 3 etc.
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        # Once over, time to settle the tab. Passing the dict, bids, as the parameter.
        find_highest_bidder(bids)
    elif should_continue =="yes":
        system('clear')

    