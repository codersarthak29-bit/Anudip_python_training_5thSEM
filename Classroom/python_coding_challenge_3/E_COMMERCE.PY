# Program: Coupon Usage Analysis

# Read coupon records from file
file = open("coupons.txt", "r")
coupons = [line.strip() for line in file]
file.close()

# 1. Count usage frequency of each coupon
frequency = {}

for coupon in coupons:
    if coupon in frequency:
        frequency[coupon] += 1
    else:
        frequency[coupon] = 1

print("Coupon Usage Frequency:")
for coupon in frequency:
    print(coupon, ":", frequency[coupon])

# 2. Identify coupons used more than 3 times
suspicious = []

for coupon in frequency:
    if frequency[coupon] > 3:
        suspicious.append(coupon)

print("\nSuspicious Coupons:")
for coupon in suspicious:
    print(coupon)

# 3. Create a set of unique coupons
unique_coupons = set(coupons)

print("\nUnique Coupons:")
print(unique_coupons)

# 4. Display the most frequently used coupon
most_used = max(frequency, key=frequency.get)

print("\nMost Frequently Used Coupon:")
print(most_used)

# 5. Save suspicious coupon records into fraud_report.txt
file = open("fraud_report.txt", "w")

for coupon in suspicious:
    file.write(coupon + "\n")

file.close()

print("\nSuspicious coupon records saved to fraud_report.txt")