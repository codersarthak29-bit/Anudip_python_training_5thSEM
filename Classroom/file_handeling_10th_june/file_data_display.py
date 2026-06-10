'''To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.'''
# Program to read data from a file and display:
# 1. Number of vowels
# 2. Number of characters
# 3. Number of lines

# Open the file in read mode
file = open("text.txt", "r")

# Read all data from file
data = file.read()

# Count vowels
vowels = 0
for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1

# Count characters
characters = len(data)

# Count lines
file.seek(0)          # Move cursor back to beginning
lines = file.readlines()
line_count = len(lines)

# Display results
print("Number of vowels =", vowels)
print("Number of characters =", characters)
print("Number of lines =", line_count)

# Close file
file.close()
