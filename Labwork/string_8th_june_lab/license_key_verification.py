'''A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  
Sample Output 
License Key: 
ABCD-EFGH-IJKL-MNOP 
 
Groups: 
['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
 
Number of Groups: 4 
 
Total Letters: 16 
Total Vowels: 4 
 
Merged Key: 
ABCDEFGHIJKLMNOP 
 
License Key Status: Valid'''
# Program to analyze and validate a software license key

# --------------------------------------------------
# Taking a valid license key from the user
# --------------------------------------------------
while True:

    # Taking license key as input
    license_key = input("Enter License Key: ").upper()

    # Splitting the key into groups
    groups = license_key.split("-")

    # Validating the format
    if len(groups) == 4:

        valid = True

        # Checking length of each group
        for group in groups:
            if len(group) != 4:
                valid = False
                break

        if valid:
            print("Valid License Key Entered")
            break

    print("Invalid License Key! Please try again.")

print("\nLicense Key:")
print(license_key)

# --------------------------------------------------
# Task 1: Verify there are exactly 4 groups
# --------------------------------------------------
number_of_groups = len(groups)

# --------------------------------------------------
# Task 2: Verify each group contains exactly
# 4 characters
# --------------------------------------------------
group_status = True

# Checking each group
for group in groups:

    # Verifying group length
    if len(group) != 4:
        group_status = False
        break

# --------------------------------------------------
# Task 3: Count total letters
# --------------------------------------------------
letter_count = 0

# Checking each character
for ch in license_key:

    # Counting only letters
    if ch.isalpha():
        letter_count += 1

# --------------------------------------------------
# Task 4: Count vowels
# --------------------------------------------------
vowel_count = 0

# Checking each character
for ch in license_key:

    # Counting vowels only
    if ch in "AEIOU":
        vowel_count += 1

# --------------------------------------------------
# Task 5: Remove hyphens and display
# the merged key
# --------------------------------------------------

# Removing all hyphens
merged_key = license_key.replace("-", "")

# --------------------------------------------------
# Task 6: Create a list containing all groups
# --------------------------------------------------
group_list = groups

# --------------------------------------------------
# Task 7: Display whether the key format
# is valid
# --------------------------------------------------
if number_of_groups == 4 and group_status:
    status = "Valid"
else:
    status = "Invalid"

# --------------------------------------------------
# Displaying Results
# --------------------------------------------------
print("\nGroups:")
print(group_list)

print("\nNumber of Groups:", number_of_groups)

print("\nTotal Letters:", letter_count)
print("Total Vowels:", vowel_count)

print("\nMerged Key:")
print(merged_key)

print("\nLicense Key Status:", status)

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------