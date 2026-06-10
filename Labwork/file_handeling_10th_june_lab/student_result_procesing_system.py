# ==========================================================
# Student Result Management System
# ==========================================================
# Load student records from file
def load_records():
    students = []
    file = open("results.txt", "r")
    for line in file:
        students.append(line.strip().split(","))
    file.close()
    return students
# Display all student records
def display_records():
    students = load_records()
    print("\nStudent Records")
    print("-" * 40)
    for student in students:
        print(student[0], student[1], student[2])
# Search student by ID
def search_student():
    student_id = input("Enter Student ID : ")
    students = load_records()
    found = False
    for student in students:
        if student[0] == student_id:
            print("\nStudent Found")
            print("ID    :", student[0])
            print("Name  :", student[1])
            print("Marks :", student[2])
            found = True
    if found == False:
        print("Student not found.")
# Find topper and lowest scorer
def topper_lowest():
    students = load_records()
    topper_name = students[0][1]
    topper_marks = int(students[0][2])
    lowest_name = students[0][1]
    lowest_marks = int(students[0][2])
    for student in students:
        marks = int(student[2])
        if marks > topper_marks:
            topper_marks = marks
            topper_name = student[1]
        if marks < lowest_marks:
            lowest_marks = marks
            lowest_name = student[1]
    print("\nTopper :", topper_name, "-", topper_marks)
    print("Lowest Scorer :", lowest_name, "-", lowest_marks)
# Calculate class average
def class_average():
    students = load_records()
    total = 0
    for student in students:
        total += int(student[2])
    average = total / len(students)
    print("\nClass Average :", round(average, 2))
# Count pass and fail students
def pass_fail_count():
    students = load_records()
    pass_count = 0
    fail_count = 0
    for student in students:
        marks = int(student[2])
        if marks >= 40:
            pass_count += 1
        else:
            fail_count += 1
    print("\nPass Students :", pass_count)
    print("Fail Students :", fail_count)
# Assign grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
# Generate grades and display
def generate_grades():
    students = load_records()
    print("\nGrade Report")
    print("-" * 40)
    for student in students:
        marks = int(student[2])
        grade = get_grade(marks)
        print(student[1], "->", grade)
# Write grade report to grades.txt
def write_grades_file():
    students = load_records()
    file = open("grades.txt", "w")
    for student in students:
        marks = int(student[2])
        grade = get_grade(marks)
        file.write(student[0] + "," +
                   student[1] + "," +
                   str(marks) + "," +
                   grade + "\n")
    file.close()
    print("\nGrades written successfully to grades.txt")
# ==========================================================
# Menu Driven Program
# ==========================================================
while True:
    print("\n")
    print("=" * 45)
    print("      STUDENT RESULT MANAGEMENT")
    print("=" * 45)
    print("1. Display All Records")
    print("2. Search Student")
    print("3. Find Topper & Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass & Fail Students")
    print("6. Generate Grades")
    print("7. Write Grades to grades.txt")
    print("8. Exit")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        display_records()
    elif choice == 2:
        search_student()
    elif choice == 3:
        topper_lowest()
    elif choice == 4:
        class_average()
    elif choice == 5:
        pass_fail_count()
    elif choice == 6:
        generate_grades()
    elif choice == 7:
        write_grades_file()
    elif choice == 8:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice.")