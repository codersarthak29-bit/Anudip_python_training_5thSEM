'''An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30. '''
# Program to perform various operations on product sales data

# Dictionary containing product names as keys and sales as values
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# --------------------------------------------------
# Task 1: Display products sold more than 20 times
# --------------------------------------------------
print("Products Sold More Than 20 Times:")

# Traversing the dictionary
for product, units in sales.items():

    # Checking if sales are greater than 20
    if units > 20:
        print(product)

# --------------------------------------------------
# Task 2: Find the best-selling product
# --------------------------------------------------

# Assuming the first product has the highest sales initially
best_product = ""
highest_sales = 0

# Traversing the dictionary
for product, units in sales.items():

    # Updating highest sales and product name
    if units > highest_sales:
        highest_sales = units
        best_product = product

print("\nBest Selling Product:", best_product, "(", highest_sales, ")")

# --------------------------------------------------
# Task 3: Find the least-selling product
# --------------------------------------------------

# Assuming the first product's sales as the minimum initially
least_product = list(sales.keys())[0]
least_sales = list(sales.values())[0]

# Traversing the dictionary
for product, units in sales.items():

    # Updating lowest sales and product name
    if units < least_sales:
        least_sales = units
        least_product = product

print("\nLeast Selling Product:", least_product, "(", least_sales, ")")

# --------------------------------------------------
# Task 4: Calculate total products sold
# --------------------------------------------------
total_sales = 0

# Adding sales of all products
for units in sales.values():
    total_sales += units

print("\nTotal Units Sold:", total_sales)

# --------------------------------------------------
# Task 5: Create a list of products requiring
# promotion (sales < 15)
# --------------------------------------------------
promotion_products = []

# Adding products with sales less than 15
for product, units in sales.items():

    # Checking promotion requirement
    if units < 15:
        promotion_products.append(product)

print("\nProducts Requiring Promotion:")
print(promotion_products)

# --------------------------------------------------
# Task 6: Count products having sales between
# 10 and 30
# --------------------------------------------------
count = 0

# Checking sales of each product
for units in sales.values():

    # Incrementing count if sales lie between 10 and 30
    if 10 <= units <= 30:
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)

'''
OUTPUT:
Products Sold More Than 20 Times:
Mouse
Keyboard
Headphones
Router

Best Selling Product: Mouse ( 45 )

Least Selling Product: Printer ( 8 )

Total Units Sold: 213

Products Requiring Promotion:
['Monitor', 'Printer', 'Tablet']'''
