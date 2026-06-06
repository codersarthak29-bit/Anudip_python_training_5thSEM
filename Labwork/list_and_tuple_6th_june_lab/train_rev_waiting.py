'''Passenger records: 
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
] 
Write a program to: 
• Display all waiting-list passengers.  
• Count confirmed and waiting passengers.  
• Find whether a specific passenger has a confirmed ticket.  
• Create separate lists for confirmed and waiting passengers.'''
# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# Display waiting-list passengers and create separate lists
print("Waiting-List Passengers:")
for name, status in passengers:
    if status == "Waiting":
        print(name)
        waiting_count += 1
        waiting_list.append(name)
    else:
        confirmed_count += 1
        confirmed_list.append(name)

# Find whether a specific passenger has a confirmed ticket
search_name = input("Enter passenger name to search: ")

found = False
for name, status in passengers:
    if name.lower() == search_name.lower():
        found = True
        if status == "Confirmed":
            print(name, "has a Confirmed ticket.")
        else:
            print(name, "is on the Waiting list.")
        break

if not found:
    print("Passenger not found.")

# Display counts and lists
print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

print("Confirmed List:", confirmed_list)
print("Waiting List:", waiting_list)