#program to convert time in to corresponding  hours and minute and second
#input of time in second
second=int(input("Enter time in seconds: "))
if(second<0):
    exit("Time cannot be negative")
hrs=0
min=0
if(second>=3600):
    hrs=second//3600
    second=second%3600
if(second>=60):
    min=second//60
    second=second%60
print("Equivalent time is: ",hrs,"hours",min,"minutes",second,"seconds")