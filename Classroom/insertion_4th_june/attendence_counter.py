#Program for attendence counting
i=1
pcount=0
acount=0
while (i<=30):
    attendence=input("student " + str(i) + " is present or not (y/n): ")
    if attendence=="y":
        pcount=pcount+1
        i=i+1
    elif attendence=="n":
        acount=acount+1
        i=i+1
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
print("Present students:", pcount)
print("Absent students:", acount)