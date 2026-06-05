marks=[78,45,92,35,88,40,99,56]
max=marks[0]
for i in marks:
    if max<i:
        max=i
min=marks[0]
for i in marks:
    if min>i:
        min=i
fcount=0
for i in marks:
    if(i<40):
        marks.remove(i)
        fcount+=1
print("Passed students: ",marks)
print("Failed count: ",fcount)
print("Highest Marks: ",max)
print("Lowest Marks: ",min)
merit_list=[]

for i in marks:
    if i>75:
        merit_list.append(i)
print("Merit list: ",merit_list)

