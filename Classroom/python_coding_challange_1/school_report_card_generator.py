'''Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  '''
# Student Report Card Generator using File Handling
# -----------------------------------------
# Function to calculate grade
# -----------------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
# -----------------------------------------
# Function to check pass/fail
# -----------------------------------------
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
# -----------------------------------------
# Function to read student data from file
# -----------------------------------------
def read_student_data(filename):
    students = []
    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                sid, name, marks = line.split(",")
                student = {
                    "id": sid,
                    "name": name,
                    "marks": int(marks)
                }
                students.append(student)
        file.close()
    except FileNotFoundError:
        print("File not found!")
    return students
# -----------------------------------------
# Function to generate report card file
# -----------------------------------------
def generate_report_card(students, filename):
    file = open(filename, "w")
    file.write("STUDENT REPORT CARD\n")
    file.write("=" * 50 + "\n")
    file.write("ID\tName\tMarks\tGrade\tResult\n")
    file.write("=" * 50 + "\n")
    for student in students:
        grade = calculate_grade(student["marks"])
        result = check_result(student["marks"])
        file.write(
            f"{student['id']}\t{student['name']}\t{student['marks']}\t{grade}\t{result}\n"
        )
    file.close()
# -----------------------------------------
# Function to find topper
# -----------------------------------------
def find_topper(students):
    topper = students[0]
    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student
    return topper
# -----------------------------------------
# Function to count pass and fail students
# -----------------------------------------
def count_pass_fail(students):
    pass_count = 0
    fail_count = 0
    for student in students:
        if check_result(student["marks"]) == "Pass":
            pass_count += 1
        else:
            fail_count += 1
    return pass_count, fail_count
# -----------------------------------------
# Function to display merit students
# -----------------------------------------
def display_merit_students(students):
    print("\nStudents Eligible for Merit Certificate")
    print("-" * 40)
    found = False
    for student in students:
        if student["marks"] >= 90:
            print(
                student["id"],
                student["name"],
                student["marks"]
            )
            found = True
    if found == False:
        print("No Merit Students Found")
# -----------------------------------------
# Main Program
# -----------------------------------------
students = read_student_data("marks.txt")
if len(students) > 0:
    # Generate report card file
    generate_report_card(students, "report_card.txt")
    print("Report Card Generated Successfully!")
    print("File Name : report_card.txt")
    # Display topper
    topper = find_topper(students)
    print("\nTopper Details")
    print("-" * 30)
    print("Student ID :", topper["id"])
    print("Name       :", topper["name"])
    print("Marks      :", topper["marks"])
    print("Grade      :", calculate_grade(topper["marks"]))
    # Pass Fail Count
    pass_count, fail_count = count_pass_fail(students)
    print("\nPass Students :", pass_count)
    print("Fail Students :", fail_count)
    # Merit Students
    display_merit_students(students)