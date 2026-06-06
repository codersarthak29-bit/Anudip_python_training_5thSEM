'''A company stores employee details in a tuple. Each employee record contains: 
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
Where: 
• First value = Employee ID  
• Second value = Employee Name  
• Third value = Performance Score '''
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
#Task:1 Display details of employees scoring 80 or above. 
print("Employees scoring 80 or above.")
for score in employees:
    if score[2]>=80:
        print(score)
print("----------------------------------------------")
#Task 2:Count the number of employees who need improvement (score below 60).
imp_count=0 
for score in employees:
    if score[2]<60:
        imp_count+=1
print(" The number of employees who need improvement (score below 60):  ",imp_count)
#Task 3:Find the employee with the highest score.
max=employees[0][2]
for score in employees:
    if max<score[2]:
        max=score[2]
for score in employees:
    if score[2]==max:
        print(" The employee with the highest score: ",score)
#Task 4: Create a list containing the names of all employees scoring above 75. 
new_list=[]
for score in employees:
    if score[2]>75:
        new_list.append(score[1])
print("the names of all employees scoring above 75: ",new_list)
#Task 5: Display the performance category for each employee
for score in employees:
    if score[2]>=90:
        print(score[1],"--> Excellent")
    elif score[2]>=75 and score[2]<=89:
        print(score[1],"--> Good")
    elif score[2]>=60 and score[2]<=74:
        print(score[1],"--> Average")
    else:
        print(score[1],"--> Needs improvement")
