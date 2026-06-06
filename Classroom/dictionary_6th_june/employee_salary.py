'''WRITE A PROGRAM THAT CONTAINS THE RECORD OF 10 EMPLOYEES 
,WHERE EMPLOYEE ID IS USED AS KEY AND SALERY IS USED AS A VALUE,
SO FIND OUT 
1.THE TOTAL NUMBER OF EMPOYEE HAVING SALARY>30000,
2.DISPLAY THE LIST OF EMPLOYEES WHOS SALARY IS BELOW 20000'''
# Program to store employee records

employees = {}

# Input records of 10 employees
for i in range(4):
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    
    employees[emp_id] = salary

# Count employees having salary > 30000
count = 0

for emp_id in employees:
    if employees[emp_id] > 30000:
        count += 1

print("\nNumber of employees having salary greater than 30000 =", count)

# Display employees having salary below 20000
print("\nEmployees having salary below 20000:")

for emp_id in employees:
    if employees[emp_id] < 20000:
        print(emp_id)