'''A transport department wants to verify vehicle registration numbers.
Store at least 20 vehicle numbers.
Example
MH12AB4589 DL05XY9988 KA03PQ1234
Requirements
For each registration number:
    1.Extract state code.
    2.Extract district code.
    3.Extract series.
    4.Extract vehicle number.
    5.Count letters and digits.
    6.Validate format:
        oFirst 2 characters = Alphabets
        oNext 2 characters = Digits
        oNext 2 characters = Alphabets
        oLast 4 characters = Digits
    7.Display invalid registrations.
    8.Count vehicles state-wise.
Challenge
Generate a state-wise report:
    MH -> 6 Vehicles 
    DL -> 4 Vehicles
    KA -> 5 Vehicles 
    UP -> 5 Vehicles'''

# ==========================================================
# VEHICLE REGISTRATION ANALYZER
# ==========================================================
# This program:
# 1. Extracts State Code, District Code, Series and Vehicle No.
# 2. Counts letters and digits.
# 3. Validates registration number format.
# 4. Displays invalid registrations.
# 5. Counts vehicles state-wise.
# 6. Generates a state-wise report.
# ==========================================================


# List containing 20 vehicle registration numbers
vehicle_numbers = [
    "MH12AB4589",
    "DL05XY9988",
    "KA03PQ1234",
    "UP14CD5678",
    "MH20EF1111",
    "DL08GH2222",
    "KA09IJ3333",
    "UP32KL4444",
    "MH15MN5555",
    "DL01OP6666",
    "KA05QR7777",
    "UP16ST8888",
    "MH10UV9999",
    "DL07WX1234",
    "KA02YZ5678",
    "UP80AA9876",
    "MH18BB4321",
    "DL09CC8765",
    "KA07DD2468",
    "UP25EE1357"
]


# ==========================================================
# Function to validate registration number format
# Format:
# First 2 characters  -> Alphabets
# Next 2 characters   -> Digits
# Next 2 characters   -> Alphabets
# Last 4 characters   -> Digits
# ==========================================================
def validate_registration(vehicle_no):

    # Validation 1 : Length must be exactly 10
    if len(vehicle_no) != 10:
        return False

    # Validation 2 : First 2 characters should be alphabets
    if not vehicle_no[:2].isalpha():
        return False

    # Validation 3 : Next 2 characters should be digits
    if not vehicle_no[2:4].isdigit():
        return False

    # Validation 4 : Next 2 characters should be alphabets
    if not vehicle_no[4:6].isalpha():
        return False

    # Validation 5 : Last 4 characters should be digits
    if not vehicle_no[6:].isdigit():
        return False

    return True


# ==========================================================
# Function to extract registration details
# ==========================================================
def extract_details(vehicle_no):

    state_code = vehicle_no[:2]
    district_code = vehicle_no[2:4]
    series = vehicle_no[4:6]
    vehicle_number = vehicle_no[6:]

    return state_code, district_code, series, vehicle_number


# ==========================================================
# Function to count letters and digits
# ==========================================================
def count_letters_digits(vehicle_no):

    letters = 0
    digits = 0

    for char in vehicle_no:

        if char.isalpha():
            letters += 1

        elif char.isdigit():
            digits += 1

    return letters, digits


# ==========================================================
# Function to analyze all vehicle registrations
# ==========================================================
def analyze_vehicles(vehicle_list):

    # Validation: Check if list is empty
    if len(vehicle_list) == 0:
        print("No vehicle registrations available.")
        return {}, []

    state_count = {}
    invalid_registrations = []

    print("VEHICLE REGISTRATION ANALYSIS")
    print("=" * 60)

    for vehicle in vehicle_list:

        print("\nRegistration Number :", vehicle)

        # Check registration validity
        is_valid = validate_registration(vehicle)

        if is_valid:

            print("Status : VALID")

            # Extract components
            state, district, series, number = extract_details(vehicle)

            print("State Code     :", state)
            print("District Code  :", district)
            print("Series         :", series)
            print("Vehicle Number :", number)

            # Count letters and digits
            letters, digits = count_letters_digits(vehicle)

            print("Letters :", letters)
            print("Digits  :", digits)

            # Update state count
            if state in state_count:
                state_count[state] += 1
            else:
                state_count[state] = 1

        else:

            print("Status : INVALID")
            invalid_registrations.append(vehicle)

    return state_count, invalid_registrations


# ==========================================================
# Function to display invalid registrations
# ==========================================================
def display_invalid_registrations(invalid_list):

    print("\n")
    print("=" * 60)
    print("INVALID REGISTRATIONS")
    print("=" * 60)

    if len(invalid_list) == 0:
        print("No invalid registrations found.")
        return

    for vehicle in invalid_list:
        print(vehicle)


# ==========================================================
# Function to display state-wise vehicle count
# ==========================================================
def display_state_count(state_count):

    print("\n")
    print("=" * 60)
    print("STATE-WISE VEHICLE COUNT")
    print("=" * 60)

    if len(state_count) == 0:
        print("No valid registrations found.")
        return

    for state, count in state_count.items():
        print(state, "->", count, "Vehicles")


# ==========================================================
# Function to generate final report
# ==========================================================
def generate_report(state_count):

    print("\n")
    print("=" * 60)
    print("STATE-WISE REPORT")
    print("=" * 60)

    # Validation
    if len(state_count) == 0:
        print("No data available.")
        return

    for state, count in state_count.items():
        print(f"{state} -> {count} Vehicles")


# ==========================================================
# MAIN PROGRAM
# ==========================================================

# Analyze all registrations
state_count, invalid_registrations = analyze_vehicles(vehicle_numbers)

# Display invalid registrations
display_invalid_registrations(invalid_registrations)

# Display vehicle count state-wise
display_state_count(state_count)

# Generate final report
generate_report(state_count)