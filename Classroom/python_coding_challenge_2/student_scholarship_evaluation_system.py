'''The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90). '''
#-----------------------------------------------------------
#program to make Student Scholarship Evaluation System 
#----------------------------------------------------------
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
}
#-----------------------------------------------------------
#task1:Display students scoring above 85 marks.  
#-----------------------------------------------------------
def display():
    for student,mark in marks.items():
        if mark>85:
            print(student)
print("Students scoring above 85 marks:")
#-------------------------------------------------------
#task2:Find the topper.  
#-------------------------------------------------------
def topper():
    top_score = 0
    topper = ""
    for student, score in marks.items():
        if score > top_score:
            top_score = score
            topper = student
    print("Topper:", topper)
    print("Score:", top_score)
#-----------------------------------------------------------
#task3:Find the student with the lowest marks.  
#------------------------------------------------------------
def lowest_marks_student():
    lowest_score = 101 # Initialize with a score higher than any possible mark
    lowest_scorer = ""
    for student, score in marks.items():
        if score < lowest_score:
            lowest_score = score
            lowest_scorer = student
    print("Student with lowest marks:", lowest_scorer)
    print("Score:", lowest_score)
#-----------------------------------------------------------
#task4:Calculate class average marks.   
#------------------------------------------------------------
def avg_marks():
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    print("Class average marks:", average_marks)
#--------------------------------------------------------------
#task5:Generate grades:  
#A (90+)  
#B (75–89)  
#C (50–74)  
#F (<50)  
#----------------------------------------------------------------
def grade():
    for student,score in marks.items():

        if score >= 90:
            print(f"{student}: A")
        elif score >= 75:
            print(f"{student}: B")
        elif score >=50:
            print(f"{student}: C")
        else:
            print(f"{student}: F")
#---------------------------------------------------------------
#task6:Create a list of scholarship students (marks ≥ 90). 
#---------------------------------------------------------------

def scholarship_students():
    scholarship_list = []
    for student, mark in marks.items():
        if mark >= 90:
            scholarship_list.append(student)
    print("Scholarship Students:", scholarship_list)
#-------------------------------------------------------
#MAIN PROFRAM
#-------------------------------------------------------
display()
topper()
lowest_marks_student()
avg_marks()
print("\nStudent Grades:")
grade()
scholarship_students()
