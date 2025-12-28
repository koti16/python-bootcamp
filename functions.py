#syntax
#def my_function():
#whlie loop 
# while something_is_true:
#    do this 
#     do this

'''from curses import KEY_OPTIONS


def greet () :
    print("hello ")
    print("hi ra")
    print("bye")

greet ()    
#function that allows for inputs
def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you {name}")
greet_with_name("ravi")    
'''




'''def problem_slove(name  , roll_n0):
    print(f"name:{name}")
    print(f"roll_no: {roll_n0}")
problem_slove("koti", 21)'''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encode, type 'decode' to decode:\n").lower()
shift = int(input("Enter the shift number:\n"))

def encrypt(orignal_text, shift_amount):
    cipher_text = ""
    for letter in orignal_text:
        # Get current position of the letter
        current_position = alphabet.index(letter)
        
        # Calculate new position using modulo (%) to wrap around the alphabet
        new_position = (current_position + shift_amount) % 26
        
        # Add the new letter to the cipher_text string
        cipher_text += alphabet[new_position]
        
    print(f"cipher_text: {cipher_text}") 

# Ensure "koti" is in quotes so it is recognized as a string
encrypt(orignal_text="koti", shift_amount=shift)

def decrpyt(orignal_text, shift_amount):
    plain_text = ""
    for letter in orignal_text:
        # get current postion of the letter
        current_postion = alphabet.index(letter)
        #calcute new postion 
        new_postion = (current_postion-shift_amount)%26

        #add the new letter to thr cipher_text string
        plain_text+=alphabet[new_postion]
    print(f"plain_text:{plain_text}")
decrpyt(orignal_text="ram",shift_amount= shift)        


