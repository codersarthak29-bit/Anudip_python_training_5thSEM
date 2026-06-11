'''Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
o Low Waste (<200 kg)  
o Medium Waste (200–400 kg)  
o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.'''
# City Waste Management Analyzer
# -----------------------------------------
# Sample Data
# -----------------------------------------
waste_data = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}
# -----------------------------------------
# Function to display sectors generating
# more than 400 kg waste
# -----------------------------------------
def display_high_waste_sectors(waste_data):
    print("\nSectors Generating More Than 400 kg Waste")
    print("-" * 45)
    for sector, waste in waste_data.items():
        if waste > 400:
            print(sector)
# -----------------------------------------
# Function to find maximum waste sector
# -----------------------------------------
def find_maximum_waste_sector(waste_data):
    sectors = list(waste_data.keys())
    max_sector = sectors[0]
    max_waste = waste_data[max_sector]
    for sector, waste in waste_data.items():
        if waste > max_waste:
            max_waste = waste
            max_sector = sector
    return max_sector, max_waste
# -----------------------------------------
# Function to find minimum waste sector
# -----------------------------------------
def find_minimum_waste_sector(waste_data):
    sectors = list(waste_data.keys())
    min_sector = sectors[0]
    min_waste = waste_data[min_sector]
    for sector, waste in waste_data.items():
        if waste < min_waste:
            min_waste = waste
            min_sector = sector
    return min_sector, min_waste
# -----------------------------------------
# Function to calculate total waste
# -----------------------------------------
def calculate_total_waste(waste_data):
    total = 0
    for waste in waste_data.values():
        total += waste
    return total
# -----------------------------------------
# Function to categorize sectors
# -----------------------------------------
def categorize_sectors(waste_data):
    low_waste = []
    medium_waste = []
    high_waste = []
    for sector, waste in waste_data.items():
        if waste < 200:
            low_waste.append(sector)
        elif waste <= 400:
            medium_waste.append(sector)
        else:
            high_waste.append(sector)
    return low_waste, medium_waste, high_waste
# -----------------------------------------
# Function to get awareness campaign sectors
# -----------------------------------------
def get_campaign_sectors(waste_data):
    campaign_list = []
    for sector, waste in waste_data.items():
        if waste > 300:
            campaign_list.append(sector)
    return campaign_list
# -----------------------------------------
# Function to save campaign list to file
# -----------------------------------------
def save_campaign_report(campaign_list, filename):
    file = open(filename, "w")
    file.write("AWARENESS CAMPAIGN SECTORS\n")
    file.write("=" * 35 + "\n")
    for sector in campaign_list:
        file.write(sector + "\n")
    file.close()
# -----------------------------------------
# Main Program
# -----------------------------------------
print("CITY WASTE MANAGEMENT ANALYZER")
print("=" * 50)
# Task 1
display_high_waste_sectors(waste_data)
# Task 2
max_sector, max_waste = find_maximum_waste_sector(waste_data)
print("\nMaximum Waste Generation")
print("-" * 30)
print(max_sector, f"({max_waste} kg)")
# Task 3
min_sector, min_waste = find_minimum_waste_sector(waste_data)
print("\nMinimum Waste Generation")
print("-" * 30)
print(min_sector, f"({min_waste} kg)")
# Task 4
total_waste = calculate_total_waste(waste_data)
print("\nTotal Waste Collected:", total_waste, "kg")
# Task 5
low_waste, medium_waste, high_waste = categorize_sectors(waste_data)
print("\nLow Waste:")
print(low_waste)
print("\nMedium Waste:")
print(medium_waste)
print("\nHigh Waste:")
print(high_waste)
# Task 6
campaign_list = get_campaign_sectors(waste_data)
print("\nSectors Requiring Awareness Campaign")
print("-" * 40)
for sector in campaign_list:
    print(sector)
print("\nTotal Campaign Sectors:", len(campaign_list))
# Task 7
save_campaign_report(campaign_list, "campaign_sectors.txt")
print("\nCampaign Report Generated Successfully.")
print("File Name : campaign_sectors.txt")