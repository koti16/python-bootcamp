import random

# Game data for 2026
data = [
    {"name": "MrBeast", "count": 350, "description": "YouTuber"},
    {"name": "Cristiano Ronaldo", "count": 640, "description": "Footballer"},
    {"name": "Selena Gomez", "count": 430, "description": "Musician and Actress"},
    {"name": "Lionel Messi", "count": 505, "description": "Footballer"},
    {"name": "Kylie Jenner", "count": 400, "description": "Reality TV Star"},
    {"name": "Dwayne Johnson", "count": 395, "description": "Actor and Wrestler"},
    {"name": "Ariana Grande", "count": 380, "description": "Musician"},
    {"name": "Taylor Swift", "count": 285, "description": "Musician"}
]

def play_game():
    score = 0
    game_over = False
    # Select the first random item
    item_a = random.choice(data)

    print("--- Welcome to the Higher Lower Game (2026 Edition) ---")

    while not game_over:
        # Select item B, ensuring it isn't the same as item A
        item_b = random.choice(data)
        while item_a == item_b:
            item_b = random.choice(data)

        print(f"\nCompare A: {item_a['name']}, a {item_a['description']}.")
        print(f"Against B: {item_b['name']}, a {item_b['description']}.")
        
        guess = input("Who has more followers? Type 'H' for Higher (B > A) or 'L' for Lower (B < A): ").upper()

        # Determine the correct answer
        # If B is higher than A, the correct guess is 'H'
        is_correct = False
        if guess == 'H' and item_b['count'] > item_a['count']:
            is_correct = True
        elif guess == 'L' and item_b['count'] < item_a['count']:
            is_correct = True

        if is_correct:
            score += 1
            print(f"Correct! {item_b['name']} has {item_b['count']}M followers.")
            print(f"Current score: {score}")
            # Item B becomes the new Item A for the next round
            item_a = item_b
        else:
            print(f"Wrong! {item_b['name']} has {item_b['count']}M followers while {item_a['name']} has {item_a['count']}M.")
            print(f"Game Over. Final score: {score}")
            game_over = True

if __name__ == "__main__":
    play_game()
