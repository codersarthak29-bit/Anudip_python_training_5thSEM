'''An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report.'''
# ==========================================
# E-COMMERCE INVENTORY & SALES DASHBOARD
# ==========================================

# Dictionary to store all product records
products = {}

# ------------------------------------------
# Input Details Of 30 Products
# ------------------------------------------

for i in range(30):

    print("\nEnter Details Of Product", i + 1)

    # ------------------------------------------
    # Product ID Validation
    # Format: P101
    # Must start with P
    # Last 3 characters must be digits
    # Product ID must be unique
    # ------------------------------------------

    while True:

        pid = input("Enter Product ID : ").upper().strip()

        if pid in products:
            print("Product ID Already Exists")

        elif pid.startswith("P") and len(pid) == 4 and pid[1:].isdigit():
            break

        else:
            print("Invalid Product ID! Example: P101")

    # ------------------------------------------
    # Product Name Validation
    # Remove extra spaces
    # Allow only alphabets and spaces
    # ------------------------------------------

    while True:

        name = " ".join(input("Enter Product Name : ").split()).title()

        if name.replace(" ", "").isalpha():
            break

        print("Product Name Should Contain Alphabets Only")

    # ------------------------------------------
    # Product Price Validation
    # Price must be greater than 0
    # ------------------------------------------

    while True:

        price = input("Enter Product Price : ").strip()

        if not price.isdigit():
            print("Price Must Contain Digits Only")
            continue

        price = int(price)

        if price > 0:
            break

        print("Price Must Be Greater Than Zero")

    # ------------------------------------------
    # Stock Validation
    # Stock cannot be negative
    # ------------------------------------------

    while True:

        stock = input("Enter Available Stock : ").strip()

        if not stock.isdigit():
            print("Stock Must Contain Digits Only")
            continue

        stock = int(stock)

        if stock >= 0:
            break

        print("Stock Cannot Be Negative")

    # ------------------------------------------
    # Sold Quantity Validation
    # Sold quantity cannot be negative
    # ------------------------------------------

    while True:

        sold = input("Enter Sold Quantity : ").strip()

        if not sold.isdigit():
            print("Sold Quantity Must Contain Digits Only")
            continue

        sold = int(sold)

        if sold >= 0:
            break

        print("Sold Quantity Cannot Be Negative")

    # ------------------------------------------
    # Store Product Record In Dictionary
    # ------------------------------------------

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

# ------------------------------------------
# 1. Display All Products
# ------------------------------------------

print("\n========== ALL PRODUCTS ==========")

for pid, data in products.items():

    print(
        f'{pid} -> '
        f'name="{data["name"]}", '
        f'price="{data["price"]}", '
        f'stock="{data["stock"]}", '
        f'sold="{data["sold"]}"'
    )

# ------------------------------------------
# 2. Add New Product
# ------------------------------------------

while True:

    pid = input("\nEnter New Product ID : ").upper().strip()

    if pid in products:
        print("Product ID Already Exists")

    elif pid.startswith("P") and len(pid) == 4 and pid[1:].isdigit():
        break

    else:
        print("Invalid Product ID! Example: P101")

while True:

    name = " ".join(input("Enter Product Name : ").split()).title()

    if name.replace(" ", "").isalpha():
        break

    print("Product Name Should Contain Alphabets Only")

while True:

    price = input("Enter Product Price : ").strip()

    if not price.isdigit():
        print("Price Must Contain Digits Only")
        continue

    price = int(price)

    if price > 0:
        break

    print("Price Must Be Greater Than Zero")

while True:

    stock = input("Enter Product Stock : ").strip()

    if not stock.isdigit():
        print("Stock Must Contain Digits Only")
        continue

    stock = int(stock)

    if stock >= 0:
        break

    print("Stock Cannot Be Negative")

while True:

    sold = input("Enter Sold Quantity : ").strip()

    if not sold.isdigit():
        print("Sold Quantity Must Contain Digits Only")
        continue

    sold = int(sold)

    if sold >= 0:
        break

    print("Sold Quantity Cannot Be Negative")

products[pid] = {
    "name": name,
    "price": price,
    "stock": stock,
    "sold": sold
}

print("Product Added Successfully")

# ------------------------------------------
# 3. Update Stock After Sales
# ------------------------------------------
print(" ===========Update Stock After Sales===========")
pid = input("\nEnter Product ID : ").upper().strip()

if pid in products:

    while True:

        quantity = input("Enter Quantity Sold : ").strip()

        if not quantity.isdigit():
            print("Quantity Must Contain Digits Only")
            continue

        quantity = int(quantity)

        if quantity <= products[pid]["stock"]:
            break

        print("Insufficient Stock")

    products[pid]["stock"] -= quantity
    products[pid]["sold"] += quantity

    print("Stock Updated Successfully")

else:
    print("Product Not Found")
# ------------------------------------------
# 4. Find Out Of Stock Products
# ------------------------------------------

print("\n========== OUT OF STOCK PRODUCTS ==========")

found = False

for pid, data in products.items():

    if data["stock"] == 0:

        print(pid, "->", data["name"])
        found = True

if not found:
    print("No Out Of Stock Products Found")

# ------------------------------------------
# 5. Find Products With Stock Less Than 5
# ------------------------------------------

print("\n========== LOW STOCK PRODUCTS ==========")

found = False

for pid, data in products.items():

    if data["stock"] < 5:

        print(pid, "->", data["name"], "Stock =", data["stock"])
        found = True

if not found:
    print("No Low Stock Products Found")

# ------------------------------------------
# 6. Calculate Total Inventory Value
# Inventory Value = Price × Stock
# ------------------------------------------

inventory_value = 0

for pid in products:

    inventory_value += (
        products[pid]["price"] *
        products[pid]["stock"]
    )

print("\nTotal Inventory Value =", inventory_value)

# ------------------------------------------
# 7. Find Best Selling Product
# ------------------------------------------

for pid in products:

    best_seller = pid
    break

for pid in products:

    if products[pid]["sold"] > products[best_seller]["sold"]:

        best_seller = pid

print("\n========== BEST SELLING PRODUCT ==========")

print(
    best_seller,
    "->",
    products[best_seller]["name"],
    "Sold =",
    products[best_seller]["sold"]
)

# ------------------------------------------
# 8. Find Least Selling Product
# ------------------------------------------

for pid in products:

    least_seller = pid
    break

for pid in products:

    if products[pid]["sold"] < products[least_seller]["sold"]:

        least_seller = pid

print("\n========== LEAST SELLING PRODUCT ==========")

print(
    least_seller,
    "->",
    products[least_seller]["name"],
    "Sold =",
    products[least_seller]["sold"]
)

# ------------------------------------------
# 9. Calculate Total Revenue Generated
# Revenue = Price × Sold Quantity
# ------------------------------------------

total_revenue = 0

for pid in products:

    total_revenue += (
        products[pid]["price"] *
        products[pid]["sold"]
    )

print("\nTotal Revenue Generated =", total_revenue)

# ------------------------------------------
# 10. Generate Low Stock Report
# ------------------------------------------

print("\n========== LOW STOCK REPORT ==========")

found = False

for pid, data in products.items():

    if data["stock"] < 5:

        print(
            pid,
            "->",
            data["name"],
            "| Stock =",
            data["stock"]
        )

        found = True

if not found:
    print("No Low Stock Products")

# ------------------------------------------
# 11. Products Whose Sales Exceed Average Sales
# ------------------------------------------

total_sales = 0

for pid in products:

    total_sales += products[pid]["sold"]

average_sales = total_sales / len(products)

print("\nAverage Sales =", round(average_sales, 2))

print("\n========== PRODUCTS ABOVE AVERAGE SALES ==========")

found = False

for pid, data in products.items():

    if data["sold"] > average_sales:

        print(
            pid,
            "->",
            data["name"],
            "| Sold =",
            data["sold"]
        )

        found = True

if not found:
    print("No Products Above Average Sales")

# ------------------------------------------
# 12. Create Promotion Products Dictionary
# Sales Less Than 10
# ------------------------------------------

promotion_products = {}

for pid, data in products.items():

    if data["sold"] < 10:

        promotion_products[pid] = data

print("\n========== PROMOTION PRODUCTS ==========")

if len(promotion_products) == 0:

    print("No Products Eligible For Promotion")

else:

    for pid, data in promotion_products.items():

        print(
            pid,
            "->",
            data["name"],
            "| Sold =",
            data["sold"]
        )

# ------------------------------------------
# CHALLENGE : COMPLETE BUSINESS REPORT
# ------------------------------------------

print("\n")
print("========================================")
print("         COMPLETE BUSINESS REPORT       ")
print("========================================")

print("Total Products           :", len(products))
print("Inventory Value          :", inventory_value)
print("Total Revenue            :", total_revenue)

print(
    "Best Selling Product     :",
    products[best_seller]["name"]
)

print(
    "Least Selling Product    :",
    products[least_seller]["name"]
)

print(
    "Average Sales            :",
    round(average_sales, 2)
)

low_stock_count = 0

for pid in products:

    if products[pid]["stock"] < 5:

        low_stock_count += 1

print("Low Stock Products       :", low_stock_count)

print(
    "Promotion Products       :",
    len(promotion_products)
)

print("========================================")
print("            REPORT COMPLETED            ")
print("========================================")