'''Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes) '''
#program to make  Food Delivery Performance Dashboard 
#delivery times :
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
#task1:Find the fastest delivery time.
fastest_delivery_time = min(delivery_times)
#task2: Find the slowest delivery time.
slowest_delivery_time = max(delivery_times)
#task3: Calculate the average delivery time.
average_delivery_time = sum(delivery_times) / len(delivery_times)
#task4:Display delayed orders (>45 minutes). 
delayed_orders = [time for time in delivery_times if time > 45]
#task5: Categorize deliveries:
fastest = 0
normal = 0
slowest = 0

for time in delivery_times:
    if time<=30:
        fastest+=1
    elif time >= 31 and time <= 45:
        normal+=1
    else:
        slowest+=1

print("Fastest Delivery Time:", fastest_delivery_time)
print("Slowest Delivery Time:", slowest_delivery_time)
print("Average Delivery Time:", average_delivery_time)
print("Delayed Orders (>45 minutes):", delayed_orders)
print("Fast Deliveries (<=30 minutes):", fastest)
print("Normal Deliveries (31-45 minutes):", normal)
print("Delayed Deliveries (>45 minutes):", slowest)
