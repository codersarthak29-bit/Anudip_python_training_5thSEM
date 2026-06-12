# Program: Relief Material Management

warehouses = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

# 1. Display all unique relief items
unique_resources = set()

for resources in warehouses.values():
    unique_resources.update(resources)

print("Unique Resources:")
print(unique_resources)

# 2. Find warehouses containing medicines
print("\nWarehouses with Medicines:")
for warehouse, resources in warehouses.items():
    if "Medicine" in resources:
        print(warehouse)

# 3. Count how many warehouses stock each resource
resource_count = {}

for resources in warehouses.values():
    for resource in resources:
        if resource in resource_count:
            resource_count[resource] += 1
        else:
            resource_count[resource] = 1

print("\nResource Availability:")
for resource, count in resource_count.items():
    print(resource, ":", count)

# 4. Identify the most widely available resource(s)
max_count = max(resource_count.values())

print("\nMost Widely Available Resources:")
for resource, count in resource_count.items():
    if count == max_count:
        print(resource)

# 5. Display resources available in all warehouses
common_resources = set(warehouses["Warehouse1"])

for resources in warehouses.values():
    common_resources = common_resources.intersection(set(resources))

print("\nResources Available in All Warehouses:")
if common_resources:
    for resource in common_resources:
        print(resource)
else:
    print("None")