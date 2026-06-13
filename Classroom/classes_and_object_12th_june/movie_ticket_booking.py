'''Problem Statement: 
Design a MovieTicket class containing: 
• Movie Name  
• Ticket Price  
• Number of Seats Available  
Implement methods to: 
• Book tickets.  
• Cancel tickets.  
• Display booking details.  
• Update seat availability.  
Do not allow booking if requested seats exceed availability.'''
# Movie Ticket Booking System

class MovieTicket:
    def __init__(self):
        self.movie_name = input("Enter Movie Name: ")
        self.ticket_price = float(input("Enter Ticket Price: "))
        self.available_seats = int(input("Enter Number of Seats Available: "))
        self.booked_seats = 0

    # Book tickets
    def book_tickets(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            self.booked_seats += seats
            amount = seats * self.ticket_price

            print("\nTickets Booked Successfully!")
            print("Seats Booked:", seats)
            print("Total Amount: ₹", amount)
        else:
            print("\nBooking Failed!")
            print("Requested seats exceed availability.")

    # Cancel tickets
    def cancel_tickets(self, seats):
        if seats <= self.booked_seats:
            self.booked_seats -= seats
            self.available_seats += seats

            print("\nTickets Cancelled Successfully!")
            print("Seats Cancelled:", seats)
        else:
            print("\nCancellation Failed!")
            print("You cannot cancel more seats than booked.")

    # Display booking details
    def display_details(self):
        print("\n----- MOVIE BOOKING DETAILS -----")
        print("Movie Name      :", self.movie_name)
        print("Ticket Price    : ₹", self.ticket_price)
        print("Booked Seats    :", self.booked_seats)
        print("Available Seats :", self.available_seats)


# Main Program
movie = MovieTicket()

movie.display_details()

choice = int(input("\n1. Book Tickets\n2. Cancel Tickets\nEnter Choice: "))

if choice == 1:
    seats = int(input("Enter Number of Seats to Book: "))
    movie.book_tickets(seats)

elif choice == 2:
    seats = int(input("Enter Number of Seats to Cancel: "))
    movie.cancel_tickets(seats)

else:
    print("Invalid Choice!")

movie.display_details()