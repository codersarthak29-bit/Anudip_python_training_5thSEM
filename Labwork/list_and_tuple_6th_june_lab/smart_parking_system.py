'''Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.  '''
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
#Task1:Count occupied and available slots.
occupied=0
available=0
for i in slots:
    if i==0:
        available+=1
    elif i==1:
        occupied+=1
print("Occupied: ",occupied)
print("Available: ",available)
#Task2:Find the first available slot
seat=slots.index(0)
print("First available seat is at : ",seat+1)
#Task3:Display all available slot numbers.
aval=[]
for i in range(0,len(slots)):
    if slots[i]==0:
        aval.append(i+1)
print("All available slots numbers are: ",aval)
#Task4:Check whether parking occupancy exceeds 75%. 
if (occupied/len(slots)*100)>75:
    print("Parking occupacy exceeds 75%")
else:
    print("Parking occupacy does'nt exceeds 75%")