'''. Mobile Phone Inventory (Intermediate) 
Problem Statement: 
Create a MobilePhone class to store: 
• Brand Name  
• Model Name  
• Price  
• Available Stock  
Implement methods to: 
• Display phone details.  
• Sell a specified quantity of phones.  
• Update stock after sale.  
Display an appropriate message if sufficient stock is unavailable.'''
# Mobile Phone Inventory Management

class MobilePhone:
    def __init__(self):
        self.brand_name = input("Enter Brand Name: ")
        self.model_name = input("Enter Model Name: ")
        self.price = float(input("Enter Price: "))
        self.stock = int(input("Enter Available Stock: "))

    # Display phone details
    def display_details(self):
        print("\n----- MOBILE PHONE DETAILS -----")
        print("Brand Name     :", self.brand_name)
        print("Model Name     :", self.model_name)
        print("Price          :", self.price)
        print("Available Stock:", self.stock)

    # Sell phones and update stock
    def sell_phone(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            amount = quantity * self.price

            print("\nSale Successful!")
            print("Quantity Sold :", quantity)
            print("Total Amount  :", amount)
            print("Remaining Stock:", self.stock)
        else:
            print("\nInsufficient Stock!")
            print("Available Stock:", self.stock)


# Main Program
phone = MobilePhone()

phone.display_details()

qty = int(input("\nEnter Quantity to Sell: "))
phone.sell_phone(qty)

print("\nUpdated Inventory:")
phone.display_details()