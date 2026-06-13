'''Problem Statement: 
Create an Employee class containing employee ID, name, and monthly salary. 
Implement methods to: 
• Display employee details.  
• Calculate annual salary.  
• Increase salary by a given percentage.  '''

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Monthly Salary: ${self.monthly_salary:.2f}")

    def calculate_annual_salary(self):
        print("Annual salary: ",(self.monthly_salary * 12))

    def increase_salary(self, percentage):
        self.monthly_salary += self.monthly_salary * (percentage / 100)
        print("Updated Salary: ",self.monthly_salary)

#-----------------------------------------------------------------
#main program 
#-----------------------------------------------------------------
name =input("Enter student name: ")
if name.isspace() or name.isdigit():
    print("Invalid name. Name cannot be empty or contain only digits.") # This print statement will execute, but the program will continue with the invalid name.
monthly_salary =float(input("Enter your Monthly salary: "))
if monthly_salary <= 0: # Check if salary is non-positive
    print("Invalid salary. Salary cannot be zero or negative.")
emp = Employee(name, monthly_salary)
while True:
    print("=========================================================")
    print("========== Employee Salary Management System ==========")
    print("=========================================================")
    print("1. Display Employee Details")
    print("2. Calculate Annual Salary")
    print("3. Update Salary ")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        emp.display_details()
    elif choice == '2':
        emp.calculate_annual_salary()
    elif choice == '3':
        percentage = float(input("Enter percentage to increase salary by: "))
        if percentage < 0 or percentage > 100:
            print("Percentage cannot be negative or greater than 100.")
        else:
            emp.increase_salary(percentage)
            print("Salary updated successfully!") # The increase_salary method already prints the updated salary.
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")  
