'''Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  
Sample Output 
Attendance Record: 
PPAPPPAAPPPPAPP 
 
Present Days: 11 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Longest Present Streak: 4 
Longest Absent Streak: 2 
 
Attendance Status: Below 75%'''
# Program to analyze student attendance

# Taking attendance record as input from the user
attendance = input("Enter Attendance Record (P/A): ").upper()

print("\nAttendance Record:")
print(attendance)

# --------------------------------------------------
# Task 1: Count Present and Absent days
# --------------------------------------------------
present_days = 0
absent_days = 0

# Checking each day's attendance
for status in attendance:

    # Counting present days
    if status == "P":
        present_days += 1

    # Counting absent days
    elif status == "A":
        absent_days += 1

print("\nPresent Days:", present_days)
print("Absent Days:", absent_days)

# --------------------------------------------------
# Task 2: Calculate attendance percentage
# --------------------------------------------------

# Calculating attendance percentage
attendance_percentage = (present_days / len(attendance)) * 100

print("\nAttendance Percentage:", round(attendance_percentage, 2), "%")

# --------------------------------------------------
# Task 3: Find the longest consecutive streak
# of Presence
# --------------------------------------------------
current_present = 0
longest_present = 0

# Checking attendance record
for status in attendance:

    # Incrementing current streak of presence
    if status == "P":
        current_present += 1

        # Updating longest streak
        if current_present > longest_present:
            longest_present = current_present

    # Resetting streak when absent
    else:
        current_present = 0

print("\nLongest Present Streak:", longest_present)

# --------------------------------------------------
# Task 4: Find the longest consecutive streak
# of Absence
# --------------------------------------------------
current_absent = 0
longest_absent = 0

# Checking attendance record
for status in attendance:

    # Incrementing current streak of absence
    if status == "A":
        current_absent += 1

        # Updating longest streak
        if current_absent > longest_absent:
            longest_absent = current_absent

    # Resetting streak when present
    else:
        current_absent = 0

print("Longest Absent Streak:", longest_absent)

# --------------------------------------------------
# Task 5: Determine whether attendance is
# below 75%
# --------------------------------------------------

# Checking attendance percentage
if attendance_percentage < 75:
    status = "Below 75%"
else:
    status = "75% or Above"

print("\nAttendance Status:", status)

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------