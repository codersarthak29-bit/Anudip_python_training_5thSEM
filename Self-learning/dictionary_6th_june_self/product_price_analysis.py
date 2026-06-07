'''prices = { 
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1800, 
    "Monitor": 12000, 
    "Printer": 9000, 
    "Tablet": 28000, 
    "Speaker": 3500, 
    "Webcam": 2500, 
    "Headphones": 4200, 
    "Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products.  '''
# Program to perform various operations on product prices

# Dictionary containing product names as keys and prices as values
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# --------------------------------------------------
# Task 1: Display products costing more than ₹5000
# --------------------------------------------------
print("Products costing more than ₹5000:")

# Traversing the dictionary
for product, price in prices.items():

    # Checking if price is greater than ₹5000
    if price > 5000:
        print(product, "-", price)

# --------------------------------------------------
# Task 2: Count products costing less than ₹3000
# --------------------------------------------------
count = 0

# Checking price of each product
for price in prices.values():

    # Incrementing count if price is less than ₹3000
    if price < 3000:
        count += 1

print("\nNumber of products costing less than ₹3000:", count)

# --------------------------------------------------
# Task 3: Find the most expensive product
# --------------------------------------------------

# Assuming the first product is the most expensive initially
expensive_product = ""
highest_price = 0

# Traversing the dictionary
for product, price in prices.items():

    # Updating highest price and product name
    if price > highest_price:
        highest_price = price
        expensive_product = product

print("\nMost Expensive Product:")
print(expensive_product, "-", highest_price)

# --------------------------------------------------
# Task 4: Create a list of products priced
# between ₹2000 and ₹10000
# --------------------------------------------------
products_2000_10000 = []

# Adding eligible products to the list
for product, price in prices.items():

    # Checking if price lies between ₹2000 and ₹10000
    if 2000 <= price <= 10000:
        products_2000_10000.append(product)

print("\nProducts priced between ₹2000 and ₹10000:")
print(products_2000_10000)

# --------------------------------------------------
# Task 5: Calculate the total value of all products
# --------------------------------------------------
total_value = 0

# Adding prices of all products
for price in prices.values():
    total_value += price

print("\nTotal Value of All Products:", total_value)