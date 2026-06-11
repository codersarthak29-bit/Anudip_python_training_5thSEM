'''Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price. '''
# Online Shopping Cart Analyzer
# Sample Cart Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
# -----------------------------------------
# Function to calculate total cart value
# -----------------------------------------
def calculate_total(cart):
    total = 0
    for price in cart:
        total += price
    return total
# -----------------------------------------
# Function to find most expensive product
# -----------------------------------------
def find_most_expensive(cart):
    return max(cart)
# -----------------------------------------
# Function to find cheapest product
# -----------------------------------------
def find_cheapest(cart):
    return min(cart)
# -----------------------------------------
# Function to count premium shipping products
# (Price > ₹1000)
# -----------------------------------------
def count_premium_shipping(cart):
    count = 0
    for price in cart:
        if price > 1000:
            count += 1
    return count
# -----------------------------------------
# Function to generate discount list
# (Products above ₹1500)
# -----------------------------------------
def generate_discount_list(cart):
    discount_products = []
    for price in cart:
        if price > 1500:
            discount_products.append(price)
    return discount_products
# -----------------------------------------
# Function to calculate average price
# -----------------------------------------
def calculate_average(cart):
    total = calculate_total(cart)
    average = total / len(cart)
    return average
# -----------------------------------------
# Main Program
# -----------------------------------------
print("ONLINE SHOPPING CART ANALYZER")
print("=" * 40)
print("\nCart Items:")
print(cart)
# Total Cart Value
total_value = calculate_total(cart)
print("\nTotal Cart Value: ₹", total_value)
# Most Expensive Product
costliest = find_most_expensive(cart)
print("Most Expensive Product: ₹", costliest)
# Cheapest Product
cheapest = find_cheapest(cart)
print("Cheapest Product: ₹", cheapest)
# Premium Shipping Count
premium_count = count_premium_shipping(cart)
print("Products Eligible for Premium Shipping:", premium_count)
# Discount List
discount_products = generate_discount_list(cart)
print("Products Eligible for Discount:", discount_products)
# Average Product Price
average_price = calculate_average(cart)
print("Average Product Price: ₹", round(average_price, 2))