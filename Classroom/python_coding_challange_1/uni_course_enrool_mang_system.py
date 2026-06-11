'''Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
} 
"Operating Systems": 37 
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
o High Demand (>40)  
o Medium Demand (30–40)  
o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments).  '''
# University Course Enrollment Analyzer
# -----------------------------------------
# Sample Data
# -----------------------------------------
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}
# -----------------------------------------
# Function to display courses having
# more than 40 enrollments
# -----------------------------------------
def display_high_enrollment_courses(enrollment):
    print("\nCourses with More Than 40 Enrollments")
    print("-" * 40)
    for course, students in enrollment.items():
        if students > 40:
            print(course)
# -----------------------------------------
# Function to find most popular course
# -----------------------------------------
def find_most_popular_course(enrollment):
    course_list = list(enrollment.keys())
    most_popular = course_list[0]
    highest = enrollment[most_popular]
    for course, students in enrollment.items():
        if students > highest:
            highest = students
            most_popular = course
    return most_popular, highest
# -----------------------------------------
# Function to find least popular course
# -----------------------------------------
def find_least_popular_course(enrollment):
    course_list = list(enrollment.keys())
    least_popular = course_list[0]
    lowest = enrollment[least_popular]
    for course, students in enrollment.items():
        if students < lowest:
            lowest = students
            least_popular = course
    return least_popular, lowest
# -----------------------------------------
# Function to calculate total enrollments
# -----------------------------------------
def calculate_total_enrollments(enrollment):
    total = 0
    for students in enrollment.values():
        total += students
    return total
# -----------------------------------------
# Function to categorize courses
# -----------------------------------------
def categorize_courses(enrollment):
    high_demand = []
    medium_demand = []
    low_demand = []
    for course, students in enrollment.items():
        if students > 40:
            high_demand.append(course)
        elif students >= 30:
            medium_demand.append(course)
        else:
            low_demand.append(course)
    return high_demand, medium_demand, low_demand
# -----------------------------------------
# Function to count courses requiring
# promotional activities (<35 enrollments)
# -----------------------------------------
def count_promotion_courses(enrollment):
    count = 0
    for students in enrollment.values():
        if students < 35:
            count += 1
    return count
# -----------------------------------------
# Main Program
# -----------------------------------------
print("UNIVERSITY COURSE ENROLLMENT ANALYZER")
print("=" * 50)
# Task 1
display_high_enrollment_courses(enrollment)
# Task 2
most_course, most_students = find_most_popular_course(enrollment)
least_course, least_students = find_least_popular_course(enrollment)
print("\nMost Popular Course:")
print(f"{most_course} ({most_students} students)")
print("\nLeast Popular Course:")
print(f"{least_course} ({least_students} students)")
# Task 3
total = calculate_total_enrollments(enrollment)
print("\nTotal Enrollments:", total)
# Task 4
high_demand, medium_demand, low_demand = categorize_courses(enrollment)
print("\nHigh Demand:")
print(high_demand)
print("\nMedium Demand:")
print(medium_demand)
print("\nLow Demand:")
print(low_demand)
# Task 5
promotion_count = count_promotion_courses(enrollment)
print("\nCourses Requiring Promotion:", promotion_count)