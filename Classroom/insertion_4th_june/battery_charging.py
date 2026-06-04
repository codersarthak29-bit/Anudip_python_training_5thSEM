#program for displaying battery charging status
charging_level=20
while (charging_level<=100):
    print("Battery level:",charging_level,"%")
    charging_level = charging_level + 10
print("Battery is fully charged.")
