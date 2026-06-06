'''Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers.  '''
# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find the busiest stop
max_passengers = max(passengers)
busiest_stop = passengers.index(max_passengers) + 1

# Display stops with fewer than 10 passengers
low_passenger_stops = []
for i in range(len(passengers)):
    if passengers[i] < 10:
        low_passenger_stops.append(i + 1)

# Calculate average passengers
average = sum(passengers) / len(passengers)

# Determine whether any stop exceeded 25 passengers
exceeded_25 = False
for p in passengers:
    if p > 25:
        exceeded_25 = True
        break

# Display results
print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)
print("Stops with Fewer Than 10 Passengers:", low_passenger_stops)
print("Average Passengers:", round(average, 2))

if exceeded_25:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")