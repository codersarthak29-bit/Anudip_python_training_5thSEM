#program to chech if entered 3 sides can form a triangle or not
a = int(input("Enter the first side of triangle: "))
if(a<=0):
    exit("Invalid input! Side of a triangle cannot be zero or negative.")
b = int(input("Enter the second side of triangle: "))
if(b<=0):
    exit("Invalid input! Side of a triangle cannot be zero or negative.")
c = int(input("Enter the third side of triangle: "))
if(c<=0):
    exit("Invalid input! Side of a triangle cannot be zero or negative.")
if(a+b>c and a+c>b and b+c>a):  
    if(a==b and b==c):
        print("The given sides can form an equilateral triangle.")
    elif(a==b or b==c or a==c):
         print("The given sides can form an isosceles triangle.")
    else:
        print("The given sides can form a scalene triangle.")
else:
    print("No, the given sides cannot form a triangle.")
