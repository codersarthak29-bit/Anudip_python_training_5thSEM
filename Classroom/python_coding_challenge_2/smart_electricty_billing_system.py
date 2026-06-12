'''Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
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
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). '''
#-----------------------------------------------------------------
#program to make the smart electricity billing system
#-----------------------------------------------------------------
#sample data for the program
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
#----------------------------------------------------------------
#task1:  Display houses consuming more than 400 units.  
#----------------------------------------------------------------
def display():
    for house_num,unit in units.items():
        if unit>400:
            print(house_num)
print("Houses consuming more than 400 units:")
#----------------------------------------------------------------
#task2: Find the highest-consuming house. 
#----------------------------------------------------------------
def highest_unit():
    highest_consumption = 0
    highest_consumer_house = ""
    for house, consumption in units.items():
        if consumption > highest_consumption:
            highest_consumption = consumption
            highest_consumer_house = house
    print("Highest-consuming house:", highest_consumer_house)
    print("Units consumed:", units[highest_consumer_house])
#--------------------------------------------------------
#task3: Find the lowest-consuming house.  
#--------------------------------------------------------
def lowest_unit():
    lowest_house = min(units, key=units.get)
    print("Lowest-consuming house:", lowest_house)
    print("Units consumed:", units[lowest_house])
#--------------------------------------------------------
#task4:Calculate the total units consumed.  
#--------------------------------------------------------
def total_units():
    total_consumption = sum(units.values())

    print("Total units consumed:", total_consumption)
#--------------------------------------------------------
#task5:   Create separate lists for:  
#Low Consumption (< 200)  
#Medium Consumption (200–400)  
#High Consumption (> 400)   
#-------------------------------------------------------
def consumption_categories():
    low_consumption = []
    medium_consumption = []
    high_consumption = []
    for house, consumption in units.items():
        if consumption < 200:
            low_consumption.append(house)
        elif 200 <= consumption <= 400:
            medium_consumption.append(house)
        else:
            high_consumption.append(house)
    print("Low Consumption:\n",low_consumption)
    print("Medium Consumption:\n", medium_consumption)
    print("High Consumption:\n", high_consumption)
#-------------------------------------------------------
#task6: Count houses eligible for an energy-saving campaign (consumption > 300). 
#-------------------------------------------------------
def energy_saving_campaign():
    eligible_houses = 0
    for consumption in units.values():
        if consumption > 300:
            eligible_houses += 1
    print("Houses eligible for energy-saving campaign:", eligible_houses)
#-------------------------------------------------------
#MAIN FUNCTION
#-------------------------------------------------------
display()
highest_unit()
lowest_unit()
total_units()
consumption_categories()
energy_saving_campaign()