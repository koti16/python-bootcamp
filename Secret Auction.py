# Initial Setup
logo = ''  # You can add your logo art here
print(logo)
print("Welcome to the secret auction program.")

bids = {}
continue_bidding = True

# Data Collection Loop
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid in rupees: /-"))

    


    # Save data to dictionary {name: price}
    bids[name] = price

    # Check for additional bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        # Clear the screen for the next bidder (standard trick for console apps)
        print("\n" * 50)

# Function to compare bids and find the winner
def find_highest(bidding_dictionary):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    if winner:
        print(f"The winner is {winner} with a bid of {highest_bid}")
    else:
        print("No bids were placed.")

# Call the function to display the result
find_highest(bids)



