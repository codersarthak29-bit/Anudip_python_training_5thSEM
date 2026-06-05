# Electricity Bill Simulator

units = int(input("Enter the number of units consumed: ")) #input from user to specify the number of units consumed, taken as an integer for calculation

if units <= 100 :
    bill = units*5 #if the units consumed are less than or equal to 100, the bill is calculated at a rate of Rs. 5 per unit
elif units <= 200 :
    bill = 100*5 + (units-100)*7 #if the units consumed are greater than 100 and less than or equal to 200, the bill is calculated at a rate of Rs. 5 per unit for the first 100 units and Rs. 7 per unit for the remaining units
elif units > 200 :
    bill = 100*5 + 100*7 + (units-200)*10 #if the units consumed are greater than 200, the bill is calculated at a rate of Rs. 5 per unit for the first 100 units, Rs. 7 per unit for the next 100 units and Rs. 10 per unit for the remaining units

print("The total electricity bill is: Rs.", bill)

if bill > 5000 : #if the total bill exceeds Rs. 5000, a surcharge of 10% is applied to the bill
    print("You have to pay a surcharge of 10% on the bill.")
    bill = bill + (bill*0.10)
    print("This bill includes a surcharge of 10% as the total bill exceeds Rs. 5000.")
    print("The total electricity bill is: Rs.", bill)
else:
    print("The total electricity bill is: Rs.", bill)