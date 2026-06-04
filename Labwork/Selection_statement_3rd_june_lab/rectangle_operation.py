#program to area and perimeter of a rectangle
#input of length and breadth
length=int(input("Enter the length of the rectangle: "))
if(length<0):
    exit("Length cannot be negative")
breadth=int(input("Enter the breadth of the rectangle: "))
if(breadth<0):
    exit("Breadth cannot be negative")
print("Area of the rectangle is: ",length*breadth)
print("Perimeter of the rectangle is: ",2*(length+breadth))