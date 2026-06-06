'''Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000.  '''
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
#Task1:Display employees earning above ₹50,000.
print("Employees earning above ₹50,000: ") 
for i in employees:
    if i[1]>50000:
        print(i[0])
#Task2:Find the highest-paid employee.  
most_paid=employees[0][1]
for i in employees:
    if i[1]>most_paid:
        most_paid=i[1]
for i in employees:
    if i[1]==most_paid:
        print("\nHighest-paid employee: ",i[0])
#Task3:Calculate total salary expenditure.  
total=0 
for i in employees:
    total+=i[1]
print("\nThe total salary expenditure: ",total)
#Task4:Count employees earning below ₹40,000.
below_count=0  
print("\nEmployees earning below ₹40,000: ")
for i in employees:
    if i[1]<40000:
        below_count+=1
print(below_count)