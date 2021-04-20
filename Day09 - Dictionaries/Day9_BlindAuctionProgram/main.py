from loggingfunction import log_bids
from logo import logo
from os import system

end_auction = False

print(logo)
print("Welcome to the secret auction program.")
top_bidder = ""
top_bid = 0
while not end_auction:

    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What's your bid?: "))

    if bidder_amount > top_bid:
        top_bidder = bidder_name
        top_bid = bidder_amount

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders != 'yes':
        end_auction = True
        print("Goodbye.")
        print(f"{top_bidder} won the auction with a bid of {top_bid}")

    else:
        system('clear')