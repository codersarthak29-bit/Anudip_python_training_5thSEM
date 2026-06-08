'''Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4'''
# Program to perform various operations on city temperature data

# Dictionary containing city names as keys and temperatures as values
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# --------------------------------------------------
# Task 1: Display cities having temperature above 40°C
# --------------------------------------------------
print("Cities Above 40°C:")

# Traversing the dictionary
for city, temp in temperature.items():

    # Checking if temperature is above 40°C
    if temp > 40:
        print(city)

# --------------------------------------------------
# Task 2: Find the hottest city
# --------------------------------------------------

# Assuming the first city's temperature as the highest initially
hottest_city = list(temperature.keys())[0]
highest_temp = list(temperature.values())[0]

# Traversing the dictionary
for city, temp in temperature.items():

    # Updating highest temperature and city name
    if temp > highest_temp:
        highest_temp = temp
        hottest_city = city

print("\nHottest City:", hottest_city, "(", highest_temp, "°C)")

# --------------------------------------------------
# Task 3: Find the coolest city
# --------------------------------------------------

# Assuming the first city's temperature as the lowest initially
coolest_city = list(temperature.keys())[0]
lowest_temp = list(temperature.values())[0]

# Traversing the dictionary
for city, temp in temperature.items():

    # Updating lowest temperature and city name
    if temp < lowest_temp:
        lowest_temp = temp
        coolest_city = city

print("\nCoolest City:", coolest_city, "(", lowest_temp, "°C)")

# --------------------------------------------------
# Task 4: Calculate average temperature
# --------------------------------------------------
total_temp = 0

# Calculating total temperature
for temp in temperature.values():
    total_temp += temp

# Calculating average temperature
average_temp = total_temp / len(temperature)

print("\nAverage Temperature:", average_temp, "°C")

# --------------------------------------------------
# Task 5: Create a list of pleasant cities
# (temperature < 35°C)
# --------------------------------------------------
pleasant_cities = []

# Adding cities with temperature below 35°C
for city, temp in temperature.items():

    # Checking if city is pleasant
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)

# --------------------------------------------------
# Task 6: Count cities with temperature between
# 35°C and 40°C
# --------------------------------------------------
count = 0

# Checking temperature of each city
for temp in temperature.values():

    # Incrementing count if temperature lies between 35°C and 40°C
    if 35 <= temp <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)
'''
OUTPUT:
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4 '''
