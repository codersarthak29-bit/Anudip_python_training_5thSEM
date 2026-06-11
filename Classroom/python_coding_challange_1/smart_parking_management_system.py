'''Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  '''

parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
]

# Task 1: Display vacant parking slot numbers
def display_vacant_slots(slots):
    print("Vacant parking slots:")
    for i, status in enumerate(slots):
        if status == "Vacant":
            print(f"Slot {i+1}")

# Task 2: Count occupied and vacant slots
def count_slots(slots):
    occupied_count = slots.count("Occupied")
    vacant_count = slots.count("Vacant")
    print(f"Occupied slots: {occupied_count}")
    print(f"Vacant slots: {vacant_count}")
    return occupied_count, vacant_count

# Task 3: Allocate the first vacant slot to a new vehicle
def allocate_slot(slots):
    for i, status in enumerate(slots):
        if status == "Vacant":
            slots[i] = "Occupied"
            print(f"Allocated slot {i+1} to a new vehicle.")
            return True
    print("No vacant slots available.")
    return False

# Task 4: Calculate parking occupancy percentage
def calculate_occupancy_percentage(slots):
    total_slots = len(slots)
    occupied_count = slots.count("Occupied")
    occupancy_percentage = (occupied_count / total_slots) * 100 if total_slots > 0 else 0
    print(f"Parking occupancy: {occupancy_percentage:.2f}%")
    return occupancy_percentage

# Task 5: Store updated parking information in parking.txt
def store_parking_info(slots, filename="parking.txt"):
    with open(filename, 'w') as f:
        for i, status in enumerate(slots):
            f.write(f"Slot {i+1}: {status}\n")
    print(f"Parking information stored in {filename}")
#main driven menu
while True:
    print("\n==============================================================================")
    print("=====================Smart Parking Management System Menu=====================")
    print("==============================================================================")
    print("1. Display vacant parking slots")
    print("2. Count occupied and vacant slots")
    print("3. Allocate a parking slot")
    print("4. Calculate parking occupancy percentage")
    print("5. Store parking information to file")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_vacant_slots(parking_slots)
    elif choice == '2':
        count_slots(parking_slots)
    elif choice == '3':
        allocate_slot(parking_slots)
    elif choice == '4':
        calculate_occupancy_percentage(parking_slots)
    elif choice == '5':
        store_parking_info(parking_slots)
    elif choice == '6':
        print("Exiting Smart Parking Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
