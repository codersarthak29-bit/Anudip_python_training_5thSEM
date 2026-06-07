'''salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary.  '''
# Program to perform various operations on employee salary records

# Dictionary containing employee IDs as keys and salaries as values
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# --------------------------------------------------
# Task 1: Display employees earning above ₹60,000
# --------------------------------------------------
print("Employees earning above ₹60,000:")

# Traversing the dictionary
for emp_id, sal in salary.items():

    # Checking if salary is above ₹60,000
    if sal > 60000:
        print(emp_id, "-", sal)

# --------------------------------------------------
# Task 2: Count employees earning below ₹40,000
# --------------------------------------------------
count = 0

# Checking salary of each employee
for sal in salary.values():

    # Incrementing count if salary is below ₹40,000
    if sal < 40000:
        count += 1

print("\nNumber of employees earning below ₹40,000:", count)

# --------------------------------------------------
# Task 3: Find the highest-paid employee
# --------------------------------------------------

# Assuming the first employee as highest-paid initially
highest_paid = ""
highest_salary = 0

# Traversing the dictionary
for emp_id, sal in salary.items():

    # Updating highest salary and employee ID
    if sal > highest_salary:
        highest_salary = sal
        highest_paid = emp_id

print("\nHighest-Paid Employee:")
print(highest_paid, "-", highest_salary)

# --------------------------------------------------
# Task 4: Create a list of employees eligible
# for bonus (salary > ₹50,000)
# --------------------------------------------------
bonus_employees = []

# Adding eligible employees to the bonus list
for emp_id, sal in salary.items():

    # Checking bonus eligibility
    if sal > 50000:
        bonus_employees.append(emp_id)

print("\nEmployees Eligible for Bonus:")
print(bonus_employees)

# --------------------------------------------------
# Task 5: Calculate the average salary
# --------------------------------------------------
total_salary = 0

# Calculating total salary
for sal in salary.values():
    total_salary += sal

# Calculating average salary
average_salary = total_salary / len(salary)

print("\nAverage Salary:", average_salary)