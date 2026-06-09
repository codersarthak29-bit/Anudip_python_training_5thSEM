'''A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  
Sample Output 
Email: rahul.sharma2026@gmail.com 
 
Username: rahul.sharma2026 
Domain: gmail 
Extension: com 
 
Digits Found: 4 
Special Characters Found: 2 
 
Email Status: Valid'''
# Program to analyze and validate an email address

# --------------------------------------------------
# Taking email as input from the user
# --------------------------------------------------
while True:

    # Taking email input
    email = input("Enter Email Address: ")

    # Validating email format
    if email.count("@") == 1:

        at_pos = email.index("@")

        # Checking if at least one '.' exists after '@'
        if "." in email[at_pos:]:
            print("Valid Email Entered")
            break

    print("Invalid Email! Please try again.")

print("\nEmail:", email)

# --------------------------------------------------
# Task 1: Extract username
# --------------------------------------------------

# Extracting username before '@'
username = email[:email.index("@")]

print("\nUsername:", username)

# --------------------------------------------------
# Task 2: Extract domain name
# --------------------------------------------------

# Extracting domain between '@' and '.'
domain = email[email.index("@")+1 : email.rindex(".")]

print("Domain:", domain)

# --------------------------------------------------
# Task 3: Extract extension
# --------------------------------------------------

# Extracting extension after the last '.'
extension = email[email.rindex(".")+1:]

print("Extension:", extension)

# --------------------------------------------------
# Task 4: Count digits present in username
# --------------------------------------------------
digit_count = 0

# Checking each character in username
for ch in username:

    # Counting digits
    if ch.isdigit():
        digit_count += 1

print("\nDigits Found:", digit_count)

# --------------------------------------------------
# Task 5: Count special characters
# --------------------------------------------------
special_count = 0

# Checking each character in email
for ch in email:

    # Counting special characters
    if not ch.isalnum():
        special_count += 1

print("Special Characters Found:", special_count)

# --------------------------------------------------
# Task 6: Check email validation rules
# --------------------------------------------------

# Checking:
# Exactly one '@' exists
# At least one '.' exists after '@'
if email.count("@") == 1 and "." in email[email.index("@"):]:
    status = "Valid"
else:
    status = "Invalid"

# --------------------------------------------------
# Task 7: Display Valid Email or Invalid Email
# --------------------------------------------------
print("\nEmail Status:", status)

# --------------------------------------------------