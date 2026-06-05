#Program to make student result management system
#Taking input from the user
sub1=float(input("Enter marks for subject 1: "))
while sub1<0 or sub1>100:
    print("Please enter marks between 0 and 100.")
    sub1=float(input("Enter marks for subject 1: "))
sub2=float(input("Enter marks for subject 2: "))
while sub2<0 or sub2>100:
    print("Please enter marks between 0 and 100.")
    sub2=float(input("Enter marks for subject 2: "))
sub3=float(input("Enter marks for subject 3: "))
while sub3<0 or sub3>100:
    print("Please enter marks between 0 and 100.")
    sub3=float(input("Enter marks for subject 3: "))
sub4=float(input("Enter marks for subject 4: "))
while sub4<0 or sub4>100:
    print("Please enter marks between 0 and 100.")
    sub4=float(input("Enter marks for subject 4: "))
sub5=float(input("Enter marks for subject 5: "))
while sub5<0 or sub5>100:
    print("Please enter marks between 0 and 100.")
    sub5=float(input("Enter marks for subject 5: "))
#Calculating total marks and percentage
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
#Determining the grade based on the percentage
if percentage>=90:
    grade='A+'
elif percentage>=75:
    grade='A'
elif percentage>=60:
    grade='B'
elif percentage>=40:
    grade='C'
else:
    grade='F'
#printing failed subjects   
failed_subjects=0
if sub1<40:
    failed_subjects+=1
if sub2<40:
    failed_subjects+=1
if sub3<40:
    failed_subjects+=1
if sub4<40:
    failed_subjects+=1
if sub5<40:
    failed_subjects+=1
#Printing the results
print("Total Marks:",total)
print("Percentage:",percentage,"%")
print("Grade:",grade)
if failed_subjects:
    print("Failed Subjects:",failed_subjects)
else:
    print("Congratulations! You passed all subjects.")