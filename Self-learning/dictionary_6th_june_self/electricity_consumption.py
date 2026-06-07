'''units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units '''
# Program to perform various operations on electricity consumption data

# Dictionary containing house numbers as keys and units consumed as values
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# --------------------------------------------------
# Task 1: Display houses consuming more than 300 units
# --------------------------------------------------
print("Houses consuming more than 300 units:")

# Traversing the dictionary
for house, consumption in units.items():

    # Checking if consumption is greater than 300 units
    if consumption > 300:
        print(house, "-", consumption)

# --------------------------------------------------
# Task 2: Count houses consuming less than 200 units
# --------------------------------------------------
count = 0

# Checking consumption of each house
for consumption in units.values():

    # Incrementing count if consumption is less than 200 units
    if consumption < 200:
        count += 1

print("\nNumber of houses consuming less than 200 units:", count)

# --------------------------------------------------
# Task 3: Find the house with the highest consumption
# --------------------------------------------------

# Assuming the first house has the highest consumption initially
highest_house = ""
highest_consumption = 0

# Traversing the dictionary
for house, consumption in units.items():

    # Updating highest consumption and house number
    if consumption > highest_consumption:
        highest_consumption = consumption
        highest_house = house

print("\nHouse with Highest Consumption:")
print(highest_house, "-", highest_consumption)

# --------------------------------------------------
# Task 4: Create a list of houses eligible for an
# energy-saving awareness campaign (consumption > 400)
# --------------------------------------------------
campaign_houses = []

# Adding eligible houses to the list
for house, consumption in units.items():

    # Checking campaign eligibility
    if consumption > 400:
        campaign_houses.append(house)

print("\nHouses Eligible for Energy-Saving Awareness Campaign:")
print(campaign_houses)

# --------------------------------------------------
# Task 5: Categorize houses based on consumption
# --------------------------------------------------
print("\nHouse Categories:")

# Traversing the dictionary
for house, consumption in units.items():

    # Categorizing consumption level
    if consumption < 200:
        category = "Low"
    elif consumption <= 350:
        category = "Medium"
    else:
        category = "High"

    # Displaying house category
    print(house, ":", category)