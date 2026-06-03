#program to check if three angles can form a triangle
angle1 = float(input("Enter the first angle: "))
if angle1 <= 0 or angle1 >= 180:
    exit("Invalid angle. Please enter an angle between 0 and 180 degrees.")

angle2 = float(input("Enter the second angle: "))
if angle2 <= 0 or angle2 >= 180:
    exit("Invalid angle. Please enter an angle between 0 and 180 degrees.")

angle3 = float(input("Enter the third angle: "))
if angle3 <= 0 or angle3 >= 180:
    exit("Invalid angle. Please enter an angle between 0 and 180 degrees.")

# Check if the angles can form a triangle
if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")