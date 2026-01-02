print('''____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________''')

name = input("what's the first name:")

def add(n1, n2):
    return n1 + n2

def sub (n1 , n2 ):
    return n1 -n2

def  multi(n1,n2):
    return n1* n2

def  divide (n1 , n2):
    return n1/n2
operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide,
}
n1= int(input("what is the first  number:"))
for symbol in operation:
    print(symbol)
operation_symbol = input("pick an operation:")
n2= input("what is second number:")
answer = operation[operation_symbol](n1, n2 )
print(f"{n1}{operation_symbol}{n2}={answer}")



