# Program: Crop Moisture Analysis

moisture = {
    "Field1": 55,
    "Field2": 30,
    "Field3": 72,
    "Field4": 28,
    "Field5": 64,
    "Field6": 35,
    "Field7": 80,
    "Field8": 42,
    "Field9": 25,
    "Field10": 68
}

# 1. Identify fields requiring irrigation (< 40%)
print("Fields Requiring Irrigation:")
for field, value in moisture.items():
    if value < 40:
        print(field)

# 2. Classify fields
low = []
moderate = []
high = []

for field, value in moisture.items():
    if value < 40:
        low.append(field)
    elif value <= 65:
        moderate.append(field)
    else:
        high.append(field)

# 3. Count fields in each category
print("\nLow Moisture Fields:")
print(low)

print("\nModerate Moisture Fields:")
print(moderate)

print("\nHigh Moisture Fields:")
print(high)

print("\nCount of Low Moisture Fields:", len(low))
print("Count of Moderate Moisture Fields:", len(moderate))
print("Count of High Moisture Fields:", len(high))

# 4. Find highest and lowest moisture fields
highest_field = max(moisture, key=moisture.get)
lowest_field = min(moisture, key=moisture.get)

print("\nField with Highest Moisture:")
print(highest_field, f"({moisture[highest_field]}%)")

print("\nField with Lowest Moisture:")
print(lowest_field, f"({moisture[lowest_field]}%)")

# 5. Generate irrigation priority list
priority_list = sorted(
    [field for field, value in moisture.items() if value < 40],
    key=lambda x: moisture[x]
)

print("\nIrrigation Priority List:")
print(priority_list)