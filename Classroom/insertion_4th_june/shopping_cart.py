#Program for managing a shopping cart
total=0
while True:
    item = int(input("Enter the item price:"))
    if (item==0):
        print("Total Bill: ", total)
        break
    else:
        total = total + item
