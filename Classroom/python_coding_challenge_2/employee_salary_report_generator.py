'''Problem Statement 
Employee details are stored in a text file named employees.txt. 
Sample Input/Data (employees.txt) 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Tasks 
1. Display employees earning more than ₹50,000.  
2. Find the highest-paid employee.  
3. Find the lowest-paid employee.  
4. Calculate the average salary.  
5. Generate salary categories:  
o High (≥ ₹60,000)  
o Medium (₹40,000 – ₹59,999)  
o Low (< ₹40,000)  '''
employees = []

with open("employees.txt", "r") as file:
    for line in file:
        emp_id, name, salary = line.strip().split(",")
        employees.append((emp_id, name, int(salary)))

# Employees earning above ₹50,000
print("Employees Earning Above ₹50,000:")
for emp in employees:
    if emp[2] > 50000:
        print(emp[1])

# Highest-paid employee
highest = employees[0]
for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Paid Employee:")
print(f"{highest[1]} (₹{highest[2]:,})")

# Lowest-paid employee
lowest = employees[0]
for emp in employees:
    if emp[2] < lowest[2]:
        lowest = emp

print("\nLowest Paid Employee:")
print(f"{lowest[1]} (₹{lowest[2]:,})")

# Average salary
total_salary = 0
for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / len(employees)

print("\nAverage Salary: ₹{:,.0f}".format(average_salary))

# Salary categories
high = []
medium = []
low = []

for emp in employees:
    if emp[2] >= 60000:
        high.append(emp[1])
    elif emp[2] >= 40000:
        medium.append(emp[1])
    else:
        low.append(emp[1])

print("\nHigh Salary:")
print(high)

print("\nMedium Salary:")
print(medium)

print("\nLow Salary:")
print(low)