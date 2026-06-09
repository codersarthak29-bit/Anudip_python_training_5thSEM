'''A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  
Sample Output 
Original Name: Rahul Sharma 
 
Generated Username: 
rahulsharma2026 
 
Username Length: 15 
 
Vowels: 5 
Consonants: 10 
 
Status: Username Generated Successfully'''
# Program to generate a username from a student's name

# --------------------------------------------------
# Taking student's name as input
# --------------------------------------------------
name = input("Enter Student Name: ")

print("\nOriginal Name:", name)

# --------------------------------------------------
# Task 1: Remove spaces
# --------------------------------------------------

# Removing all spaces from the name
username = name.replace(" ", "")

# --------------------------------------------------
# Task 2: Convert to lowercase
# --------------------------------------------------

# Converting username to lowercase
username = username.lower()

# --------------------------------------------------
# Task 3: Append current year (2026)
# --------------------------------------------------

# Adding current year to the username
username = username + "2026"

# --------------------------------------------------
# Task 4: If username length exceeds 12,
# keep only first 12 characters
# --------------------------------------------------

# Checking username length
if len(username) > 12:
    username = username[:12]

print("\nGenerated Username:")
print(username)

# --------------------------------------------------
# Task 5 & 6: Count vowels and consonants
# --------------------------------------------------
vowel_count = 0
consonant_count = 0

# Checking each character in username
for ch in username:

    # Considering only alphabets
    if ch.isalpha():

        # Counting vowels
        if ch in "aeiou":
            vowel_count += 1

        # Remaining alphabets are consonants
        else:
            consonant_count += 1

# --------------------------------------------------
# Task 7: Display username statistics
# --------------------------------------------------
print("\nUsername Length:", len(username))

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)

print("\nStatus: Username Generated Successfully")

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------