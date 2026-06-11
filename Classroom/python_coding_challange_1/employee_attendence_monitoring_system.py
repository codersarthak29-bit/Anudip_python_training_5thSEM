'''Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance). '''
# Employee Attendance Analyzer
# -----------------------------------------
# Function to read attendance data from file
# -----------------------------------------
def read_attendance(filename):
    employees = []
    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                emp_id, status = line.split(",")
                employees.append([emp_id, status])
        file.close()
    except FileNotFoundError:
        print("Attendance file not found!")
    return employees
# -----------------------------------------
# Function to count present employees
# -----------------------------------------
def count_present(employees):
    count = 0
    for employee in employees:
        if employee[1] == "P":
            count += 1
    return count
# -----------------------------------------
# Function to count absent employees
# -----------------------------------------
def count_absent(employees):
    count = 0
    for employee in employees:
        if employee[1] == "A":
            count += 1
    return count
# -----------------------------------------
# Function to get absent employee IDs
# -----------------------------------------
def get_absent_employees(employees):
    absent_list = []
    for employee in employees:
        if employee[1] == "A":
            absent_list.append(employee[0])
    return absent_list
# -----------------------------------------
# Function to calculate attendance percentage
# -----------------------------------------
def calculate_attendance_percentage(employees):
    total = len(employees)
    present = count_present(employees)
    percentage = (present / total) * 100
    return percentage
# -----------------------------------------
# Function to generate absentee report file
# -----------------------------------------
def generate_absent_report(absent_list, filename):
    file = open(filename, "w")
    file.write("ABSENT EMPLOYEE REPORT\n")
    file.write("=" * 30 + "\n")
    for emp_id in absent_list:
        file.write(emp_id + "\n")
    file.close()
# -----------------------------------------
# Function to display attendance award employees
# (100% attendance means Present)
# -----------------------------------------
def display_award_employees(employees):
    print("\nEmployees Eligible for Attendance Award")
    print("-" * 40)
    found = False
    for employee in employees:
        if employee[1] == "P":
            print(employee[0])
            found = True
    if found == False:
        print("No employee eligible.")
# -----------------------------------------
# Main Program
# -----------------------------------------
employees = read_attendance("attendance.txt")
if len(employees) > 0:
    # Present and Absent Count
    present_count = count_present(employees)
    absent_count = count_absent(employees)
    print("EMPLOYEE ATTENDANCE REPORT")
    print("=" * 40)
    print("\nPresent Employees :", present_count)
    print("Absent Employees  :", absent_count)
    # Absent Employee IDs
    absent_list = get_absent_employees(employees)
    print("\nAbsent Employee IDs")
    print("-" * 25)
    for emp_id in absent_list:
        print(emp_id)
    # Attendance Percentage
    attendance_percentage = calculate_attendance_percentage(employees)
    print("\nAttendance Percentage:",
          round(attendance_percentage, 2), "%")
    # Generate Absentee Report File
    generate_absent_report(absent_list, "absent_report.txt")
    print("\nAbsent Report Generated Successfully!")
    print("File Name : absent_report.txt")
    # Attendance Award Employees
    display_award_employees(employees)