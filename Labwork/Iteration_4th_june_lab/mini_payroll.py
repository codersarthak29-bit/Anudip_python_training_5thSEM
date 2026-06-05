# Mini employee payroll system

name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))

# calaculate HRA (20% of salary) and DA (10% of salary) and  PF (12% of salary

hra = 0.20 * salary
da = 0.10 * salary  
pf = 0.12 * salary

# calculate gross salary
gross_salary = salary + hra + da 

# calculate net salary  
net_salary = gross_salary - pf

print("/n Employee Name:", name)
print("Basic Salary:", salary)
print("HRA:", hra)  
print("DA:", da)
print("PF:", pf)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)    

if net_salary > 50000:
    print("senior employee.")
elif net_salary > 30000:
    print("mid-level employee.")
else:
    print("junior employee.")