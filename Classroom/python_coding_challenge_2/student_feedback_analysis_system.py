'''Problem Statement 
A training institute collects feedback from students after completing a Python course. The feedback 
comments are stored in a text file named feedback.txt. 
Sample Input/Data (feedback.txt) 
The sessions were very interactive and informative. 
Excellent teaching methodology and practical examples. 
The pace of the course was appropriate. 
More real-world projects should be included. 
The trainer explained concepts very clearly. 
Tasks 
1. Count the total number of lines.  
2. Count the total number of words.  
3. Count the total number of characters.  
4. Find the longest feedback comment.  
5. Find the shortest feedback comment.  
6. Count the total number of vowels present in the file.  '''
#program to make  Student Feedback Analysis System
# Open and read the file
with open("feedback.txt", "r") as file:
    lines = file.readlines()

# 1. Count total number of lines
total_lines = len(lines)

# 2. Count total number of words
total_words = sum(len(line.split()) for line in lines)

# 3. Count total number of characters
total_characters = sum(len(line) for line in lines)

# 4. Find the longest feedback comment
longest_comment = max(lines, key=len).strip()

# 5. Find the shortest feedback comment
shortest_comment = min(lines, key=len).strip()

# 6. Count total number of vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for line in lines:
    for char in line:
        if char in vowels:
            vowel_count += 1

# Display results
print("Total Number of Lines:", total_lines)
print("Total Number of Words:", total_words)
print("Total Number of Characters:", total_characters)
print("Longest Feedback Comment:")
print(longest_comment)
print("Shortest Feedback Comment:")
print(shortest_comment)
print("Total Number of Vowels:", vowel_count)
