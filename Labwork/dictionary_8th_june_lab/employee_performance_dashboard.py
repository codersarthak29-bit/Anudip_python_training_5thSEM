'''Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']'''
# Program to perform various operations on employee performance data

# Dictionary containing employee IDs as keys and performance scores as values
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# --------------------------------------------------
# Task 1: Display employees scoring above 80
# --------------------------------------------------
print("Employees Scoring Above 80:")

# Traversing the dictionary
for emp_id, score in performance.items():

    # Checking if score is greater than 80
    if score > 80:
        print(emp_id)

# --------------------------------------------------
# Task 2: Count employees needing improvement
# (score less than 60)
# --------------------------------------------------
improvement_count = 0

# Checking performance score of each employee
for score in performance.values():

    # Incrementing count if score is less than 60
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# --------------------------------------------------
# Task 3: Find the top performer
# --------------------------------------------------

# Assuming the first employee's score as the highest initially
top_employee = list(performance.keys())[0]
highest_score = list(performance.values())[0]

# Traversing the dictionary
for emp_id, score in performance.items():

    # Updating highest score and employee ID
    if score > highest_score:
        highest_score = score
        top_employee = emp_id

print("\nTop Performer:", top_employee, "(", highest_score, ")")

# --------------------------------------------------
# Task 4: Calculate average performance score
# --------------------------------------------------
total_score = 0

# Calculating total performance score
for score in performance.values():
    total_score += score

# Calculating average score
average_score = total_score / len(performance)

print("\nAverage Score:", average_score)

# --------------------------------------------------
# Task 5: Create separate lists based on
# performance categories
# --------------------------------------------------
excellent = []
good = []
average = []
poor = []

# Categorizing employees based on score
for emp_id, score in performance.items():

    # Checking for Excellent category
    if score >= 90:
        excellent.append(emp_id)

    # Checking for Good category
    elif 75 <= score <= 89:
        good.append(emp_id)

    # Checking for Average category
    elif 60 <= score <= 74:
        average.append(emp_id)

    # Remaining employees belong to Poor category
    else:
        poor.append(emp_id)

# Displaying categorized employee lists
print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)
'''
OUTPUT:
Employees Scoring Above 80:
EMP101
EMP104
EMP105
EMP107

Employees Needing Improvement: 3

Top Performer: EMP105 ( 97 )

Average Score: 71.3

Excellent:
['EMP101', 'EMP105']

Good:
['EMP102', 'EMP104', 'EMP107']

Average:
['EMP108', 'EMP110']

Poor:
['EMP103', 'EMP106', 'EMP109']'''
