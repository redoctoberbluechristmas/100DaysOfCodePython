from loggingfunction import log_bids
from logo import logo
from os import system

end_auction = False

print(logo)
print("Welcome to the secret auction program.")
log_name = bidslog = []
top_bidder = ""
top_bid = 0
while not end_auction:
    # top_bidder = ""
    # top_bid = 0
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What's your bid?: "))
    
    # def log_bids(name_of_bidder, amount_of_bid, log_name):
    
    #     new_bid_log_entry = {}
    #     new_bid_log_entry["bidder name"] = bidder_name,
    #     new_bid_log_entry["bid amount"] = bidder_amount
    #     bidslog.append(new_bid_log_entry)

    if bidder_amount > top_bid:
        top_bidder = bidder_name
        top_bid = bidder_amount

    log_bids(bidder_name, bidder_amount, log_name)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders != 'yes':
        end_auction = True
        print("Goodbye.")
        print(f"{top_bidder} won the auction with a bid of {top_bid}")
        print(f"Here is the logging:\n{bidslog}")
    else:
        system('clear')