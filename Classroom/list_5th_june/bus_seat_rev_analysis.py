#program to cheack the seat availablity
seats=[1,0,1,1,0,0,1,1,1,0]
booked=0
aval=0
for i in seats:
    if (i==1):
        booked+=1
    if(i==0):
        aval+=1
print("Booked seats: ",booked)
print("Available seats: ",aval)
faval=seats.index(0)
print("First available seat: ",faval+1)
aval_seat=[]
for i in range(len(seats)):
    if seats[i]==0:
        aval_seat.append(i+1)
print("Availabile seat numbers: ",aval_seat)
occupancy = (booked / len(seats)) * 100
print("Bus Occupancy:", str(int(occupancy)) + "%")
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")