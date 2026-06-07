'''marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50 '''
# Program to perform various operations on student marks using dictionary

# Dictionary containing student names as keys and marks as values
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# --------------------------------------------------
# Task 1: Display students scoring 80 or above
# --------------------------------------------------
print("Students scoring 80 or above:")

# Traversing the dictionary
for name, score in marks.items():
    if score >= 80:
        print(name, "-", score)

# --------------------------------------------------
# Task 2: Count the number of students who failed
# (Marks less than 40)
# --------------------------------------------------
fail_count = 0

# Checking each student's marks
for score in marks.values():
    if score < 40:
        fail_count += 1

print("\nNumber of failed students:", fail_count)

# --------------------------------------------------
# Task 3: Find the highest scorer
# --------------------------------------------------

# Finding the student with maximum marks
highest_scorer = max(marks, key=marks.get)

print("\nHighest Scorer:")
print(highest_scorer, "-", marks[highest_scorer])

# --------------------------------------------------
# Task 4: Create a list of students scoring
# between 60 and 75
# --------------------------------------------------
students_60_75 = []

# Adding eligible students to the list
for name, score in marks.items():
    if 60 <= score <= 75:
        students_60_75.append(name)

print("\nStudents scoring between 60 and 75:")
print(students_60_75)

# --------------------------------------------------
# Task 5: Assign grades to students
# A : Marks >= 90
# B : Marks between 75 and 89
# C : Marks between 50 and 74
# F : Marks below 50
# --------------------------------------------------
print("\nStudent Grades:")

# Traversing the dictionary to assign grades
for name, score in marks.items():

    # Assigning grade based on marks
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Displaying student name and grade
    print(name, ":", grade)