print("Welcome to python Pizza Deliveries!")
size =input("what size of pizza do you want? S,M or L: ")
pepperoni=input("Do you went pepperoni on pizza? Y or N:")
extra_cheese = input("Do you went extra cheese? Y or N :")
# todo: work out how much they need to pay based on their size choice.
bill=0
if size == "s":
    bill += 120
elif size =="M":
    bill +=140
elif size== "L":
    bill += 160
else:
    print("size is not there")
# todo : work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    bill+= 10
elif pepperoni == "N" :
    bill+=0
#todo : work out their final amount based on whether if they want etra cheese.
if extra_cheese =="y":
    bill+= 5
elif extra_cheese == "N":
    bill+= 0
#final bill
print(f"Your final bill is :${bill}")

         
