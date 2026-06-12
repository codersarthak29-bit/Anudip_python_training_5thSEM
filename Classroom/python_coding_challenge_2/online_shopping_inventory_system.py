'''An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
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
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  '''
#program to make Online Shopping Inventory System 
#inventory list:
inventory = { 
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
#task1:Display products with stock below 15 units.
print("Products with stock below 15 units:")
for product,unit in inventory.items():
    if unit<15:
        print(product)
#task2: Find the product with maximum stock.
max_stock_product = max(inventory, key=inventory.get)
print(f"\nProduct with maximum stock:", max_stock_product,"(",max(inventory.values()),"units)")
#tsk3:Find the product with minimum stock.  
min_stock_product = min(inventory,key=inventory.get)
print(f"Product with minimum stock:", min_stock_product,"(",min(inventory.values())," units)")
#task4:Calculate total stock available.
total_stock = sum(inventory.values())
print("\nTotal stock available:", total_stock)
#task5: Create a list of products requiring restocking (<10 units).
restock_products = []
for product, stock in inventory.items():
    if stock < 10:
        restock_products.append(product)
print("\nProducts requiring restocking (below 10 units):", restock_products)

