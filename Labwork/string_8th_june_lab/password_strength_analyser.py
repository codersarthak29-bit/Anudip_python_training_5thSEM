'''A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. '''
# Program to analyze password strength

# Taking password as input from the user
password = input("Enter Password: ")
#check the password is empty
# --------------------------------------------------
# Initializing counters and lists
# --------------------------------------------------
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0
#first check whether digit and special ch exist or not  
digit_list = []
special_list = []

# --------------------------------------------------
# Counting uppercase, lowercase, digits,
# and special characters
# --------------------------------------------------
for ch in password:

    # Checking for uppercase letter
    if ch.isupper():
        uppercase_count += 1

    # Checking for lowercase letter
    elif ch.islower():
        lowercase_count += 1

    # Checking for digit
    elif ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

    # Remaining characters are special characters
    else:
        special_count += 1
        special_list.append(ch)

# --------------------------------------------------
# Determining password strength
# --------------------------------------------------

# Checking all conditions for a strong password
if (len(password) >= 8 and
    uppercase_count >= 1 and
    lowercase_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

# Checking conditions for a medium password
elif len(password) >= 8 and (uppercase_count > 0 or
                             lowercase_count > 0 or
                             digit_count > 0):
    strength = "Medium"

# Otherwise password is weak
else:
    strength = "Weak"

# --------------------------------------------------
# Displaying results
# --------------------------------------------------
print("\nPassword:", password)

print("\nUppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("\nDigits Found:", digit_list)
print("Special Characters Found:", special_list)

print("\nPassword Strength:", strength)
