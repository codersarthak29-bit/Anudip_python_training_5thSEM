#program to calculate the area and perimeter of a triangle
#input of three sides
print("----------------------------------------------------------------------------------")
print("Enter the sides of the triangle:")
side1=int(input("Enter first side (in cm): "))
side2=int(input("Enter second side (in cm): "))
side3=int(input("Enter third side (in cm): "))
print("----------------------------------------------------------------------------------")
print("first side: ",side1,"cm")
print("second side: ",side2,"cm")
print("third side: ",side3,"cm")
#calculating the perimeter
perimeter=side1+side2+side3
s=perimeter/2
#printing the area and perimeter
print("The area of the triangle is: ",(s*(s-side1)*(s-side2)*(s-side3))**0.5,"cm^2")
print("The perimeter of the triangle is: ",perimeter,"cm")
