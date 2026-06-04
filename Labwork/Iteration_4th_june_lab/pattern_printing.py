#Program for pattern printing
#Taking input for the number of rows
rows=int(input("Enter the number of rows: "))
#Validating the input to ensure it's a positive integer
while rows<=0:
    print("Please enter a positive integer for the number of rows.")
    rows=int(input("Enter the number of rows: "))
#Printing the pattern
for i in range(1, rows+1):
    for j in range(1, i+1):
        #Using end=" " to print numbers on the same line with a space in between
        print(j, end=" ")
    print() #Using print() to move to the next line after each row is printed
#Reversing the pattern
print("Reversed Pattern:")
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ") #Using end=" " to print numbers on the same line with a space in between
    print() #Using print() to move to the next line after each row is printed

