'''Design a Python program to calculate the area of a triangle using Heron's Formula. The program should 
accept the lengths of the three sides of the triangle from the user and display the calculated area. 
However, the program must handle the following exceptional situations gracefully: 
1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error 
message.  
2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be 
greater than zero.  
3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality 
Theorem, notify the user that the triangle is invalid.  
4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful 
feedback using exception handling.  
5. Display a message indicating that the triangle area calculation process has been completed, 
regardless of whether the calculation was successful or an exception occurred.  
Note: Use Heron's Formula to calculate the area of the triangle: 
�
�=𝑎+𝑏+𝑐
2 
Area=√𝑠(𝑠−𝑎)(𝑠−𝑏)(𝑠−𝑐) 
 
Sample Scenario: 
A construction engineer is using an application to estimate the amount of material required for a triangular 
plot of land. Incorrect measurements or invalid data entry should not cause the application to crash; 
instead, it should guide the user by displaying appropriate error messages and allowing them to understand 
the issue with the provided inputs. '''
try:
    # Input sides of triangle
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    # Check for positive values
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be greater than zero.")
    # Check Triangle Inequality Theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Invalid triangle! The given sides cannot form a triangle.")
    # Heron's Formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    print(f"Area of the triangle = {area:.2f}")

except ValueError as e:
    print("Error:", e)

except Exception:
    print("Error: Please enter valid numeric values.")

