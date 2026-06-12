'''Problem Statement 
The prices of products purchased by a customer are stored in a tuple. 
Sample Data 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 
Tasks 
1. Calculate the total bill amount.  
2. Find the most expensive product.  
3. Find the least expensive product.  
4. Count products costing more than ₹1,000.  
5. Create a list of products eligible for discount (price > ₹800).  '''
#program to make Shopping Cart Billing System 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 

# 1. Calculate the total bill amount.
total_bill = sum(prices)
print(f"Total bill amount: ₹{total_bill}")

# 2. Find the most expensive product.
most_expensive = max(prices)
print(f"Most expensive product: ₹{most_expensive}")

# 3. Find the least expensive product.
least_expensive = min(prices)
print(f"Least expensive product: ₹{least_expensive}")

# 4. Count products costing more than ₹1,000.
count_more_than_1000 = 0
for price in prices:
    if price > 1000:
        count_more_than_1000 += 1
print(f"Number of products costing more than ₹1,000: {count_more_than_1000}")

# 5. Create a list of products eligible for discount (price > ₹800).
eligible_for_discount = []
for price in prices:
    if price > 800:
        eligible_for_discount.append(price)
print(f"Products eligible for discount: {eligible_for_discount}")
