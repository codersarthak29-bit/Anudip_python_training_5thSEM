'''Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent.  '''
# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P','A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = attendance.count('P')
absent = attendance.count('A')

# Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

# Determine eligibility
if percentage >= 75:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

# Find positions of absences
absent_positions = []
for i in range(len(attendance)):
    if attendance[i] == 'A':
        absent_positions.append(i + 1)   # +1 for day number

# Display results
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", round(percentage, 2), "%")
print("Eligibility:", eligibility)
print("Absent on Days:", absent_positions)