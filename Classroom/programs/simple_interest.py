#program to calculate the simple interest
#input of principal amount, rate of interest and time
principal=int(input("Enter the principal amount: "))
if(principal<0):
    exit("Principal amount cannot be negative")
rate=int(input("Enter the rate of interest: "))
if(rate<0):
    exit("Rate of interest cannot be negative")
time=int(input("Enter the time: "))
if(time<0):
    exit("Time cannot be negative")
print("Simple interest is: ",(principal*rate*time)/100)