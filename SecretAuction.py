from replit import clear

from art import logo_secret_auction as logo

print(logo)
print("Welcome to the secret auction program.")

bidding_finished = True

client = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finished:    
    name = input("What is your name?: ").lower()
    bid = int(input("What's your bid?: "))
    client[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = False
        find_highest_bidder(client)
    elif should_continue == "yes":
        clear()

