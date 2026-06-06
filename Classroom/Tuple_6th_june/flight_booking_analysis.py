'''A flight reservation system stores passenger records as tuples: 
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 
Where: 
• Passenger ID  
• Destination  
• Booking Status  '''
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
)
#Task 1: Display all passengers whose booking status is Confirmed. 
print("All passengers whose booking status is Confirmed.:  ")
for i in bookings:
    if i[2]=='Confirmed':
        print(i)
#Task2: Count the number of passengers travelling to Delhi. 
delhi=0
for i in bookings:
    if i[1]=='Delhi':
        delhi+=1
print("Tthe number of passengers travelling to Delhi: ",delhi)
#Task 3: Count Confirmed, Waiting, and Cancelled bookings separately
confirm=0
waiting=0
cancel=0
for i in bookings:
    if i[2]=='Confirmed':
        confirm+=1
    elif i[2]=='Waiting':
        waiting+=1
    elif i[2]=='Cancelled':
        cancel+=1
print("Confirmed: ",confirm)
print("Waiting: ",waiting)
print("Cancelled: ",cancel)
#Task 4: Create a list containing passenger IDs with Waiting status.
waiting_list=[]
for i in bookings:
    if i[2]=='Waiting':
        waiting_list.append(i[0])
print("Waiting list: ",waiting_list)
#Task5:  Determine which destination has the highest number of bookings. 
book = []
for i in bookings:
    book.append(i[1])

max_count = 0
most_booked = ""

for city in book:
    count = book.count(city)
    if count > max_count:
        max_count = count
        most_booked = city

print("Most Booked Destination:", most_booked)