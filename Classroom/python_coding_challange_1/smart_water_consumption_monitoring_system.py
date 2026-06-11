'''Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres). '''
# Water Consumption Analyzer
# -----------------------------------------
# Sample Data
# -----------------------------------------
water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}
# -----------------------------------------
# Function to display houses consuming
# more than 3000 litres
# -----------------------------------------
def display_high_consumption_houses(water_usage):
    print("\nHouses Consuming More Than 3000 Litres")
    print("-" * 40)
    for house, usage in water_usage.items():
        if usage > 3000:
            print(house, ":", usage, "litres")
# -----------------------------------------
# Function to find highest consumer
# -----------------------------------------
def find_highest_consumer(water_usage):
    highest_house = ""
    highest_usage = 0
    for house, usage in water_usage.items():
        if usage > highest_usage:
            highest_usage = usage
            highest_house = house
    return highest_house, highest_usage
# -----------------------------------------
# Function to find lowest consumer
# -----------------------------------------
def find_lowest_consumer(water_usage):
    houses = list(water_usage.keys())
    lowest_house = houses[0]
    lowest_usage = water_usage[lowest_house]
    for house, usage in water_usage.items():
        if usage < lowest_usage:
            lowest_usage = usage
            lowest_house = house
    return lowest_house, lowest_usage
# -----------------------------------------
# Function to calculate total consumption
# -----------------------------------------
def calculate_total_consumption(water_usage):
    total = 0
    for usage in water_usage.values():
        total += usage
    return total
# -----------------------------------------
# Function to categorize houses
# -----------------------------------------
def categorize_houses(water_usage):
    print("\nHouse Categories")
    print("-" * 40)
    for house, usage in water_usage.items():
        if usage < 2000:
            category = "Low"
        elif usage <= 3500:
            category = "Medium"
        else:
            category = "High"
        print(house, "->", category)
# -----------------------------------------
# Function to count houses eligible for
# conservation awareness program
# (>2500 litres)
# -----------------------------------------
def count_awareness_program_houses(water_usage):
    count = 0
    for usage in water_usage.values():
        if usage > 2500:
            count += 1
    return count
# -----------------------------------------
# Main Program
# -----------------------------------------
print("WATER CONSUMPTION ANALYZER")
print("=" * 45)
# Task 1
display_high_consumption_houses(water_usage)
# Task 2
highest_house, highest_usage = find_highest_consumer(water_usage)
lowest_house, lowest_usage = find_lowest_consumer(water_usage)
print("\nHighest Consumer")
print("-" * 20)
print(highest_house, ":", highest_usage, "litres")
print("\nLowest Consumer")
print("-" * 20)
print(lowest_house, ":", lowest_usage, "litres")
# Task 3
total_consumption = calculate_total_consumption(water_usage)
print("\nTotal Water Consumption:",
      total_consumption, "litres")
# Task 4
categorize_houses(water_usage)
# Task 5
eligible_count = count_awareness_program_houses(water_usage)
print("\nHouseholds Eligible for")
print("Conservation Awareness Program:",
      eligible_count)