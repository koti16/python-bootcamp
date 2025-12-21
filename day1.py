#p1
#add two numbers
'''num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
sum = num1+ num2
print(f"sum:{num1}+{num2}={sum}")'''
#p2:division
'''num1= float(input("enter first number:"))
num2= float(input("enter second number:"))
if num1 == 0:
    print("product doesn't exist")
else:
    div_result= num1/num2
    print(f"division:{num1}/{num2}={div_result}")'''
#p3: area of triangle
'''base= float(input("enter base"))
height = float(input("enter height"))
area = 0.5*base*height
print(F"area:{0.5}*{base}*{height}={area}")'''

#p4: swap two variables 
'''a = float(input("enter a value"))
b= float(input("enter b value"))
#display the original values
print(f"orginal values :a={a},b={b}")
#swap the values using a temp  variable
temp = a
a = b
b = temp
#display  the swapped values
print(f"swapped values: a={a},b={b}")'''
#p5:write a python program to generate a random number.
import random
print(f"Random number :{random.randint(1,100)}")


