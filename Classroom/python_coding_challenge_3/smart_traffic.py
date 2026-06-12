# Program: Traffic Condition Analysis

traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]

low = []
moderate = []
high = []

# 1. Classify traffic conditions
print("Traffic Conditions:")

for count in traffic:
    if count < 80:
        print(count, "→ Low")
        low.append(count)
    elif count <= 150:
        print(count, "→ Moderate")
        moderate.append(count)
    else:
        print(count, "→ High")
        high.append(count)

# 2. Count occurrences of each traffic condition
print("\nLow Traffic Intervals:", len(low))
print("Moderate Traffic Intervals:", len(moderate))
print("High Traffic Intervals:", len(high))

# 3. Find the peak traffic interval
peak = max(traffic)

print("\nPeak Traffic Count:")
print(peak, "vehicles")

# 4. Create separate lists for each traffic category
print("\nLow Traffic List:")
print(low)

print("\nModerate Traffic List:")
print(moderate)

print("\nHigh Traffic List:")
print(high)

# 5. Recommend manual traffic control
print("\nManual Traffic Control Required:")

if len(high) > 3:
    print("Yes")
else:
    print("No")