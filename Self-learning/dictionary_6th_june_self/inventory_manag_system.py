'''inventory = { 
    "Notebook": 45, 
    "Pen": 120, 
    "Pencil": 80, 
    "Eraser": 25, 
    "Marker": 15, 
    "Stapler": 8, 
    "Glue": 12, 
    "Scale": 30, 
    "Folder": 5, 
    "Calculator": 3 
} 
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count. '''
# Program to perform various inventory management operations

# Dictionary containing product names as keys and stock quantities as values
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# --------------------------------------------------
# Task 1: Display products with stock less than 10
# --------------------------------------------------
print("Products with stock less than 10:")

# Traversing the dictionary
for product, stock in inventory.items():
    if stock < 10:
        print(product, "-", stock)

# --------------------------------------------------
# Task 2: Count products having stock more than 50
# --------------------------------------------------
count = 0

# Checking stock of each product
for stock in inventory.values():
    if stock > 50:
        count += 1

print("\nNumber of products having stock more than 50:", count)

# --------------------------------------------------
# Task 3: Find the product with minimum stock
# --------------------------------------------------

# Finding the product having minimum stock
min_product = min(inventory, key=inventory.get)
# dictionary.get() returns the value associated with each key, allowing min() to find the lowest-valued key

print("\nProduct with minimum stock:")
print(min_product, "-", inventory[min_product])

# --------------------------------------------------
# Task 4: Create a list of products that require
# restocking (stock less than 20)
# --------------------------------------------------
restocking_products = []

# Adding products with stock less than 20 to the list
for product, stock in inventory.items():
    if stock < 20:
        restocking_products.append(product)

print("\nProducts requiring restocking:")
print(restocking_products)

# --------------------------------------------------
# Task 5: Calculate the total inventory count
# --------------------------------------------------
total_inventory = 0

# Adding stock of all products
for stock in inventory.values():
    total_inventory += stock

print("\nTotal Inventory Count:", total_inventory)