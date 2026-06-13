''' Electricity Bill Generator (Intermediate) 
Problem Statement: 
Create an ElectricityBill class containing: 
• Consumer Name  
• Consumer Number  
• Units Consumed  
Implement methods to: 
• Calculate electricity charges using the following slab:  
Units Rate 
First 100 units ₹5/unit 
Next 100 units ₹7/unit 
Above 200 units ₹10/unit 
• Display the final bill. '''
# Electricity Bill Generator

class ElectricityBill:
    def __init__(self):
        self.consumer_name = ""
        self.consumer_number = ""
        self.units_consumed = 0

    # Accept consumer details
    def accept_details(self):
        self.consumer_name = input("Enter Consumer Name: ")
        self.consumer_number = input("Enter Consumer Number: ")
        self.units_consumed = int(input("Enter Units Consumed: "))

    # Calculate electricity charges
    def calculate_bill(self):
        units = self.units_consumed

        if units <= 100:
            amount = units * 5

        elif units <= 200:
            amount = (100 * 5) + ((units - 100) * 7)

        else:
            amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)

        return amount

    # Display final bill
    def display_bill(self):
        print("\n----- ELECTRICITY BILL -----")
        print("Consumer Name   :", self.consumer_name)
        print("Consumer Number :", self.consumer_number)
        print("Units Consumed  :", self.units_consumed)
        print("Total Bill      : ₹", self.calculate_bill())


# Main Program
bill = ElectricityBill()
bill.accept_details()
bill.display_bill()