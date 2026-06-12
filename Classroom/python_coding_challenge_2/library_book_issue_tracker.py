'''Problem Statement 
A library stores the number of times books were issued during a month. 
Sample Data 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
Tasks 
1. Find the maximum number of issues.  
2. Find the minimum number of issues.  
3. Calculate the average number of issues.  
4. Count books issued more than 15 times.  
5. Create a list of books issued fewer than 10 times. '''
#program to make  Library Book Issue Tracker 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# 1. Find the maximum number of issues.
max_issues = max(book_issues)
print(f"Maximum number of issues: {max_issues}")

# 2. Find the minimum number of issues.
min_issues = min(book_issues)
print(f"Minimum number of issues: {min_issues}")

# 3. Calculate the average number of issues.
average_issues = sum(book_issues) / len(book_issues)
print(f"Average number of issues: {average_issues:.2f}")

# 4. Count books issued more than 15 times.
count_more_than_15 = 0
for issues in book_issues:
    if issues > 15:
        count_more_than_15 += 1
print(f"Number of books issued more than 15 times: {count_more_than_15}")

# 5. Create a list of books issued fewer than 10 times.
fewer_than_10 = []
for issues in book_issues:
    if issues < 10:
        fewer_than_10.append(issues)
print(f"Books issued fewer than 10 times: {fewer_than_10}")
