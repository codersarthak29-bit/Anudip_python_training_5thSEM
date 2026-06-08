'''A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.  
Sample Output 
Employee ID: EMP2026ANUJ458 
 
Uppercase Letters: 7 
Digits: 7 
 
Joining Year: 2026 
Employee Name: ANUJ 
 
Digit List: [2, 0, 2, 6, 4, 5, 8] 
Sum of Digits: 27 
 
ID Status: Valid'''
# Program to validate and process Employee ID

# --------------------------------------------------
# Taking a valid Employee ID from the user
# --------------------------------------------------
while True:

    # Taking Employee ID as input
    emp_id = input("Enter Employee ID: ")

    # Checking all validation rules
    if (emp_id.startswith("EMP") and
        len(emp_id) >= 10 and
        emp_id[3:7].isdigit() and
        emp_id[-3:].isdigit()
        and emp_id[7:-3].isalpha()):

        print("Valid Employee ID Entered")
        break

    else:
        print("Invalid Employee ID! Please try again.")

print("\nEmployee ID:", emp_id)

# --------------------------------------------------
# Task 1: Count the number of uppercase letters
# --------------------------------------------------
uppercase_count = 0

for ch in emp_id:
    if ch.isupper():
        uppercase_count += 1

print("\nUppercase Letters:", uppercase_count)

# --------------------------------------------------
# Task 2: Count the number of digits
# --------------------------------------------------
digit_count = 0

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

print("Digits:", digit_count)

# --------------------------------------------------
# Task 3: Extract the joining year
# --------------------------------------------------
joining_year = emp_id[3:7]

print("\nJoining Year:", joining_year)

# --------------------------------------------------
# Task 4: Extract the employee name
# --------------------------------------------------
employee_name = emp_id[7:-3]

print("Employee Name:", employee_name)

# --------------------------------------------------
# Task 5: Create a list containing all digits
# present in the ID
# --------------------------------------------------
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

print("\nDigit List:", digit_list)

# --------------------------------------------------
# Task 6: Find the sum of all digits
# present in the ID
# --------------------------------------------------
digit_sum = 0

for digit in digit_list:
    digit_sum += digit

print("Sum of Digits:", digit_sum)

# --------------------------------------------------
# Task 7: Display whether the ID is valid
# --------------------------------------------------
print("\nID Status: Valid")
# --------------------------------------------------