'''An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
#Task 1: Display all products costing more than ₹1000. 
print("All products costing more than ₹1000: ") 
for i in orders:
    if i[1]>1000:
        print(i[0])
#Task2: Find the most expensive product.
expencive=orders[0][1]
for i in orders:
    if i[1]>expencive:
        expencive=i[1]
for i in orders:
    if i[1]==expencive:
        print("\nMost expensive product: ",i[0])
#Task 3:Calculate the total order value. 
total=0 
for i in orders:
    total+=i[1]
print("\nThe total order value: ",total)
#task 4: Count products costing below ₹1000. 
print("\nProducts costing below ₹1000: ")
for i in orders:
    if i[1]<1000:
        print(i[0])