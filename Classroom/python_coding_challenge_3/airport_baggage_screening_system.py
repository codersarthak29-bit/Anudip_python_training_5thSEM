'''Problem Statement 
Passenger baggage weights (in kg) are stored as tuples: 
baggage = ( 
("P101", 18), 
("P102", 32), 
("P103", 24), 
("P104", 36), 
("P105", 28), 
("P106", 20), 
("P107", 41), 
("P108", 26), 
("P109", 19), 
("P110", 34) 
) 
Tasks 
1. Display passengers carrying baggage above 30 kg.  
2. Count passengers within and exceeding limits.  
3. Calculate excess baggage charges (₹500 per kg above 30 kg).  
4. Create a list of passengers requiring manual inspection.  
5. Find the passenger carrying the heaviest baggage. '''
# Passenger baggage data

baggage = (
    ("P101", 18),
    ("P102", 32),
    ("P103", 24),
    ("P104", 36),
    ("P105", 28),
    ("P106", 20),
    ("P107", 41),
    ("P108", 26),
    ("P109", 19),
    ("P110", 34)
)

# 1. Display passengers carrying baggage above 30 kg
print("Passengers Exceeding 30 kg Limit:")
for passenger, weight in baggage:
    if weight > 30:
        print(passenger)

# 2. Count passengers within and exceeding limits
within_limit = 0
exceeding_limit = 0

for passenger, weight in baggage:
    if weight > 30:
        exceeding_limit += 1
    else:
        within_limit += 1

print("\nPassengers Within Limit:", within_limit)
print("Passengers Exceeding Limit:", exceeding_limit)

# 3. Calculate excess baggage charges
print("\nExcess Baggage Charges:")
for passenger, weight in baggage:
    if weight > 30:
        excess_weight = weight - 30
        charge = excess_weight * 500
        print(passenger, ": ₹" + str(charge))

# 4. Create a list of passengers requiring manual inspection
inspection_list = []

for passenger, weight in baggage:
    if weight > 30:
        inspection_list.append(passenger)

print("\nPassengers Requiring Manual Inspection:")
print(inspection_list)

# 5. Find the passenger carrying the heaviest baggage
heaviest_passenger = ""
max_weight = 0

for passenger, weight in baggage:
    if weight > max_weight:
        max_weight = weight
        heaviest_passenger = passenger

print("\nPassenger with Heaviest Baggage:")
print(heaviest_passenger, "(" + str(max_weight) + " kg)")