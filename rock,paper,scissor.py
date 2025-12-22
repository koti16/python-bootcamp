import random
paper=('''           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   ''')
scissors = ('''
  .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/''')

rock = ('''         ___________    ____
    ______/   \__//   \__/____\
  _/   \_/  :           //____\\
 /|      :  :  ..      /        \
| |     ::     ::      \        /
| |     :|     ||     \ \______/
| |     ||     ||      |\  /  |
 \|     ||     ||      |   / | \
  |     ||     ||      |  / /_\ \
  | ___ || ___ ||      | /  /    \
   \_-_/  \_-_/ | ____ |/__/      \
                _\_--_/    \      /
               /____             /
              /     \           /
              \______\_________/''')

game_images = [rock,paper,scissors]
user_chioce = int(input("0 for scissors, 1 for paper 2 for rock"))
if user_chioce>= 0 and user_chioce <=2:
    print(game_images[user_chioce])
compter_chioce = random.randint(0,2)
print(f"compter chioce:{compter_chioce}")

if compter_chioce ==2 and user_chioce == 0:
    print("you win !")
elif compter_chioce ==0 and user_chioce == 2:
    print("you losse!")     
elif   compter_chioce > user_chioce:
    print("you loose!")
elif compter_chioce==  user_chioce:
    print("it's a drew") 
elif user_chioce >= 3 or user_chioce<0:
    print("invaild. you lose")    



