#Program to calaculate the electric bill based on the units consumed
#Taking input from the user
units=int(input("Enter the number of units consumed: "))
while units<0:
    print("Please enter a positive number")
    units=int(input("Enter the number of units consumed: "))
#Calculating the bill based on the units consumed
print("Units consumed:",units)
if units<=100:
    bill=units*5
    print("Low consumption! ")
elif units>100 and units<=200:
    bill=100*5+(units-100)*7    
    print("Medium consumption! ")
else:
    bill=100*5+100*7+(units-200)*10
    print("High consumption! ")
print("Your total electricity bill is: Rs.",bill)
