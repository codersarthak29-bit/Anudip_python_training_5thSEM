'''Problem Statement 
The attendance status of a student for 15 days is represented as follows: 
Sample Data 
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
Tasks 
1. Count present days.  
2. Count absent days.  
3. Calculate attendance percentage.  
4. Determine whether attendance is below 75%.  
5. Display the attendance status. '''

# Sample Data
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

# 1. Count present days
present_days = attendance.count('P')

# 2. Count absent days
absent_days = attendance.count('A')

# 3. Calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

# 4. Determine whether attendance is below 75%
below_75_percent = attendance_percentage < 75

# 5. Display the attendance status
print("Attendance Status:")
print(f"Total Days: {total_days}")
print(f"Present Days: {present_days}")
print(f"Absent Days: {absent_days}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if below_75_percent:
    print("Attendance is below 75%.")
else:
    print("Attendance is 75% or above.")
