# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

continue_auction = ''
bidders_and_bids = {}

while continue_auction != "no":
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: "))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'")
    bidders_and_bids[user_name] = user_bid
    if continue_auction != "no":
        print("\n" * 100)

max_bid = 0
max_bidder = ''
for bidder in bidders_and_bids:
    if bidders_and_bids[bidder] > max_bid:
        max_bid = bidders_and_bids[bidder]
        max_bidder = bidder
print(f"The winner is {max_bidder} with a bid of ${max_bid}")