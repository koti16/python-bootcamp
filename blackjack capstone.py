import random
print('''___.   .__                 __         __               __    
\_ |__ |  | _____    ____ |  | __    |__|____    ____ |  | __
 | __ \|  | \__  \ _/ ___\|  |/ /    |  \__  \ _/ ___\|  |/ /
 | \_\ \  |__/ __ \\  \___|    <     |  |/ __ \\  \___|    < 
 |___  /____(____  /\___  >__|_ \/\__|  (____  /\___  >__|_ \
      
     \/          \/     \/     \/\______|    \/     \/     \/''')
import random

# 1. Define all your helper functions first
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) # Fix: correctly replace 11 with 1
    return sum(cards)

def compare(u_score, c_score):
    # (Your comparison logic here...)
    pass 

# 2. Define the main game logic
def play_game():
    user_cards = []
    compter_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        compter_cards.append(deal_card())

    while not is_game_over:
        u_score = calculate_score(user_cards)
        c_score = calculate_score(compter_cards)
        print(f"Your cards: {user_cards}, current score: {u_score}")
        print(f"Computer's first card: {compter_cards[0]}")

        if u_score == 0 or c_score == 0 or u_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while c_score != 0 and c_score < 17:
        compter_cards.append(deal_card())
        c_score = calculate_score(compter_cards)

    print(f"Your final hand: {user_cards}, final score: {u_score}")
    print(f"Computer's final hand: {compter_cards}, final score: {c_score}")
    print(compare(u_score, c_score))

# 3. ACTUALLY START THE GAME
play_game() # This line is mandatory to start the script!
