'''
Monthly electricity consumption (units) is stored as: 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5'''
# Program to perform various operations on electricity consumption data

# Dictionary containing house numbers as keys and units consumed as values
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# --------------------------------------------------
# Task 1: Display houses consuming more than 400 units
# --------------------------------------------------
print("Houses Consuming More Than 400 Units:")

# Traversing the dictionary
for house, consumption in units.items():

    # Checking if consumption is greater than 400 units
    if consumption > 400:
        print(house)

# --------------------------------------------------
# Task 2: Find the highest-consuming house
# --------------------------------------------------

# Assuming the first house's consumption as the highest initially
highest_house = list(units.keys())[0]
highest_consumption = list(units.values())[0]

# Traversing the dictionary
for house, consumption in units.items():

    # Updating highest consumption and house number
    if consumption > highest_consumption:
        highest_consumption = consumption
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_consumption, "units)")

# --------------------------------------------------
# Task 3: Find the lowest-consuming house
# --------------------------------------------------

# Assuming the first house's consumption as the lowest initially
lowest_house = list(units.keys())[0]
lowest_consumption = list(units.values())[0]

# Traversing the dictionary
for house, consumption in units.items():

    # Updating lowest consumption and house number
    if consumption < lowest_consumption:
        lowest_consumption = consumption
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_consumption, "units)")

# --------------------------------------------------
# Task 4: Calculate total units consumed
# --------------------------------------------------
total_units = 0

# Calculating total consumption
for consumption in units.values():
    total_units += consumption

print("\nTotal Units Consumed:", total_units)

# --------------------------------------------------
# Task 5: Create lists based on consumption category
# --------------------------------------------------
low_consumption = []
medium_consumption = []
high_consumption = []

# Categorizing houses based on consumption
for house, consumption in units.items():

    # Checking for Low Consumption category
    if consumption < 200:
        low_consumption.append(house)

    # Checking for Medium Consumption category
    elif 200 <= consumption <= 400:
        medium_consumption.append(house)

    # Remaining houses belong to High Consumption category
    else:
        high_consumption.append(house)

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)

# --------------------------------------------------
# Task 6: Count houses eligible for an
# energy-saving campaign (consumption > 300)
# --------------------------------------------------
campaign_count = 0

# Checking consumption of each house
for consumption in units.values():

    # Incrementing count if consumption is greater than 300
    if consumption > 300:
        campaign_count += 1

print("\nEligible for Energy-Saving Campaign:", campaign_count)
'''
OUTPUT:
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5'''