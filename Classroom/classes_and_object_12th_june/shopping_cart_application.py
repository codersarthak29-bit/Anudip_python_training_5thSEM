'''Problem Statement: 
Create a Product class containing product name, quantity, and price per unit. 
Implement methods to: 
• Calculate total price.  
• Update quantity.  
• Display product details. '''
class Product:
    def __init__(self,name,quantity,unit_price):
        self.name=name
        self.quantity=quantity
        self.unit_price=unit_price
    def total_price(self):
        print("Total price: ",(self.quantity*self.unit_price))
    def update_quantity(self,new_quantity):
        self.quantity=new_quantity
        print(f"Quantity updated to {self.quantity}")
    def display_product_details(self):
        print(f"Product: {self.name}, Quantity: {self.quantity}, Unit Price: {self.unit_price}")
name=input("Enter the name of the product:")
if name.isdigit or name.isspace():
    print("Invalid product name. Product name cannot be a number or just spaces.")
quantity=int(input("Enter the quantity:"))
if quantity <= 0:
    print("Invalid quantity. Quantity must be a positive number.")
unit_price=float(input("Enter the unit price:"))
if unit_price <= 0:
    print("Invalid unit price. Unit price must be a positive number.")
product = Product(name, quantity, unit_price)
while True:
    print("=======================================================")
    print("=================SHOPPING CART MENU====================")
    print("============================================================")
    print("1. View Cart")
    print("2.Calculate Total Price")
    print("3.Upadte Quantity")
    print("4. Exit")
    choice = input("Enter your choice: ")
    print("============================================================")

    if choice == '1':
        product.display_product_details()
    elif choice == '2':
        product.total_price()
    elif choice == '3':
        product.update_quantity()
    elif choice == '4':
        print("Thanks for visting us!!!")
        break
