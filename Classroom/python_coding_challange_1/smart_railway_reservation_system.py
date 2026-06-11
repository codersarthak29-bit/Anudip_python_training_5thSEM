'''Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage. '''
#-----------------------------------------------------------
#Program to make smart railway reservation system
#-----------------------------------------------------------
#-----------------------------------------------------------
#Dictionary containg the data of the seats whether booked or not
#-----------------------------------------------------------
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
#----------------------------------------------------------
#TASK:1 :Display all available seats numbers(here using function: def display_all_seats)
#----------------------------------------------------------
def display_all_seats():
    print("Available Seats:")
    for seat_num, status in seats.items():
        if status == "Available":
            print(seat_num, end=" ")
    print("\n")
#-----------------------------------------------------------
#TASK:2 :Count booked and available seats(her using function: def count_aval)
#-----------------------------------------------------------
def count_aval():
    available_seats = 0
    booked_seats = 0
    for status in seats.values():
        if status == "Available":
            available_seats += 1
        else:
            booked_seats += 1
    print(f"Booked Seats: {booked_seats}")
    print(f"Available Seats: {available_seats}")
#---------------------------------------------------------
#TASK3: Reserve the first available seat( here using function : def reserve)
#---------------------------------------------------------
def reserve():
    for seat_num, status in seats.items():
        if status == "Available":
            seats[seat_num] = "Booked"
            print(f"Seat {seat_num} Reserved Successfully.")
            return
    print("No available seats to reserve.")

#---------------------------------------------------------
#TASK4: Cancel booking for a given seat number( here using function : def cancel_booking)
#---------------------------------------------------------
def cancel_booking():
    seat_to_cancel = int(input("Enter the seat number to cancel: "))
    if seat_to_cancel in seats:
        if seats[seat_to_cancel] == "Booked":
            seats[seat_to_cancel] = "Available"
            print(f"Booking for seat {seat_to_cancel} cancelled successfully.")
        else:
            print(f"Seat {seat_to_cancel} is already Available.")
    else:
        print(f"Seat {seat_to_cancel} does not exist.")
#---------------------------------------------------------
#TASK5: Store the updated reservation status in reservations.txt(here using function: def store_status)
#---------------------------------------------------------
def store_status():
    with open("reservations.txt", "w") as file:
        for seat_num, status in seats.items():
            file.write(f"Seat {seat_num}: {status}\n")

#---------------------------------------------------------
#TASK6: Display occupancy percentage(here using function: def occupancy_percentage)
#---------------------------------------------------------
def occupancy_percentage():
    total_seats = len(seats)
    booked_seats = sum(1 for status in seats.values() if status == "Booked")
    
    if total_seats == 0:
        print("No seats available to calculate occupancy.")
        return
    
    occupancy = (booked_seats / total_seats) * 100
    print(f"Occupancy Percentage: {occupancy:.1f}%")

#---------------------------------------------------------
#MAIN DRIVEN MENU
#---------------------------------------------------------
while True:
    print("\n=================== Railway Reservation System Menu ===============")
    print("1. Display Available Seats")
    print("2. Count Booked and Available Seats")
    print("3. Reserve a Seat")
    print("4. Cancel Booking")
    print("5. Store Reservation Status")
    print("6. Display Occupancy Percentage")
    print("7. Exit")
    choice = input("\nEnter your choice: ")
    print("\n")
    if choice == '1':
        display_all_seats()
    elif choice == '2':
        count_aval()
    elif choice == '3':
        reserve()
    elif choice == '4':
        cancel_booking()
    elif choice == '5':
        store_status()
        print("Reservation Details Saved Successfully.")
    elif choice == '6':
        occupancy_percentage()
    elif choice == '7':
        print("Exiting Railway Reservation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

'''Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully.'''