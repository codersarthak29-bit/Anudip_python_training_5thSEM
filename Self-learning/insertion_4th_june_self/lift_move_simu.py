'''A lift starts at floor 0. 
The user repeatedly enters destination floors. 
Display: 
• Floors travelled in each trip  
• Total floors travelled  
• Stop when user enters -1 '''
current_floor = 0
total_travelled = 0

print("Current Floor:", current_floor)

while True:
    destination = int(input("Enter Destination (-1 to stop): "))

    if destination == -1:
        break

    travelled = abs(destination - current_floor)

    print("Travelled:", travelled, "floors")

    total_travelled += travelled
    current_floor = destination

print("Total Travelled:", total_travelled, "floors")