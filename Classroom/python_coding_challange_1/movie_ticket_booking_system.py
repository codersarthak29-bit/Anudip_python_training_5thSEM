'''Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage. '''
# Cinema Hall Seat Booking System
# -----------------------------------------
# Sample Seat Data
# -----------------------------------------
tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}
# -----------------------------------------
# Function to display available seats
# -----------------------------------------
def display_available_seats(tickets):
    print("\nAvailable Seats:")
    print("-" * 20)
    for seat, status in tickets.items():
        if status == "Available":
            print(seat)
# -----------------------------------------
# Function to count booked seats
# -----------------------------------------
def count_booked_seats(tickets):
    count = 0
    for status in tickets.values():
        if status == "Booked":
            count += 1
    return count
# -----------------------------------------
# Function to count available seats
# -----------------------------------------
def count_available_seats(tickets):
    count = 0
    for status in tickets.values():
        if status == "Available":
            count += 1
    return count
# -----------------------------------------
# Function to reserve first available seat
# -----------------------------------------
def reserve_first_available_seat(tickets):
    for seat in tickets:
        if tickets[seat] == "Available":
            tickets[seat] = "Booked"
            return seat
    return None
# -----------------------------------------
# Function to save booking details to file
# -----------------------------------------
def save_booking_details(tickets, filename):
    file = open(filename, "w")
    for seat, status in tickets.items():
        file.write(seat + "," + status + "\n")
    file.close()
# -----------------------------------------
# Function to calculate occupancy percentage
# -----------------------------------------
def calculate_occupancy(tickets):
    booked = count_booked_seats(tickets)
    total = len(tickets)
    percentage = (booked / total) * 100
    return percentage
# -----------------------------------------
# Main Program
# -----------------------------------------
print("CINEMA HALL BOOKING REPORT")
print("=" * 40)
# Display Available Seats
display_available_seats(tickets)
# Count Seats
booked_count = count_booked_seats(tickets)
available_count = count_available_seats(tickets)
print("\nBooked Seats    :", booked_count)
print("Available Seats :", available_count)
# Reserve First Available Seat
reserved_seat = reserve_first_available_seat(tickets)
if reserved_seat:
    print("\nSeat Reserved Successfully!")
    print("Reserved Seat :", reserved_seat)
else:
    print("\nNo Seats Available.")
# Save Updated Data
save_booking_details(tickets, "tickets.txt")
print("\nUpdated booking details saved to tickets.txt")
# Occupancy Percentage
occupancy = calculate_occupancy(tickets)
print("\nHall Occupancy Percentage:",
      round(occupancy, 2), "%")