'''Problem Statement 
A file named login_logs.txt contains user login attempts in the following format: 
username,status 
anuj,Success 
rahul,Failed 
anuj,Failed 
priya,Failed 
rahul,Failed 
neha,Success 
anuj,Failed 
karan,Failed 
rahul,Success 
priya,Failed 
Tasks 
1. Count successful and failed login attempts.  
2. Identify users with more than 2 failed attempts.  
3. Create a dictionary storing the number of failures per user.  
4. Create a set of users who logged in successfully.  
5. Display users whose accounts should be reviewed.  '''

# Initialize counters and data structures
successful_attempts = 0
failed_attempts = 0
failed_users = {}  # To store failure count per user
successful_logins = set()  # To store users with successful logins

# Read the log file
with open("login_logs.txt", "r") as file:
    # Skip the header line
    next(file)
    for line in file:
        username, status = line.strip().split(',')

        if status == "Success":
            successful_attempts += 1
            successful_logins.add(username)
        elif status == "Failed":
            failed_attempts += 1
            failed_users[username] = failed_users.get(username, 0) + 1

# 1. Count successful and failed login attempts
print("1. Login Attempt Summary:")
print(f"   Successful Attempts: {successful_attempts}")
print(f"   Failed Attempts: {failed_attempts}")

# 2. Identify users with more than 2 failed attempts
users_with_many_failures = []
for user, failures in failed_users.items():
    if failures > 2:
        users_with_many_failures.append(user)

print("\n2. Users with more than 2 failed attempts:")
if users_with_many_failures:
    for user in users_with_many_failures:
        print(f"   - {user}")
else:
    print("   No users with more than 2 failed attempts.")

# 3. Create a dictionary storing the number of failures per user
print("\n3. Number of failures per user:")
for user, failures in failed_users.items():
    print(f"   {user}: {failures} failures")

# 4. Create a set of users who logged in successfully
print("\n4. Users who logged in successfully:")
print(f"   {successful_logins}")

# 5. Display users whose accounts should be reviewed (e.g., failed attempts but no successful login, or many failed attempts)
accounts_to_review = set()
for user, failures in failed_users.items():
    if failures > 0 and user not in successful_logins:
        accounts_to_review.add(user)
    if failures > 2: # Also include users with many failures even if they eventually succeeded
        accounts_to_review.add(user)

print("\n5. Users whose accounts should be reviewed:")
if accounts_to_review:
    for user in accounts_to_review:
        print(f"   - {user}")
else:
    print("   No accounts require immediate review.")
