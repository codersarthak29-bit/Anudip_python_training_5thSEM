'''passengers = { 
    "Stop1": 12, 
    "Stop2": 25, 
    "Stop3": 18, 
    "Stop4": 32, 
    "Stop5": 9, 
    "Stop6": 28, 
    "Stop7": 14, 
    "Stop8": 7, 
    "Stop9": 21, 
    "Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers.  '''
# Program to perform various operations on bus stop passenger data

# Dictionary containing stop names as keys and passenger counts as values
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# --------------------------------------------------
# Task 1: Display stops having more than 20 passengers
# --------------------------------------------------
print("Stops having more than 20 passengers:")

# Traversing the dictionary
for stop, count in passengers.items():

    # Checking if passenger count is greater than 20
    if count > 20:
        print(stop, "-", count)

# --------------------------------------------------
# Task 2: Count stops with fewer than 10 passengers
# --------------------------------------------------
low_passenger_stops = 0

# Checking passenger count at each stop
for count in passengers.values():

    # Incrementing count if passengers are fewer than 10
    if count < 10:
        low_passenger_stops += 1

print("\nNumber of stops with fewer than 10 passengers:", low_passenger_stops)

# --------------------------------------------------
# Task 3: Find the busiest stop
# --------------------------------------------------

# Assuming the first stop is the busiest initially
busiest_stop = ""
max_passengers = 0

# Traversing the dictionary
for stop, count in passengers.items():

    # Updating busiest stop if a higher passenger count is found
    if count > max_passengers:
        max_passengers = count
        busiest_stop = stop

print("\nBusiest Stop:")
print(busiest_stop, "-", max_passengers)

# --------------------------------------------------
# Task 4: Create a list of stops requiring an extra bus
# (passengers > 25)
# --------------------------------------------------
extra_bus_stops = []

# Adding eligible stops to the list
for stop, count in passengers.items():

    # Checking if passenger count is greater than 25
    if count > 25:
        extra_bus_stops.append(stop)

print("\nStops Requiring an Extra Bus:")
print(extra_bus_stops)

# --------------------------------------------------
# Task 5: Calculate the average number of passengers
# --------------------------------------------------
total_passengers = 0

# Calculating total passengers
for count in passengers.values():
    total_passengers += count

# Calculating average passengers
average_passengers = total_passengers / len(passengers)

print("\nAverage Number of Passengers:", average_passengers)