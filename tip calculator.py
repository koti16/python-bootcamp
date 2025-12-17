print("Welcome to the tip calculator!")
total_bill = float(input("whatm is total bill? rupees"))
tip = int(input("what is the tip ?10,20, or 30?"))
people = int(input("how many people to split the billl?"))
bill_with_tip=tip+total_bill/people
print(bill_with_tip)