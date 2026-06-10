'''
A railway coach has seats represented as follows:
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

Requirements:
1. count_seats(seats)
   Returns the number of booked and available seats.

2. first_available(seats)
   Returns the seat number of the first available seat.

3. occupancy_percentage(seats)
   Returns the percentage of occupied seats.

4. display_available_seats(seats)
   Displays all available seat numbers.
'''

# ==========================================================
# Railway Reservation Seat Analyzer
# ==========================================================

# List representing the status of seats in a railway coach
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# ----------------------------------------------------------
# Function: count_seats()
# Purpose : Count booked and available seats
# ----------------------------------------------------------
def count_seats(seats):

    # Initialize counters
    booked_count = 0
    available_count = 0

    # Traverse through each seat
    for seat in seats:

        # Check seat status
        if seat == "Booked":
            booked_count += 1
        else:
            available_count += 1

    # Return both counts
    return booked_count, available_count


# ----------------------------------------------------------
# Function: first_available()
# Purpose : Find the first available seat number
# ----------------------------------------------------------
def first_available(seats):

    # Traverse through seat list using index
    for i in range(len(seats)):

        # Check for first available seat
        if seats[i] == "Available":
            return i + 1      # Seat numbers start from 1

    # Return -1 if no seat is available
    return -1


# ----------------------------------------------------------
# Function: occupancy_percentage()
# Purpose : Calculate percentage of booked seats
# ----------------------------------------------------------
def occupancy_percentage(seats):

    # Find total number of seats
    total_seats = len(seats)

    # Prevent division by zero
    if total_seats == 0:
        return 0.0

    # Get booked seat count
    result = count_seats(seats)
    booked_count = result[0]

    # Calculate and return occupancy percentage
    return (booked_count / total_seats) * 100


# ----------------------------------------------------------
# Function: display_available_seats()
# Purpose : Display all available seat numbers
# ----------------------------------------------------------
def display_available_seats(seats):

    # Create an empty list to store available seat numbers
    available_seat_numbers = []

    # Traverse through seat list
    for i in range(len(seats)):

        # Check if seat is available
        if seats[i] == "Available":
            available_seat_numbers.append(i + 1)

    # Display available seat numbers
    print("Available Seats :", available_seat_numbers)


# ==========================================================
# Main Program
# ==========================================================

# Get booked and available seat counts
booked, available = count_seats(seats)

# Display seat statistics
print("Total Seats      :", len(seats))
print("Booked Seats     :", booked)
print("Available Seats  :", available)

# Display first available seat
print("First Available Seat :", first_available(seats))

# Display occupancy percentage
print("Occupancy Percentage :", round(occupancy_percentage(seats), 2), "%")

# Display all available seat numbers
display_available_seats(seats)