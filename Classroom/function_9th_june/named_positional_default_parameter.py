'''Program to demonstrate positional, named and default parameters in python'''
#function to calculate addition
def add(num1, num2=45,num3=0):
    print("Sum of ", num1, ",", num2,"and",num3, "is : ", num1 + num2 + num3)
#--------------------------------------------------------------------
#main program
x = 35
y = 56
#to calculate addition using positional parameters
add(x)
add(y, x)
#to calculate addition using named parameters
add(num2 = y, num1 = x)