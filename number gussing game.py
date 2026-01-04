import random

print('''                                    .__                                     ___.                  
   ____  __ __   ____   ______ _____|__| ____    ____     ____  __ __  _____\_ |__   ___________  
  / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\   /    \|  |  \/     \| __ \_/ __ \_  __ \ 
 / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \___  /|____/  \___  >____  >____  >__|___|  /\___  /  |___|  /____/|__|_|  /___  /\___  >__|    
/_____/             \/     \/     \/        \//_____/        \/            \/    \/     \/        ''')
print("Wecome  to  the number guessing Game!")
print("choose Level:")
print("1.Easy(10 attempts)")
print("2.Hard(5 attempts)")

#step-1: take input for the user
level = int(input("enter your choice ?type '1' for easy or '2' for hard"))
#step-2: take secret number input for random modluw
secret_number= random.randint(1 ,100)
#step-3: select the level  and print the level.
if level == 1 :
    attempts = 10 
    print("Easy level selected")
elif level == 2 :
    attempts = 5
    print("hard level selected")
#step-4:take while loop for attempts bez chioces are not fixed
while attempts > 0 :
    guess = int(input("enter your guess: "))
    attempts-=1
#step-5:attempts left after user input 
    if guess > secret_number:
        print("Too low ")
    elif  guess < secret_number:
        print("to high")
    else:
        print("you win the game")
        break
    print("Attempts left : ", attempts)
#step-6:print secret number 
    if attempts == 0:
        print("game over")
        print(f"the correct number was : {secret_number}")

