'''Problem Statement: 
Design a Vehicle class containing: 
• Vehicle Number  
• Vehicle Type  
• Rent per Day  
Implement methods to: 
• Accept vehicle details.  
• Calculate total rental amount based on the number of days rented.  
• Display the bill. '''
# Vehicle Class Program

class Vehicle:
    def __init__(self):
        self.vehicle_no = ""
        self.vehicle_type = ""
        self.rent_per_day = 0

    # Accept vehicle details
    def accept_details(self):
        self.vehicle_no = input("Enter Vehicle Number: ")
        self.vehicle_type = input("Enter Vehicle Type: ")
        self.rent_per_day = float(input("Enter Rent Per Day: "))

    # Calculate total rental amount
    def calculate_rent(self, days):
        return self.rent_per_day * days

    # Display bill
    def display_bill(self, days):
        total_amount = self.calculate_rent(days)

        print("\n----- VEHICLE RENTAL BILL -----")
        print("Vehicle Number :", self.vehicle_no)
        print("Vehicle Type   :", self.vehicle_type)
        print("Rent Per Day   :", self.rent_per_day)
        print("Days Rented    :", days)
        print("Total Amount   :", total_amount)


# Main Program
vehicle = Vehicle()
vehicle.accept_details()

days = int(input("Enter Number of Days Rented: "))
vehicle.display_bill(days)
