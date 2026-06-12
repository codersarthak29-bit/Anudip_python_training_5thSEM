# Program: Sensor Telemetry Analysis

# 1. Read all sensor readings
file = open("telemetry.txt", "r")

readings = []
for line in file:
    readings.append(int(line.strip()))

file.close()

# 2. Display abnormal readings (< 90 or > 110)
abnormal = []
normal_count = 0
abnormal_count = 0

for reading in readings:
    if reading < 90 or reading > 110:
        abnormal.append(reading)
        abnormal_count += 1
    else:
        normal_count += 1

print("Abnormal Sensor Readings:")
for reading in abnormal:
    print(reading)

# 3. Calculate average sensor value
average = sum(readings) / len(readings)

print("\nAverage Sensor Value:")
print(round(average, 1))

# 4. Count normal and abnormal readings
print("\nNormal Readings:", normal_count)
print("Abnormal Readings:", abnormal_count)

# 5. Store abnormal readings in alerts.txt
file = open("alerts.txt", "w")

for reading in abnormal:
    file.write(str(reading) + "\n")

file.close()

print("\nAlert File Generated Successfully.")