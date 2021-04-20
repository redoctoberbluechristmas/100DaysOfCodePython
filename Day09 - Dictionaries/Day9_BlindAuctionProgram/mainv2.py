
# This is vastly more complicated than the first solution, but we had to use a dictionary.

from logo import logo
from os import system

end_auction = False

print(logo)
print("Welcome to the secret auction program.")

bid_log_dict = {}
bid_log_dict["bidders"] = []
bid_log_dict["bid amounts"] = []

while not end_auction:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $ "))
    
    def log_bids(name_of_bidder, amount_of_bid):
            bid_log_dict["bidders"].append(name_of_bidder)
            bid_log_dict["bid amounts"].append(amount_of_bid)

    log_bids(name, amount)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders != 'yes':

        bid_amounts_list = bid_log_dict["bid amounts"]
        top_bid = max(bid_amounts_list)
        max_bid_index = bid_amounts_list.index(top_bid)
        top_bidder = bid_log_dict["bidders"][max_bid_index]

        print(f"The top bidder is {top_bidder} with a top bid of {top_bid}.")
        
        end_auction = True
        print("Goodbye.")
        # print(f"Here is the logging:\n{bidslog}")
    else:
        system('clear')