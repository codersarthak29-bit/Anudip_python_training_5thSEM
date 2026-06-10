'''
Delivery times (in minutes) for different orders are given below:

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

Requirements:
1. fastest_delivery(times)
   Returns the shortest delivery time.

2. delayed_orders(times)
   Returns a list of orders taking more than 45 minutes.

3. average_delivery_time(times)
   Returns the average delivery time.

4. delivery_category(times)
   Displays order categories:
   • Fast    → ≤ 30 minutes
   • Normal  → 31–45 minutes
   • Delayed → > 45 minutes
'''

# ==========================================================
# Delivery Performance Analyzer
# ==========================================================

# List containing delivery times (in minutes)
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# ----------------------------------------------------------
# Function: fastest_delivery()
# Purpose : Find the shortest delivery time
# ----------------------------------------------------------
def fastest_delivery(times):

    # Return the minimum delivery time
    return min(times)


# ----------------------------------------------------------
# Function: delayed_orders()
# Purpose : Find all deliveries taking more than 45 minutes
# ----------------------------------------------------------
def delayed_orders(times):

    # Create an empty list to store delayed orders
    delayed = []

    # Traverse through all delivery times
    for time in times:

        # Check if delivery time exceeds 45 minutes
        if time > 45:

            # Add delayed order to the list
            delayed.append(time)

    # Return list of delayed orders
    return delayed


# ----------------------------------------------------------
# Function: average_delivery_time()
# Purpose : Calculate average delivery time
# ----------------------------------------------------------
def average_delivery_time(times):

    # Check if the list is empty
    if not times:
        return 0

    # Calculate and return average delivery time
    return sum(times) / len(times)


# ----------------------------------------------------------
# Function: delivery_category()
# Purpose : Categorize deliveries as Fast, Normal, or Delayed
# ----------------------------------------------------------
def delivery_category(times):

    print("\nDelivery Categories:")

    # Traverse through all delivery times
    for i in range(len(times)):

        time = times[i]

        # Categorize delivery based on time taken
        if time <= 30:
            category = "Fast"

        elif time <= 45:
            category = "Normal"

        else:
            category = "Delayed"

        # Display order number, delivery time, and category
        print("Order", i + 1, ":", time, "minutes -", category)


# ==========================================================
# Main Program
# ==========================================================

# Display complete delivery time list
print("Delivery Times :", delivery_time)

# Display fastest delivery time
print("Fastest Delivery Time :", fastest_delivery(delivery_time), "minutes")

# Display delayed orders
print("Delayed Orders (>45 min) :", delayed_orders(delivery_time))

# Display average delivery time
print("Average Delivery Time :", round(average_delivery_time(delivery_time), 2), "minutes")

# Display category of each order
delivery_category(delivery_time)
