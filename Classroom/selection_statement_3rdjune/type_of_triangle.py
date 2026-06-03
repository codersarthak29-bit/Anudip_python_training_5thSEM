#program to check if three angles can form a triangle
#if yes then find the type of triangle
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
    #acute triangle
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("The angles can form an acute triangle.")
    #right triangle
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("The angles can form a right triangle.")
    #obtuse triangle
    else:
        print("The angles can form an obtuse triangle.")
else:
    print("The angles cannot form a triangle.")