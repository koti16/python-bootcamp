#p6: km-> miles
'''kilometer = float(input("enter distance in kilometers:"))
#conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371 
miles = kilometer*conversion_factor
print(f"kilometers is equal to {miles} miles")'''
#p7:convert form celsuies to fahrenhit.
#celsius=float(input("Enter themperature in celsius:"))

# conversion formula : fahernheit = (celsius*9/5)+32
'''fahrenheit = (celsius*9/5)+32
print(f"fahrenheit is equal to {celsius} in degree")'''

#python program to display calender 
'''import calendar

year = int(input("enter year:"))
month=int(input("enter month of the year:"))

cal =  calendar.month(year , month)
print(cal)'''

''' to slove quadratic equation '''
'''import math
#-b**2-4*a*c = discriment
#input coefficent 
a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))
#calculate the discriminant
discriment = b**2 - 4*a*c
# check if the discrimant is postive, nigative, or zero 
if discriment > 0:
    #two real and distict roots
    root1 = (-b+math.squrt(discriment)/(2*a))
    root2 = (-b+math.squrt(discriment)/(2*a))
    print(f"root 1 : {root1}")
    print(f"Root 2: {root2}")
elif discriment == 0 :
    # one real root (repeated)
    root = -b/(2*a)
    print(f"root : {root}")
else :
    #complex roots
    real_part=-b/(2*a)
    imaginary_part = math.sqrt(abs(discriment))/2*a
    print(f"Root 1 : {real_part}+{imaginary_part}i")
    print(f"Root 2 : {real_part}-{imaginary_part}i")'''
# swap two varibles without temp variable
'''a = 5
b= 10 
#swapping withot a temporaryvariable 
a,b = b,a

print("after swapping")
print("a=", a)
print("b=", b)'''

# to check if a number is +ve ,-ve, 0
'''num = float(input("enter a number"))
if(num>0):
    print("postive")
elif(num<0):
    print("negitive")
else:
    print("zero")'''

#check even or odd 
num = int(input("enter a number "))
if num%2 == 0:
    print("this is even")
else:
    print("odd")            




