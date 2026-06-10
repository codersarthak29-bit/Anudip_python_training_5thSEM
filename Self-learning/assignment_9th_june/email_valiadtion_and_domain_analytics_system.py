# Email Analysis Program
# Author: ChatGPT
# Description: Analyze 20 email addresses and generate domain report

# ----------------------------
# FUNCTION 1: Validate email
# ----------------------------
def is_valid_email(email):
    """
    Checks email validity:
    - exactly one @
    - contains .
    - no spaces
    """
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    if "." not in email:
        return False

    return True


# ----------------------------
# FUNCTION 2: Extract username
# ----------------------------
def get_username(email):
    return email.split("@")[0]


# ----------------------------
# FUNCTION 3: Extract domain
# ----------------------------
def get_domain(email):
    return email.split("@")[1]


# ----------------------------
# FUNCTION 4: Extract extension
# ----------------------------
def get_extension(email):
    domain = get_domain(email)
    return domain.split(".")[-1]


# ----------------------------
# FUNCTION 5: Count digits in username
# ----------------------------
def count_digits(username):
    count = 0
    for ch in username:
        if ch.isdigit():
            count += 1
    return count


# ----------------------------
# FUNCTION 6: Count special characters in email
# ----------------------------
def count_special_characters(email):
    count = 0
    for ch in email:
        if not ch.isalnum() and ch not in ['@', '.']:
            count += 1
    return count


# ----------------------------
# FUNCTION 7: Display invalid emails
# ----------------------------
def display_invalid_emails(invalid_list):
    print("\nInvalid Emails:")
    if len(invalid_list) == 0:
        print("None")
    else:
        for email in invalid_list:
            print(email)


# ----------------------------
# FUNCTION 8: Domain counting
# ----------------------------
def update_domain_count(domain, domain_dict):
    if domain in domain_dict:
        domain_dict[domain] += 1
    else:
        domain_dict[domain] = 1


# ----------------------------
# MAIN PROGRAM
# ----------------------------

emails = []
invalid_emails = []
domain_count = {}

print("Enter 20 email addresses:\n")

# Input 20 emails with validation check
i = 0
while i < 20:
    email = input(f"Enter email {i+1}: ").strip()

    if email == "":
        print("Empty input not allowed!\n")
        continue

    emails.append(email)
    i += 1


print("\n================ EMAIL ANALYSIS REPORT ================\n")

# Process each email
for email in emails:

    print("\nEmail:", email)

    # Check validity
    if not is_valid_email(email):
        print("Status: INVALID EMAIL")
        invalid_emails.append(email)
        continue

    # Extract parts
    username = get_username(email)
    domain = get_domain(email)
    extension = get_extension(email)

    # Analysis
    digit_count = count_digits(username)
    special_count = count_special_characters(email)

    # Update domain count
    update_domain_count(domain, domain_count)

    # Display results
    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)
    print("Digits in Username:", digit_count)
    print("Special Characters:", special_count)
    print("Status: VALID")

    print("----------------------------------------")


# Show invalid emails
display_invalid_emails(invalid_emails)


# ----------------------------
# FINAL DOMAIN REPORT
# ----------------------------
print("\n================ DOMAIN REPORT ================\n")

for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")

print("\n==============================================")