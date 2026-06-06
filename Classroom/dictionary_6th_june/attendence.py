'''Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value. 
Display the roll number of students who are Present'''
# Attendance Tracker for 30 Students

attendance = {}

# Input attendance for 30 students
for i in range(30):
    roll_no = int(input("Enter Roll Number: "))
    
    status = input("Enter Attendance (Present/Absent): ").strip().capitalize()
    
    while status not in ["Present", "Absent"]:
        print("Invalid input! Please enter Present or Absent.")
        status = input("Enter Attendance (Present/Absent): ").strip().capitalize()
    
    attendance[roll_no] = status

# Display attendance dictionary
print("\nAttendance Record:")
print(attendance)

# Display roll numbers of present students
print("\nStudents who are Present:")
for roll_no, status in attendance.items():
    if status == "Present":
        print(roll_no)