'''A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85). '''
# ==========================================
# Student Performance Analysis System
# ==========================================

students = {}

# ------------------------------------------
# Taking input of 30 students
# ------------------------------------------
for i in range(30):

    # Student ID Validation
    while True:

        sid = input("Enter Student ID : ").upper()

        if sid in students:
            print("Duplicate Student ID")

        elif sid.startswith("S") and len(sid) == 4 and sid[1:].isdigit():
            break

        else:
            print("Invalid ID! Example: S101")

    # Student Name Validation
# Student Name Validation
    while True:

        name = input("Enter Student Name : ").strip()

        # Remove extra spaces and keep only one space between words
        name = " ".join(name.split())

        # Validate name
        if name.replace(" ", "").isalpha():
            break

        print("Name should contain only alphabets")

    # Marks Validation
    while True:

        marks = input("Enter Marks (0-100) : ").strip()

        # Check if input contains only digits
        if not marks.isdigit():
            print("Marks must contain digits only")
            continue

        marks = int(marks)

        # Check marks range
        if 0 <= marks <= 100:
            break

        print("Marks must be between 0 and 100")

    # Storing data in dictionary
    students[sid] = {"name": name, "marks": marks}

# ------------------------------------------
# 1. Display all student records
# ------------------------------------------
print("\nAll Student Records")

for sid, data in students.items():

    name = data["name"]
    marks = data["marks"]

    print(f'{sid} -> name="{name}", marks={marks}')

# ------------------------------------------
# 2. Search Student
# ------------------------------------------
sid = input("\nEnter Student ID to Search : ").upper()

if sid in students:
    print("Record Found :", students[sid])
else:
    print("Student Not Found")

# ------------------------------------------
# 3. Add New Student
# ------------------------------------------
# Add New Student

while True:

    sid = input("\nEnter New Student ID : ").upper().strip()

    if sid in students:
        print("Student ID Already Exists")

    elif sid.startswith("S") and len(sid) == 4 and sid[1:].isdigit():
        break

    else:
        print("Invalid Student ID! Example: S101")

# Name Validation
while True:

    name = " ".join(input("Enter Name : ").split()).title()

    if name.replace(" ", "").isalpha():
        break

    print("Name should contain only alphabets")

# Marks Validation
while True:

    marks = input("Enter Marks (0-100) : ").strip()

    if not marks.isdigit():
        print("Marks must contain digits only")
        continue

    marks = int(marks)

    if 0 <= marks <= 100:
        break

    print("Marks must be between 0 and 100")

# Adding Student Record
students[sid] = {
    "name": name,
    "marks": marks
}

print("Student Added Successfully")

# ------------------------------------------
# 4. Update Marks
# ------------------------------------------ 

# Take Student ID input
sid = input("\nEnter Student ID to Update : ").upper().strip()

# Check whether Student ID exists
if sid in students:

    # Validate marks
    while True:

        # Take marks input
        marks = input("Enter New Marks (0-100) : ").strip()

        # Check whether input contains only digits
        if not marks.isdigit():
            print("Marks must contain digits only")
            continue

        # Convert marks into integer
        marks = int(marks)

        # Check marks range
        if 0 <= marks <= 100:
            break

        print("Marks must be between 0 and 100")

    # Update marks
    students[sid]["marks"] = marks

    print("Marks Updated Successfully")

else:
    print("Student Not Found")

# ------------------------------------------
# 5. Delete Student
# ------------------------------------------
sid = input("\nEnter Student ID to Delete : ").upper()

if sid in students:
    del students[sid]
    print("Student Deleted Successfully")
else:
    print("Student Not Found")

# ------------------------------------------
# 6. Topper and Lowest Scorer
# ------------------------------------------

# Take the first student ID as initial topper and lowest scorer
for sid in students:
    topper = sid
    lowest = sid
    break

# Compare marks of all students
for sid in students:

    # Update topper if higher marks are found
    if students[sid]["marks"] > students[topper]["marks"]:
        topper = sid

    # Update lowest scorer if lower marks are found
    if students[sid]["marks"] < students[lowest]["marks"]:
        lowest = sid

# Display topper details
print("\nTopper :", topper)
print(f'Name = {students[topper]["name"]}, Marks = {students[topper]["marks"]}')

# Display lowest scorer details
print("\nLowest Scorer :", lowest)
print(f'Name = {students[lowest]["name"]}, Marks = {students[lowest]["marks"]}')

# ------------------------------------------
# 7. Class Average
# ------------------------------------------

# Variable to store total marks
total_marks = 0

# Add marks of all students
for student in students.values():
    total_marks += student["marks"]

# Calculate average marks
average = total_marks / len(students)

# Display average up to 2 decimal places
print("\nClass Average =", round(average, 2))

# ------------------------------------------
# 8. Pass and Fail Count
# Pass Marks = 50
# ------------------------------------------
pass_count = 0

for student in students.values():
    if student["marks"] >= 50:
        pass_count += 1

fail_count = len(students) - pass_count

print("\nPass Students :", pass_count)
print("Fail Students :", fail_count)

# ------------------------------------------
# 9. Generate Grades
# ------------------------------------------
print("\nStudent Grades")

for sid, data in students.items():

    marks = data["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, "-", data["name"], ":", grade)

# ------------------------------------------
# 10. Students Above Average
# ------------------------------------------
print("\nStudents Scoring Above Average")

for sid, data in students.items():

    if data["marks"] > average:
        print(sid, "-", data)

# ------------------------------------------
# 11. Top 5 Performers
# ------------------------------------------
# Convert dictionary into a list
student_list = list(students.items())

# Sort students in descending order of marks
for i in range(len(student_list) - 1):

    for j in range(i + 1, len(student_list)):

        if student_list[i][1]["marks"] < student_list[j][1]["marks"]:

            # Swap records
            student_list[i], student_list[j] = student_list[j], student_list[i]

# Display Top 5 students
print("\nTop 5 Performers")

for i in range(min(5, len(student_list))):

    sid = student_list[i][0]
    name = student_list[i][1]["name"]
    marks = student_list[i][1]["marks"]

    print(f'{sid} -> name="{name}", marks="{marks}"')

# ------------------------------------------
# 12. Scholarship Students
# Marks > 85
# ------------------------------------------
scholarship_students = {}

for sid, data in students.items():

    if data["marks"] > 85:
        scholarship_students[sid] = data

print("\nScholarship Students")

for sid, data in scholarship_students.items():
    print(sid, "-", data)