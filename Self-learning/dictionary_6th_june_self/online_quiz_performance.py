'''quiz_scores = { 
    "S001": 18, 
    "S002": 12, 
    "S003": 9, 
    "S004": 20, 
    "S005": 14, 
    "S006": 7, 
    "S007": 16, 
    "S008": 10, 
    "S009": 19, 
    "S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average.  '''
# Program to perform various operations on quiz scores

# Dictionary containing student IDs as keys and quiz scores as values
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# --------------------------------------------------
# Task 1: Display students scoring 15 or above
# --------------------------------------------------
print("Students scoring 15 or above:")

# Traversing the dictionary
for student, score in quiz_scores.items():

    # Checking if score is 15 or above
    if score >= 15:
        print(student, "-", score)

# --------------------------------------------------
# Task 2: Count students scoring below 10
# --------------------------------------------------
count_below_10 = 0

# Checking score of each student
for score in quiz_scores.values():

    # Incrementing count if score is below 10
    if score < 10:
        count_below_10 += 1

print("\nNumber of students scoring below 10:", count_below_10)

# --------------------------------------------------
# Task 3: Find the top performer
# --------------------------------------------------

# Assuming the first student is the top performer initially
top_student = ""
highest_score = 0

# Traversing the dictionary
for student, score in quiz_scores.items():

    # Updating highest score and student ID
    if score > highest_score:
        highest_score = score
        top_student = student

print("\nTop Performer:")
print(top_student, "-", highest_score)

# --------------------------------------------------
# Task 4: Create a list of students who passed
# (Score >= 10)
# --------------------------------------------------
passed_students = []

# Adding students who passed to the list
for student, score in quiz_scores.items():

    # Checking passing criteria
    if score >= 10:
        passed_students.append(student)

print("\nStudents Who Passed:")
print(passed_students)

# --------------------------------------------------
# Task 5: Calculate the class average
# --------------------------------------------------
total_score = 0

# Calculating total score of all students
for score in quiz_scores.values():
    total_score += score

# Calculating average score
class_average = total_score / len(quiz_scores)

print("\nClass Average:", class_average)