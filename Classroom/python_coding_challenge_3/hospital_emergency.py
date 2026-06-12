# Program: Emergency Ward Patient Management

patients = [
    ("P101", "Critical"),
    ("P102", "Stable"),
    ("P103", "Critical"),
    ("P104", "Moderate"),
    ("P105", "Stable"),
    ("P106", "Critical"),
    ("P107", "Moderate"),
    ("P108", "Stable"),
    ("P109", "Critical"),
    ("P110", "Moderate")
]

# 1. Count patients in each category
count = {"Critical": 0, "Moderate": 0, "Stable": 0}

# 2 & 3. Create separate lists
critical = []
moderate = []
stable = []

for pid, category in patients:
    count[category] += 1

    if category == "Critical":
        critical.append(pid)
    elif category == "Moderate":
        moderate.append(pid)
    else:
        stable.append(pid)

print("Patient Count by Category:")
for category, num in count.items():
    print(category, ":", num)

# Display critical patients
print("\nCritical Patients:")
for pid in critical:
    print(pid)

# Display separate lists
print("\nCritical Patients List:")
print(critical)

print("\nModerate Patients List:")
print(moderate)

print("\nStable Patients List:")
print(stable)

# 4. Determine category requiring maximum attention
max_category = max(count, key=count.get)

print("\nCategory Requiring Maximum Attention:")
print(max_category)

# 5. Save critical patient IDs to file
file = open("critical_patients.txt", "w")

for pid in critical:
    file.write(pid + "\n")

file.close()

print("\nCritical Patient Report Generated Successfully.")