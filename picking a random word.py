#randomly choose a word for given list
''''import random
word_list= ["koti","navaneeth","ravi"]
#random.chioce function
choosen_word = random.choice(word_list)
print(choosen_word)
#  ask the user to assign their answer to a variable called guess. Make guess lowercase.
guess=(input("guess a letter:")).lower()
print(guess)
#check if the letter the user guessed is one  of the letters in the chosen_words.print "right"if the it is,"wrong" if it id not.
for letter in choosen_word:
    if letter == guess:
        print("right")
    else:
        print("worng")    '''


#Replacing Blanks with guesses
import random
word_list = ["luffy","nami","zoro"]
chosen_word = random.choice(word_list)
#Create a "placeholder with the same number of blanks as the chosen_word"
placeholder=""
for postions in range(1,5):
    placeholder+="_"
guess = input("guess a letter:").lower()
#display
display = ""
for letter in chosen_word:
    if letter== guess:
        display += letter
    else:    
        display+="-"





