'''Problem Statement 
Daily sales figures (in ₹) for 10 days are stored in a list. 
Sample Data 
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000] 
Tasks 
1. Find the highest sales.  
2. Find the lowest sales.  
3. Calculate average sales.  
4. Count days with sales above ₹20,000.  
5. Display sales figures below average. '''
# Daily sales figures
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# Highest sales
highest_sales = max(sales)

# Lowest sales
lowest_sales = min(sales)

# Average sales
average_sales = sum(sales) / len(sales)

# Count days with sales above ₹20,000
count_above_20000 = 0
for amount in sales:
    if amount > 20000:
        count_above_20000 += 1

# Display sales figures below average
below_average = []
for amount in sales:
    if amount < average_sales:
        below_average.append(amount)

# Output
print("Highest Sales: ₹", highest_sales)
print("Lowest Sales: ₹", lowest_sales)
print("Average Sales: ₹", average_sales)
print("Days with Sales Above ₹20,000:", count_above_20000)

print("Sales Figures Below Average:")
for amount in below_average:
    print("₹", amount)