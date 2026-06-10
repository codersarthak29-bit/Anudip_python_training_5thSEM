# Password Security Analyzer Program
# Author: ChatGPT
# Description: Analyzes 15 user passwords and generates a security report
# ----------------------------
# FUNCTION 1: Validate password input
# ----------------------------
def validate_password(pwd):
    """
    Checks if password input is valid (not empty)
    Returns True if valid, False otherwise
    """
    if len(pwd.strip()) == 0:
        return False
    return True
# ----------------------------
# FUNCTION 2: Count character types
# ----------------------------
def count_characters(pwd):
    upper = lower = digits = special = 0
    for ch in pwd:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1
    return upper, lower, digits, special
# ----------------------------
# FUNCTION 3: Check password length
# ----------------------------
def check_length(pwd):
    return len(pwd) >= 8
# ----------------------------
# FUNCTION 4: Check spaces
# ----------------------------
def check_spaces(pwd):
    return " " in pwd
# ----------------------------
# FUNCTION 5: Count vowels and consonants
# ----------------------------
def count_vowels_consonants(pwd):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in pwd:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c
# ----------------------------
# FUNCTION 6: Find most frequent character
# ----------------------------
def most_frequent_character(pwd):
    freq = {}
    for ch in pwd:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    max_char = None
    max_count = 0
    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch
    return max_char, max_count, freq
# ----------------------------
# FUNCTION 7: Display repeated characters
# ----------------------------
def repeated_characters(freq_dict):
    repeated = {}
    for ch in freq_dict:
        if freq_dict[ch] > 1:
            repeated[ch] = freq_dict[ch]
    return repeated
# ----------------------------
# FUNCTION 8: Determine password strength
# ----------------------------
def password_strength(pwd):
    upper, lower, digits, special = count_characters(pwd)
    length_ok = check_length(pwd)
    space = check_spaces(pwd)
    score = 0
    # scoring system
    if length_ok:
        score += 1
    if upper > 0:
        score += 1
    if lower > 0:
        score += 1
    if digits > 0:
        score += 1
    if special > 0:
        score += 1
    if not space:
        score += 1
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"
# ----------------------------
# MAIN PROGRAM
# ----------------------------
passwords = []
print("Enter 15 passwords for analysis:\n")
# Input 15 passwords with validation
i = 0
while i < 15:
    pwd = input(f"Enter password {i+1}: ")
    if not validate_password(pwd):
        print("Invalid input! Password cannot be empty.\n")
        continue
    passwords.append(pwd)
    i += 1
# Report counters
strong = 0
medium = 0
weak = 0
print("\n================ PASSWORD SECURITY REPORT ================\n")
# Analyze each password
for index, pwd in enumerate(passwords, start=1):
    print(f"\nPassword {index}: {pwd}")
    upper, lower, digits, special = count_characters(pwd)
    length_ok = check_length(pwd)
    space_ok = check_spaces(pwd)
    vowels, consonants = count_vowels_consonants(pwd)
    max_char, max_count, freq_dict = most_frequent_character(pwd)
    repeated = repeated_characters(freq_dict)
    strength = password_strength(pwd)
    # count category
    if strength == "Strong":
        strong += 1
    elif strength == "Medium":
        medium += 1
    else:
        weak += 1
    # Display analysis
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)
    print("Digits:", digits)
    print("Special Characters:", special)
    print("Minimum Length (8 chars):", length_ok)
    print("Spaces Present:", space_ok)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Most Frequent Character:", max_char, "->", max_count)
    if len(repeated) == 0:
        print("Repeated Characters: None")
    else:
        print("Repeated Characters:", repeated)
    print("Password Strength:", strength)
    print("----------------------------------------------------")
# Final Summary Report
print("\n================ FINAL SUMMARY REPORT ================\n")
print("Total Passwords Analyzed:", len(passwords))
print("Strong Passwords:", strong)
print("Medium Passwords:", medium)
print("Weak Passwords:", weak)
print("\n======================================================")