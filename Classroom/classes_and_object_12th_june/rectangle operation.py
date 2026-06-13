#creating a class to for rectangle
class Rectangle:
    #defining a constructor
    def __init__(self,lenghth,breahth):
        self.lenghth=lenghth
        self.breahth=breahth
    #Method to display the lenghth and breahth of the rectangle
    def display_sides(self):
        print("Lenghth",self.lenghth)
        print("Breadth",self.breahth)
    #---------------------------------------------------
    #Method to find the area of the rectangle
    def area(self):

        print("Area of the rectangle:",(self.lenghth*self.breahth))
   #---------------------------------------------------
    #Method to withdraw money from the account
    def perimeter(self):
        print("Perimeter of the rectangle :",(2*(self.lenghth+self.breahth)))
        
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#------- Main Program ---------------------------------------------------------------
#Ask the user to enter the lenghth and breahth
lenghth=int(input("Enter the lenghth: "))
#to validate LENGHTH input
if lenghth<0:
    exit("===========INVALID LENGHTH=========")
#---------------------------------------------------------------
breahth=int(input("Enter the breahth: "))
#to validate BREAHTH input
if breahth<0:
    exit("===========INVALID BREAHTH=========")
#-----------------------------------------------------------------
#create an object of the Rectangle class
account=Rectangle(lenghth,breahth)
#menu driven program to perform various operations on the account
while True:
    print("\n------- Rectangle Operations -------")
    print("1. Display sides")
    print("2. AREA ")
    print("3. PERIMETER")
    print("4. Exit")
    choice=int(input("Select operation: "))
    if choice==1:
        account.display_sides()
    elif choice==2:
        account.area()
    elif choice==3:
        account.perimeter()
    elif choice==4:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.")
    #---------------------------------------------------------------
    #Ask the user if they want to perform another operation
    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")

