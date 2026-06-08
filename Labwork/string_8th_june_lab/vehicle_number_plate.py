'''A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  '''
# Program to validate and analyze a vehicle number plate

# --------------------------------------------------
# Taking a valid vehicle number from the user
# --------------------------------------------------
while True:

    # Taking input from the user
    vehicle_no = input("Enter Vehicle Number: ").upper()

    # Checking vehicle number format
    if (len(vehicle_no) == 10 and
        vehicle_no[0:2].isalpha() and
        vehicle_no[2:4].isdigit() and
        vehicle_no[4:6].isalpha() and
        vehicle_no[6:10].isdigit()):

        print("Valid Vehicle Number Entered")
        break

    else:
        print("Invalid Vehicle Number! Please try again.")

print("\nVehicle Number:", vehicle_no)

# --------------------------------------------------
# Task 1: Extract state code
# --------------------------------------------------
state_code = vehicle_no[0:2]

print("State Code:", state_code)

# --------------------------------------------------
# Task 2: Extract district code
# --------------------------------------------------
district_code = vehicle_no[2:4]

print("District Code:", district_code)

# --------------------------------------------------
# Task 3: Extract vehicle series
# --------------------------------------------------
series = vehicle_no[4:6]

print("Series:", series)

# --------------------------------------------------
# Task 4: Extract vehicle number
# --------------------------------------------------
vehicle_number = vehicle_no[6:10]

print("Vehicle Number:", vehicle_number)

# --------------------------------------------------
# Task 5: Count letters and digits separately
# --------------------------------------------------
letter_count = 0
digit_count = 0

for ch in vehicle_no:

    # Counting letters
    if ch.isalpha():
        letter_count += 1

    # Counting digits
    elif ch.isdigit():
        digit_count += 1

print("\nTotal Letters:", letter_count)
print("Total Digits:", digit_count)

# --------------------------------------------------
# Task 6: Verify vehicle number format
# --------------------------------------------------

# Since the input is already validated,
# vehicle number is valid
status = "Valid"

# --------------------------------------------------
# Task 7: Display whether the number plate is valid
# --------------------------------------------------
print("\nVehicle Number Status:", status)