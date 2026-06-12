'''Problem Statement 
Employee performance scores are stored below. 
Sample Data 
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
5. Categorize employees:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
'''
# Employee performance scores

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

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement (score < 60)
improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find the top performer
top_employee = ""
top_score = 0

for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_employee = emp

print("\nTop Performer:")
print(top_employee, "(", top_score, ")", sep="")

# 4. Calculate average performance score
total = sum(performance.values())
average_score = total / len(performance)

print("\nAverage Score:", round(average_score, 1))

# 5. Categorize employees
excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average.append(emp)
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)